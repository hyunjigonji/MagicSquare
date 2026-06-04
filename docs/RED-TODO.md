# MagicSquare — RED 단계 Todo List

**문서:** docs/RED-TODO.md  
**버전:** 0.1  
**일자:** 2026-06-04  
**근거:** `.cursorrules`, `docs/PRD.md`, `.cursor/skills/magic-square-tdd/reference.md`

Dual-Track TDD **RED** 단계 — Boundary(UI)와 Logic(Domain) 설계표를 실행 가능한 Todo로 정리한다.  
각 항목 완료 기준: 해당 테스트 **FAIL** (ImportError·경로 오류는 RED 완료 아님).

---

## 공통 픽스처

| 기호 | 의미 |
|------|------|
| **G0** | 완성 4×4 마방진 — T0·`is_magic_square()` Happy path |
| **G1** | 빈칸 2개(`0`) 부분 격자 — 1-index `(2,2)`, `(3,3)` |
| **T1~T3** | Mom Test 증거 기반 실패 격자 (`docs/PRD.md` §9) |

---

## Track A — UI/Boundary RED

**Layer:** `boundary` · **파일:** `tests/test_u_*.py` · **Mock:** 허용

| Test ID | Given | Then (기대값) | Expected RED Failure |
|---------|-------|---------------|----------------------|
| U-IN-01 | `grid=None` | `E003` `INVALID_NULL` | `ModuleNotFoundError` 또는 `AssertionError` |
| U-IN-02 | `grid=3×4` | `E001` `INVALID_SIZE` | `AssertionError` |
| U-IN-03 | 빈칸 0개 | `E002` `INVALID_BLANKS` | `AssertionError` |
| U-OUT-01 | 유효 입력 **G1** | `len(result)==6` | `pytest.fail()` / `AssertionError` |
| U-FLOW-02 | `grid=None` | Control `execute()` **0회** | `pytest.fail()` / `AssertionError` |

### Todo

- [ ] **U-IN-01** — `grid=None` → `E003 INVALID_NULL` (`tests/test_u_input.py`)
- [ ] **U-IN-02** — `grid=3×4` → `E001 INVALID_SIZE` (`tests/test_u_input.py`)
- [ ] **U-IN-03** — 빈칸 0개 → `E002 INVALID_BLANKS` (`tests/test_u_input.py`)
- [ ] **U-OUT-01** — 유효 입력 G1 → `len(result)==6` (`tests/test_u_output.py`)
- [ ] **U-FLOW-02** — `grid=None` → `execute()` 0회 호출 (`tests/test_u_flow.py`)

**규칙:** E001~E005는 Boundary 전용 — Entity로 내리지 않음.

---

## Track B — Domain/Logic RED

**Layer:** `entity` / `control` · **파일:** `tests/test_d_*.py` · **Mock:** 금지

### B-1. ECB·솔버 (`.cursorrules` 기준)

| Test ID | 대상 함수 | Given / Then | Invariant |
|---------|-----------|--------------|-----------|
| D-LOC-01 | `find_blank_coords()` | G1 → `[(2,2),(3,3)]` | I6 row-major |
| D-MIS-01 | `find_not_exist_nums()` | G1 → `[7, 10]` 오름차순 | I7, I11 |
| D-VAL-01 | `is_magic_square()` | G0 → `True` | I1~I5 |
| D-SOL-01 | `solution()` | G1 Step A 성공 | I8 (`int[6]` 1-index) |

#### Todo

- [ ] **D-LOC-01** — `find_blank_coords(G1)` → `[(2,2),(3,3)]` (`tests/test_d_solver.py`)
- [ ] **D-MIS-01** — `find_not_exist_nums(G1)` → `[7, 10]` (`tests/test_d_solver.py`)
- [ ] **D-VAL-01** — `is_magic_square(G0)` → `True` (`tests/test_d_validate.py`)
- [ ] **D-SOL-01** — `solution(G1)` Step A 성공 (`tests/test_d_solver.py`)

### B-2. 검증 Command (PRD · `reference.md` — v0.1 우선)

| Test ID | 대상 함수 | Given / Then | Rule / PRD |
|---------|-----------|--------------|------------|
| D-T0 | `validate()` | G0 → `ok=true`, `failures=[]` | T0 |
| D-T1 | `validate()` | 대각선 하나 ≠34 → `R3` | T1, SC1 |
| D-T2 | `validate()` | 숫자 중복 → `R4` | T2, SC2 |
| D-T3 | `validate()` | R3+R4 동시 | T3, SC3 |
| D-R1 | `validate()` | 행 합 ≠34 → `R1` | R1 |
| D-R2 | `validate()` | 열 합 ≠34 → `R2` | R2 |
| D-R5 | `validate()` | 0 잔존 → `R5` | R5 |
| D-C01 | `constants` | `34`/`16`/`4` SSOT | `.cursorrules` |

#### Todo (PRD v0.1 1차 — `/tdd-red` 권장 순서)

- [ ] **D-T0** — G0 완성 격자 → `ok=true` (`tests/test_d_validate.py`)
- [ ] **D-T1** — T1 격자 → `failures`에 `R3` (`tests/test_d_validate.py`)
- [ ] **D-T2** — T2 격자 → `failures`에 `R4` (`tests/test_d_validate.py`)
- [ ] **D-T3** — T3 격자 → `R3` + `R4` (`tests/test_d_validate.py`)
- [ ] **D-R1** — 행 합 ≠34 → `R1` (`tests/test_d_validate.py`)
- [ ] **D-R2** — 열 합 ≠34 → `R2` (`tests/test_d_validate.py`)
- [ ] **D-R5** — 0 잔존 → `R5` (`tests/test_d_validate.py`)
- [ ] **D-C01** — MagicConstant SSOT (`tests/test_d_constants.py`)

---

## 권장 진행 순서

1. **B-2** `D-T0` → `D-T1` → `D-T2` → `D-T3` (PRD v0.1, Mom Test 증거)
2. **B-2** `D-R1`, `D-R2`, `D-R5`, `D-C01`
3. **B-1** `D-LOC-01` → `D-MIS-01` → `D-VAL-01` → `D-SOL-01` (ECB·솔버)
4. **Track A** `U-IN-01` ~ `U-FLOW-02` (Boundary — E001~E007 명세 후속)

---

## RED 완료 체크 (항목당)

- [ ] Phase 선언: `Phase: RED`, `Layer`, `Track`, `Target: D-*` 또는 `U-*`
- [ ] AAA 테스트 작성 (`tests/`만 수정)
- [ ] `pytest tests/test_*_<file>.py::<test_name> -v` → **FAILED**
- [ ] FAIL 원인 1줄 기록 → GREEN으로 전환

---

## 참고

| 문서 | 경로 |
|------|------|
| PRD | `docs/PRD.md` |
| D-* ID SSOT | `.cursor/skills/magic-square-tdd/reference.md` |
| TDD RED Command | `.cursor/commands/tdd-red.md` |
| Cursor Rules | `.cursorrules` |
