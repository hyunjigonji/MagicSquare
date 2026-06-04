"""Partial magic square solver — Step A (row-sum fill)."""

from __future__ import annotations

from magicsquare.entity.constants import COORD_BASE, GRID_SIZE, MAGIC_CONSTANT
from magicsquare.entity.locator import find_blank_coords


def solution(grid: list[list[int]]) -> list[int]:
    """Step A: fill each blank from its row sum. Returns int[6] 1-index (I8)."""
    out: list[int] = []
    for row_1, col_1 in find_blank_coords(grid):
        row = row_1 - COORD_BASE
        row_sum = sum(grid[row][c] for c in range(GRID_SIZE))
        value = MAGIC_CONSTANT - row_sum
        out.extend([row_1, col_1, value])
    return out
