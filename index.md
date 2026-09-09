---
type: note
id: root-index
updated: 2026-09-09
status: active
---

# DLab LLM Wiki — Index

Agent·사람 모두 **여기서 시작**한다. 상세 규칙은 `AGENTS.md`, `schema/`를 본다.

## Schema

- [[schema/OVERVIEW|Overview]]
- [[schema/INGEST|Ingest]]
- [[schema/QUERY|Query]]
- [[schema/LINT|Lint]]
- [[schema/PAGE-TYPES|Page types]]
- [[schema/EXTERNAL-ASSETS|External assets (Git 밖 PDF)]]
- [AGENTS.md](AGENTS.md)
- [CLAUDE.md](CLAUDE.md) (Claude Code 자동 로드)

## Lab

- [[wiki/lab/overview|DLab overview]]

## People (현재 멤버)

- [[wiki/people/index|People index]]
- [[wiki/people/hangsik-shin|신항식]]
- [[wiki/people/yunchan-nam|남윤찬]]
- [[wiki/people/jaewook-jin|진재욱]]
- [[wiki/people/gayeon-ryu|류가연]]
- [[wiki/people/yujin-han|한유진]]
- [[wiki/people/yeongdon-kim|김영돈]]
- [[wiki/people/jiwon-you|유지원]]
- [[wiki/people/geon-lee|이건]]
- [[wiki/people/minso-kim|김민소]]
- [[wiki/people/juhyeon-kang|강주현]]
- [[wiki/people/yeonjin-lee|이연진]]
- [[wiki/people/heeyoung-kim|김희영]]
- [[wiki/people/saenal-oh|오새날]]

## Alumni (졸업생)

- [[wiki/people/alumni/index|Alumni index]]
- [[wiki/people/alumni/ye-eun-choi|최예은]]
- [[wiki/people/alumni/jaehyung-lee|이재형]]
- [[wiki/people/alumni/hyeon-seok-seok|석현석]]
- [[wiki/people/alumni/changwon-wang|왕창원]]

## Publications

- [[wiki/publications/overview|Publications overview]]
- [[wiki/publications/patent|Patent]] (321)
- [[wiki/publications/conference|Conference]] (240)
- [[wiki/publications/journal|Journal]] (101)
- [[wiki/publications/lecture|Lecture]] (90)
- [[wiki/publications/award|Award]] (50)
- [[wiki/publications/project|Project]] (38)
- [[wiki/publications/extracurricular|Extracurricular]] (38)
- [[wiki/publications/career|Career]] (15)
- [[wiki/publications/invited_lecture|Invited Lecture]] (14)
- [[wiki/publications/membership|Membership]] (9)
- [[wiki/publications/technology_transfer|Technology Transfer]] (6)
- [[wiki/publications/book|Book]] (3)
- [[wiki/publications/education|Education]] (3)


## Raw (Source of Truth)

### DB (repo 안)
- `raw/db/indexes/` — 연도·category·author·member (`catalog.json`)
- `raw/db/stats.json`, `members.json`, `authors.json`, `publications.json`
- `raw/db/member_author_links.json`, `MAPPING_NOTES.md`

### External assets (PDF는 Git 밖)
- `raw/assets/roots.example.json` → 복사해 `roots.local.json` (`resolve_from: repo_root`, 상대경로)
- `raw/assets/papers/manifest.json`
- `raw/assets/papers/extracts/`
- 바이너리: `../DLab_assets/achievements/` (journal, conference, patent-*, software, award) · `videos/` · `archives/`

## Ops

- [[log|Change log]]
- [README](README.md)
- **Web UI (PoC):** 형제 폴더 `../DLab_web/` — Claude CLI 챗봇 (`http://127.0.0.1:8080`)
