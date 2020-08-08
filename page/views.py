from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html') # 홈에서는 요청 (request)이 들어오면 요청과 함께 home.html을 돌려줌

def introduce(request):
    return render(request, 'introduce.html')