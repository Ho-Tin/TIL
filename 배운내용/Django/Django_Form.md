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
- forms.py 제작
```
from django import forms

class ArticleForm(forms.Form)
```
- view 함수 new로 변경(예시임)
```
def new(request):
  form = ArticleForm()
```
- new 페이지에서 form 인스턴스 추력
```
<form 태그>
{{form}}
</form>
```
- {{form.as_p}},{{form.as_div}} 처럼 렌더링 가능
- Widget 적용
  - input 요소의 속성 및 출력되는 부분을 변경하는 것
  - ex) forms.charField(widget=form.Textarea)
### Django ModelForm
- Form
  - 사용자 입력 데이터를 DB에 저장하지 않을 때 사용 (검색, 로그인)
- ModelForm
  - 사용자 입력 데이터를 DB에 저장해야 할 때 사용 (게시글 작성 , 회원가입)
  - Model과 연결된 Form을 자동으로 생성해주는 기능을 제공
- 
