# TDD RED — 실패 테스트 먼저

MagicSquare Dual-Track TDD **RED 단계만** 수행한다. `src/` 구현·GREEN·REFACTOR는 하지 않는다.

근거: `.cursorrules`, `docs/PRD.md`, D-* ID는 `.cursor/skills/magic-square-tdd/reference.md`.

---

## 필수 선언

응답 **첫 줄**에 반드시 출력:

```
Phase: red | Layer: entity | control | boundary | Track: Logic | UI | Target: D-<id> | U-<id>
```

- **Logic Track** → `tests/test_d_*.py`, ID `D-*`
- **UI Track** → `tests/test_u_*.py`, ID `U-*`

---

## 절차

1. **ID 확인** — `reference.md`에서 `D-*`/`U-*` 선택. PRD T0~T3·R1~R5·SC1~SC3와 1:1 연결. 없으면 규칙에 맞게 부여.
2. **Track·Layer** — entity/control → Logic. boundary → UI. Logic Track에서 mock/patch **금지**.
3. **AAA 테스트 작성** — `tests/`에만 추가·수정.
   - **Arrange** — Mom Test 격자(T1 대각선, T2 중복, T3 동시) 또는 Rule별 실패 입력
   - **Act** — `validate(grid)` 등 대상 API 호출(아직 없으면 import 실패 → RED 아님, 테스트·경로 수정)
   - **Assert** — 기대 Rule ID·`ok=false` 등 **엄격한** assertion. 완화 금지.
4. **pytest 실행** — 대상 테스트 **1개**만 실행.
5. **FAIL 확인** — **반드시 FAIL**. PASS면 테스트·기대값 재검토. ImportError/수집 오류는 RED 완료가 아님.
6. **보고** — 아래 [보고](#보고) 형식으로 마무리.

---

## pytest 예시 (bash)

Logic Track — 단일 테스트 (RED 확인):

```bash
pytest tests/test_d_validate.py::test_d_t1_wrong_diagonal -v
```

UI Track — 단일 테스트:

```bash
pytest tests/test_u_cli.py::test_u_e001_invalid_input -v
```

파일 단위 (여러 RED 후보 중 하나만 FAIL이어야 함):

```bash
pytest tests/test_d_validate.py -v
```

**RED 완료 기준:** 대상 테스트 **FAILED** (not passed, not error from wrong path).

---

## 보고

RED 완료 시 아래만 출력:

```markdown
## RED 완료

- Target: D-T1 (또는 U-...)
- pytest: FAILED — [한 줄 FAIL 요약, 예: AssertionError: failures missing R3]
- 변경 파일: tests/test_d_validate.py (tests/만)
- 다음: GREEN — src/ 최소 구현
```

---

## 금지

| 금지 | 이유 |
|------|------|
| **`src/` 수정** | RED는 테스트만 |
| **Logic Track Domain Mock** | `unittest.mock`, `patch`, Entity/Control stub 금지 |
| **assert 완화** | `pytest.approx`, 조건 삭제, 기대값 느슨하게 변경 |
| **`skip` / `xfail` / 테스트 삭제** | GREEN을 우회하는 수단 |
| **GREEN·REFACTOR** | 별도 Command·Phase에서 수행 |
