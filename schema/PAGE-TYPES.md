# Page Types

## `lab`

연구실 소개·미션·구성 개요.

필수 섹션: Summary, Members (링크), Related, Sources

## `person`

멤버(및 연결 저자) 인물 페이지.

필수 섹션:
- Summary (역할, 학위, 한 줄 소개)
- Profile (tags, email if public in raw)
- Authorship (author_id, achievement_count, resolved_in_pubs)
- **Recent Work** (카테고리 링크 + 최근 성과 표; raw id 근거)
- Related / Sources

Recent Work는 Query·Ingest 때 낡았으면 갱신한다.

slug: `wiki/people/<name-eng-kebab>.md`

## `publication-index`

성과 개요·유형 요약 페이지.

- `wiki/publications/overview.md` — 전체 집계
- `wiki/publications/<category>.md` — category별 1페이지 (journal, conference, …)

1차 PoC: 개별 publication 928개 페이지는 만들지 않음.  
필요 시 중요 성과만 `wiki/publications/items/<id-or-slug>.md`로 추가.

## `decision` / `project` / `note`

예비. 회의록·프로젝트 raw가 들어오는 Ingest부터 사용.

## Frontmatter `type` 값

`lab` | `person` | `publication-index` | `decision` | `project` | `note`
