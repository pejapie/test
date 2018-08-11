from django.urls import path
# 어떤 주소로 접속했을 때 어떤 뷰를 작동할 것인지?
from .views import *

urlpatterns = [
    # http://127.0.0.1:8000/?/
    # path(urlpatterns, view, name),
    # name: 그 이름으로 해당 패턴을 찾고 싶을 때 사용
    path('', index, name='index'),
]