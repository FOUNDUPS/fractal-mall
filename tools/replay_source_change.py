"""Replay the paper's two-Mall source-recovery case. Requires Python 3.8+ and Git 2.29+."""

import argparse
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import tempfile


CASE = Path(__file__).resolve().parents[1] / "cases" / "source-recovery"
SOURCE = "components/player.rules"
RENAMED = "components/playback.rules"
PLAYER = "component.shared-player"
MALLS = ("studio", "screening-room")
VARIANTS = ("original", "insert", "edit", "duplicate", "rename", "delete", "context")
DEPENDENCIES = {
    "opening-note": ("opening",),
    "caption-note": ("captions",),
    "preview-opening-note": ("scope", "opening"),
}


def git(directory, *args):
    # The miniature history has its own identity, clock and configuration on every host.
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update({
        "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
        "GIT_AUTHOR_NAME": "Fixture", "GIT_AUTHOR_EMAIL": "fixture@example.invalid",
        "GIT_COMMITTER_NAME": "Fixture", "GIT_COMMITTER_EMAIL": "fixture@example.invalid",
        "GIT_AUTHOR_DATE": "2000-01-01T00:00:00+0000",
        "GIT_COMMITTER_DATE": "2000-01-01T00:00:00+0000",
    })
    return subprocess.check_output(
        ["git", "-C", str(directory), "-c", "core.autocrlf=false",
         "-c", "core.filemode=false", *args], env=env,
    )


def commit(directory, message):
    git(directory, "add", "-A")
    git(directory, "commit", "-q", "-m", message)
    return git(directory, "rev-parse", "HEAD").decode("ascii").strip()


def write_json(path, value):
    path.write_bytes((json.dumps(value, indent=2, sort_keys=True) + "\n").encode("utf-8"))


def copy_seed(source, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    # The fixture defines UTF-8 text with LF, independent of checkout settings.
    target.write_bytes(source.read_text(encoding="utf-8").encode("utf-8"))


def make_history(root):
    root.mkdir()
    git(root, "init", "-q", "--object-format=sha1", "-b", "original")
    seed = CASE / "seed"
    second_mall = seed / "malls" / "screening-room.json"
    for source in sorted(seed.rglob("*")):
        if source.is_file() and source != second_mall:
            copy_seed(source, root / source.relative_to(seed))
    original = commit(root, "original")
    catalog = json.loads((root / "library.json").read_bytes())
    handoff = make_handoff(root, original, catalog[PLAYER])
    git(root, "switch", "-q", "-c", "reuse-screening-room", original)
    copy_seed(second_mall, root / second_mall.relative_to(seed))
    commit(root, "second Mall references the existing component")
    for name in VARIANTS[1:]:
        git(root, "switch", "-q", "-c", name, original)
        path = root / SOURCE
        content = path.read_bytes()
        if name == "insert":
            path.write_bytes(b"# new heading\n" + content)
        elif name == "edit":
            path.write_bytes(content.replace(b"open_policy = muted", b"open_policy = audible"))
        elif name == "duplicate":
            path.write_bytes(content + b"open_policy = muted\n")
        elif name == "rename":
            path.rename(root / RENAMED)
            write_json(root / "moves.json", {SOURCE: RENAMED})
        elif name == "delete":
            path.unlink()
        elif name == "context":
            path.write_bytes(content.replace(b"scope = preview", b"scope = public"))
        commit(root, name)
    git(root, "switch", "-q", "original")
    return handoff


def tree_entry(repo, revision, path):
    entry = git(repo, "ls-tree", "-z", revision, "--", path)
    if not entry:
        return None
    metadata, _ = entry.rstrip(b"\0").split(b"\t", 1)
    mode, kind, oid = metadata.decode("ascii").split()
    if kind != "blob" or mode != "100644":
        raise ValueError(f"Expected an ordinary fixture file at {path}")
    return mode, oid


def read_file(repo, revision, path):
    return git(repo, "show", f"{revision}:{path}")


def make_handoff(repo, revision, component):
    path = component["path"]
    mode, blob = tree_entry(repo, revision, path)
    lines = read_file(repo, revision, path).splitlines(keepends=True)
    anchors = {}
    for name, line in component["selectors"].items():
        anchors[name] = {"line": line, "sha256": sha256(lines[line - 1]).hexdigest()}
    return {"component": PLAYER, "revision": revision, "path": path, "mode": mode,
            "blob": blob, "anchors": anchors}


def recover_original(repo, record):
    entry = tree_entry(repo, record["revision"], record["path"])
    if entry != (record["mode"], record["blob"]):
        raise ValueError("Historical tree entry differs from the handoff")
    lines = git(repo, "cat-file", "blob", record["blob"]).splitlines(keepends=True)
    recovered = {}
    for name, anchor in record["anchors"].items():
        index = anchor["line"] - 1
        if not 0 <= index < len(lines) or sha256(lines[index]).hexdigest() != anchor["sha256"]:
            raise ValueError(f"Historical selector disagrees for {name}")
        recovered[name] = lines[index]
    return recovered


def inspect_revision(repo, revision, record, recovered):
    old_path = record["path"]
    moves = {}
    if tree_entry(repo, revision, "moves.json"):
        moves = json.loads(read_file(repo, revision, "moves.json"))
    path = moves.get(old_path, old_path)
    entry = tree_entry(repo, revision, path)
    lines = read_file(repo, revision, path).splitlines(keepends=True) if entry else []
    old_lines = lines if path == old_path else []
    anchors = {}
    for name, original_bytes in recovered.items():
        index = record["anchors"][name]["line"] - 1
        hits = [n for n, line in enumerate(lines, 1) if line == original_bytes]
        status = "missing-file"
        if entry:
            status = {0: "absent", 1: "unique"}.get(len(hits), "ambiguous")
        anchors[name] = {"status": status, "lines": hits,
                         "old_position_matches": old_lines[index:index + 1] == [original_bytes]}
    reusable = {
        name: all(anchors[part]["status"] == "unique" for part in parts)
        for name, parts in DEPENDENCIES.items()
    }
    return {"commit": revision, "path": path, "blob_identical": bool(entry and entry[1] == record["blob"]),
            "anchors": anchors, "all_declared_inputs_match": reusable}


def enter(caller, links, selection, catalog, trail):
    target = links[selection]
    if target not in catalog:
        return None
    trail.append(caller.copy())
    return {"component": target, "path": catalog[target]["path"]}


def read_branch(repo, name):
    return git(repo, "rev-parse", f"refs/remotes/origin/{name}").decode("ascii").strip()


def caller_trials(repo):
    trials = []
    for mall, branch in zip(MALLS, ("original", "reuse-screening-room")):
        revision = read_branch(repo, branch)
        catalog = json.loads(read_file(repo, revision, "library.json"))
        fixture = json.loads(read_file(repo, revision, f"malls/{mall}.json"))
        caller = {"mall": fixture["mall"], **fixture["caller"]}
        stack = []
        selected = enter(caller, fixture["links"], "screen", catalog, stack)
        # Restore data from its serialized form, as a different client would.
        restored = json.loads(json.dumps(stack)).pop()
        selected["blob"] = tree_entry(repo, revision, selected["path"])[1]
        trials.append({"caller": caller, "caller_revision": revision, "target": selected, "back": restored})
        if "missing" in fixture["links"]:
            rejected_stack = [caller.copy()]
            before = list(rejected_stack)
            target = enter(caller, fixture["links"], "missing", catalog, rejected_stack)
            missing = {"target": target, "trail_unchanged": rejected_stack == before}
    return trials, missing


def replay():
    with tempfile.TemporaryDirectory() as temporary:
        workspace = Path(temporary)
        writer = workspace / "writer"
        handoff = make_history(writer)
        write_json(workspace / "handoff.json", handoff)
        git(workspace, "clone", "-q", "--no-local", str(writer), "reader")
        reader = workspace / "reader"
        git(reader, "switch", "-q", "--detach", read_branch(reader, "edit"))
        record = json.loads((workspace / "handoff.json").read_bytes())
        recovered = recover_original(reader, record)
        callers, missing = caller_trials(reader)
        return {"schema": 1, "handoff": record, "callers": callers, "unresolved_target": missing,
                "variants": {name: inspect_revision(reader, read_branch(reader, name), record, recovered)
                             for name in VARIANTS}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path, help="compare the full result with a saved JSON receipt")
    args = parser.parse_args()
    result = replay()
    if args.check:
        if result != json.loads(args.check.read_bytes()):
            parser.exit(1, "Replay differs from the stored receipt.\n")
        print("Replay matches the complete stored receipt.")
    else:
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
