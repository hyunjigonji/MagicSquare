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
| Magic constant | **34** |
| 10선 | 행 4 + 열 4 + 주대각선 + 부대각선 |
| 솔버 출력 | `int[6]` = `[r1,c1,n1,r2,c2,n2]` — 좌표 **1-index** (`.cursorrules`) |

---

## 페르소나

4×4 격자, 빈칸 2개(0), 1~16, 합 34 맞추는 **학습자** — 프로그래밍/OO 수업에서 부분 마방진 과제를 손·코드로 다룸.

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
│   ├── 01.REPORT.md          # STEP 1 — Mom Test
│   ├── 02.REPORT.md          # STEP 2 — 문제 정의
│   ├── 03.REPORT.md          # STEP 3 — .cursorrules 거버넌스
│   ├── 04.REPORT.md          # STEP 4 — Skill·Command
│   └── 05.REPORT.md          # STEP 5 — RED 설계·계획
├── .cursor/
│   ├── commands/             # /tdd-red, /review-ecb
│   └── skills/magic-square-tdd/
├── src/magicsquare/          # (예정) entity / control / boundary
├── tests/                    # (예정) test_d_* · test_u_* · entity/
└── prompt/
    ├── 01.Export Transcript.md … 05.Export Transcript.md
```

> **현재 단계:** STEP 5(RED 설계·계획) 완료. **STEP 6+** — `src/`·`tests/`에 RED → GREEN → REFACTOR ([docs/RED-TODO.md](docs/RED-TODO.md)).

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

TDD 세션 시작 시 Agent는 `Phase` / `Layer` / `Track` / `Target`을 선언한다. RED만: [.cursor/commands/tdd-red.md](.cursor/commands/tdd-red.md).

---

## 문서 가이드

| 문서 | 용도 |
|------|------|
| [report/01.REPORT.md](report/01.REPORT.md) | Mom Test 인터뷰, 증거 3줄 |
| [report/02.REPORT.md](report/02.REPORT.md) | R-G-I-O, Rule R1~R5, SC1~SC3 |
| [report/03.REPORT.md](report/03.REPORT.md) | 8계층 · `.cursorrules` v0.1 |
| [report/04.REPORT.md](report/04.REPORT.md) | Skill `magic-square-tdd`, slash Command |
| [report/05.REPORT.md](report/05.REPORT.md) | RED 설계·D-LOC/U-IN 계획, G1 SSOT |
| [docs/PRD.md](docs/PRD.md) | Goals, `validate`, T0~T3, Acceptance |
| [docs/RED-TODO.md](docs/RED-TODO.md) | RED 설계표·픽스처 G0/G1·진행 Todo |
| [.cursorrules](.cursorrules) | 코딩 세션 Rule SSOT |
| [.cursor/skills/magic-square-tdd/SKILL.md](.cursor/skills/magic-square-tdd/SKILL.md) | RED/GREEN/REFACTOR 절차 |
| [prompt/01.Export Transcript.md](prompt/01.Export%20Transcript.md) | 인터뷰 Q&A |
| [prompt/02.Export Transcript.md](prompt/02.Export%20Transcript.md) ~ [05](prompt/05.Export%20Transcript.md) | STEP별 Cursor Export |

---

## Mom Test 증거

1. "지난주 OO 과제에서 빈칸 2개 넣고 행·열·대각선 합 맞췄는데 **대각선 하나를 빼먹어서 20분 날렸다**."
2. "**마지막에 검토하니** 대각선의 합이 달랐거나 숫자가 겹쳤어."
3. "**둘다야.**"

---

## v0.1 범위

### In Scope (세션 3 — PRD)

| 계층 | 내용 |
|------|------|
| **Rule** | R1~R5 — 행·열·대각선 합 34, 1~16 중복, 0 없음 |
| **Command** | `validate(grid)` — 통과/실패 + Rule ID |
| **Test Loop** | T0~T3 Red → Green (Mom Test 증거) |

### Out of Scope (PRD v0.1)

- 빈칸 **자동 채우기** Solver (일괄 구현 금지 — 단계별 RED는 RED-TODO B-1)
- **GUI** / GridUI
- ECB **한 번에** 전부 구현
- Rule+Test 없는 `SquareValidator` 껍데기

### 거버넌스 확장 (STEP 3~4, PRD revision 예정)

- Boundary 오류 **E001~E007** (E001~E005는 Entity 금지)
- 솔버 `int[6]` 1-index, MagicConstant SSOT (`34`/`16`/`4`)

---

## 성공 기준 (Acceptance)

| ID | 기준 |
|----|------|
| SC1 | **두 대각선** 모두 검사 (T1) |
| SC2 | **1~16 중복** 검사 (T2) |
| SC3 | **한 Command**로 즉시 판정 (T3 포함) |

---

## Dual-Track TDD

| Track | Layer | 테스트 | Mock |
|-------|-------|--------|------|
| **Logic** | entity, control | `tests/test_d_*.py`, `D-*` | **금지** |
| **UI** | boundary | `tests/test_u_*.py`, `U-*` | **허용** |

**공통 픽스처** ([docs/RED-TODO.md](docs/RED-TODO.md)): **G0** 완성 마방진 · **G1** 빈칸 `(2,2)`, `(3,3)` 1-index · **T1~T3** Mom Test 실패 격자

---

## 워크플로우 (STEP)

```
STEP 1  Mom Test 인터뷰     → report/01.REPORT.md
STEP 2  문제 정의           → report/02.REPORT.md
STEP 3  PRD + .cursorrules  → docs/PRD.md, report/03.REPORT.md
STEP 4  Skill·Command       → .cursor/skills/, report/04.REPORT.md
STEP 5  RED 설계·계획       → docs/RED-TODO.md, report/05.REPORT.md
STEP 6+ RED → GREEN → REFACTOR
```

---

## RED 단계 체크리스트

Dual-Track **RED** — `tests/`에 실패 테스트를 먼저 작성한다.  
**완료 기준:** 대상 테스트 **FAILED** (`AssertionError` 등). **RED 아님:** ImportError·수집 오류만으로 종료.

상세 Given/Then·Track A 표: [docs/RED-TODO.md](docs/RED-TODO.md)

### 권장 진행 순서

1. Logic **B-2** — `validate()` (D-T0 → T1~T3 → R1/R2/R5 → C01)
2. Logic **B-1** — ECB·솔버 (D-LOC-01 → D-MIS-01 → D-VAL-01 → D-SOL-01)
3. UI **Track A** — Boundary (U-IN-01 ~ U-FLOW-02)

### Logic Track — 검증 Command (우선)

`tests/test_d_*.py` · Domain Mock **금지**

- [ ] **D-T0** — G0 → `ok=true` (`tests/test_d_validate.py`)
- [ ] **D-T1** — T1 → `R3` (`tests/test_d_validate.py`)
- [ ] **D-T2** — T2 → `R4` (`tests/test_d_validate.py`)
- [ ] **D-T3** — T3 → `R3` + `R4` (`tests/test_d_validate.py`)
- [ ] **D-R1** / **D-R2** / **D-R5** — Rule별 실패 (`tests/test_d_validate.py`)
- [ ] **D-C01** — MagicConstant SSOT (`tests/test_d_constants.py`)

### Logic Track — ECB·솔버

- [ ] **D-LOC-01** — `find_blank_coords(G1)` → `[(2,2),(3,3)]` (`tests/test_d_solver.py` 또는 `tests/entity/test_d_loc_01.py`)
- [ ] **D-MIS-01** — `find_not_exist_nums(G1)` → `[7, 10]` (`tests/test_d_solver.py`)
- [ ] **D-VAL-01** — `is_magic_square(G0)` → `True` (`tests/test_d_validate.py`)
- [ ] **D-SOL-01** — `solution(G1)` Step A (`tests/test_d_solver.py`)

### UI Track — Boundary

`tests/test_u_*.py` · Mock **허용** · E001~E005 Boundary 전용

- [ ] **U-IN-01** — `grid=None` → `E003` `INVALID_NULL` (`tests/test_u_input.py`)
- [ ] **U-IN-02** — `grid=3×4` → `E001` `INVALID_SIZE` (`tests/test_u_input.py`)
- [ ] **U-IN-03** — 빈칸 0개 → `E002` `INVALID_BLANKS` (`tests/test_u_input.py`)
- [ ] **U-OUT-01** — G1 → `len(result)==6` (`tests/test_u_output.py`)
- [ ] **U-FLOW-02** — `grid=None` → Control `execute()` 0회 (`tests/test_u_flow.py`)

### RED 완료 체크 (항목당)

- [ ] `Phase: RED` · `Layer` · `Track` · `Target: D-*` / `U-*`
- [ ] AAA 테스트 (`tests/`만, `src/` 수정 금지)
- [ ] `python -m pytest tests/...::<test_name> -v` → **FAILED**
- [ ] FAIL 원인 1줄 기록 → GREEN

---

## 참고

- 문제 정의: Rob Fitzpatrick, *The Mom Test*
- Mom Test 워크북 자가 채점: **7.5 / 10** (Q4·Q5 미답)
- D-* ID SSOT: [.cursor/skills/magic-square-tdd/reference.md](.cursor/skills/magic-square-tdd/reference.md)

---

## License

미정 (학습용 프로젝트)
