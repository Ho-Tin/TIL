***

# Django Form 정리

## HTML Form
- 사용자로부터 데이터를 제출받기 위해 사용하는 방법  
- 하지만 단순 HTML `<form>`만 사용하면 **비정상적이거나 악의적인 요청을 필터링할 수 없음**  
- 따라서 Django에서는 **Form Class**를 통해 데이터를 검증하고, 보안을 강화하며 DB 무결성과 UX를 보장  

### 유효성 검사 필요성
- 데이터 정확성과 유효성 확보  
- CSRF, SQL injection 등 보안 문제 예방  
- Model(DB)의 무결성 보장  
- 에러 메시지를 통한 사용자 경험 향상  

***

## Django Form Class

### 일반 Form (forms.Form)
- DB에 직접 저장되지 않고, 단순히 **사용자의 입력값을 처리**할 때 사용  
- 예: 로그인, 검색창, 설문 입력 등  

#### 사용 방법
1. **forms.py 작성**
```python
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
```

2. **view 함수 작성**
```python
def new(request):
    form = ArticleForm()
    return render(request, 'articles/new.html', {'form': form})
```

3. **템플릿에서 출력**
```html
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">제출</button>
</form>
```

- 렌더링 방식: `form.as_p`, `form.as_table`, `form.as_ul`  
- Widget을 통해 input 태그 속성과 UI 변경 가능  

예시:
```python
forms.CharField(widget=forms.Textarea(attrs={'placeholder': '여기에 내용을 입력하세요'}))
```

***

## Django ModelForm

### 개념
- Django의 **Model**과 연결된 Form  
- 사용자 입력값을 **DB에 저장**할 수 있도록 자동으로 필드 생성  
- **Form vs ModelForm**
  - Form: 입력 데이터만 검증 (DB 저장 X)  
  - ModelForm: 입력 데이터를 DB에 저장 (게시글 작성, 회원가입 등)  

### 정의 방법
```python
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'   # 모든 필드 사용
        # fields = ('title', )   # 특정 필드만 선택
        # exclude = ('author', ) # 특정 필드 제외
```

- **Meta class** : ModelForm의 구조 정의  
- `fields` 또는 `exclude`로 사용할 필드 지정  

***

## ModelForm 활용

### Create (생성)
```python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()   # DB 저장
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    return render(request, 'articles/create.html', {'form': form})
```

- `form.save()` : Model 인스턴스를 자동으로 저장  
- `is_valid()` : 데이터 유효성 검사 → Boolean 값 반환  

***

### Update (수정)
```python
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)  # 기존 데이터 수정
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)  # 기존 데이터 채워 넣기
    return render(request, 'articles/update.html', {'form': form, 'article': article})
```

- `instance=article`: 기존 객체를 기반으로 Form을 채움 → 수정 기능 가능  

***

## HTTP 요청 다루기

- **new & create** (생성과 관련된 두 개의 함수 → 하나로 합침)  
- **edit & update** (수정과 관련된 두 개의 함수 → 하나로 합침)  

### 예시: create 함수 (GET + POST 처리)
```python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    return render(request, 'articles/create.html', {'form': form})
```

***

## 참고 사항

### ModelForm 키워드 인자
- `data` : 첫 번째 인자 (생략 가능, 예: `ArticleForm(request.POST)`)  
- `instance` : 수정 시 사용 (생략 불가, 예: `ArticleForm(request.POST, instance=obj)`)  

### 필드를 개별적으로 렌더링
```html
<div>
    {{ form.title.label_tag }}
    {{ form.title }}
    {{ form.title.errors }}
</div>
```

- 에러 메시지를 보여주는 방식 제공  

### save(commit=False)
- `form.save(commit=False)`로 실행 시 DB에 즉시 저장하지 않고 객체만 반환  
- 추가 가공 후 저장 가능  
```python
article = form.save(commit=False)
article.author = request.user
article.save()
```

***

## 정리
- **Form**: 단순히 입력값 검증 (로그인, 검색)  
- **ModelForm**: 모델과 연결되어 DB 저장 가능 (게시글 CRUD)  
- `is_valid()` → 유효성 검사 필수  
- `instance`로 새 객체 생성 vs 기존 객체 수정 구분  
- 하나의 View 함수에 GET/POST를 동시에 처리하면 코드가 더 깔끔해짐  

***
