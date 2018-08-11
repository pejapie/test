from django.contrib import admin

# Register your models here.
# 관리자 페이지에 내가 원하는 모델과 기능을 추가하기 위한 파일

from .models import *

# admin.site.register(모델명)
admin.site.register(Question)
# admin.site.register(Choice)

# python manage.py createsuperuser 로 최초 로그인 할 수 있는 어드민 계정을 만든다.
# 아이디, 이메일 주소, 비밀번호, 비밀번호 확인을 입력하라고 하는데 이메일은 필수가 아니다.

