
---

# 생성형 AI 및 RAG, LangChain 강의 요약

## 1. 생성형 AI (Generative AI)

### 1.1. 생성형 AI의 시작과 현재

* **파운데이션 모델(Foundation Models):** 스탠포드 HAI(Stanford HAI)의 연구("On the Opportunities and Risks of Foundation Models")를 인용하며, 거대 언어 모델의 기반이 되는 파운데이션 모델의 등장과 중요성을 언급함.
* **언어 모델의 한계:**
* **문맥 파악의 어려움:** "웃-프다"(웃기고 슬프다)와 같은 신조어나 복합적인 감정, 상황적 맥락(Context)을 AI가 정확히 이해하거나 표현하지 못하는 경우가 있음.
* **단순함의 한계:** 언어는 단순하지 않으며, "여자어 능력 평가" 예시처럼 표면적인 텍스트 뒤에 숨겨진 의도를 파악해야 함.


* **멀티모달(Multimodal)의 등장:** 텍스트 기반 언어 모델의 한계를 극복하기 위해 이미지, 오디오, 비디오 등 다양한 데이터를 처리하는 멀티모달 AI로 진화함.

### 1.2. 추론 모델의 등장

* **Chain of Thought (CoT):** 단순히 답을 내는 것보다 사고 과정을 거치게 했을 때 정확도가 비약적으로 상승함(벤치마크 점수 비교 그래프 참조).
* 인간의 선호도 평가에서도 추론 과정을 포함한 모델이 더 높은 점수를 받음.

---

## 2. RAG (Retrieval-Augmented Generation, 검색 증강 생성)

### 2.1. LLM의 한계 극복을 위한 RAG

* **LLM 최적화 4분면:** 외부 지식(External Knowledge) 필요 여부와 컨텍스트 최적화(Context Optimization) 정도에 따른 분류.
* **RAG:** 외부 지식 필요 높음 / 컨텍스트 최적화 낮음 (정보 검색 중심)
* **Fine-Tuning:** 외부 지식 필요 낮음 / 컨텍스트 최적화 높음 (모델 적응 필요)
* **Hybrid:** 둘 다 높음
* **Prompt Engineering:** 둘 다 낮음



### 2.2. RAG의 개념

* **정의:** 입력 프롬프트와 검색 기반의 정보를 결합(증강)하여, 증강된 정보를 기반으로 답변을 생성하도록 하는 방식.
* **Retrieval (검색):** 외부 데이터 및 소스를 검색하여 정보 확보.
* **Augmented (증강):** 사용자의 질문을 보강하여 보다 정확한 문맥 제공.
* **Generation (생성):** 향상된 정보를 기반으로 더 좋은 답변 생성 (확실한 출처 기반).



### 2.3. RAG vs Fine-Tuning 비교

| 구분 | RAG (Retrieval-Augmented Generation) | Fine-tuning |
| --- | --- | --- |
| **개념** | 외부 지식을 추가하여 정확도, 신뢰도를 높일 수 있다. | 특정 작업에 대한 성능을 높일 수 있다. (예: 요약 작업 성능 향상) |
| **장점** | - 새로운 정보를 추가할 때, 추가 학습이 필요하지 않다.<br>

<br>- 답변의 근거(출처)를 확인할 수 있다. | - 매우 구체적인 태스크에 유용하며, 일관된 품질을 제공한다. |
| **단점** | - 검색된 정보의 품질에 의존한다.<br>

<br>- 검색 시스템을 통합해야 하므로 시스템 복잡도가 증가한다. | - 많은 양의 학습 데이터가 필요하다.<br>

<br>- 학습한 데이터 외의 질의에는 좋은 답변을 얻을 수 없다(Hallucination). |

### 2.4. RAG 이해를 위한 검색 이론 (Retrieval Algorithms)

* **역색인 (Inverted Index):** 각 단어가 어떤 문서(페이지)에 있는지 연결시켜 놓은 구조. (예: "학교" -> 3, 49, 100 페이지)
* **TF-IDF:** 문서 내 단어 빈도와 전체 문서 내 빈도를 고려하여 중요도 산출.
* **BM25:** TF-IDF의 단점을 보완한 알고리즘으로, 검색에 더 좋은 성능을 보임.
* **벡터 임베딩 (Vector Embedding):**
* **Sparse Embedding (희소 임베딩):** 키워드 기반 매칭. 단어가 다르면 의미가 같아도 매칭이 안 될 수 있음.
* *예시:* "점심을 못 먹었다" vs "식사를 거른 상태" (의미적 유사성이 있어도 단어가 달라 매칭 실패 가능성 있음)


* **Dense Embedding (밀집 임베딩):** 문장의 의미를 벡터화하여 비교.
* *특징:* 의미적 유사성이 필요한 경우 Dense Embedding을 사용해야 함. (BERT 등의 모델 사용 시 BM25보다 성능이 높은 경우가 많음)





---

## 3. LangChain (랭체인)

### 3.1. LangChain이란?

* LLM이 프로그래밍 언어(Python/Javascript)와 상호작용하여 외부 기능을 자유자재로 사용할 수 있게 해주는 **강력한 프레임워크**.
* **공식:** `Language Model + Chain = LangChain`
* LLM을 이용한 모든 것을 LangChain을 통해서 할 수 있음을 의미 (프롬프트 엔지니어링, 에이전트, RAG 등).

### 3.2. LangChain 구성 요소

1. **LLM 추상화 (Abstraction):** 사용자가 복잡한 내부 로직을 몰라도 사용할 수 있도록 추상화 제공.
2. **Prompts (프롬프트):** AI 모델에 전달할 명령어 템플릿.
3. **Index (인덱스):** 자체 학습 데이터셋이 포함되어 있지 않은 특정 외부 데이터 소스 지칭 (Document Loader, VectorDB, Text Splitters).
4. **Chains:** 여러 LLM 호출이나 작업을 연결.
5. **Agents:** LLM이 수행할 작업을 결정하고 도구를 사용.

### 3.3. 프롬프트 템플릿 예시 (Prompt Code)

영상 00:23에 등장한 RAG 시스템용 프롬프트 템플릿 내용입니다.

```text
You are an assistant for question-answering tasks.
이 프롬프트는 AI 모델이 답변 도우미 역할을 수행하는 것을 지정

Use the following pieces of retrieved context to answer the question.
모델이 질문에 답변할 때, 검색된 문서의 컨텍스트를 사용하도록 지시

If you don't know the answer, just say that you don't know.
모델이 답변을 모를 경우, 그냥 모른다고 답변하도록 지시
이는 모델이 부정확하거나 잘못된 정보를 생성하는 것을 방지하기 위함

Answer in Korean.
이 지시를 통해 답변이 항상 한국어로 생성

#Question: {question}
여기서 {question}은 사용자가 입력한 질문이 들어갈 자리
템플릿이 실행될 때 이 부분이 실제 질문으로 대체

#Context: {context}
{context}는 검색된 문서의 컨텍스트가 들어갈 자리
이 문맥 정보를 바탕으로 모델이 질문에 답변을 생성

#Answer:
이 부분은 모델이 답변을 작성하는 곳

```

### 3.4. Chat Model 및 파이프라인 (LCEL)

* **Chat Model:** `Input` (SystemMessage: 역할 지시, HumanMessage: 사용자 질문) -> `ChatGPT` -> `Output` (AIMessage: 답변).
* **LCEL (LangChain Expression Language):** 여러 체인을 연결하여 복잡한 워크플로우를 제어.

**[LCEL 파이프라인 예시]**

1. **Input:** `{'country': "미국"}`
2. **PromptTemplate:** `"{country}의 수도를 알려줘."`
3. **PromptValue:** `HumanMessage(content="미국의 수도를 알려줘.")`
4. **Model:** `model=ChatOpenAI()`
5. **AIMessage:** `content="워싱턴입니다."`
6. **StrOutputParser:** 문자열 파싱
7. **Result:** `"워싱턴입니다."`

### 3.5. LangChain 핵심: Retrieval (챗봇 구축 예시)

문서를 기반으로 챗봇을 구축하는 5단계 프로세스:

1. **문서 업로드 (Document Loader):** PDF 등의 문서를 가져옴.
2. **문서 분할 (Text Splitter):** 문서를 여러 분할(Chunk)로 나눔.
3. **문서 임베딩 (Embed to VectorStore):** LLM이 이해할 수 있도록 텍스트를 벡터(수치)화.
4. **임베딩 검색 (VectorStore Retriever):** 질문과 연관성이 높은 문서를 추출. (예: "What is Python?" 질의 시 관련 텍스트 검색)
5. **답변 생성 (QA Chain):** 검색된 관련 텍스트(Relevant Text)와 질문(Question)을 LLM에 넣어 답변 생성.

---

## 4. AI Agent (AI 에이전트)

### 4.1. 기본 개념

* **정의:** 사용자의 목표를 달성하기 위해 스스로 문제를 분석하고, 해결 가능한 작은 작업 단위로 분해(Planning)한 뒤, 필요시 외부 툴이나 API를 활용하여 작업을 수행하며, 결과를 반복적으로 검토(Self-Reflection)하고 개선하는 시스템.
* 단순히 텍스트를 생성하는 ChatGPT(LLM)의 상위 개념 또는 구성 요소로 볼 수 있음.

### 4.2. AI Agent vs ChatGPT 비교

| 구분 | AI Agent | ChatGPT |
| --- | --- | --- |
| **자율성과 상호작용 능력** | 사용자가 요구한 작업의 완료를 위해 활용 가능한 여러 도구와의 상호작용을 연쇄적, 자율적으로 수행할 수 있는 기술 | 기본 ChatGPT는 툴과 직접 상호작용하지 않음 (주로 단일 플러그인 등을 사용하여 질문에 답변) |

---
