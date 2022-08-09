from django.db import models

# Create your models here.
class Category(models.Model) :
    # 테이블에 category_name 이라는 문자열을 저장할 컬럼을 추가하는 코드
    category_name = models.CharField(max_length=100)

class Restaurant(models.Model) : # 맛집 table
    # category 필드는 ForeignKey로 설정(만약 특정 카테고리를 삭제하면 해당 카테고리에 포함되어 있던 맛집들은 기본그룹으로 변경)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=6)
    restaurant_name = models.CharField(max_length=100) # 맛집 이름
    restaurant_link = models.CharField(max_length=500) # 맛집 URL
    restaurant_content = models.TextField() # 맛집 설명
    restaurant_keyword = models.CharField(max_length=50) # 키워드
