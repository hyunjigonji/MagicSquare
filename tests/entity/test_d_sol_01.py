"""D-SOL-01 — solution(G1) Step A success (I8 int[6] 1-index)."""

from __future__ import annotations

from magicsquare.entity.solver import solution


def test_d_sol_01_step_a_success(grid_g1: list[list[int]]) -> None:
    # Given: G1 격자 (빈칸 2개, 1-index (2,2)·(3,3))
    # When: solution(grid_g1) — Step A
    result = solution(grid_g1)
    # Then: int[6] [r1,c1,n1,r2,c2,n2] 1-index, row-major
    assert result == [2, 2, 10, 3, 3, 7]
