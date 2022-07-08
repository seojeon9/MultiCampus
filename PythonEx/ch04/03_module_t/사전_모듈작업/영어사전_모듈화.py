# 영어사전 프로그램 - 모듈화

# dict_const.py
# 사전 생성 모듈 : 단어를 사전에 등록하는 기능
# 1. 단어를 전달 받아 사전에 단어를 등록 : input_dict(eng)
# 2. 등록된 단어 필터링 : const_dict()

# dict_search.py
# 사전 검색 함수 : 등록된 사전을 이용해 검색 기능
# 1. 단어를 전달받아 뜻을 검색 후 출력하는 함수 :dict_search(eng)
# 2. 검색하려는 단어를 입력받아 사전에 있는지 필터링 : search()

# 공용 사용 변수 모음
# dict_var.py

# 필요 모듈 import
from dict.dict_const import * # dict 패키지의 dict_const모듈의 모든 함수 사용
from dict.dict_search import * # dict 패키지의 dict_search모듈의 모든 함수 사용
from dict.dict_inout import * # dict 패키지의 dict_search모듈의 모든 함수 사용

# 사전 사용 메뉴 프로그램

#################################################
# 메뉴 : 사전 프로그램은 사용자가 종료를 선택하면 완전 종료

while True :
    print("=================메 뉴==================")
    print("1. 시잔 등록 : ")
    print("2. 사전 검색 : ")
    print("3. 종료 : ")

    sel = input("사용할 메뉴를 선책 하세요. 1/2/3 : ")

    if sel == '1' :
        print("사전에 단어를 등록합니다. 원하는 단어 수 만큼 등록이 가능합니다.")
        # 사전 등록 함수
        const_dict()
    elif sel == '2' :
        print("단어 1개에 대하여 검색합니다.")
        # 사전 검색 전 필터링 함수
        search()
    else :
        print("사전 프로그램을 종료 합니다.")
        save_dict()  # 사전을 파일로 저장하는 함수
        break
