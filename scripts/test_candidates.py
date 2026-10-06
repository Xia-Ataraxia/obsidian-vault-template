#!/usr/bin/env python3
"""Static candidate package acceptance, not live onboarding or Obsidian runtime QA."""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from export_candidates import (
    ROOT, ROLES, PLUGINS, canonical, export, prepare, read_asset,
    safe_path, verify_package,
)
from verify_structure import verify

INTERNAL_GOAL_ID = re.compile(rb"(?i)(?<![a-z0-9_])g00[0-9](?![a-z0-9_])")

class Candidates(unittest.TestCase):
    def setUp(self):
        (ROOT / ".gjc").mkdir(exist_ok=True)
        self.scratch = tempfile.TemporaryDirectory(prefix="candidate-tests-", dir=ROOT / ".gjc")
        self.directory = Path(self.scratch.name)
        self.relative = self.directory.relative_to(ROOT).as_posix()

    def tearDown(self):
        self.scratch.cleanup()

    def build(self, role, name=None):
        path = f"{self.relative}/{name or role}"
        manifest = export(role, path)
        return ROOT / path, manifest

    def test_each_role_alone_deterministic_and_structurally_valid(self):
        for role in ROLES:
            with self.subTest(role=role):
                first, manifest = self.build(role)
                second, repeated = self.build(role, f"{role}-again")
                self.assertEqual(manifest, repeated)
                self.assertEqual(verify_package(first), repeated)
                self.assertEqual(verify_package(second), repeated)
                self.assertEqual(verify(first, strict=False), [])
                opposite = "knowledge" if role == "personal" else "personal"
                self.assertFalse((first / opposite).exists())
                self.assertFalse((first / ".git").exists())
                self.assertFalse((first / ".gjc").exists())
                self.assertFalse((first / ".agents").exists())
                roots = json.loads((first / "90. Settings/04 Index/folder-structure.json").read_bytes())["roots"]
                self.assertEqual(len(roots), 10 if role == "personal" else 7)
                self.assertNotIn("50. AI", roots)
                self.assertNotIn("60. Saint", roots)
                if role == "personal":
                    for leaf in ("01 Sermon", "02 QT", "03 Pray", "04 Bible", "05 Worship"):
                        self.assertTrue((first / "15. Work/02 Area/Saint" / leaf).is_dir())
                else:
                    for leaf in ("01 Concepts", "02 Entities", "03 Guides", "04 Maps", "05 Questions", "06 Personas"):
                        self.assertTrue((first / "20. Wiki" / leaf).is_dir())

    def test_native_features_assets_and_routes_are_preserved(self):
        enabled = ("canvas", "bases", "global-search", "backlink", "graph", "properties", "file-recovery", "daily-notes", "templates")
        for role in ROLES:
            package, _ = self.build(role)
            core = json.loads((package / ".obsidian/core-plugins.json").read_bytes())
            self.assertTrue(all(core[key] for key in enabled))
            for plugin in PLUGINS:
                for filename in ("main.js", "manifest.json", "styles.css"):
                    relative = f".obsidian/plugins/{plugin}/{filename}"
                    self.assertEqual((package / relative).read_bytes(), (ROOT / relative).read_bytes())
            config = json.loads((package / ".obsidian/plugins/templater-obsidian/data.json").read_bytes())
            self.assertTrue((package / config["templates_folder"]).is_dir())
            if role == "knowledge":
                self.assertEqual(config["folder_templates"], [])
                self.assertEqual(config["trigger_on_file_creation_mode"], "none")
            else:
                self.assertEqual({route["folder"] for route in config["folder_templates"]}, {
                    "10. Time/01 Daily Notes", "10. Time/02 Weekly Notes",
                    "10. Time/03 Monthly Notes", "10. Time/04 Yearly Notes",
                    "10. Time/05 Quarterly Notes",
                })
            manual = {entry.name for entry in (package / "90. Settings/02 Templates/manual").iterdir()}
            expected = {f"{name}.template.md" for name in ("note", "book", "guideline", "source")}
            if role == "personal":
                expected |= {f"{name}.template.md" for name in ("task", "project", "log", "video")}
            self.assertEqual(manual, expected)
            for route in config["folder_templates"]:
                self.assertTrue((package / route["folder"]).is_dir())
                self.assertTrue((package / route["template"]).is_file())
                self.assertNotEqual(route["folder"], "10. Time/06 Dashboard")
            daily = json.loads((package / ".obsidian/daily-notes.json").read_bytes())
            self.assertTrue((package / daily["folder"]).is_dir())
            drawings = json.loads((package / ".obsidian/plugins/obsidian-excalidraw-plugin/data.json").read_bytes())
            self.assertTrue((package / drawings["folder"]).is_dir())

    def test_existing_synthetic_vault_refused_and_everything_preserved(self):
        fixture = json.loads((ROOT / "candidates/fixtures/preservation.json").read_bytes())
        self.assertTrue(fixture["synthetic"])
        for role in ROLES:
            existing = self.directory / f"existing-{role}"
            existing.mkdir()
            originals = fixture["existing_vault"]["files"]
            for relative, body in originals.items():
                path = existing / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(body, encoding="utf-8")
            for link in fixture["existing_vault"]["symlinks"]:
                (existing / link["path"]).symlink_to(link["target"])
            before = {relative: (existing / relative).read_bytes() for relative in originals}
            with self.assertRaises(FileExistsError):
                export(role, existing.relative_to(ROOT).as_posix())
            after = {relative: (existing / relative).read_bytes() for relative in originals}
            self.assertEqual(before, after)
            self.assertEqual(
                set(p.relative_to(existing).as_posix() for p in existing.rglob("*") if p.is_file() and not p.is_symlink()),
                set(originals),
            )
            for link in fixture["existing_vault"]["symlinks"]:
                self.assertEqual(os.readlink(existing / link["path"]), link["target"])

    def test_export_rerun_empty_directory_and_file_refused(self):
        package, original = self.build("personal")
        with self.assertRaises(FileExistsError):
            export("personal", package.relative_to(ROOT).as_posix())
        self.assertEqual(verify_package(package), original)
        empty = self.directory / "empty"
        empty.mkdir()
        with self.assertRaises(FileExistsError):
            export("knowledge", empty.relative_to(ROOT).as_posix())
        marker = self.directory / "file"
        marker.write_bytes(b"synthetic protected")
        with self.assertRaises(FileExistsError):
            export("knowledge", marker.relative_to(ROOT).as_posix())
        self.assertEqual(marker.read_bytes(), b"synthetic protected")

    def test_paths_hidden_files_and_private_assets_denied(self):
        for path in ("../outside", "/outside", "a/../outside", "a//b", "./a", "a\\b", ".env", "a/.secret"):
            with self.subTest(path=path), self.assertRaises(ValueError):
                safe_path(path)
        for source in ("Me.md", ".git/config", ".gjc/config.yml", ".obsidian/workspace.json", "80. References/_attachments/private.svg", "candidates/common/.env"):
            with self.subTest(source=source), self.assertRaises(ValueError):
                read_asset(ROOT, source)

    def test_unlisted_source_files_never_exported(self):
        alternate = self.directory / "source"
        alternate.mkdir()
        shutil.copytree(ROOT / "candidates", alternate / "candidates")
        # Materialize only allowlisted public source bytes, plus synthetic intruders.
        files, _ = prepare("personal")
        native = json.loads((ROOT / "candidates/common/native.json").read_bytes())
        for entry in native["files"]:
            path = alternate / entry["source"]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes((ROOT / entry["source"]).read_bytes())
        for relative in (".obsidian/workspace.json", ".env", "candidates/common/.hidden", "80. References/_attachments/private.svg"):
            path = alternate / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b"SYNTHETIC-NOT-FOR-EXPORT")
        result, _ = prepare("personal", alternate)
        self.assertEqual(files, result)
        self.assertFalse(any(b"SYNTHETIC-NOT-FOR-EXPORT" in data for data in result.values()))

    def test_symlink_source_components_and_output_ancestors_denied(self):
        source = self.directory / "source"
        source.mkdir()
        (source / "candidates").symlink_to(ROOT / "candidates", target_is_directory=True)
        with self.assertRaises(ValueError):
            prepare("personal", source)
        alias = self.directory / "alias"
        alias.symlink_to(self.directory, target_is_directory=True)
        with self.assertRaises(ValueError):
            export("personal", f"{self.relative}/alias/package")
        dangling = self.directory / "dangling"
        dangling.symlink_to(self.directory / "absent")
        with self.assertRaises(ValueError):
            export("personal", dangling.relative_to(ROOT).as_posix())
        local = self.directory / "candidates/common"
        local.mkdir(parents=True)
        (local / "asset.md").symlink_to(ROOT / "Me.md")
        with self.assertRaises(ValueError):
            read_asset(self.directory, "candidates/common/asset.md")

    def test_preflight_failure_does_not_create_destination(self):
        with patch("export_candidates.prepare", side_effect=ValueError("missing synthetic asset")):
            with self.assertRaises(ValueError):
                export("personal", f"{self.relative}/not-created")
        self.assertFalse((self.directory / "not-created").exists())

    def test_postcreate_failure_is_distinct_and_preserves_partial_candidate(self):
        output = f"{self.relative}/incomplete"
        original_open = Path.open

        def fail_write(path, *args, **kwargs):
            if args and args[0] == "xb":
                raise PermissionError("synthetic permission revocation")
            return original_open(path, *args, **kwargs)

        with patch.object(Path, "open", fail_write):
            with self.assertRaisesRegex(OSError, "incomplete candidate retained.*not a verified package"):
                export("personal", output)
        self.assertTrue((ROOT / output).is_dir())
        self.assertFalse((ROOT / output / "candidate-manifest.json").exists())
        with self.assertRaises(FileExistsError):
            export("personal", output)

    def test_shipped_preservation_expectations_do_not_claim_onboarding(self):
        shared = []
        for role in ROLES:
            files, _ = prepare(role)
            expectations = json.loads(files["90. Settings/04 Index/onboard-expectations.json"])
            self.assertTrue(expectations["synthetic"])
            self.assertEqual(expectations["fresh_vault"]["counterpart"], None)
            existing = expectations["existing_vault"]
            self.assertEqual(existing["mode"], "additive-only")
            self.assertIs(existing["implementation_behavior_pending"], True)
            self.assertTrue(existing["implementation_cases"])
            self.assertIn("exact", existing["approval_required"])
            rules = files["90. Settings/01 Guideline/00 Common Rules.md"]
            shared.append(rules)
            self.assertIn(b"Do not write a work record automatically", rules)
            self.assertIn(b"Do not create a paired note", rules)
            for path, data in files.items():
                self.assertNotRegex(data, INTERNAL_GOAL_ID, path)
        self.assertEqual(shared[0], shared[1])

    def test_internal_identifier_guard_covers_cases_not_embedded_vendor_data(self):
        for token in (b"G003", b"g003", b'"G002": "synthetic"', b"(g001)"):
            with self.subTest(token=token):
                self.assertRegex(token, INTERNAL_GOAL_ID)
        for token in (b"base64AG003embedded", b"notAG003identifier"):
            with self.subTest(token=token):
                self.assertNotRegex(token, INTERNAL_GOAL_ID)

    def test_real_cli_and_repository_control_paths(self):
        for role in ROLES:
            output = f"{self.relative}/cli-{role}"
            command = [sys.executable, str(ROOT / "scripts/export_candidates.py"), "--role", role, "--output", output]
            first = subprocess.run(command, capture_output=True, text=True, check=False)
            self.assertEqual(first.returncode, 0, first.stderr)
            result = json.loads(first.stdout)
            self.assertEqual(result["candidate_sha256"], verify_package(ROOT / output)["candidate_sha256"])
            second = subprocess.run(command, capture_output=True, text=True, check=False)
            self.assertEqual(second.returncode, 1)
            self.assertIn("refusing existing destination", second.stderr)
            self.assertEqual(verify_package(ROOT / output)["candidate_sha256"], result["candidate_sha256"])
        for output in (".git/new-candidate", ".obsidian/new-candidate", f"{self.relative}/.git/package"):
            with self.assertRaises(ValueError):
                export("personal", output)

    def test_candidate_tampering_detected_bodies_names_hidden_attachments_and_links(self):
        for kind in ("body", "rename", "hidden", "attachment", "link", "manifest", "folder", "manifest-extra", "manifest-whitespace", "manifest-duplicate"):
            with self.subTest(kind=kind):
                package, _ = self.build("knowledge", kind)
                if kind == "body":
                    (package / "Me.md").write_bytes(b"synthetic tamper")
                elif kind == "rename":
                    (package / "Me.md").rename(package / "Renamed.md")
                elif kind == "hidden":
                    (package / ".obsidian/workspace.json").write_bytes(b"{}")
                elif kind == "attachment":
                    (package / "80. References/_attachments/injected.svg").write_bytes(b"synthetic")
                elif kind == "link":
                    (package / "injected-link").symlink_to(ROOT / "Me.md")
                elif kind == "manifest":
                    manifest = json.loads((package / "candidate-manifest.json").read_bytes())
                    manifest["role"] = "personal"
                    (package / "candidate-manifest.json").write_bytes(canonical(manifest))
                elif kind == "folder":
                    (package / "unlisted").mkdir()
                elif kind.startswith("manifest-"):
                    path = package / "candidate-manifest.json"
                    manifest = json.loads(path.read_bytes())
                    if kind == "manifest-extra":
                        manifest["synthetic_unreviewed_field"] = "synthetic private payload"
                        path.write_bytes(canonical(manifest))
                    elif kind == "manifest-whitespace":
                        path.write_text(json.dumps(manifest, ensure_ascii=False, indent=4), encoding="utf-8")
                    else:
                        path.write_bytes(path.read_bytes().replace(b'{\n', b'{\n  "role": "knowledge",\n', 1))
                with self.assertRaises(ValueError):
                    verify_package(package)

    def test_provenance_conflict_is_not_a_new_creator_value(self):
        fixture = json.loads((ROOT / "candidates/fixtures/preservation.json").read_bytes())
        self.assertNotIn(fixture["provenance_conflict"]["created_by"], ("user", "agent"))
        for role in ROLES:
            files, _ = prepare(role)
            rules = files["90. Settings/01 Guideline/00 Common Rules.md"].decode()
            self.assertIn("never silently normalized", rules)
            self.assertIn(fixture["provenance_conflict"]["created_by"], rules)

    def test_agent_routing_owners_resolve_without_counterpart(self):
        for role in ROLES:
            files, _ = prepare(role)
            agents = files["AGENTS.md"].decode()
            for heading in ("Purpose", "User Context", "Agent Identity", "Task Routes", "Work Records"):
                self.assertIn(f"## {heading}", agents)
            self.assertNotIn("{{", agents)
            for owner in ("00 Common Rules.md", "01 Role Placement.md", "02 Native Usage.md"):
                self.assertIn(f"90. Settings/01 Guideline/{owner}", files)
                self.assertIn(owner, agents)
            self.assertIn("unknown", agents.lower())
            self.assertIn("destination", agents.lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
