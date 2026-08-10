# DLab LLM Wiki

서울아산병원 디지털의학연구실(DLab) 지식을 LLM이 읽고·요약·연결·갱신하는 **장기 지식 저장소** PoC.

## 구조

```
raw/       Source of Truth (원본). LLM 수정 금지
schema/    Wiki 관리 규칙 (Ingest / Query / Lint)
wiki/      LLM이 생성·수정하는 Markdown
```

| 층 | 역할 |
|---|---|
| **Raw** | 변경하지 않는 원본. 근거는 전부 여기 (`raw/db`, 회의록, 논문 등) |
| **Schema** | Agent 규칙 — `AGENTS.md` + `schema/` |
| **Wiki** | 요약·연결·갱신되는 지식 페이지 |
| **Index / Log** | `index.md`, `log.md` |
| **Git / Obsidian** | 이력·조회·그래프 |

## 빠른 시작

1. 이 폴더를 Obsidian vault로 연다.
2. Agent는 `AGENTS.md` → `schema/` → `index.md` 순으로 읽는다.
3. 새 자료는 `raw/`에만 추가한 뒤 **Ingest**를 요청한다.
4. 질문은 **Query**로 요청한다.

## 핵심 동작

1. **Ingest** — `raw/` → `wiki/` 반영, 관련 페이지 동시 갱신, `log.md` 기록
2. **Query** — `index.md`부터 관련 페이지를 찾아 답변
3. **Lint** — 고아 링크·중복·스키마 위반 점검

상세: `schema/`
