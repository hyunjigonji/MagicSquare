"""Canonical golden text — STATUS line + INT6 (1-index int[6]) or error code string."""

from __future__ import annotations


def format_golden_ok_int6(values: list[int] | tuple[int, ...]) -> str:
    """Success: STATUS=OK and INT6=r1,c1,n1,r2,c2,n2 (1-index, trailing newline)."""
    if len(values) != 6:
        raise ValueError(f"int[6] required, got {len(values)}")
    body = ",".join(str(v) for v in values)
    return f"STATUS=OK\nINT6={body}\n"


def format_solution_success(result: list[int]) -> str:
    """D-SOL-01: solution() int[6] → golden text (alias)."""
    return format_golden_ok_int6(result)


def format_golden_error(code: str) -> str:
    """Failure: STATUS=E00x (Boundary error code string)."""
    return f"STATUS={code}\n"


def format_error(code: str, name: str) -> str:
    """Failure (legacy): STATUS=ERR + ERR line — Boundary reserved."""
    return f"STATUS=ERR\nERR {code} {name}\n"


def format_loc_step_a(coords: list[tuple[int, int]]) -> str:
    """D-LOC-01 Step A: blank (r,c) pairs → int[6] with n=0 placeholders."""
    flat: list[int] = []
    for row, col in coords:
        flat.extend([row, col, 0])
    if len(flat) != 6:
        raise ValueError(f"expected 2 blank cells (6 ints), got {len(flat)} from {coords!r}")
    return format_golden_ok_int6(flat)
