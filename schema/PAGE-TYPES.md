# Page Types

## `lab`

연구실 소개·미션·구성 개요.

필수 섹션: Summary, Members (현재), Alumni (링크), Related, Sources

## `person`

**현재 소속** 멤버(및 연결 저자) 인물 페이지.

필수 섹션:
- Summary (역할, 학위, 한 줄 소개)
- Profile (tags, email if public in raw)
- Authorship (author_id, achievement_count, resolved_in_pubs)
- **Recent Work** (카테고리 링크 + 최근 성과 표; raw id 근거)
- Related / Sources

Recent Work는 Query·Ingest 때 낡았으면 갱신한다.

- frontmatter: `type: person`, `status: active`
- slug: `wiki/people/<name-eng-kebab>.md`

## `alumni`

**졸업·퇴사** 인물 페이지. 성과·저자 인덱스는 `person`과 동일하게 유지하되, **현재 멤버 목록에는 올리지 않는다**.

필수 섹션: Summary, Academic History (가능 시), Profile, Authorship, Recent Work, Related / Sources

- frontmatter: `type: alumni`, `status: alumni`, `graduated: YYYY-MM` (가능하면)
- slug: `wiki/people/alumni/<name-eng-kebab>.md`
- 인덱스: `wiki/people/alumni/index.md` (`type: alumni-index`)

## `people-index` / `alumni-index`

- `wiki/people/index.md` — 현재 멤버만
- `wiki/people/alumni/index.md` — Alumni만
- 서로 교차 링크

## `publication-index`

성과 개요·유형 요약 페이지.

- `wiki/publications/overview.md` — 전체 집계
- `wiki/publications/<category>.md` — category별 1페이지 (journal, conference, …)

1차 PoC: 개별 publication 928개 페이지는 만들지 않음.  
필요 시 중요 성과만 `wiki/publications/items/<id-or-slug>.md`로 추가.

## `decision` / `project` / `note`

예비. 회의록·프로젝트 raw가 들어오는 Ingest부터 사용.

## Frontmatter `type` 값

`lab` | `person` | `alumni` | `people-index` | `alumni-index` | `publication-index` | `decision` | `project` | `note`
