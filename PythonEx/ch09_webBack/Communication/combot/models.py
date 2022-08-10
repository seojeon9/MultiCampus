from django.db import models
from django.utils import timezone

def default_time():
    return timezone.now() + timezone.timedelta()

# Create your models here.
class Question(models.Model) :
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(default=default_time)

    def __str__(self):
        return self.subject

# Question 입장에서는 Answer가 ForeignKey로 연결되어 있으므로
# 장고는 Question 객체 메서드로 ForeignKey로 연결된 클래스명_set.create()를 제공
# 클래스명은 전부 소문자여야 함
# 이 메서드의 기능은 ForeignKey로 연결된 클래스(table)에 레코드(행)저장을 가능하게 한다.

class Answer(models.Model) :
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
