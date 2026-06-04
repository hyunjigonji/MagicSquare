"""Blank-cell coordinate discovery (FR-LOC-01)."""

from __future__ import annotations

from magicsquare.entity.constants import BLANK_CELL, COORD_BASE, GRID_SIZE


def find_blank_coords(grid: list[list[int]]) -> list[tuple[int, int]]:
    """Return 1-index (row, col) of each blank cell, row-major order (I6)."""
    coords: list[tuple[int, int]] = []
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == BLANK_CELL:
                coords.append((row + COORD_BASE, col + COORD_BASE))
    return coords
