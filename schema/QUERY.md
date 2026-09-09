# Query

사용자가 Wiki에 질문할 때의 절차.

LLM Wiki에서 Query는 **읽기만**이 아니다.  
답하는 과정에서 얻은 **재사용 가능한 연결·요약**은 Wiki에 되돌려 쓴다 (writeback).  
단, 모든 질문에 페이지를 새로 만들거나 장문을 붙여 넣지는 않는다.

## 절차

1. **`index.md`를 먼저 읽는다** — 관련 섹션·페이지 후보를 고른다.
2. **후보 Wiki 페이지를 연다** — 여러 페이지의 **연결**을 따라간다 (인물↔카테고리↔개요). 부족하면 `raw/` 보조.
3. **아래 답변 형식으로 답한다** (필수). 근거 wikilink는 **가능하면 2개 이상** (예: 인물 + 성과 카테고리).
4. **Writeback 판단** (아래 기준) → 해당하면 `wiki/` 갱신 + `log.md` append.
5. 단순 조회만으로 끝나면 Wiki/`log.md`를 건드리지 않는다.

## Writeback 기준

| 상황 | Wiki 갱신? |
|---|---|
| 이미 Wiki에 있는 내용 재서술 | 아니오 |
| raw에서 확인한 **새 사실·목록·수치**를 인물/카테고리 페이지에 반영할 수 있음 | **예** (기존 페이지 갱신) |
| 페이지 간 링크·Recent Work·집계가 비어 있거나 낡음 | **예** |
| 일회성 의견·추측 | 아니오 |
| 새 raw 파일 추가에 따른 대규모 반영 | Ingest로 분리 |

Writeback 시:
- **관련 페이지를 함께** 수정 (예: 인물 Recent Work + 필요 시 category 언급)
- 중복 페이지 생성 금지
- `log.md`에 Query writeback임을 명시

## Fast path (속도)

인물+연도 / 카테고리 / **논문 본문 요약** 질문은 **아래만** 하고 끝낸다. 디버그하지 않는다.

| 질문 유형 | 열 파일 (최대 2~3개) |
|---|---|
| 최예은 최근 | `wiki/people/alumni/ye-eun-choi.md` |
| 이재형 최근 | `wiki/people/alumni/jaehyung-lee.md` |
| 석현석 최근 | `wiki/people/alumni/hyeon-seok-seok.md` → 필요 시 `indexes/by_author/<author_id>.json` |
| 왕창원 최근 | `wiki/people/alumni/changwon-wang.md` → 필요 시 `indexes/by_author/<author_id>.json` |
| 현재 멤버 목록 | `wiki/people/index.md` |
| Alumni 목록 | `wiki/people/alumni/index.md` |
| 최예은 2024 | 인물 md → `member_id` → `raw/db/indexes/by_member/<member_id>.json` → `year_resolved==2024` |
| journal 규모 | `wiki/publications/journal.md` 또는 `indexes/by_category/journal.json` |
| 2024 conference | `indexes/by_year/2024.json`에서 category 필터 (또는 category∩year) |
| 멤버 논문+PDF 유무 | `raw/assets/papers/by_member/<member_id>.json` (date desc, `has_extract`) |
| 논문 **주제/초록/방법·지표** | `papers/by_member/<mid>.json` 또는 `by_member` → `papers/extracts/<publication_id>.json` |
| publication_id → PDF 경로 | `raw/assets/papers/by_publication_id.json` 또는 `indexes/by_publication/<id>.json` |
| PDF 1건 바이너리 상세 | `by_publication`의 `storage_root`+`relative_path` → `roots.local`로 **1파일만** (전체 통독 금지) |

### 논문 PDF 내용 질문 (중요)

1. 인물 페이지 → `member_id`
2. **`raw/assets/papers/by_member/<member_id>.json`** 에서 최근 항목 (`has_extract: true` 우선)
3. **`raw/assets/papers/extracts/<publication_id>.json`** 의 `abstract` / `keywords` / `first_pages_text` 로 답변
4. extracts가 없을 때만 `by_publication_id.json`으로 PDF 경로 확인 후 **해당 1건만** 읽기

**하지 말 것:** `manifest.json` 전체 스캔, `DATA/` 폴더 일괄 Read, extracts가 있는데도 PDF 재통독.

### Query에서 금지

- `publications.json` / `authors.json` **전체** 로드·grep·python 스캔
- Git 밖 PDF 폴더 **전체** grep·일괄 Read (973MB ZIP 등)
- `manifest.json` 전체를 멤버 논문 찾기로 사용 (→ `by_member` / `by_publication_id` 사용)
- unresolved id 10건을 찾으러 `grep -r` / 다중 bash
- “데이터 정합성 검증”을 사용자 질문 없이 시작

unresolved ids는 인물 페이지에 이미 숫자로 있으면 **공백 섹션에 한 줄**만 쓰고 넘어간다.

## 탐색 우선순위

1. `index.md`
2. `wiki/` (여러 문서 연결) — 인물: 현재는 `people/`, 졸업생은 `people/alumni/`
3. **`raw/db/indexes/`** (연도·category·author·member·**publication**)
4. **`raw/assets/papers/by_member/` + `extracts/` + `by_publication_id.json`**
5. `raw/assets/papers/manifest.json` (매칭 디버그·미연결 PDF만)
6. `raw/db/*.json` 전체 (인덱스·extracts로 부족할 때만)

> “멤버 누구야?” / 구성원 목록 질문 → **현재**는 `people/index`만. Alumni는 사용자가 졸업생·Alumni를 물을 때 또는 이름으로 Alumni 페이지가 매칭될 때.

### 인덱스 조회 예

- 2024년 전체 → `raw/db/indexes/by_year/2024.json`
- 논문(journal) / 학회(conference) → `indexes/by_category/journal.json`, `conference.json`
- 최예은 2024년 → `indexes/by_member/<member_id>.json`에서 `year_resolved==2024`
- 최예은 journal만 → 같은 멤버 파일에서 `category==journal` (또는 author 인덱스)
- 유지원 논문 모델/데이터/지표 → `papers/by_member/<mid>.json` → `extracts/<id>.json`
- publication 1건 PDF 경로 → `indexes/by_publication/<id>.json`
- **금지:** 단순 연도/카테고리/인물/논문내용 질문인데 `publications.json`·`manifest.json` 전체를 읽기

## 답변 형식 (필수)

```markdown
## 답변
(한국어. 인물↔성과↔카테고리 연결을 드러낼 것)

## 근거
- [[people/...]] 또는 [[people/alumni/...]]
- [[publications/...]]
- (필요 시) `raw/db/...` id

## 공백 / 다음 행동
- Wiki에 없거나 부족했던 점: ...
- Writeback 여부: 함 / 안 함 (+ 어떤 페이지)
- Ingest 권장: 예/아니오
```

### 규칙

- 근거 없는 단정 금지.
- Wiki 미반영·raw만 있으면 명시.
- 단일 문서만 근거로 끝내지 말 것 (연결이 질문에 해당하면).
