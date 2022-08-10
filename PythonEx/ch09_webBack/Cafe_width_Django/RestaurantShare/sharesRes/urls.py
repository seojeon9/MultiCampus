# sharesRes > urls.py

from django.urls import path
from . import views

urlpatterns = [
    #http://127.0.0.1:8000의 요청에 대한 처리
    path('',views.index, name='index'),

    # http://127.0.0.1:8000/restaurantDetail/delete
    path('restaurantDetail/delete', views.restaurantDelete, name='resDelete'),
    # http://127.0.0.1:8000/restaurantDetail/1
    path('restaurantDetail/<str:res_id>', views.restaurantDetail, name='resDetailPage'),
    # http://127.0.0.1:8000/restaurantDetail/updatePage/update
    path('restaurantDetail/updatePage/update', views.Update_restaurant, name='resUpdate'),
    # http://127.0.0.1:8000/restaurantDetail/updatePage/1 # update과 같은 모든 문자열도 파라미터로 보고 가져가기 때문에 순서를 뒤로 바꿔줘야 함
    path('restaurantDetail/updatePage/<str:res_id>', views.restaurantUpdate, name='resUpdatePage'),

    # http://127.0.0.1:8000/restaurantCreate/
    path('restaurantCreate/', views.restaurantCreate, name='resCreatePage'),
    # http://127.0.0.1:8000/restaurantCreate/create
    path('restaurantCreate/create', views.Create_restaurant, name='resCreate'),

    # http://127.0.0.1:8000/categoryCreate/
    path('categoryCreate/',views.categoryCreate, name='categoryCreatePage'),
    # http://127.0.0.1:8000/categoryCreate/create
    path('categoryCreate/create',views.Create_category, name='cateCreatePage'),
    # http://127.0.0.1:8000/categoryCreate/delete
    path('categoryCreate/delete',views.Delete_category, name='cateDeletePage'),




]
