"""Golden master approval — compare canonical text to tests/golden/*.approved.txt."""

from __future__ import annotations

import os
from pathlib import Path

_GOLDEN_DIR = Path(__file__).resolve().parent / "golden"


def golden_path(relative: str) -> Path:
    return _GOLDEN_DIR / relative


def assert_matches_golden(actual: str, relative: str) -> None:
    """Match actual against tests/golden/<relative>. Set UPDATE_GOLDEN=1 to rewrite."""
    path = golden_path(relative)
    if os.environ.get("UPDATE_GOLDEN") == "1":
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(actual, encoding="utf-8")
        return

    if not path.is_file():
        raise AssertionError(f"Golden file missing: {path}")

    expected = path.read_text(encoding="utf-8")
    if actual == expected:
        return

    exp_lines = expected.splitlines()
    act_lines = actual.splitlines()
    summary: list[str] = [f"Golden mismatch: {relative}"]
    max_lines = max(len(exp_lines), len(act_lines))
    for i in range(max_lines):
        exp_line = exp_lines[i] if i < len(exp_lines) else "<missing>"
        act_line = act_lines[i] if i < len(act_lines) else "<missing>"
        if exp_line != act_line:
            summary.append(f"  line {i + 1}: expected {exp_line!r} != actual {act_line!r}")
    raise AssertionError("\n".join(summary))
