from django.contrib import admin
from django.urls import path, include
from page import views # 뷰즈를 볼 수 있게 해줌
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
