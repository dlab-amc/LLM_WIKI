# Ingest

새 원본 자료를 Wiki에 반영하는 절차.

## 입력

- 사람이 `raw/` 하위에 파일을 추가·교체했거나
- Git 밖 자산 폴더에 PDF 등을 추가하고 `raw/assets/papers/manifest.json`을 갱신했거나
- 사용자가 “이 내용 반영해줘”라고 텍스트/경로를 준 경우

## External PDF (Git 밖)

1. PDF를 `../DLab_assets/achievements/<category>/`에 둔다. **973MB ZIP은 repo에 넣지 않음.** (`증빙자료제출` 래퍼 폴더 불필요)
2. `raw/assets/roots.local.json` — `"resolve_from": "repo_root"`, 상대경로 (`roots.example.json` 참고).
3. `raw/assets/papers/manifest.json`에 항목 append (`original_filename`, `storage_root`, `relative_path`, `publication_id`).
4. (권장) `papers/extracts/<publication_id>.json` — 초록·키워드만 (Query용).
5. Ingest → wiki 갱신 + `log.md`.

Agent는 Git 밖 PDF를 **삭제·이동하지 않는다.** manifest/extracts만 읽거나, 사람 요청 시 1건 Read.

상세: `schema/EXTERNAL-ASSETS.md`

## 절차

1. **원본 확인**  
   - 근거는 **`raw/`만**. Wiki만 고치고 `raw/`는 바꾸지 않는다.  
   - DB 계열이면 `raw/db/`와 `raw/db/MAPPING_NOTES.md`를 읽는다.

2. **영향 범위 파악** (`index.md` + 기존 wiki 검색)  
   - 관련 인물 / 프로젝트 / 성과 유형 / lab 개요 페이지 목록화  
   - 이미 있는 페이지 = **갱신**, 없는 개념만 **신규**

3. **쓰기** (`wiki/`만)  
   - 요약·사실·링크를 해당 페이지에 반영  
   - 여러 페이지를 한 패스에서 일관되게 수정  
   - `index.md`에 신규 페이지 링크 추가  
   - Sources에는 `raw/...` 경로를 명시

4. **기록**  
   - `log.md`에 append:
     ```
     ## YYYY-MM-DD HH:MM (KST)
     - Ingest: <원본 경로 또는 요약>
     - Updated: [[page1]], [[page2]], ...
     - Notes: <매핑 이슈, 불확실성>
     ```

5. **간단 self-lint**  
   - 깨진 wikilink, 같은 인물 중복 페이지 여부 확인

## `raw/db` 특칙

| 상황 | 행동 |
|---|---|
| 멤버 추가/변경 | `people/` 갱신 + `publications/overview` 통계 |
| 저자-멤버 매핑 변경 | 인물 페이지 `author_id` 갱신 (`MAPPING_NOTES` 참고) |
| 대량 publication | PoC에서는 **유형별 집계**만 Wiki화. 928개 개별 페이지 금지 |
| year 결측 | “연도 미상(raw)” 표기, 추정 금지 |

## 하지 말 것

- `raw/` 아래 JSON·manifest 편집을 LLM이 임의로 (SoT — 사람/승인된 Ingest)
- Git 밖 PDF/ZIP 디렉터리 전체 스캔·통독
- 973MB PDF를 Git에 커밋
- 매칭 confidence가 낮은데 member_id 단정
- 출처 없는 연구실 연혁/업적 창작
