# Django_Form
### HTML Form
  - 사용자로부터 데이터를 제출 받기위해 활용한 방법
  - **비정상적이거나 악의적인 요청을 필터링 할 수 없음**
- 유효한 검사 필요
  - 수집한 데이터가 정확하고 유효한지 확인하는 과정
  - 보안 강화
  - DB 무결성 검사
  - UX 강화
## Form Class
### Django Form
- 백엔드 Form
1. forms.py 제작
```
from django import forms

class ArticleForm(forms.Form)
```
2. view 함수 new로 변경(예시임)
```
def new(request):
  form = ArticleForm()
```
3. new 페이지에서 form 인스턴스 추력
```
<form 태그>
{{form}}
</form>
```
- `{{form.as_p}},{{form.as_div}}` 처럼 렌더링 가능
- Widget 적용
  - input 요소의 속성 및 출력되는 부분을 변경하는 것
  - `forms.charField(widget=form.Textarea)`
### Django ModelForm
- Form
  - 사용자 입력 데이터를 DB에 저장하지 않을 때 사용 (검색, 로그인)
- ModelForm
  - 사용자 입력 데이터를 DB에 저장해야 할 때 사용 (게시글 작성 , 회원가입)
1. ModelForm class 정의
```
from django import forms

class ArticleForm(forms.ModelForm):
  class Meta:
      model = Article
      fields = '__all__'
```
- 메타 데이터 : 데이터의 데이터 (데이터를 설명하는 데이터) = 세부항목
- Meta clas
  - modelForm의 정보를 작성하는 곳
  - `__all__` : 전부다 불러오기
  - `('title',)` : title만 불러오기
  - `exclude = ('title',)` : title만 빼고 불러오기
  - Model과 연결된 Form을 자동으로 생성해주는 기능을 제공
### ModelForm 적용
- ModelForm을 적용한 create 로직
```
from .forms import ArticleForm

def create(request):
  form = ArticleForm(request.POST)
  if form.is_valid():   # 유효성 검
    article = form.save()
    return redirect('articles:detail', article.pk)
  context = {
    'form' : form,
  }
  return render(request, 'articles/new.html', context)
```
  - `is_valid`() : 데이터의 유효 여부를 Boolean으로 반환
- ModelForm을 적용한 edit 로직
```
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm()
    context = {
        'article' : article,
        'form':form,
        }
    return render(request, 'articles/edit.html', context)
```
- ModelForm을 적용한 update 로직
```
def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'form':form,
        }
    return render(request, 'articles/edit.html', context)
```
  - `instance=article` : instance 여부를 통해 수정인지 생성인지 확인 가능
### HTTP 요청 다루기
- view 함수 구조 변환
- new & create view 함수간 공통점과 차이점
  - 공통점
    - 데이터 생성을 구현학 위함
  - 차이점
    - new는 GET method 요청, create는 POST method 요청
  - 2개의 view 함수를 하나로 구조화
1. new & create 함수 결합
```
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid(): # 유효성 검사
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)
```
2. 기존 new 관련 코드 수정
3. 사용하지 않는 new url 제거
4. new 관련 키워드를 create로 변경
5. render에서 new 템플릿을 create 템플릿으로 변경

- update와 edit 결합
```
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form':form,
        }
    return render(request, 'articles/update.html', context)
```
1. 사용하지 않는 edit url 제거
2. edit 관련 키워드를 update로 변경
### 참고
- ModelForm 키워드 인자 data와 instance
  - data는 첫번째에 위치한 키워드 인자이기 때문에 생략 가능
  - instance는 9번째에 위치한 키워드 인자이기 때문에 생략 불가능
