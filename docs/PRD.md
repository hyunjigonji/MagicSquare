# MagicSquare — Product Requirements Document (PRD)

**문서:** docs/PRD.md  
**버전:** 0.1 (초안)  
**일자:** 2026-06-04  
**상태:** Draft  
**근거:** [Problem Definition Report](../Report/01.MagicSquare_ProblemDefinition_Report.md)

---

## 1. Overview

MagicSquare는 4×4 부분 마방진(빈칸 2개, 1~16, 합 34) 과제에서 **늦은 검토로 인한 시간 낭비**를 줄이기 위한 **검증(validation) 최소 제품**이다.

**한 줄 요약:** 채운 격자가 **10선 합 34**와 **1~16 중복 없음**을 **한 번의 실행**으로 판정한다.

---

## 2. Problem Statement

### 2.1 진짜 문제

4×4 부분 마방진 과제에서 빈칸 2개를 채운 뒤 행·열만 맞다고 보고 넘어갔다가, 마지막 검토에서 대각선 합 불일치와 숫자 중복을 동시에 발견해 **20분**을 허비한다.

### 2.2 Mom Test 증거

1. "지난주 OO 과제에서 빈칸 2개 넣고 행·열·대각선 합 맞췄는데 **대각선 하나를 빼먹어서 20분 날렸다**."
2. "**마지막에 검토하니** 대각선의 합이 달랐거나 숫자가 겹쳤어."
3. "**둘다야.**"

---

## 3. Goals & Non-Goals

### 3.1 Goals

| ID | Goal |
|----|------|
| G1 | 완성 격자에 대해 **10선**(행4+열4+대각선2) 합 34 검증 |
| G2 | **1~16 중복·누락** 검출 |
| G3 | **한 번의 Command**로 통과/실패 + **실패 Rule ID** 반환 |
| G4 | Mom Test 증거 기반 **T1~T3** 테스트 통과 (Test Loop) |

### 3.2 Non-Goals (Out of Scope — v0.1)

| 항목 | 이유 |
|------|------|
| MagicSquare **Solver** (빈칸 자동 채우기) | 표면 문제 — 솔루션 선행 |
| **GUI** / GridUI / 공유 링크 | 검증 Command만으로 SC3 충족 가능 |
| **ECB 전체** 구현 | 세션 3 범위 외 |
| **SquareValidator** 이름만 있는 빈 껍데기 | Rule+Test 없는 형식 구현 금지 |

---

## 4. Users & Persona

| 항목 | 내용 |
|------|------|
| **Primary user** | 4×4 격자, 빈칸 2개(0), 1~16, 합 34 맞추는 **학습자** |
| **Context** | 프로그래밍/OO 수업 부분 마방진 과제 |
| **Pain** | 행·열만 확인 → 대각선·중복은 마지막에야 발견 |

---

## 5. R-G-I-O

| | |
|---|---|
| **Role** | 부분 마방진 과제 학습자 |
| **Goal** | 제출 전 대각선 누락·숫자 중복 조기 발견 |
| **Input** | `int[4][4]` — 값 0~16, 0=빈칸 |
| **Output** | `{ ok: bool, failures: RuleId[] }` 또는 동등 구조 |

---

## 6. Domain Specification

### 6.1 Grid

- 크기: **4×4**
- 완성 격자: 각 칸 **1~16** 정확히 1회
- 부분 격자: **0** = 빈칸, 최대 **2칸**
- **Magic constant:** **34**

### 6.2 Ten Lines (10선)

| # | Line |
|---|------|
| 1–4 | Row 0..3 |
| 5–8 | Col 0..3 |
| 9 | Main diagonal (0,0)→(3,3) |
| 10 | Anti diagonal (0,3)→(3,0) |

완성 격자 검증 시 각 line sum **= 34**.

---

## 7. Functional Requirements

### 7.1 Rule Layer

| Rule ID | Requirement | Priority |
|---------|-------------|----------|
| R1 | 각 행 합 = 34 (0 제외 완성 격자) | P0 |
| R2 | 각 열 합 = 34 | P0 |
| R3 | 주대각선·부대각선 합 = 34 (**둘 다**) | P0 |
| R4 | 1~16 중복 없음 (0 제외) | P0 |
| R5 | 0 없음 (완성 격자 모드) | P1 |

### 7.2 Command Layer

| ID | Requirement |
|----|-------------|
| C1 | `validate(grid: int[4][4]) -> ValidationResult` 단일 진입점 |
| C2 | 실패 시 **Rule ID** 목록 반환 (예: `["R3", "R4"]`) |
| C3 | CLI/REPL에서 4×4 입력 후 즉시 실행 가능 (형식은 구현 선택) |
| C4 | Solver·UI 호출 **하지 않음** |

### 7.3 Skill Layer (Optional — P2)

| ID | Requirement |
|----|-------------|
| S1 | 수동 체크리스트: 행 → 열 → 대각선(2) → 1~16 중복 |
| S2 | 실패 메시지 → "어느 줄/칸을 다시 볼지" 1줄 가이드 |

### 7.4 Test Loop

| ID | Requirement |
|----|-------------|
| TL1 | T1~T3 테스트 **선작성(Red)** 후 구현(Green) |
| TL2 | CI 또는 로컬에서 `validate` + tests 일괄 실행 |
| TL3 | 솔버/UI 추가 없이 Refactor |

---

## 8. Success Criteria (Acceptance)

| ID | Criterion | Evidence link |
|----|-----------|---------------|
| SC1 | 두 대각선 모두 검사 — T1 FAIL on wrong diagonal | "대각선 하나를 빼먹어서" |
| SC2 | 중복 검사 — T2 FAIL on duplicate | "숫자가 겹쳤어" |
| SC3 | 한 Command 실행으로 전 Rule 결과 확인 — T3 포함 | "마지막에 검토하니" / 20분 |

**Definition of Done (v0.1):** SC1~SC3 + C1~C2 + T1~T3 통과.

---

## 9. Test Cases

### T1 — Wrong diagonal (R3)

- **Given:** 행·열 합 34, **한 대각선만** ≠34
- **When:** `validate(grid)`
- **Then:** `ok=false`, failures contains `R3`

### T2 — Duplicate (R4)

- **Given:** 10선 합은 맞지만 **동일 숫자 2칸**
- **When:** `validate(grid)`
- **Then:** `ok=false`, failures contains `R4`

### T3 — Both failures (R3 + R4)

- **Given:** 대각선 오류 **와** 숫자 중복 **동시**
- **When:** `validate(grid)`
- **Then:** `ok=false`, failures contains `R3` and `R4` (순서·전략은 구현 문서화)

### T0 — Happy path (baseline)

- **Given:** 유효한 완성 4×4 마방진
- **When:** `validate(grid)`
- **Then:** `ok=true`, failures empty

---

## 10. API Sketch (Non-binding)

```
ValidationResult {
  ok: boolean
  failures: ("R1"|"R2"|"R3"|"R4"|"R5")[]
  messages?: string[]   // optional human-readable
}

validate(grid: number[4][4]): ValidationResult
```

---

## 11. Milestones

| Phase | Scope | Deliverable |
|-------|-------|-------------|
| **Session 3** | Rule + Command + Test Loop | `validate`, R1~R4, T0~T3 |
| **Future** | Skill checklist doc | `CHECKLIST.md` |
| **Future** | ECB Entity/Control/Boundary | 별도 PRD revision |
| **Future** | Solver, UI | 별도 PRD revision |

---

## 12. Open Questions

1. Q4·Q5 미답: 행·열만 확인했는지 vs 대각선도 했다고 **착각**했는지?
2. 부분 격자(0 포함) 검증 시 R1~R3 적용 범위 — 0 있는 line은 skip vs fail?
3. T3에서 **첫 실패만** vs **전체 failures** 반환 정책?

---

## 13. References

- [01.MagicSquare_ProblemDefinition_Report.md](../Report/01.MagicSquare_ProblemDefinition_Report.md)
- Mom Test Transcript: `prompt/01.REPORT-prompt.md`
