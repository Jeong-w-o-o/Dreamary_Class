"""dremaryporject URL Configuration

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
from page import views # 뷰즈를 볼 수 있게 해줌

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), #아무 주소도 안 들어갔을 때 views에서 home이라는 함수 불러옴 이 path에 대해 home이라고 부름 
    #path는 세가지로 나눠짐 1. 어떤 주소 지정할지 2. 이 url은 어떤 함수를 실행할지 3. 이 url을 장고 프로젝트에서 어떻게 부를지 지정
]
