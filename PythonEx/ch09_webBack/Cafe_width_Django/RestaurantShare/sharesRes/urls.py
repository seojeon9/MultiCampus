# sharesRes > urls.py

from django.urls import path
from . import views

urlpattern ={
    #http://127.0.0.1:8000의 요청에 대한 처리
    path('',views.index, name='index'),
    # http://127.0.0.1:8000/categoryCreate/
    path('categoryCreate/',views.categoryCreate, name='categoryCreatePage'),
    # http://127.0.0.1:8000/restaurantCreate/
    path('restaurantCreate/', views.restaurantCreate, name='restaurantCreatePage'),
    # http://127.0.0.1:8000/restaurantDetail/
    path('restaurantDetail', views.restaurantDetail, name='restaurantDetailPage')
}
