# Papers / PDF (External Assets)

논문·학회·특허 **PDF 원본**은 Git에 넣지 않는다.

## 배치

1. PDF를 `../DLab_assets/achievements/<category>/`에 둔다 (repo **형제** 폴더, 카테고리별 — `schema/EXTERNAL-ASSETS.md` 참고)
2. `raw/assets/roots.local.json` — `"resolve_from": "repo_root"`, 상대경로 (`roots.example.json` 참고)
3. 이 폴더의 `manifest.json`에 항목 추가
4. (선택) `extracts/<publication_id>.json` — 초록·키워드만

## Agent

- Query: `manifest.json` + `extracts/` 우선
- PDF 바이너리: 특정 1건 상세 요청 시에만 `roots.local` + `relative_path`로 접근
- Git 밖 파일 **수정·삭제 금지**

상세: `schema/EXTERNAL-ASSETS.md`
