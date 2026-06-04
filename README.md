# MagicSquare

4×4 부분 마방진(빈칸 2개, 1~16, 합 34) 과제에서 **늦은 검토로 시간을 낭비하는 문제**를 Mom Test로 정의하고, **10선 검증**을 최소 제품으로 구현하는 학습 프로젝트입니다.

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

---

## 페르소나

4×4 격자, 빈칸 2개(0), 1~16, 합 34 맞추는 **학습자** — 프로그래밍/OO 수업에서 부분 마방진 과제를 손·코드로 다룸.

---

## 프로젝트 구조

```
MagicSquare/
├── README.md                 # 이 파일
├── docs/
│   └── PRD.md                # 제품 요구사항 (v0.1 초안)
├── report/
│   ├── 01.REPORT.md          # STEP 1 — Mom Test 인터뷰 보고서
│   └── 02.REPORT.md          # 문제 정의 보고서 (Problem Definition)
└── prompt/
    ├── 01.Export Transcript.md   # STEP 1 인터뷰 Transcript
    └── 02.Export Transcript.md   # Cursor 세션 전체 Export
```

> **Note:** 구현 코드(`src/`, 테스트)는 아직 없습니다. 현재 단계는 **문제 정의 · PRD**까지입니다.

---

## 문서 가이드

| 문서 | 용도 |
|------|------|
| [report/01.REPORT.md](report/01.REPORT.md) | Mom Test 인터뷰 결과, 증거 3줄, 표면/진짜 문제 |
| [report/02.REPORT.md](report/02.REPORT.md) | R-G-I-O, 성공 기준, Rule R1~R5, 세션 3 범위 |
| [docs/PRD.md](docs/PRD.md) | Goals/Non-Goals, FR, Acceptance, 테스트 T0~T3 |
| [prompt/01.Export Transcript.md](prompt/01.Export%20Transcript.md) | 인터뷰 Q&A 원문 |
| [prompt/02.Export Transcript.md](prompt/02.Export%20Transcript.md) | 워크북·채점·시뮬레이션 포함 전체 대화 |

---

## Mom Test 증거

1. "지난주 OO 과제에서 빈칸 2개 넣고 행·열·대각선 합 맞췄는데 **대각선 하나를 빼먹어서 20분 날렸다**."
2. "**마지막에 검토하니** 대각선의 합이 달랐거나 숫자가 겹쳤어."
3. "**둘다야.**"

---

## v0.1 범위

### In Scope (세션 3)

| 계층 | 내용 |
|------|------|
| **Rule** | R1~R5 — 행·열·대각선 합 34, 1~16 중복, 0 없음 |
| **Command** | `validate(grid)` — 통과/실패 + Rule ID |
| **(Skill)** | 검증 체크리스트 (선택) |
| **Test Loop** | T1~T3 Red → Green (Mom Test 증거 기반) |

### Out of Scope

- MagicSquare **Solver** (빈칸 자동 채우기)
- **GUI** / GridUI
- **ECB 전체** (Entity · Control · Boundary)
- 이름만 있는 `SquareValidator` 껍데기

---

## 성공 기준 (Acceptance)

| ID | 기준 |
|----|------|
| SC1 | **두 대각선** 모두 검사 (T1) |
| SC2 | **1~16 중복** 검사 (T2) |
| SC3 | **한 Command**로 즉시 판정 (T3 포함) |

---

## 워크플로우 (STEP)

```
STEP 1  Mom Test 인터뷰     → report/01.REPORT.md
STEP 2  문제 정의           → report/02.REPORT.md
STEP 3  PRD                 → docs/PRD.md
STEP 4+ Rule · Command · Test Loop 구현 (예정)
```

---

## 참고

- 문제 정의 방법: Rob Fitzpatrick, *The Mom Test*
- Mom Test 워크북 자가 채점: **7.5 / 10** (Q4·Q5 미답, 10선·1~16 증거 보강 필요)

---

## License

미정 (학습용 프로젝트)
