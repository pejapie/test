from django.shortcuts import render

# Create your views here.
# 기능과 로직을 담당하는 부분
# 함수형, 클래스형의 두 가지가 존재.

from django.http import HttpResponse

# 함수형 뷰
def index(request):
    return HttpResponse("Hello Django.")