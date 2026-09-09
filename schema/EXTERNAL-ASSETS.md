# External Assets (Git 밖 원본)

대용량 바이너리(PDF, ZIP, 동영상)는 **Git 저장소 밖**에 두고,  
repo 안에는 **경로·manifest·extracts**만 둔다.

## 권장 배치 (서버 공통)

**저장소와 자산 폴더를 형제(sibling)로** 두면, 모든 서버에서 **같은 상대경로**를 쓸 수 있다.

```
parent/                         ← 예: Desktop/, /opt/dlab/
  LLM_WIKI/                     ← Git clone (repo root)
    raw/assets/...
  DLab_assets/                  ← Git 밖
    achievements/
      journal/                  ← 논문 PDF
      conference/               ← 학술대회 PDF
      patent-filed/             ← 특허 출원 PDF
      patent-registered/        ← 특허 등록 PDF
      software/                 ← SW PDF
      award/                    ← 수상 PDF
    videos/                     ← 영상 (홈페이지 연동 예정)
    archives/                   ← 원본 ZIP 백업 (선택)
```

**`증빙자료제출` 같은 ZIP 래퍼 폴더는 만들지 않는다.** PDF는 `achievements/<category>/`에 **직접** 둔다.

## ZIP → DLab_assets 매핑 (구 폴더명)

| ZIP 안 (구) | `DLab_assets` 경로 |
|---|---|
| `증빙자료_논문/` | `achievements/journal/` |
| `증빙자료_학술대회/` | `achievements/conference/` |
| `증빙자료_특허출원일반/` | `achievements/patent-filed/` |
| `증빙자료_특허등록일반/` | `achievements/patent-registered/` |
| `증빙자료_SW/` | `achievements/software/` |
| `증빙자료_수상/` | `achievements/award/` |

하위 폴더(`~2025.12.31`, `삼성전자` 등)는 유지하거나 평탄화해도 된다. manifest `relative_path`에 반영.

## 경로 해석 (상대경로 우선)

### `roots.local.json`

```json
{
  "version": 1,
  "resolve_from": "repo_root",
  "roots": {
    "journal": "../DLab_assets/achievements/journal",
    "conference": "../DLab_assets/achievements/conference",
    "patent_filed": "../DLab_assets/achievements/patent-filed",
    "patent_registered": "../DLab_assets/achievements/patent-registered",
    "software": "../DLab_assets/achievements/software",
    "award": "../DLab_assets/achievements/award",
    "videos": "../DLab_assets/videos"
  }
}
```

| 필드 | 설명 |
|---|---|
| `resolve_from` | `"repo_root"` (기본·권장) — Git 저장소 루트 기준 |
| `roots.<key>` | repo root에서의 **상대경로** |
| `storage_root` | manifest 항목이 참조하는 `roots`의 **키** (예: `"journal"`, `"patent_registered"`) |

**실제 파일 경로:**

```
<repo_root> / roots[storage_root] / manifest.relative_path
```

예: `LLM_WIKI/../DLab_assets/achievements/journal/2026A00125_....pdf`

### 절대경로 (예외)

`roots` 값이 `D:/...` 또는 `/home/...` 처럼 **절대경로**면 그대로 사용한다.  
다중 서버 배포에는 **상대경로 + 동일 폴더 구조**를 권장한다.

### `manifest.json` 항목

- `storage_root`: `roots`의 키 (예: `"journal"`, `"conference"`)
- `relative_path`: 해당 루트 **아래** 경로 (예: `"2026A00125_....pdf"` 또는 `"삼성전자/foo.pdf"`)
- `publication_id`: `raw/db/publications.json` id (매칭 후)
- ~~`absolute_path`~~ — 가급적 쓰지 않음 (서버마다 깨짐)

## repo 안 구조

```
raw/assets/
  roots.example.json
  roots.local.json         ← Git 제외
  papers/
    manifest.json          ← PoC: 통합 manifest (추후 category별 분리 가능)
    extracts/
```

## 서버 배포 체크리스트

1. `git clone` → `.../parent/LLM_WIKI/`
2. `DLab_assets/` 형제 폴더 생성 (또는 rsync)
3. PDF를 `achievements/<category>/`에 배치
4. `cp raw/assets/roots.example.json raw/assets/roots.local.json`
5. `manifest.json` 채우기 → Ingest

## Agent 규칙

- Query: `manifest.json` + `extracts/` 우선
- PDF 바이너리: 특정 1건 요청 시 `repo_root` + 상대경로로 Resolve
- Git 밖 파일 **삭제·이동 금지**
- PDF 폴더 전체 스캔 금지

## Ingest / Query

- Ingest: `schema/INGEST.md`
- Query: `schema/QUERY.md`
