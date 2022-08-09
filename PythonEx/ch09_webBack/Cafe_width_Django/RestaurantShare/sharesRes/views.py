# from django.http import HttpResponse
from django.shortcuts import render

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
    return render(request,'SharesRes/index.html')
    # return HttpResponse('index')

def restaurantDetail(request) :
    return render(request, 'SharesRes/restaurantDetail.html')


def restaurantCreate(request) :
    return render(request, 'SharesRes/restaurantDetail.html')


def categoryCreate(request) :
    return render(request, 'SharesRes/restaurantDetail.html')
