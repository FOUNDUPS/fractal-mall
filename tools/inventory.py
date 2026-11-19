"""Inventory this notebook's tracked paths at a single Git commit as JSON."""

import argparse
import json
import os
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def inventory(revision):
    commit = git("rev-parse", "--verify", "--end-of-options", revision + "^{commit}").decode().strip()
    entries = []
    for record in git("ls-tree", "-rz", "--full-tree", commit).split(b"\0"):
        if record:
            metadata, path = record.split(b"\t", 1)
            mode, kind, oid = metadata.decode("ascii").split()
            entries.append({"path": os.fsdecode(path), "mode": mode, "type": kind, "object_id": oid})
    return {"commit": commit, "entry_count": len(entries), "entries": entries}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("revision", nargs="?", default="HEAD", help="commit, branch or tag (default HEAD)")
    args = parser.parse_args()
    try:
        result = inventory(args.revision)
    except (OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Inventory failed: {error}\n")
    json.dump(result, sys.stdout, indent=2, ensure_ascii=True)
    print()


if __name__ == "__main__":
    main()
