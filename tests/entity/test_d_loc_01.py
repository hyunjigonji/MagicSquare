"""D-LOC-01 — find_blank_coords(G1) → [(2,2), (3,3)] (FR-LOC-01, I6 row-major)."""

from __future__ import annotations

from magicsquare.entity.locator import find_blank_coords

from _approval import assert_matches_golden
from _golden_format import format_loc_step_a

_GOLDEN_D_LOC_01_G1_STEP_A = "d_loc_01_g1_step_a.approved.txt"


def test_d_loc_01_blank_coords_row_major(grid_g1: list[list[int]]) -> None:
    # Given: G1 격자 (0이 2개)
    # When: find_blank_coords(grid_g1) 호출
    result = find_blank_coords(grid_g1)
    # Then: [(2,2),(3,3)] 반환 (1-index, row-major)
    assert result == [(2, 2), (3, 3)]


def test_d_loc_01_step_a_success(grid_g1: list[list[int]]) -> None:
    # Given: G1 격자 (Step A — blank discovery)
    # When: find_blank_coords(grid_g1)
    coords = find_blank_coords(grid_g1)
    # Then: golden master (STATUS=OK, INT6 1-index, n=0)
    actual = format_loc_step_a(coords)
    assert_matches_golden(actual, _GOLDEN_D_LOC_01_G1_STEP_A)
