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
