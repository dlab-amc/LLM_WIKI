# Lint

Wiki 품질 점검 절차.

## 체크리스트

### 구조
- [ ] `raw/`에 LLM이 쓴 변경이 없는가
- [ ] `index.md`에 있는 링크가 실제 파일을 가리키는가
- [ ] `wiki/` 고아 페이지(인덱스·다른 문서에서 링크되지 않음)가 과도하지 않은가

### 중복
- [ ] 동일 인물/개념의 페이지가 둘 이상인가 (slug·이름 교차 확인)
- [ ] members와 authors를 별개 실체로 중복 서술하지 않았는가 (인물 페이지에서 통합)

### 내용
- [ ] frontmatter `updated` / `sources`가 최근 변경과 맞는가
- [ ] 수치(성과 수 등)가 `raw/db/stats.json`과 크게 어긋나지 않는가
- [ ] year·매핑 등 불확실 항목에 단정이 없는가

### 로그
- [ ] 최근 Wiki 수정이 `log.md`에 반영되었는가

## 출력

Lint 결과는 채팅에 보고하고, **수정까지 수행했다면** `log.md`에 남긴다.

```
## Lint report (YYYY-MM-DD)
- OK: ...
- Issues: ...
- Fixed: ...
```

## 자동화 (향후)

- wikilink 존재 여부 스크립트
- member_author_links와 people 페이지 id 일치 검사
