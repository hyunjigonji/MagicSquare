"""Canonical golden text for int[6] success and Boundary error codes."""

from __future__ import annotations


def format_solution_success(result: list[int]) -> str:
    """Success: STATUS=OK + INT6=r1,c1,n1,r2,c2,n2 (1-index, row-major blanks)."""
    if len(result) != 6:
        raise ValueError(f"int[6] required, got len={len(result)}")
    body = ",".join(str(x) for x in result)
    return f"STATUS=OK\nINT6={body}\n"


def format_error(code: str, name: str) -> str:
    """Error: ERR <code> <name> — Boundary error code string."""
    return f"STATUS=ERR\nERR {code} {name}\n"
