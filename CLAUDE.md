# CLAUDE.md — DLab LLM Wiki (Claude Code)

Claude Code가 **매 세션 자동으로 읽는** 진입 파일이다.  
상세 규칙은 아래에 두고, 여기서는 항상 지켜야 할 것만 적는다.

## 이 프로젝트

서울아산병원 디지털의학연구실(DLab) **LLM Wiki** PoC.  
일회성 Q&A가 아니라 `raw/` 원본을 보존한 채 `wiki/`를 **질의·수집할수록 축적**한다.

구조는 세 층만 쓴다: **`raw/` · `schema/` · `wiki/`**

## 매 세션 읽기 순서

1. 본 파일 (`CLAUDE.md`)
2. @AGENTS.md
3. @schema/OVERVIEW.md
4. @index.md
5. 작업별: @schema/INGEST.md | @schema/QUERY.md | @schema/LINT.md | @schema/EXTERNAL-ASSETS.md

## 절대 규칙 (요약)

- **`raw/`는 Source of Truth. 읽기만. 수정·삭제 금지.**
- Wiki만 수정한다. 관련 페이지를 함께 갱신하고, 중복 페이지를 만들지 않는다.
- Wiki를 바꿀 때마다 **`log.md`에 타임스탬프 + 변경 요약 append.**
- 근거 경로는 항상 `raw/...`. 추측 금지.
- 연도·카테고리·저자·멤버 필터는 **`raw/db/indexes/` 우선**
- 논문 **주제·초록**은 **`raw/assets/papers/manifest.json` + `extracts/`** (PDF는 Git 밖, 경로만)
- Wiki 본문: 한국어. 링크: `[[wikilink]]`

## External Assets (Git 밖 PDF)

- PDF/ZIP **바이너리는 repo에 넣지 않음.** `roots.local.json` + manifest (`resolve_from: repo_root`, **상대경로**)
- Query: manifest·extracts 우선. PDF 통독·폴더 전체 스캔 금지
- 상세: @schema/EXTERNAL-ASSETS.md

## Query 속도 규칙 (중요)

단순 조회(인물·연도·카테고리)는 **Fast path**:

1. `wiki/people/<slug>.md` (member_id / Recent Work)
2. `raw/db/indexes/by_member/<member_id>.json` 또는 `by_year/` / `by_category/`
3. 바로 답변

**하지 말 것**

- `publications.json` / `authors.json` 전체를 `json.load`·`grep`·파이썬으로 스캔
- unresolved achievement id를 추적하는 디버그 세션
- 단순 Query에 bash를 여러 번 실행

자세한 절차: @schema/QUERY.md

## 작업 트리거

| 사용자가… | 하면 |
|---|---|
| Ingest / 반영 / 새 자료 | `schema/INGEST.md` |
| 질문 / Query | `schema/QUERY.md` — Fast path → 답변/근거/공백 → 필요 시 writeback |
| Lint / 점검 | `schema/LINT.md` |

## Query writeback

재사용 가능한 사실·목록·링크만 Wiki에 반영. 이미 있는 재서술은 쓰지 않음. 기준: @schema/QUERY.md

## 하지 말 것

- `data/` 같은 네 번째 지식 계층 만들기
- `raw/db` JSON을 손으로 고치기
- 928개 성과 개별 Wiki 페이지 생성
- Git에 대용량 PDF/ZIP 커밋 / Git 밖 PDF 폴더 전체 스캔
- 모든 Query마다 장문 추가 / 풀 DB 스캔

## 참고

- @README.md · @log.md
