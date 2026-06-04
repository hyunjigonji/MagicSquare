---
name: magic-square-tdd
description: MagicSquare Dual-Track TDD·ECB 개발 시 Agent가 따를 절차. validate·Rule R1~R5·entity/control/boundary 구현, test_d_*/test_u_* 작성, RED/GREEN/REFACTOR, pytest 실행 시 적용.
---

# MagicSquare Dual-Track TDD

`.cursorrules`, `docs/PRD.md`, `report/02.REPORT.md`와 함께 사용한다. D-* ID 목록은 [reference.md](reference.md).

## Skill을 켜는 때

다음 **하나 이상**이면 이 Skill을 읽고 절차를 따른다.

| 트리거 | 예 |
|--------|-----|
| TDD 사이클 | RED / GREEN / REFACTOR, "테스트 먼저", T0~T3 |
| ECB 계층 작업 | `entity/`, `control/`, `boundary/` 코드·테스트 |
| Dual-Track | Logic(entity/control) vs UI(boundary) 테스트 |
| 검증·솔버 구현 | `validate`, R1~R5, Mom Test 격자(T1~T3) |
| pytest 규약 | `test_d_*`, `test_u_*`, `D-*`, `U-*` |

**켜지 않을 때:** 문서만 수정, Mom Test·PRD 작성, git commit, v0.1 Non-Goals(Solver·UI·ECB 일괄 구현).

---

## 세션 시작 선언 (매 Phase)

작업 첫 줄에 반드시 출력:

```
Phase: RED | GREEN | REFACTOR
Layer: entity | control | boundary
Track: Logic | UI
Target: D-<id> (또는 U-<id>)
```

---

## RED — 7단계

1. **범위 고정** — PRD FR·Rule ID·Acceptance(SC1~SC3)와 이번 테스트 1개만 연결한다.
2. **Track·Layer 결정** — Logic(entity/control) vs UI(boundary). [Track 표](#logic-track-vs-ui-track) 확인.
3. **테스트 ID** — [reference.md](reference.md)에서 `D-*`/`U-*` 선택. 없으면 PRD T0~T3·R1~R5에 맞춰 부여하고 reference.md에 추가.
4. **파일·함수** — Logic → `tests/test_d_<주제>.py`, docstring/주석에 `D-<id>`. UI → `tests/test_u_<주제>.py`, `U-<id>`.
5. **격자·픽스처** — Mom Test 증거 기반 실패 격자 사용(T1 대각선, T2 중복, T3 동시). Logic Track에서 **mock/patch 금지**.
6. **실행** — 대상 테스트만 실행(아래 [Test/Review Loop](#testreview-loop)).
7. **RED 확인** — **FAIL**이어야 한다. 통과하면 테스트·기대값을 재검토. FAIL 원인 1줄 기록 후 GREEN으로 넘어간다.

---

## GREEN — 6단계

1. **선언** — Phase/Layer/Track/Target 재출력.
2. **최소 구현** — RED를 통과시키는 **가장 작은** 코드만 해당 Layer에 추가. 다른 Layer·기능 확장 금지.
3. **ECB·오류 경계** — Entity는 순수 도메인만. E001~E005는 Entity에서 생성·처리·변환하지 않는다(아래 [금지/허용](#ecbmocke001e007-금지허용)).
4. **MagicConstant SSOT** — `34`/`16`/`4` 리터럴 산재 금지. `entity` constants에서 import.
5. **실행** — 대상 테스트 PASS → 해당 Track 회귀 pytest(Loop 표).
6. **GREEN 금지** — assert 완화, `@pytest.mark.skip`, `xfail`, 테스트 삭제로 통과시키지 않는다.

---

## REFACTOR — 6단계

1. **선언** — Phase/Layer/Track.
2. **테스트 동결** — 행위·기대값 변경 없이 구조만 개선(이름, 추출, ECB 경계, 중복 제거).
3. **의존 방향** — boundary → control → entity 단방향 유지. Entity 외부 import 금지.
4. **리터럴 정리** — 남은 magic number를 constants로 이동.
5. **회귀** — Logic: `pytest tests/test_d_*.py`. UI 작업 포함 시 `test_u_*.py` 추가. 최종 `pytest tests/`.
6. **완료 보고** — 아래 [완료 보고](#완료-보고) 템플릿으로 마무리.

---

## Logic Track vs UI Track

| | **Logic Track** | **UI Track** |
|---|-----------------|--------------|
| **대상 Layer** | entity, control | boundary |
| **테스트 파일** | `tests/test_d_*.py` | `tests/test_u_*.py` |
| **테스트 ID** | `D-*` | `U-*` |
| **Domain Mock** | **금지** — 실제 객체·순수 함수만 | **허용** — 입력 스텁, stdout 캡처 등 |
| **patch/mock** | Entity·Control mock/patch **금지** | Boundary I/O mock **허용** |
| **검증 초점** | R1~R5, `validate`, 솔버 도메인 | CLI/UI, E001~E007, 입출력 형식 |
| **우선 순위(v0.1)** | T0~T3, SC1~SC3 | PRD milestone 이후 |

---

## ECB·Mock·E001~E007 금지/허용

### ECB 의존

```
Boundary → Control → Entity
```

| Layer | 역할 | 허용 | 금지 |
|-------|------|------|------|
| **Entity** | 규칙·솔버·값 객체 | 순수 Python, constants | 외부 패키지 import, I/O, E001~E005 |
| **Control** | 유스케이스 조율 | Entity 호출, Boundary DTO 변환 | Boundary 오류를 Entity로 내림 |
| **Boundary** | CLI/UI, 입력 검증 | E001~E007 발생·표시 | Entity 규칙 직접 구현 |

### Mock

| Track | Mock | patch |
|-------|------|-------|
| Logic | **금지** | Entity/Control **금지** |
| UI | **허용** | stdin/stdout·Boundary **허용** |

### 오류 코드 E001~E007

| 코드 | 담당 | Entity | Boundary/Control |
|------|------|--------|------------------|
| **E001~E005** | 입력·형식·범위 | **처리 금지** | Boundary **전용** |
| **E006~E007** | (명세 후속) | **처리 금지** | Boundary 또는 Control — PRD revision 따름 |

### v0.1 구현 금지 (Skill과 함께 확인)

- Solver·UI·ECB 전체 일괄 구현
- `SquareValidator` 등 Rule+Test 없는 빈 껍데기
- Logic Track에서 GREEN을 mock으로 달성

---

## Test/Review Loop

| 시점 | 명령 | 통과 기준 |
|------|------|-----------|
| **RED 직후** | `pytest tests/test_d_<file>.py::test_<name> -v` (또는 `test_u_*`) | **FAIL** (ImportError는 RED 아님 → 경로·패키지 수정) |
| **GREEN 직후** | 위 단일 테스트 + `pytest tests/test_d_*.py -v` | 대상 **PASS**, 기존 Logic **회귀 없음** |
| **UI GREEN** | `pytest tests/test_u_*.py -v` | 대상·기존 UI PASS |
| **REFACTOR 중·후** | `pytest tests/test_d_*.py -v` → `pytest tests/ -v` | 전체 PASS |
| **Layer/Track 전환 전** | `pytest tests/ -v` | 전체 PASS 후 다음 RED |
| **세션 종료** | `pytest tests/ -v` | 0 failed; SC1~SC3 해당 D-* 모두 PASS |

**Review Loop:** pytest 실패 시 구현을 고치기 **전에** Phase가 RED인지 GREEN인지 확인. RED에서 통과한 테스트는 기대값·격자 오류. GREEN에서 실패하면 회귀 — REFACTOR 전 GREEN 커밋(또는 stash) 기준으로 되돌린다.

---

## 완료 보고

Phase 사이클·Track 전환·세션 종료 시 아래 형식으로 보고:

```markdown
## TDD 완료 보고

- Phase / Layer / Track / Target: ...
- 추가·수정 테스트: D-... (PASS/FAIL)
- 구현 파일: ...
- pytest: `...` → N passed, 0 failed
- PRD 정합: SC? / T? / R?
- ECB 위반 없음: Entity import / E001~E005 / Mock
- 다음 RED 후보: D-...
```

---

## 참고

- Rule SSOT: `.cursorrules`
- 제품 요구: `docs/PRD.md` (T0~T3, R1~R5, Non-Goals)
- D-* ID: [reference.md](reference.md)
