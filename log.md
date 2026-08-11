# Change Log

Wiki 변경 이력. 최신 항목을 **아래에 append**한다.

## 2026-08-10 15:42 (KST)
- Bootstrap: LLM Wiki PoC 골격 생성
- Added: `AGENTS.md`, `schema/*`, `README.md`, `index.md`
- Mapping: member↔author 14/15 연결 (미연결: 오새날)
- Wiki seeded:
  - [[wiki/lab/overview]]
  - [[wiki/people/index]] + member pages (15)
  - [[wiki/publications/overview]]
- Notes: publications year 결측 다수; 개별 성과 페이지는 PoC에서 미생성

## 2026-08-10 15:55 (KST)
- Structure cleanup: **`raw` / `schema` / `wiki`만** 유지
- Removed: `data/`, `raw/raw-db/`(Mongo 덤프), `.gitkeep` 빈 폴더 플레이스홀더, `scripts/process_raw_db.py`
- SoT: 가공본을 `raw/db/`에 두고 Source of Truth로 명시 (`schema/OVERVIEW.md`, `AGENTS.md`)
- Updated: wiki sources 경로 `raw/db/...`

## 2026-08-11 08:25 (KST)
- Ingest: `raw/db/publications.json` 카테고리별 요약 Wiki 생성
- Added: [[wiki/publications/patent]], [[wiki/publications/conference]], [[wiki/publications/journal]], [[wiki/publications/lecture]], [[wiki/publications/award]], [[wiki/publications/project]], [[wiki/publications/extracurricular]], [[wiki/publications/career]], [[wiki/publications/invited_lecture]], [[wiki/publications/membership]], [[wiki/publications/technology_transfer]], [[wiki/publications/book]], [[wiki/publications/education]]
- Updated: [[wiki/publications/overview]], [[wiki/lab/overview]], [[index]]
- Notes: 개별 성과 페이지는 여전히 미생성; 샘플·집계만

## 2026-08-11 09:15 (KST)
- Added: `CLAUDE.md` (Claude Code 세션 자동 진입점; `AGENTS.md`/`schema`로 위임)
- Updated: `README.md`, `index.md` (Claude Code 안내)

## 2026-08-11 10:10 (KST)
- Updated: `schema/QUERY.md` — Query 답변 형식(답변/근거/공백)을 **필수**로 명시
- Updated: `CLAUDE.md` — Query 시 해당 형식 준수 안내

## 2026-08-11 10:15 (KST)
- Added: 전 멤버 `wiki/people/*`에 **Recent Work** (카테고리 링크 + 최근 8건, claimed vs resolved)
- Updated: `schema/QUERY.md` — Query **writeback** 정책 (재사용 지식은 Wiki 반영)
- Updated: `CLAUDE.md`, `AGENTS.md`, `schema/PAGE-TYPES.md`, `README.md`

## 2026-08-11 10:25 (KST)
- Added: `raw/db/indexes/` — `by_year` / `by_author` / `by_member` + `catalog.json` (LLM 조회용)
- Added: `raw/db/rebuild_indexes.py` (인덱스 재생성)
- Updated: `schema/OVERVIEW.md`, `schema/QUERY.md`, `CLAUDE.md`, `index.md` — 풀 스캔 대신 인덱스 우선

## 2026-08-11 10:35 (KST)
- Added: `raw/db/indexes/by_category/` (journal, conference, patent, …) + catalog `category_labels`
- Updated: schema / CLAUDE — 카테고리 필터도 인덱스 우선

## 2026-08-11 11:05 (KST)
- Updated: `CLAUDE.md`, `schema/QUERY.md` — Query **Fast path** (인덱스만, pubs 풀스캔·bash 디버그 금지)
