# Django에서의 View는 기능을 담당(페이지 단위로)
# 화면이 나타나는 뷰(템플릿이 있음), 화면이 없는 뷰(템플릿이 없을 때도 있음)

# View 내용(함수, 클래스) => URL이 있으면 동작한다.

# 함수형 : request를 매개변수로 받고(추가 매개변수 가능), 모양은 함수
#		  내가 원하는대로 동작들을 설계하고 만들고 싶을 때 사용한다.

# 클래스형 : CRUD(Create, R, Update, Delete) 기존에 많이 사용하는 기능을 미리 클래스로 만들어두고
#			상속받아서 사용한다.
#			보통 클래스형을 많이 씀(제네릭 뷰가 편하기 때문에)

# 장고가 미리 만들어 놓은 뷰(읽기, 쓰기 등)를 제네릭 뷰(Generic View)라고 한다.


from django.http import HttpResponse
# 템플릿을 렌더링 해주는 것
from django.shortcuts import render


# 이 화면을 보려면 URL 주소가 필수 !
# 어떤 매개변수를 가지고 있는지 request안에 들어가 있음
# 기본 함수형 사용
def index(request):
    # 어떤 계산이나 데이터베이스 조회, 수정, 등록 작업을 하여
    # 응답 메시지를 만들어서 반환.
    # html 변수를 대신해서 템플릿을 사용할 것임(앞으로)
    html = "<html><body>Hello</body></html>"
    return HttpResponse(html)


# 실습
# 뷰의 이름은 : welcome
# 뷰의 접속 주소 : welcome/
# 내용은 : Welcome to Django.
def welcome(request):
    html = "<html><body>Welcome to Django!</body></html>"
    return HttpResponse(html)


# 템플릿 이용
def template_test(request):
    # 기본 템플릿 폴더
    # 1. admin 앱
    # 2. 각 앱의 폴더에 있는 templates 폴더
    # 3. 우리가 설정한 폴더
    return render(request, 'test.html')


# 연습할 것
# 함수형 뷰 만들기, 템플릿 만들기, URL 연결하기, 브라우저로 접속해보기
