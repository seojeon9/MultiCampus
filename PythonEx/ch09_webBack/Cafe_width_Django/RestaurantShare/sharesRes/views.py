from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *

## 오늘의 과제
## index함수 구성 : https:/127.0.1:8000
## 1. "메인페이지를 호출했습니ㅏㄷ." 가 클라이엍느로 전송되게 코딩
## 2. 위에서 작성한 코드를 주석처리 하고 index.html파일이 클라이언트 한테 전송되게 코딩

# def index(request) :
#     # 1. "메인페이지를 호출했습니다" 가 클라이언트로 전송되게 코딩 HttpResponse()
#     # return HttpResponse('메인 페이지를 호출했습니다.')
#     # 2. 위에서 작성한 코드를 주석처리하고 index.html 파일이 클라이언트에게 전송되게 코딩 render()
#     return render(request,'sharesRes/index.html')

# Create your views here.
def index(request) :
    categories = Category.objects.all() # select * from category
    restaurants = Restaurant.objects.all() # select * from restaurant;
    # rendering 하기 위한 dict로 구성
    content = {'categories':categories, 'restaurants':restaurants}
    return render(request,'SharesRes/index.html', content)
    # return HttpResponse('index')

def restaurantDetail(request, res_id) :
    # res_id는 url에 포함되어 전달되는 맛집 id임 url패턴 설정시 추가해준
    # arg이기 때문에 반드시 처리함수에서 파라미터로 받아줘야 함

    # res_id에 해당하는 맛집 정보를 db에서 추출
    rest = Restaurant.objects.get(id=res_id)
    content = {'rest':rest}
    return render(request, 'SharesRes/restaurantDetail.html', content)


def restaurantCreate(request) :
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'SharesRes/restaurantCreate.html', content)


def categoryCreate(request):
    categories = Category.objects.all()
    content = {'categories':categories}
    return render(request, 'sharesRes/categoryCreate.html',content)


def Create_category(request) : # 카테고리 새로 추가하는 함수(카테고리 추가 후 다른 함수로 reverse)
    # 서버에 전달된 추가될 카테고리명 반환받기 - request에 저장되어 있음
    category_name = request.POST['categoryName']
    # db table(sharesRes_category)에 저장하기 위해 모델 객체 생성
    new_category = Category(category_name = category_name)
    # 모델 객체를 통해 db저장
    new_category.save()
    # index 페이지 재요총
    return HttpResponseRedirect(reverse('index'))

def Delete_category(request) :
    category_id = request.POST['categoryId'] # hidden 태그로 전송됨
    del_cate = Category.objects.get(id=category_id) # db 접근 객체 생성
    del_cate.delete() # 접근객체이용 해당 행 삭제
    return HttpResponseRedirect(reverse('categoryCreatePage'))

def Create_restaurant(request) :
    # 맛집 정보를 추출해 db에 저장
    # 맛집 추가에 사용자가 입력한 정보를 추출
    category_id = request.POST['resCategory']
    # 해당 category_id가 있는지 확인 추출
    # id가 없어서 none이 반환되면 기본 id로 저장됨
    category = Category.objects.get(id=category_id)
    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']

    # 저장을 위한 모델 객체 생성
    new_res = Restaurant(category=category,
                         restaurant_name=name,
                         restaurant_link=link,
                         restaurant_content=content,
                         restaurant_keyword=keyword)
    # db 저장
    new_res.save()
    # 기본 index 페이지로 reverse
    return HttpResponseRedirect(reverse('index'))

def restaurantUpdate(request,res_id) :
    categories = Category.objects.all()
    rest = Restaurant.objects.get(id=res_id)
    content = {'categories':categories,'rest': rest}
    return render(request,'sharesRes/restaurantUpdate.html', content)

def Update_restaurant(request) :
    # 클라이언트가 전송한 맛집 수정 값 추출
    res_id = request.POST['resId']
    cng_cte_id = request.POST['resCategory']    # ForeignKey로 되어 있어 id를 저장하는 것이 아니라 객체를 저장해줘야함
    cng_category = Category.objects.get(id=cng_cte_id)
    cng_name = request.POST['resTitle']
    cng_link = request.POST['resLink']
    cng_content = request.POST['resContent']
    cng_keyword = request.POST['resLoc']
    # 수정한 대상인 맛집의 테이블내 행(레코드) 접근 객체 생성
    b_rest = Restaurant.objects.get(id=res_id)
    # 접근 객체의 각 컬럼에 수정한 내용 대입
    b_rest.category = cng_category
    b_rest.restaurant_name = cng_name
    b_rest.restaurant_link = cng_link
    b_rest.restaurant_content = cng_content
    b_rest.restaurant_keyword = cng_keyword
    # 테이블에 변경내용 저장
    b_rest.save()
    # resDetailPage Url은 args가 설정되어 있으므로 해단 args를 같이 넘겨줘야 함 : kwargs={'res_id': res_id}
    return HttpResponseRedirect(reverse('resDetailPage',kwargs={'res_id': res_id}))

def restaurantDelete(request) :
    # 삭제하려는 맛집 id 추출
    res_id = request.POST['resId']
    # 해당 id의 접근 객체 생성
    del_rest = Restaurant.objects.get(id=res_id)
    # 해당 맛집 삭제
    del_rest.delete()

    return HttpResponseRedirect(reverse('index'))








