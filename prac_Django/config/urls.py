"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import index, welcome, template_test

urlpatterns = [
    path('admin/', admin.site.urls),
    # ''은 가장 넓은 범위이기 때문에 위에서 매칭이 안되면 ''path로 갈 가능성이 높기 때문에 가급적 가장 아래 두는게 좋음
    path('welcome/', welcome),
    path('test/', template_test),
    # path(주소, 뷰, 주소의 별명)   
    # index라는 뷰를 동작하게 할 것이다
    path('', index),
]
