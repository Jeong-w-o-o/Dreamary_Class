from django.contrib import admin
from django.urls import path
from page import views # 뷰즈를 볼 수 있게 해줌
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), #아무 주소도 안 들어갔을 때 views에서 home이라는 함수 불러옴 이 path에 대해 home이라고 부름 
    #path는 세가지로 나눠짐 1. 어떤 주소 지정할지 2. 이 url은 어떤 함수를 실행할지 3. 이 url을 장고 프로젝트에서 어떻게 부를지 지정
    path('introduce/', views.introduce, name="introduce"),
    path('profile/<int:designer_id>', views.detail, name="detail"),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
