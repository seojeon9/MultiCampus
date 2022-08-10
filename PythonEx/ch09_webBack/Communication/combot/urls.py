# combot > urls.py
from django.urls import path,include
from . import views

app_name = 'combot' # 네임스페이스 등록
urlpatterns = [
    # http://ocalhost:8000/combot/
    path('',views.index),

    # http://127.0.0.1:8000/combot/1 : 1은 질문번호
    path('<int:question_id>',views.detail, name='detail'),
    path('answer/create/<int:question_id>', views.answer_create, name='answer_create'),
    path('question/create/',views.question_create, name="question_create"),
]
