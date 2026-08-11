# Schema Overview

DLab LLM Wiki 관리 규칙. Agent는 `AGENTS.md` 다음으로 본 문서를 읽는다.

## 저장소 구조 (이 세 층만)

```
LLM_WIKI/
├── raw/       # Source of Truth — 원본. LLM 수정 금지
├── schema/    # Wiki 운영 규칙
├── wiki/      # LLM이 생성·수정하는 Markdown
├── AGENTS.md  # Agent 진입 요약
├── index.md   # 인덱스
└── log.md     # 변경 이력
```

다른 지식 계층(`data/` 등)을 두지 않는다. 모든 원본 참조는 **`raw/`만** 사용한다.

## 디렉터리 계약

| 경로 | 소유자 | 규칙 |
|---|---|---|
| `raw/` | 사람 | **Source of Truth. 불변.** LLM은 읽기만. 추가·교체는 사람 |
| `schema/` | 사람(+합의) | 규칙. 명시적 요청 없이 Agent가 바꾸지 않음 |
| `wiki/` | LLM | 생성·수정. 페이지당 단일 주제 |
| `index.md` | LLM | 섹션별 진입 링크 유지 |
| `log.md` | LLM | Wiki 변경마다 append |

## `raw/` = Source of Truth

1. Wiki·답변·매핑의 **근거 원본은 전부 `raw/`** 이다.
2. LLM은 `raw/` 아래 파일을 **수정·삭제·덮어쓰지 않는다.**
3. 새 자료는 사람이 `raw/`에 넣은 뒤 **Ingest**로 `wiki/`에만 반영한다.
4. Mongo 덤프처럼 LLM이 읽기 어려운 형태는, 사람이 가공한 뒤 **`raw/`에 그 가공본을 SoT로 둔다.** (별도 `/data` 계층 금지)

### 현재 `raw/` 내용

| 경로 | 내용 |
|---|---|
| `raw/db/` | 연구실 DB 가공본 (members, authors, publications, links, stats) |
| `raw/db/MAPPING_NOTES.md` | 멤버↔저자 매핑 메모 |
| `raw/db/indexes/` | **조회 인덱스** (연도·author·member). 풀 스캔 대신 여기 우선 |

#### `raw/db/indexes` 사용법

| 필터 | 파일 |
|---|---|
| 연도 (예: 2024) | `indexes/by_year/2024.json` |
| 카테고리 (journal, conference, …) | `indexes/by_category/<category>.json` |
| 저자 | `indexes/by_author/<author_id>.json` |
| 멤버 | `indexes/by_member/<member_id>.json` |
| 카탈로그·연도/카테고리 건수 | `indexes/catalog.json` |

`publications.json` 전체 로드는 **최후 수단**. 인덱스 재생성: `python raw/db/rebuild_indexes.py`

앞으로 회의록·논문·매뉴얼 등이 생기면 사람이 `raw/meeting-logs/`, `raw/papers/` 등 하위 폴더를 **필요할 때** 만들어 넣는다. 빈 폴더를 미리 두지 않는다.

## Wiki 정보 구조

```
wiki/
  lab/           # 연구실 소개
  people/        # 멤버 인물 페이지
  publications/  # 성과 개요
  decisions/     # (필요 시) 결정 기록
  projects/      # (필요 시) 프로젝트
  system/        # (필요 시) 인프라·툴
```

없는 하위 폴더는 첫 Ingest 때 생성한다.

## 페이지 작성 원칙

1. **One concept per page**
2. **중복 금지** — 같은 실체는 갱신·병합
3. **링크** — `[[wikilink]]`
4. **출처** — 반드시 `raw/...` 경로 (및 id)
5. **프론트매터** 권장:

```yaml
---
type: person | publication-index | lab | decision | project | note
id: <stable-id-or-slug>
updated: YYYY-MM-DD
sources:
  - raw/db/members.json
status: active | draft | needs-review
---
```

## 파일명(slug)

- 인물: `name-eng` 소문자 케밥 (`hangsik-shin.md`)

## `raw/db` 해석 요약

- `members` (15): 구성원 프로필
- `authors` (209): 성과 저자. `achievement_ids` → publication id
- `publications` (928): journal/conference/patent 등 혼합 (`category`)
- `member_author_links`: 멤버↔저자 14명 연결 (행정 1명 미연결)

## 관련 문서

- `schema/INGEST.md`
- `schema/QUERY.md`
- `schema/LINT.md`
- `schema/PAGE-TYPES.md`
