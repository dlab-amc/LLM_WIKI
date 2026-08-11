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
5. 작업별: @schema/INGEST.md | @schema/QUERY.md | @schema/LINT.md

## 절대 규칙 (요약)

- **`raw/`는 Source of Truth. 읽기만. 수정·삭제 금지.**
- Wiki만 수정한다. 관련 페이지를 함께 갱신하고, 중복 페이지를 만들지 않는다.
- Wiki를 바꿀 때마다 **`log.md`에 타임스탬프 + 변경 요약 append.**
- 근거 경로는 항상 `raw/...`. 추측 금지.
- 연도·카테고리·저자·멤버 필터는 **`raw/db/indexes/` 우선** (`publications.json` 풀 스캔 금지).
  - journal=학술지, conference=학술대회/학회 → `indexes/by_category/<key>.json`- Wiki 본문: 한국어 기본. 링크: Obsidian `[[wikilink]]`.

## 작업 트리거

| 사용자가… | 하면 |
|---|---|
| Ingest / 반영 / 새 자료 | `schema/INGEST.md` |
| 질문 / Query | `schema/QUERY.md` — `index`→연결 탐색, 답변 **답변/근거/공백**, **유용한 지식은 Wiki writeback** |
| Lint / 점검 | `schema/LINT.md` |

## Query writeback (중요)

Query는 단순 검색이 아니다. 답변 중 확인한 **재사용 가능한 사실·목록·링크**는 관련 `wiki/` 페이지에 반영하고 `log.md`에 남긴다.  
이미 Wiki에 있는 재서술·일회성 질문은 쓰지 않는다. 기준은 @schema/QUERY.md.

## 하지 말 것

- `data/` 같은 네 번째 지식 계층 만들기
- `raw/db` JSON을 손으로 고치기
- 928개 성과를 전부 개별 Wiki 페이지로 만들기 (PoC 정책)
- 모든 Query마다 무조건 장문 추가 (writeback 기준 따를 것)

## 참고

- 사람용 요약: @README.md
- 변경 이력: @log.md
