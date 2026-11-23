"""Predictions for the published cases, written separately from the resolver."""

import copy
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
import replay_source_change as study


class SourceRecoveryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = study.replay()

    def test_two_real_callers_share_one_component(self):
        first, second = self.result["callers"]
        self.assertNotEqual(first["caller_revision"], second["caller_revision"])
        self.assertEqual([first["caller"]["mall"], second["caller"]["mall"]],
                         ["mall.studio", "mall.screening-room"])
        self.assertNotEqual(first["caller"], second["caller"])
        self.assertEqual(first["target"], second["target"])
        self.assertEqual(first["target"]["component"], "component.shared-player")
        self.assertEqual(first["target"]["blob"], self.result["handoff"]["blob"])
        for trial in (first, second):
            self.assertEqual(trial["back"], trial["caller"])
        self.assertEqual(self.result["unresolved_target"], {"target": None, "trail_unchanged": True})

    def test_current_selectors_and_derived_notes(self):
        # Order within a triple is scope, opening, captions for anchors and
        # opening-note, caption-note, preview-opening-note for derivative eligibility.
        expectations = {
            "original":  (("unique", "unique", "unique"), (True, True, True)),
            "insert":    (("unique", "unique", "unique"), (True, True, True)),
            "edit":      (("unique", "absent", "unique"), (False, True, False)),
            "duplicate": (("unique", "ambiguous", "unique"), (False, True, False)),
            "rename":    (("unique", "unique", "unique"), (True, True, True)),
            "delete":    (("missing-file",) * 3, (False, False, False)),
            "context":   (("absent", "unique", "unique"), (True, True, False)),
        }
        self.assertEqual(set(self.result["variants"]), set(expectations))
        for name, (statuses, eligible) in expectations.items():
            with self.subTest(name=name):
                row = self.result["variants"][name]
                self.assertEqual(tuple(row["anchors"][key]["status"] for key in
                                       ("scope", "opening", "captions")), statuses)
                self.assertEqual(tuple(row["all_declared_inputs_match"][key] for key in
                                       ("opening-note", "caption-note", "preview-opening-note")), eligible)

    def test_position_and_file_baselines(self):
        cases = self.result["variants"]
        self.assertEqual(cases["insert"]["anchors"]["opening"]["lines"], [3])
        self.assertFalse(cases["insert"]["anchors"]["opening"]["old_position_matches"])
        self.assertEqual(cases["duplicate"]["anchors"]["opening"]["lines"], [2, 5])
        self.assertTrue(cases["duplicate"]["anchors"]["opening"]["old_position_matches"])
        self.assertEqual({k for k, row in cases.items() if row["blob_identical"]}, {"original", "rename"})
        self.assertFalse(cases["rename"]["anchors"]["opening"]["old_position_matches"])

    def test_historical_handoff_rejects_wrong_blob_position_and_digest(self):
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary) / "fixture"
            record = study.make_history(repo)
            self.assertEqual(study.recover_original(repo, record)["opening"], b"open_policy = muted\n")
            bad_blob = copy.deepcopy(record)
            bad_blob["blob"] = "0" * 40
            bad_position = copy.deepcopy(record)
            bad_position["anchors"]["opening"]["line"] = 3
            bad_digest = copy.deepcopy(record)
            bad_digest["anchors"]["opening"]["sha256"] = "0" * 64
            for bad in (bad_blob, bad_position, bad_digest):
                with self.assertRaises(ValueError):
                    study.recover_original(repo, bad)
