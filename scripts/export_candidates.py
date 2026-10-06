#!/usr/bin/env python3
"""Export reviewed static role assets, never initialize or merge an existing vault."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
ROLES = ("personal", "knowledge")
DECLARATION = "90. Settings/04 Index/folder-structure.json"
MANIFEST = "candidate-manifest.json"
PLUGINS = (
    "templater-obsidian", "homepage", "omnisearch", "obsidian-excalidraw-plugin",
    "obsidian-outliner", "obsidian-linter",
)
NATIVE_FILES = {
    ".obsidian/core-plugins.json", ".obsidian/community-plugins.json",
    ".obsidian/snippets/mermaid-wide.css", ".obsidian/snippets/fix-nested-bullets.css",
    *(
        f".obsidian/plugins/{plugin}/{name}"
        for plugin in PLUGINS for name in ("main.js", "manifest.json", "styles.css")
    ),
    *(f"90. Settings/02 Templates/auto/{name}.template.md" for name in (
        "Daily Note", "Dashboard", "Weekly Notes", "Monthly Notes", "Quarterly Notes", "Yearly Note",
    )),
    *(f"90. Settings/02 Templates/manual/{name}.template.md" for name in (
        "note", "task", "project", "log", "video", "book", "guideline",
    )),
    "90. Settings/05 Bases/Books.base", "90. Settings/05 Bases/Video.base",
}
SETTINGS = {
    ".obsidian/app.json", ".obsidian/daily-notes.json",
    ".obsidian/plugins/templater-obsidian/data.json",
    ".obsidian/plugins/homepage/data.json",
    ".obsidian/plugins/obsidian-excalidraw-plugin/data.json",
}


def canonical(document: object) -> bytes:
    return (json.dumps(document, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_path(value: str, *, hidden: bool = False) -> PurePosixPath:
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError(f"invalid relative path: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or str(path) != value or any(part in (".", "..") for part in path.parts):
        raise ValueError(f"noncanonical relative path: {value!r}")
    if not hidden and any(part.startswith(".") for part in path.parts):
        raise ValueError(f"hidden path not allowed: {value}")
    return path


def confined(root: Path, value: str) -> Path:
    """Reject links at every component, including links that stay inside the root."""
    path = root
    for part in safe_path(value, hidden=True).parts:
        path = path / part
        if path.is_symlink():
            raise ValueError(f"symlink not allowed: {value}")
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"path escapes source root: {value}")
    return path


def read_asset(root: Path, source: str) -> bytes:
    safe_path(source, hidden=source in NATIVE_FILES)
    allowed = source in NATIVE_FILES or any(
        source.startswith(f"candidates/{directory}/")
        for directory in ("common", "personal", "knowledge", "fixtures")
    )
    if not allowed:
        raise ValueError(f"source outside export allowlist: {source}")
    path = confined(root, source)
    if not path.is_file():
        raise ValueError(f"missing regular asset: {source}")
    return path.read_bytes()


def prepare(role: str, root: Path = ROOT) -> tuple[dict[str, bytes], dict]:
    if role not in ROLES:
        raise ValueError(f"unknown role: {role}")
    definition = json.loads(confined(root, f"candidates/{role}.json").read_bytes())
    native = json.loads(confined(root, "candidates/common/native.json").read_bytes())
    folders = definition["folders"]
    roots = definition["roots"]
    if len(folders) != len(set(folders)) or len(roots) != len(set(roots)):
        raise ValueError("duplicate structure entry")
    for folder in folders:
        path = safe_path(folder)
        if path.parts[0] not in roots:
            raise ValueError(f"folder outside declared roots: {folder}")
        for parent in path.parents:
            if str(parent) != "." and str(parent) not in folders:
                raise ValueError(f"undeclared parent: {parent}")
    if any(root_name not in folders or "/" in root_name for root_name in roots):
        raise ValueError("invalid root declaration")
    files: dict[str, bytes] = {}

    def add(path: str, data: bytes) -> None:
        parsed = safe_path(path, hidden=path in NATIVE_FILES or path in SETTINGS)
        if path in files or path == MANIFEST:
            raise ValueError(f"duplicate or reserved destination: {path}")
        parent = str(parsed.parent)
        if parent != "." and not path.startswith(".obsidian/") and parent not in folders:
            raise ValueError(f"destination folder not declared: {path}")
        files[path] = data

    for entry in definition["files"]:
        add(entry["path"], read_asset(root, entry["source"]))
    for entry in native["files"]:
        if role not in entry["roles"]:
            continue
        if entry["source"] not in NATIVE_FILES or entry["path"] != entry["source"]:
            raise ValueError("native asset must be an exact approved source/destination")
        add(entry["path"], read_asset(root, entry["source"]))
    for path, document in native["settings"][role].items():
        if path not in SETTINGS:
            raise ValueError(f"unapproved setting: {path}")
        add(path, canonical(document))
    add(DECLARATION, canonical({
        "schema_version": 1, "description": f"Independent {role} candidate structure",
        "roots": roots, "folders": folders,
    }))
    inventory = {
        "schema_version": 1, "role": role,
        "folders": sorted(set(folders) | {
            str(parent) for path in files for parent in PurePosixPath(path).parents
            if str(parent) != "."
        }),
        "files": [
            {"path": path, "sha256": digest(data), "size": len(data)}
            for path, data in sorted(files.items())
        ],
    }
    manifest = {**inventory, "candidate_sha256": digest(canonical(inventory))}
    files[MANIFEST] = canonical(manifest)
    return files, manifest


def export(role: str, output: str, root: Path = ROOT) -> dict:
    """Materialize a new local package; refuse even an empty existing directory."""
    parts = safe_path(output, hidden=True).parts
    if any(part in (".git", ".obsidian") for part in parts):
        raise ValueError("output cannot be repository or application control data")
    destination = confined(root, output)
    if os.path.lexists(destination):
        raise FileExistsError(f"refusing existing destination: {output}")
    if not destination.parent.is_dir():
        raise ValueError("output parent must already exist")
    files, manifest = prepare(role, root)
    destination.mkdir()  # exclusive claim; never merge or replace
    try:
        for folder in manifest["folders"]:
            (destination / folder).mkdir(parents=True, exist_ok=True)
        for path, data in files.items():
            with (destination / path).open("xb") as handle:
                handle.write(data)
    except OSError as exc:
        raise OSError(
            f"incomplete candidate retained at {output}; not a verified package; "
            f"inspect it and select a new absent output path before retrying: {exc}"
        ) from exc
    return manifest


def verify_package(path: Path) -> dict:
    """Verify names, bytes, folders, hidden files and absence of symlinks."""
    if path.is_symlink():
        raise ValueError("package root is a symlink")
    manifest_bytes = confined(path, MANIFEST).read_bytes()
    manifest = json.loads(manifest_bytes)
    inventory = {key: manifest[key] for key in ("schema_version", "role", "folders", "files")}
    expected_manifest = {**inventory, "candidate_sha256": manifest["candidate_sha256"]}
    if manifest_bytes != canonical(expected_manifest):
        raise ValueError("manifest must have the exact canonical schema and bytes")
    if digest(canonical(inventory)) != manifest["candidate_sha256"]:
        raise ValueError("candidate manifest digest mismatch")
    expected = {entry["path"]: entry for entry in manifest["files"]}
    if len(expected) != len(manifest["files"]) or MANIFEST in expected:
        raise ValueError("duplicate or reserved manifest entry")
    for relative in expected:
        safe_path(relative, hidden=relative in NATIVE_FILES or relative in SETTINGS)
    for folder in manifest["folders"]:
        safe_path(folder, hidden=folder == ".obsidian" or folder.startswith(".obsidian/"))
    actual_files, actual_folders = set(), set()
    for entry in path.rglob("*"):
        relative = entry.relative_to(path).as_posix()
        if entry.is_symlink():
            raise ValueError(f"package symlink: {relative}")
        if entry.is_dir():
            actual_folders.add(relative)
        elif entry.is_file():
            actual_files.add(relative)
        else:
            raise ValueError(f"nonregular package entry: {relative}")
    if actual_files != set(expected) | {MANIFEST} or actual_folders != set(manifest["folders"]):
        raise ValueError("package inventory mismatch")
    for relative, entry in expected.items():
        data = (path / relative).read_bytes()
        if digest(data) != entry["sha256"] or len(data) != entry["size"]:
            raise ValueError(f"package content mismatch: {relative}")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--role", choices=ROLES, required=True)
    parser.add_argument("--output", required=True, help="absent repo-relative package directory")
    args = parser.parse_args()
    try:
        manifest = export(args.role, args.output)
        verify_package(ROOT / args.output)
    except (ValueError, FileExistsError, OSError) as exc:
        parser.exit(1, f"candidate export refused: {exc}\n")
    print(json.dumps({"role": args.role, "output": args.output,
                      "candidate_sha256": manifest["candidate_sha256"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
