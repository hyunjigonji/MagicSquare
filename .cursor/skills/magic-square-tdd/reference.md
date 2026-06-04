# D-* Logic 테스트 ID

| ID | 요약 | Rule / PRD |
|----|------|------------|
| D-T0 | 완성 격자 — `ok=true` | T0 |
| D-T1 | 행·열 OK, 대각선 하나 ≠34 | T1, R3 |
| D-T2 | 10선 OK, 숫자 중복 | T2, R4 |
| D-T3 | 대각선 오류 + 중복 동시 | T3, R3+R4 |
| D-R1 | 행 합 ≠34 | R1 |
| D-R2 | 열 합 ≠34 | R2 |
| D-R5 | 0 잔존 (완성 모드) | R5 |
| D-C01 | MagicConstant SSOT (`34`/`16`/`4`) | `.cursorrules` |
| D-LOC-01 | `find_blank_coords(G1)` → `[(2,2),(3,3)]` | I6 row-major |
| D-SOL-01 | `solution(G1)` Step A → `int[6]` | I8 1-index |
