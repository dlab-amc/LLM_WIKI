---
type: person
id: 68590514c33c441ee93e9750
slug: jiwon-you
updated: 2026-09-09
sources:
  - raw/db/members.json
  - raw/db/authors.json
  - raw/db/member_author_links.json
  - raw/assets/papers/manifest.json
  - DATA/achievements/journal/ (PDF)
  - DATA/achievements/conference/ (PDF)
status: active
---

# 유지원 (Jiwon You)

## Summary

- Role: **Researcher**
- Degree: M.S.
- Status: Active
- Order: 9

## Profile

[E-mail](mailto:71one.you@gmail.com)  

Research Areas : Machine learning, Large Language Model, Bioinformatics

- Tags: #Machine learning #Large Language Model #Bioinformatics
- Email: 71one.you@gmail.com

## Authorship

- author_id: `8a86bdcb-831e-484e-81a8-2efc1418ba6b`
- member_id: `68590514c33c441ee93e9750`
- mapping: `existing_memberId` (high)
- achievement_count: **19**
- resolved_in_pubs: **15** (unresolved ids: 4)


## Recent Work

`author.achievement_ids` ∩ `raw/db/publications.json` 기준.
- claimed (author 기록): **19**
- resolved (pubs에 존재): **15**
- unresolved ids: **4**

### By category

- [[../publications/conference|conference]]: **10**
- [[../publications/journal|journal]]: **3**
- [[../publications/award|award]]: **2**

### Recent (최대 8건)

| Year | Category | Title | id |
|---|---|---|---|
| 2026 | [[../publications/journal|journal]] | Structural insights into clinical large language models and their barriers to translational readines... | `7766f561…` |
| 2026 | [[../publications/conference|conference]] | Development of a Clinical Chemistry Retest Ontology through Inductive Externalization of Expert Know... | `6f180265…` |
| 2026 | [[../publications/conference|conference]] | Development and Multicenter External Validation of an AI-based Screening Model for Retesting Clinica... | `537dc980…` |
| 2026 | [[../publications/conference|conference]] | Evaluation of the Feasibility of Large Language Models for Re-test Decision in Clinical Chemistry Te... | `65be53c6…` |
| 2026 | [[../publications/award|award]] | Evaluation of the Feasibility of Large Language Models for Re-test Decision in Clinical Chemistry Te... | `90c8f0ea…` |
| 2026 | [[../publications/journal|journal]] | Large language models for interpretation of health checkup results | `42d3a100…` |
| 2025 | [[../publications/conference|conference]] | Can Large Language Models Analyze Health Data?: For Multi-Stage Items | `bf623bcc…` |
| 2025 | [[../publications/conference|conference]] | Instruction-tuning이 대규모 언어 모델의 건강검진 결과 해석에 미치는 영향 | `865070f8…` |

> 개별 성과 Wiki 페이지는 PoC에서 만들지 않음. 상세는 raw id로 조회.

### 연구 방법론 요약 (PDF 기준, 2024–2026)

#### 2026년

| 논문 (id) | 모델 | 데이터 | 평가지표 |
|---|---|---|---|
| 건강검진 해석 (`42d3a100`, npj Digit. Med.) | Claude Sonnet 4, Gemini 2.5 Pro, GPT-4o, LLaMA 3.1-70B | NHIS 건강검진 N=10,000 (BMI·BP·FBG·TC·TG·HDLC·LDLC·Hb·γ-GTP·UP·SC·AST·ALT 13항목) | Accuracy per item/avg, binomial GLM, Cohen's h, Holm post-hoc; Zero-shot avg 0.69 → CoT avg 0.95 |
| 임상 LLM 체계적 고찰 (`7766f561`, JAMIA) | 73편 문헌 분석 (GPT, LLaMA 등) | PubMed 2020–2025 임상 LLM 73편 | F1, AUROC, Accuracy, BLEU, ROUGE, GLEU, BERT Score, Likert (문헌 고찰 분류) |
| 임상화학 재검 LLM (`65be53c6`, 의공춘계) | LLaMA-3.1-8B-Instruct (instruction-tuning) | AMC 수기검증 N=12,938 (train 10,350 / test 2,588), 2024.09–12 | Accuracy·Precision·Recall·Specificity·F1 + BLEU·ROUGE-L + 5점 Likert 5항목 |
| 재검 온톨로지 (`6f180265`, 의공춘계) | Rule-based 3단계 알고리즘 (LLM 미사용) | AMC N=12,935 (dev 9,969 / test 2,966), 2024.09–12 | Accuracy, Precision, Recall, Specificity; test Precision·Specificity 100% |

#### 2025년

| 논문 (id) | 모델 | 데이터 | 평가지표 |
|---|---|---|---|
| 다단계 건강검진 (`bf623bcc`, 의공춘계) | Claude 3.5 Sonnet, Gemini 1.5 Pro, GPT-4o, LLaMA 3.1-70B | NHIS 2023 층화 추출 N=1,000 (BP·FBG·TC·LDLC) | Accuracy per item/model; constraint prompt → FBG·콜레스테롤 0.95+, BP 개선 제한적 |

#### 2024년

| 논문 (id) | 모델 | 데이터 | 평가지표 |
|---|---|---|---|
| 건강검진 가능성/한계 (`0a3f5d13`, 의공추계) | GPT-4o, Gemini 1.5 Pro, Claude 3.5 Sonnet, LLaMA 3.1 8B-Instruct, EXAONE-3.0-7.8B | NHIS 2023 N=100 (16항목) | Accuracy per item/avg; Claude 0.838, GPT-4o 0.824 최고; EXAONE 0.560, LLaMA 0.628 |
| 진단검사 오류감지 (`bdba12ce`, 전기학회) | XGBoost (vs Delta Percent Change) | AMC 임상화학검사 N=2,975,288건, 2021–2022 | AUROC, Accuracy, Sensitivity, Specificity, PPV, NPV, SHAP; XGBoost AUROC 0.917 vs DPC 0.589 |
| ML in Lab Medicine 고찰 (`841b7d8e`, Ann Lab Med) | CNN·MLP·Tree-based 등 144편 | PubMed 2014–2024 검사의학 ML 144편 | Accuracy, Sensitivity, Specificity, AUROC, MSE (문헌 사용 지표 분류) |
| 오류 유형/빈도 (`cfc8007b`, KSLM) | 통계 분석 (ML 미사용) | AMC N=29,000,000+건, 2021–2022 | 오류율(%), 빈도; 용혈이 82.76%로 최다 |

**공통 특징**: ① 프롬프트 전략(Zero-shot → Constraint → CoT) 비교로 일관된 성능 개선 확인 ② NHIS 공공 데이터 + AMC 원내 데이터 두 축 ③ LLM(건강검진 해석·재검 판정) ↔ ML/Rule-based(오류 감지·온톨로지) 두 갈래 병행

## Related

- Categories: [[../publications/conference|conference]] · [[../publications/journal|journal]] · [[../publications/award|award]]
- [[lab/overview]]
- [[publications/overview]]
- [[people/index]]

## Sources

- member id: `68590514c33c441ee93e9750`
- `raw/db/members.json`
