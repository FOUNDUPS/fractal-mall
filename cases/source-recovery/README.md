# Case 002 · Recover evidence after a source changes

From the notebook root, run the following with Python 3.8 or newer and Git 2.29 or newer.

```sh
python tools/replay_source_change.py --check cases/source-recovery/result.json
python -m unittest discover -s tests -p test_source_change.py -v
```

Without `--check`, the first command prints the full JSON observation. The fixture runs offline. Its temporary writer builds a real Git history with fixed dates and file contents. A second Mall references the same player on a separate branch. A freshly cloned reader starts at the edited revision, reads the serialized handoff and resolves all versions from its own object database. The original revision and other branches survive for this experiment. There is one author and no independent human participant.

The [seed](seed/) defines the Mall names, caller states, registry and source. The [test](../../tests/test_source_change.py) specifies the design's predictions independently of the resolver's output. The [receipt](result.json) records every commit, anchored digest, matching line, eligibility decision and returned caller. Its committed UTF-8/LF bytes have SHA-256 `64bd18afd1b5231d4818e36dc78c06a97f2bb27327d5e2667001976e6fad4fcd`. Identifiers inside the receipt belong to the generated fixture history. They can be rebuilt locally.

Each of six changes starts from the same original. An insertion shifts all anchors. Editing the opening rule removes one original passage. Duplicating it makes the intended occurrence ambiguous. A declared move preserves the source across a rename. Deletion removes every current anchor. Changing only the scope qualifies the opening rule differently while leaving its bytes intact. The controls also exercise an unresolved component and altered historical receipts. “All declared inputs match” means that each required passage is uniquely present at the allowed path. Semantic equivalence and review independence require additional evidence.
