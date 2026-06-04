# Review ECB — 계약 위반 리뷰

MagicSquare **ECB·도메인 계약**만 읽고 검사한다. **코드·테스트·문서 수정 금지.**

근거: `.cursorrules`, `docs/PRD.md`, `src/magicsquare/`, `tests/`.

---

## 필수 선언

응답 **첫 줄**에 반드시 출력:

```
Phase: review | Scope: ECB·계약 | Mode: read-only
```

---

## 절차

1. **범위 확인** — 사용자가 지정한 파일·디렉터리. 미지정 시 `src/magicsquare/` + `tests/` 전체.
2. **Read/Grep만** — import, `34`/`16`/`4` 리터럴, `E00*`, `mock`/`patch`, 솔버 반환·좌표 사용처 검색.
3. **5항목 체크** — 아래 [체크리스트](#체크리스트) 각각 PASS/FAIL 판정.
4. **표로 보고** — **위반만** [리뷰 표](#리뷰-표)에 기록. 위반 0건이면 "위반 없음" 1줄.
5. **수정 제안 금지** — 리팩터·패치·커밋 하지 않는다. 위반 위치(파일:줄)와 계약 조항만 명시.

---

## 체크리스트

| # | 항목 | 계약 (`.cursorrules`) | 검사 방법 |
|---|------|----------------------|-----------|
| 1 | **import 방향** | boundary → control → entity 단방향. Entity는 `entity` 패키지 **외부 import 금지** | `src/` 각 Layer의 `import`/`from` 역방향·횡단 참조 |
| 2 | **Entity E001~E005** | E001~E005 생성·처리·변환 **Entity 금지** — Boundary 전용 | `entity/` 내 `E001`~`E005` 문자열·예외·오류 타입 |
| 3 | **int[6] 1-index** | 솔버 성공 출력 `[r1,c1,n1,r2,c2,n2]`, `(r,c)` **1-index** | 솔버·Control·Boundary 반환/문서/테스트 기대값이 0-index 아닌지 |
| 4 | **MagicConstant SSOT** | `34`/`16`/`4` 리터럴 **산재 금지** — `entity` constants 단일 정의 후 import | `src/`·`tests/` 리터럴 vs `MAGIC_CONSTANT` 등 import |
| 5 | **Logic Track Domain Mock** | `test_d_*.py`에서 Entity/Control **mock·patch 금지** | `tests/test_d_*.py`의 `unittest.mock`, `patch`, `@mock` |

---

## 리뷰 표

**위반 있는 경우만** 아래 표를 채운다. 여러 위반이면 행 추가.

| 체크 | 파일:줄 | 위반 내용 | 계약 |
|------|---------|-----------|------|
| import 방향 | `src/.../foo.py:12` | entity가 boundary import | ECB 단방향 |
| Entity E001~E005 | `src/.../bar.py:45` | Entity에서 E003 raise | E001~E005 Boundary 전용 |
| int[6] 1-index | `src/.../solver.py:88` | 좌표 0-index 반환 | `[r,c,...]` 1-index |
| MagicConstant SSOT | `src/.../rules.py:7` | `sum == 34` 리터럴 | constants import |
| Logic Domain Mock | `tests/test_d_x.py:22` | `@patch("...entity...")` | Logic Track mock 금지 |

**위반 0건:**

```markdown
## ECB 리뷰 — 위반 없음

- Scope: ...
- 체크 5/5 PASS
```

**위반 1건 이상:**

```markdown
## ECB 리뷰 — N건 위반

(위 표)

- 수정은 하지 않음. GREEN/REFACTOR 또는 별도 요청에서 처리.
```

---

## 금지

| 금지 | 이유 |
|------|------|
| **코드·테스트·문서 수정** | read-only 리뷰 |
| **pytest 실행·구현 제안** | 계약 위반 표만 |
| **스타일·네이밍·성능 코멘트** | ECB·계약 외 항목 제외 |
| **git commit / push** | 사용자 요청 시만 |
