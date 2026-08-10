---
type: publication-index
id: publications-overview
updated: 2026-08-11
sources:
  - raw/db/publications.json
  - raw/db/stats.json
status: active
---

# Publications Overview

`publications` 컬렉션은 논문·학회·특허·강의·수상 등 **혼합 성과**이다. 카테고리별 요약 페이지와 집계·멤버별 카운트를 Wiki에 둔다.

## Totals

- 전체 레코드: **928**
- 카테고리 수: 13

## By category

| Category | 설명 | Count |
|---|---|---:|
| [[patent|Patent]] | 특허·디자인·SW 등록 등 | 321 |
| [[conference|Conference]] | 학회 발표·논문 | 240 |
| [[journal|Journal]] | 학술지 논문 | 101 |
| [[lecture|Lecture]] | 강의 | 90 |
| [[award|Award]] | 수상 | 50 |
| [[project|Project]] | 연구·용역 과제 | 38 |
| [[extracurricular|Extracurricular]] | 비교과·대외활동 | 38 |
| [[career|Career]] | 진로·경력 관련 기록 | 15 |
| [[invited_lecture|Invited Lecture]] | 초청 강연 | 14 |
| [[membership|Membership]] | 학회·단체 활동 | 9 |
| [[technology_transfer|Technology Transfer]] | 기술이전 | 6 |
| [[book|Book]] | 저서·도서 | 3 |
| [[education|Education]] | 교육 관련 성과 | 3 |


## By year (raw `year` 필드가 있는 것만)

> 주의: 상당수 레코드에 year가 비어 있다. 아래는 필드가 채워진 부분집합.

| Year | Count |
|---|---:|
| 2013 | 3 |
| 2014 | 10 |
| 2015 | 16 |
| 2016 | 13 |
| 2017 | 12 |
| 2018 | 11 |
| 2019 | 14 |
| 2020 | 14 |

## Member achievement counts

author.`achievement_ids` 길이 기준 (멤버에 매핑된 저자만).

| Member | Achievements |
|---|---:|
| 신항식 | 752 |
| 류가연 | 52 |
| 최예은 | 32 |
| 이재형 | 26 |
| 한유진 | 21 |
| 유지원 | 19 |
| 김영돈 | 11 |
| 진재욱 | 10 |
| 이건 | 9 |
| 김민소 | 6 |
| 이연진 | 4 |
| 남윤찬 | 2 |
| 강주현 | 2 |
| 김희영 | 2 |

## Policy (PoC)

- 개별 성과 페이지는 기본 생성하지 않음
- 질의 시 필요하면 `raw/db/publications.json`에서 id로 조회
- 중요 성과만 이후 `wiki/publications/items/`에 추가

## Related

- 카테고리: [[patent]], [[conference]], [[journal]], [[lecture]], [[award]], [[project]], [[extracurricular]], [[career]], [[invited_lecture]], [[membership]], [[technology_transfer]], [[book]], [[education]]
- [[lab/overview]]
- [[people/index]]

## Sources

- `raw/db/publications.json`
- `raw/db/stats.json`
