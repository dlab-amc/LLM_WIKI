# External Assets

Git **형제 폴더**에 두는 대용량 원본을 가리킨다.

| 파일 | Git | 역할 |
|---|---|---|
| `roots.example.json` | O | 상대경로 예시 |
| `roots.local.json` | X | `resolve_from: repo_root` + `../DLab_assets/achievements/...` |
| `papers/manifest.json` | O | PDF 목록 |
| `papers/extracts/*.json` | O | 초록·키워드 |

규칙: `schema/EXTERNAL-ASSETS.md`
