# -*- coding: utf-8 -*-
"""Build raw/db/indexes for LLM-friendly filtered reads."""
from __future__ import annotations

import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent  # raw/db/
RAW = ROOT
OUT = RAW / "indexes"


def load(name: str):
    with open(RAW / name, encoding="utf-8") as f:
        return json.load(f)


def year_of(p: dict) -> str | None:
    y = p.get("year")
    if y not in (None, "", "None"):
        return str(y)[:4]
    d = p.get("date")
    if isinstance(d, str) and len(d) >= 4 and d[:4].isdigit():
        return d[:4]
    return None


def slim(p: dict) -> dict:
    out = {
        "id": p["id"],
        "category": p.get("category"),
    }
    for k in (
        "class",
        "year",
        "date",
        "title_eng",
        "title_kor",
        "journal_eng",
        "conference_eng",
        "award_name_eng",
        "project_name_eng",
        "author_kor",
        "author_eng",
        "author_ids",
        "link",
    ):
        v = p.get(k)
        if v not in (None, "", [], {}):
            out[k] = v
    y = year_of(p)
    if y:
        out["year_resolved"] = y
    return out


def dump(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    pubs = load("publications.json")
    authors = load("authors.json")
    links = load("member_author_links.json")
    pubs_by_id = {p["id"]: p for p in pubs}

    by_year: dict[str, list] = defaultdict(list)
    by_author: dict[str, list] = defaultdict(list)
    by_category: dict[str, list] = defaultdict(list)
    unknown_year = []

    for p in pubs:
        s = slim(p)
        y = s.get("year_resolved")
        if y:
            by_year[y].append(s)
        else:
            unknown_year.append(s)
        cat = p.get("category") or "_unknown"
        by_category[cat].append(s)
        for aid in p.get("author_ids") or []:
            by_author[aid].append(s)

    # also index via author.achievement_ids (primary mapping)
    for a in authors:
        aid = a["id"]
        for pid in a.get("achievement_ids") or []:
            p = pubs_by_id.get(pid)
            if not p:
                continue
            s = slim(p)
            # avoid dup if already from embed
            ids = {x["id"] for x in by_author[aid]}
            if s["id"] not in ids:
                by_author[aid].append(s)

    # sort lists
    def sort_key(s):
        return (s.get("year_resolved") or "0000", s.get("title_eng") or s.get("title_kor") or "")

    for y in by_year:
        by_year[y].sort(key=sort_key, reverse=True)
    for aid in by_author:
        by_author[aid].sort(key=sort_key, reverse=True)
    for cat in by_category:
        by_category[cat].sort(key=sort_key, reverse=True)

    if OUT.exists():
        # clean old generated json (keep README if any written after)
        for p in OUT.rglob("*.json"):
            p.unlink()

    for y, items in by_year.items():
        dump(OUT / "by_year" / f"{y}.json", items)
    dump(OUT / "by_year" / "_unknown.json", unknown_year)

    for cat, items in by_category.items():
        dump(OUT / "by_category" / f"{cat}.json", items)

    for aid, items in by_author.items():
        dump(OUT / "by_author" / f"{aid}.json", items)

    by_member = {}
    for link in links:
        mid = link["member_id"]
        aid = link["author_id"]
        items = by_author.get(aid, [])
        dump(OUT / "by_member" / f"{mid}.json", {
            "member_id": mid,
            "member_name_kor": link.get("member_name_kor"),
            "author_id": aid,
            "count": len(items),
            "publications": items,
        })
        # year breakdown for member
        years = defaultdict(int)
        for s in items:
            years[s.get("year_resolved") or "_unknown"] += 1
        by_member[mid] = {
            "name": link.get("member_name_kor"),
            "author_id": aid,
            "count": len(items),
            "by_year": dict(sorted(years.items(), reverse=True)),
        }

    catalog = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "raw/db/publications.json (+ authors.achievement_ids)",
        "usage": {
            "by_year": "raw/db/indexes/by_year/YYYY.json",
            "by_category": "raw/db/indexes/by_category/<category>.json  # journal, conference, patent, ...",
            "by_author": "raw/db/indexes/by_author/<author_id>.json",
            "by_member": "raw/db/indexes/by_member/<member_id>.json",
            "prefer_over": "Do NOT scan full publications.json for year/category/author filters.",
        },
        "category_labels": {
            "journal": "학술지 논문",
            "conference": "학술대회/학회",
            "patent": "특허 등",
            "lecture": "강의",
            "invited_lecture": "초청 강연",
            "award": "수상",
            "project": "과제",
            "extracurricular": "비교과",
            "career": "진로/경력",
            "membership": "학회·단체",
            "technology_transfer": "기술이전",
            "book": "저서",
            "education": "교육",
        },
        "years": {y: len(by_year[y]) for y in sorted(by_year.keys())},
        "categories": {c: len(by_category[c]) for c in sorted(by_category.keys(), key=lambda x: -len(by_category[x]))},
        "unknown_year_count": len(unknown_year),
        "author_index_count": len(by_author),
        "member_summaries": by_member,
    }
    dump(OUT / "catalog.json", catalog)

    readme = """# raw/db/indexes

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
"""
    (OUT / "README.md").write_text(readme, encoding="utf-8")

    print("years", {y: len(by_year[y]) for y in sorted(by_year)})
    print("categories", {c: len(by_category[c]) for c in sorted(by_category, key=lambda x: -len(by_category[x]))})
    print("unknown_year", len(unknown_year))
    print("authors indexed", len(by_author))
    print("members indexed", len(links))
    full = (RAW / "publications.json").stat().st_size
    idx = sum(p.stat().st_size for p in OUT.rglob("*.json"))
    print(f"publications.json {full:,} bytes; indexes total {idx:,} bytes")


if __name__ == "__main__":
    main()
