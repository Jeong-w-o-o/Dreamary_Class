from django.shortcuts import render, get_object_or_404
from .models import Designer

# Create your views here.

def home(request):
    designers = Designer.objects.all()
    return render(request, 'home.html', {'designers' : designers}) # 홈에서는 요청 (request)이 들어오면 요청과 함께 home.html을 돌려줌 + 값을 넘겨줄 게 있으면 씀

def introduce(request):
    return render(request, 'introduce.html')

def detail(request, designer_id): # views.py의 pk 변수명과 urls.py의 변수명은 같아야 함
    designer = get_object_or_404(Designer, pk = designer_id)
    return render(request, 'detail.html', {'designer' : designer})