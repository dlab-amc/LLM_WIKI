# AGENTS.md — DLab LLM Wiki

이 저장소에서 작업하는 LLM Agent의 **공통 규칙**이다. 상세는 `schema/`를 따른다.  
Claude Code는 루트 `CLAUDE.md`를 먼저 자동 로드한 뒤 본 파일·schema를 따른다.

## 정체성

- 대상: 서울아산병원 디지털의학연구실 (DLab) 지식 위키
- 목적: 원본을 보존하면서 Wiki를 장기적으로 축적·연결·갱신
- 구조: **`raw` / `schema` / `wiki`** 세 층만 사용

## 읽기 순서 (매 세션)

1. `AGENTS.md` (본 파일)
2. `schema/OVERVIEW.md`
3. `index.md`
4. 작업 유형별: `schema/INGEST.md` | `schema/QUERY.md` | `schema/LINT.md` | `schema/EXTERNAL-ASSETS.md`
5. 필요 시 `raw/db/stats.json`, `raw/assets/papers/manifest.json`, `log.md`

## 절대 규칙

1. **`raw/`는 Source of Truth다. 수정하지 않는다.** 읽기만 한다.
2. 원본 근거는 **항상 `raw/`** 를 참조한다. (`data/` 같은 별도 계층을 만들지 않음)
3. Wiki 변경 시 **관련 페이지를 함께** 갱신한다.
4. **기존 페이지와 중복되는 새 페이지를 만들지 않는다.** 갱신·병합 우선.
5. Wiki를 수정할 때마다 **`log.md`에 타임스탬프 + 변경 요약**을 남긴다.
6. 문서 간 연결은 Obsidian wikilink `[[페이지명]]`을 사용한다.
7. 불확실한 사실은 추측하지 말고 Sources / uncertainty에 명시한다.

## 작업 유형

| 의도 | 동작 | 참고 |
|---|---|---|
| Ingest / 반영 | `raw/` → `wiki/` 반영 | `schema/INGEST.md` |
| Query / 질문 | 탐색·답변 + **유용하면 Wiki writeback** | `schema/QUERY.md` |
| Lint / 점검 | 품질·일관성 검사 | `schema/LINT.md` |

## 경로 요약

| 경로 | LLM 역할 |
|---|---|
| `raw/` | 읽기 전용 (SoT). PDF 바이너리는 Git 밖, `raw/assets/` manifest로 참조 |
| `schema/` | 규칙 (함부로 변경 금지) |
| `wiki/` | 생성·수정 |
| `index.md` | 인덱스 유지 |
| `log.md` | append |

## 언어

- Wiki 본문: **한국어** 기본 (고유명·논문명·역할명은 영어 병기)
- 파일명: ASCII slug (`hangsik-shin.md`)
