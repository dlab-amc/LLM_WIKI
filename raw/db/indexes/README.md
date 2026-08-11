# raw/db/indexes

LLM이 `publications.json` 전체를 열지 않도록 만든 **조회용 인덱스**다.

## 언제 쓰나

| 질문 | 열 파일 |
|---|---|
| 2024년 성과 | `by_year/2024.json` |
| 논문(journal) / 학회(conference) 등 | `by_category/journal.json`, `by_category/conference.json` |
| 특정 저자 | `by_author/<author_id>.json` |
| 특정 멤버 | `by_member/<member_id>.json` |
| 무엇이 있는지 한눈 | `catalog.json` |

## category 키

| key | 의미 |
|---|---|
| journal | 학술지 논문 |
| conference | 학술대회/학회 |
| patent | 특허 등 |
| lecture | 강의 |
| invited_lecture | 초청 강연 |
| award | 수상 |
| project | 과제 |
| … | `catalog.json`의 `category_labels` 참고 |

Wiki 요약 페이지: `wiki/publications/<category>.md`

## 규칙

- Source of Truth 본문은 여전히 `publications.json` / `authors.json` 등.
- 인덱스는 파생본. DB JSON을 바꾼 뒤 재생성이 필요하다.
- Agent는 연도·카테고리·저자 필터 시 **풀 스캔 금지**, 이 폴더 우선.

재생성 (저장소 루트):

```bash
python raw/db/rebuild_indexes.py
```
