# Papers / PDF (External Assets)

논문·학회·특허 **PDF 원본**은 Git에 넣지 않는다.  
Query는 **인덱스 + extracts**로 끝내고, 바이너리는 최후 수단이다.

## Fast path (Agent)

| 단계 | 파일 |
|---|---|
| 1 | `wiki/people/<slug>.md` → `member_id` |
| 2 | `by_member/<member_id>.json` (date desc, `has_extract`) |
| 3 | `extracts/<publication_id>.json` → abstract / keywords / first_pages_text |
| (예외) | `by_publication_id.json` 또는 `indexes/by_publication/<id>.json` → PDF 1건 |

**금지:** `manifest.json` 전체 스캔, `DATA/` 폴더 일괄 Read, extracts 있는데 PDF 재통독.

## 파일

| 경로 | 역할 |
|---|---|
| `manifest.json` | PDF↔publication_id 매칭 결과 (구축용) |
| `by_publication_id.json` | id → storage_root/relative_path |
| `by_member/<member_id>.json` | 멤버별 논문+pdf+extract 유무 |
| `extracts/<publication_id>.json` | 자동 추출 텍스트 (앞 페이지) |
| `../roots.local.json` | Git 밖 루트 상대경로 |

## 배치·재생성

1. PDF를 `../DATA/achievements/<category>/`에 둔다
2. `roots.local.json` 설정
3. `python WEB/scripts/build_papers_manifest.py --apply`
4. `python WEB/scripts/build_paper_indexes_and_extracts.py --apply`

상세: `schema/EXTERNAL-ASSETS.md` · `schema/QUERY.md`
