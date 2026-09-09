# Raw Sources (Source of Truth)

이 디렉터리는 **변경하지 않는 원본**의 **인덱스·메타**를 둔다.

- LLM은 **읽기만** 한다 (manifest·JSON). Git 밖 PDF는 **삭제·이동 금지**.
- Wiki·답변 근거: `raw/...` 및 manifest가 가리키는 외부 경로.

## 현재

| 경로 | 내용 | Git |
|---|---|---|
| `db/` | DB 가공본 + `indexes/` | O |
| `assets/roots.example.json` | 외부 경로 설정 예시 | O |
| `assets/roots.local.json` | 머신별 실제 경로 | **X** |
| `assets/papers/manifest.json` | PDF 목록·DB 매칭 | O |
| `assets/papers/extracts/` | 초록·키워드 JSON | O |
| PDF/ZIP 바이너리 | `../DLab_assets/achievements/<category>/` 등 (repo **형제**) | **X** |

## PDF 추가 (요약)

1. ZIP PDF → `../DLab_assets/achievements/<category>/` (`증빙자료제출` 래퍼 없이 직접 배치)
2. `roots.local.json` — `resolve_from: repo_root` (`roots.example.json` 참고)
3. `papers/manifest.json` 갱신  
4. Ingest 요청  

상세: `schema/EXTERNAL-ASSETS.md`
