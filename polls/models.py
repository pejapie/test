from django.db import models

# Create your models here.
# 데이터베이스와 연결하기 위한 모델을 만드는 공간
# 여기는 데이터베이스에 연결하는 소스코드를 만드는 공간
# 데이터베이스 조작은 마이그레이션에서 한다.
# model = class

# 모든 모델은 models.Model 을 상속하여 사용한다.
# 모델 안에는 여러 개의 필드가 들어있다.
# 데이터베이스에 어떤 컬럼을 저정할 것이냐?
# 필드 이름 = 컬럼 이름
# 필드 종류 = 컬럼 데이터타입
# 필드의 인수(여기서는 max_length) = 컬럼의 제약사항

# front 관점
# 필드 이름 = form의 label
# 필드 종류 = 어떤 form tag를 사용할 것인지? input? textarea?
# 필드의 인수 = 제약사항

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# models.py 에 변경이 있을 때 마다 아래의 명령어를
# python manage.py makemigrations polls
# -> 데이터베이스에 바뀐 모델이 있음을 반영한다
#
# python manage.py sqlmigrate polls 0001
# ->어떤 쿼리로 실행되는지?
#
# python manage.py migrate polls 0001
# ->실제로 적용을 시킴