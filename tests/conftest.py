"""공통 pytest 픽스처 — Logic/UI Track (데이터만, 로직 없음)."""

from __future__ import annotations

import pytest

# G1: 부분 격자 — 빈칸 `0` 2칸, 1-index (2,2)·(3,3), row-major 스캔 순서
_GRID_G1: list[list[int]] = [
    [16, 3, 2, 13],
    [5, 0, 11, 8],
    [9, 6, 0, 12],
    [4, 15, 14, 1],
]


@pytest.fixture
def grid_g1() -> list[list[int]]:
    """G1 — 4×4, 0이 정확히 2칸 (1-index 좌표 (2,2), (3,3))."""
    return [row[:] for row in _GRID_G1]
