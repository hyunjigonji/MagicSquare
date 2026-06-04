# MagicSquare

4×4 부분 마방진(빈칸 2개, 1~16, 합 34) 과제에서 **늦은 검토로 시간을 낭비하는 문제**를 Mom Test로 정의하고, **10선 검증**을 최소 제품으로 구현하는 학습 프로젝트입니다.

**아키텍처:** ECB (`boundary` → `control` → `entity`) · **개발 방식:** Dual-Track TDD (Logic `D-*` / UI `U-*`)

---

## 문제 (한 문장)

> 4×4 부분 마방진 과제에서 빈칸 2개를 채운 뒤 행·열만 맞다고 보고 넘어갔다가, **마지막 검토**에서 대각선 합 불일치와 숫자 중복을 **동시에** 발견해 **20분**을 허비했다.

**1차 목표:** 솔버·UI·ECB 전체가 아니라, 제출 전에 **10선**(행 4 + 열 4 + 대각선 2)과 **1~16 중복**을 **한 번에 판정**할 수 있는지 확인한다.

---

## 도메인

| 항목 | 값 |
|------|-----|
| 격자 | 4×4 |
| 숫자 | 1~16 (완성 시 각 1회) |
| 빈칸 | `0`, 최대 2칸 |
| Magic constant | **34** (`entity/constants.py` SSOT) |
| 10선 | 행 4 + 열 4 + 주대각선 + 부대각선 |
| 솔버 출력 | `int[6]` = `[r1,c1,n1,r2,c2,n2]` — 좌표 **1-index** (`.cursorrules`) |

---

## 페르소나

4×4 격자, 빈칸 2개(0), 1~16, 합 34 맞추는 **학습자** — 프로그래밍/OO 수업에서 부분 마방진 과제를 손·코드로 다룸.

---

## 현재 상태 (STEP 9)

| 항목 | 상태 |
|------|------|
| **pytest** | `tests/` **2 passed** (D-LOC-01, D-SOL-01) |
| **Entity** | `find_blank_coords`, `solution` Step A (행 합 채움) |
| **Golden Master** | `_approval` · `_golden_format` · `tests/golden/` (D-SOL-01 기준 파일; 테스트는 assert-only, 재연결 예정) |
| **미구현** | `validate()`, `control/` · `boundary/`, UI Track U-* |

```bash
python -m pytest tests/ -v
# tests/entity/test_d_loc_01.py  PASSED
# tests/entity/test_d_sol_01.py   PASSED
```

**다음 권장:** `/refactor-safe` P0 — D-SOL-01 golden 재연결 ([report/09.REPORT.md](report/09.REPORT.md)) · B-2 `validate()` RED (D-T0~)

---

## 프로젝트 구조

```
MagicSquare/
├── README.md
├── .cursorrules              # Rule SSOT — 도메인·ECB·TDD·E001~E007
├── pyproject.toml            # pytest, pythonpath=src
├── docs/
│   ├── PRD.md                # 제품 요구 (v0.1)
│   └── RED-TODO.md           # RED Dual-Track Todo·설계표
├── report/
│   ├── 01.REPORT.md … 06.REPORT.md
│   ├── 07.REPORT.md          # STEP 7 — GREEN D-LOC-01
│   ├── 08.REPORT.md          # STEP 8 — GREEN D-SOL-01 + Golden 인프라
│   └── 09.REPORT.md          # STEP 9 — 코드 스멜·/refactor-smell
├── .cursor/
│   ├── commands/             # /tdd-red, /review-ecb
│   └── skills/magic-square-tdd/
├── src/magicsquare/
│   └── entity/               # constants, locator, solver (control/boundary 예정)
├── tests/
│   ├── conftest.py           # grid_g1 (G1)
│   ├── _approval.py          # Golden assert_matches_golden
│   ├── _golden_format.py
│   ├── golden/
│   │   └── d_sol_01_g1_step_a.approved.txt
│   └── entity/
│       ├── test_d_loc_01.py  # D-LOC-01 GREEN
│       └── test_d_sol_01.py  # D-SOL-01 GREEN
└── prompt/
    ├── 01.Export Transcript.md … 09.Export Transcript.md
```

---

## Entity API (구현됨)

| 함수 | 파일 | 설명 |
|------|------|------|
| `find_blank_coords(grid)` | `entity/locator.py` | 빈칸 1-index `(row,col)`, row-major (D-LOC-01) |
| `solution(grid)` | `entity/solver.py` | Step A: 행 합 34로 빈칸 값 → `int[6]` (D-SOL-01) |

**G1 예:** `solution(grid_g1)` → `[2, 2, 10, 3, 3, 7]`

---

## 개발 환경

```bash
pip install -e ".[dev]"
python -m pytest tests/ -v
```

| 설정 | 내용 |
|------|------|
| Python | ≥ 3.10 |
| 테스트 경로 | `tests/` (`pyproject.toml`) |
| import 경로 | `src/` → `magicsquare` 패키지 |

TDD 세션 시작 시 Agent는 `Phase` / `Layer` / `Track` / `Target`을 선언한다.

| Command | 용도 |
|---------|------|
| [.cursor/commands/tdd-red.md](.cursor/commands/tdd-red.md) | RED 단계 |
| [.cursor/commands/review-ecb.md](.cursor/commands/review-ecb.md) | ECB import·Mock 리뷰 |

Golden 기준 갱신 (PowerShell):

```powershell
$env:UPDATE_GOLDEN="1"
python -m pytest tests/entity/test_d_sol_01.py::test_d_sol_01_step_a_success -v
Remove-Item Env:UPDATE_GOLDEN
```

---

## 문서 가이드

| 문서 | 용도 |
|------|------|
| [report/01.REPORT.md](report/01.REPORT.md) | Mom Test 인터뷰 |
| [report/02.REPORT.md](report/02.REPORT.md) | R-G-I-O, Rule R1~R5 |
| [report/06.REPORT.md](report/06.REPORT.md) | RED 스켈레톤 D-LOC-01 |
| [report/07.REPORT.md](report/07.REPORT.md) | GREEN `find_blank_coords` |
| [report/08.REPORT.md](report/08.REPORT.md) | GREEN `solution` + Golden 인프라 |
| [report/09.REPORT.md](report/09.REPORT.md) | 코드 스멜·`/refactor-smell` |
| [docs/PRD.md](docs/PRD.md) | Goals, `validate`, T0~T3 |
| [docs/RED-TODO.md](docs/RED-TODO.md) | RED 설계표·G0/G1·Todo |
| [.cursorrules](.cursorrules) | 코딩 세션 Rule SSOT |
| [.cursor/skills/magic-square-tdd/SKILL.md](.cursor/skills/magic-square-tdd/SKILL.md) | RED/GREEN/REFACTOR |
| [prompt/09.Export Transcript.md](prompt/09.Export%20Transcript.md) | STEP 9 세션 Export |

---

## Mom Test 증거

1. "지난주 OO 과제에서 빈칸 2개 넣고 행·열·대각선 합 맞췄는데 **대각선 하나를 빼먹어서 20분 날렸다**."
2. "**마지막에 검토하니** 대각선의 합이 달랐거나 숫자가 겹쳤어."
3. "**둘다야.**"

---

## v0.1 범위

### In Scope (PRD)

| 계층 | 내용 | 상태 |
|------|------|------|
| **Rule** | R1~R5 — 10선·중복·0 없음 | ⏳ `validate()` 미구현 |
| **Command** | `validate(grid)` — Rule ID 목록 | ⏳ |
| **Test Loop** | T0~T3 Red → Green | ⏳ |
| **솔버 (단계)** | `find_blank_coords`, `solution` Step A | ✅ Entity GREEN 2건 |

### Out of Scope (일괄 구현 금지)

- 솔버 **전 단계**·GUI·ECB **한 번에** 전부
- Rule+Test 없는 `SquareValidator` 껍데기

### 거버넌스 (STEP 3~8)

- Boundary 오류 **E001~E007** (E001~E005는 Entity 금지)
- MagicConstant SSOT — `MAGIC_CONSTANT` / `GRID_SIZE` / `MAX_VALUE` / `BLANK_CELL` / `COORD_BASE`

---

## 성공 기준 (Acceptance)

| ID | 기준 |
|----|------|
| SC1 | **두 대각선** 모두 검사 (T1) |
| SC2 | **1~16 중복** 검사 (T2) |
| SC3 | **한 Command**로 즉시 판정 (T3 포함) |

---

## Dual-Track TDD

| Track | Layer | 테스트 (실제·계획) | Mock |
|-------|-------|-------------------|------|
| **Logic** | entity, control | `tests/entity/test_d_*.py` (규약: `test_d_*`), `D-*` | **금지** |
| **UI** | boundary | `tests/test_u_*.py`, `U-*` | **허용** |

**공통 픽스처** ([docs/RED-TODO.md](docs/RED-TODO.md)): **G0** 완성 마방진 · **G1** 빈칸 `(2,2)`, `(3,3)` 1-index · **T1~T3** Mom Test 실패 격자

---

## 워크플로우 (STEP)

```
STEP 1  Mom Test              → report/01.REPORT.md
STEP 2  문제 정의 + PRD       → report/02.REPORT.md
STEP 3  .cursorrules          → report/03.REPORT.md
STEP 4  Skill + Command       → report/04.REPORT.md
STEP 5  RED 설계·계획         → docs/RED-TODO.md, report/05.REPORT.md
STEP 6  RED 스켈레톤 D-LOC-01 → report/06.REPORT.md
STEP 7  GREEN find_blank_coords → report/07.REPORT.md
STEP 8  GREEN solution + Golden → report/08.REPORT.md
STEP 9  코드 스멜·refactor-smell → report/09.REPORT.md
STEP 10+ /refactor-safe · validate RED · D-MIS-01
```

---

## 진행 체크리스트

상세 Given/Then: [docs/RED-TODO.md](docs/RED-TODO.md)

### 권장 순서

1. Logic **B-2** — `validate()` (D-T0 → T1~T3 → R1/R2/R5 → C01)
2. Logic **B-1** — D-MIS-01 → D-VAL-01 (D-LOC-01 · D-SOL-01 ✅)
3. REFACTOR — golden 재연결 · `row_sum()` 추출 ([report/09.REPORT.md](report/09.REPORT.md))
4. UI **Track A** — U-IN-01 ~ U-FLOW-02

### Logic Track — 검증 Command

- [ ] **D-T0** ~ **D-T3**, **D-R1** / **D-R2** / **D-R5**, **D-C01** — `tests/test_d_validate.py` (예정)

### Logic Track — ECB·솔버

- [x] **D-LOC-01** — `find_blank_coords(G1)` → `[(2,2),(3,3)]` (`tests/entity/test_d_loc_01.py`)
- [x] **D-SOL-01** — `solution(G1)` Step A → `[2,2,10,3,3,7]` (`tests/entity/test_d_sol_01.py`)
- [ ] **D-MIS-01** — `find_not_exist_nums(G1)` → `[7, 10]`
- [ ] **D-VAL-01** — `is_magic_square(G0)` → `True`
- [ ] Golden assert 재연결 (P0 refactor)

### UI Track — Boundary

- [ ] **U-IN-01** ~ **U-FLOW-02** — `tests/test_u_*.py` (예정)

---

## 참고

- 문제 정의: Rob Fitzpatrick, *The Mom Test*
- D-* ID SSOT: [.cursor/skills/magic-square-tdd/reference.md](.cursor/skills/magic-square-tdd/reference.md)
- Mom Test 워크북 자가 채점: **7.5 / 10** (Q4·Q5 미답)

---

## License

미정 (학습용 프로젝트)
