# 영어사전 프로그램 - 클래스화

# 필요모듈 import
from dict_class import *

########################### main
# 새로운 사전 생성여부 학인
con_sel = int(input("새로운 사전을 생성하려면 1을 기존사전을 사용하려면 2를 입력하세요"))

if con_sel != 1 and con_sel != 2 :
    pass
else :
    print("새로 사전을 구성하시는 분은 새 사전의 사전명을 입력하세요")
    print("기존 사전 사용하시는 분은 기존 사전명이 필요합니다.")
    d_name = input("사전명을 입려가세요 : ")

    eng = Dict_Const(d_name) # 클래스 객체 인스턴스

    if con_sel == 2 : # 기존 사전 사용 - 사전 준비
        eng.load_dict()
    # 사전 사용 메뉴 프로그램
    #################################################
    # 메뉴 : 사전 프로그램은 사용자가 종료를 선택하면 완전 종료

    while True :
        print("=================메 뉴==================")
        print("1. 사전 등록 : ")
        print("2. 사전 검색 : ")
        print("3. 종료 : ")

        sel = input("사용할 메뉴를 선책 하세요. 1/2/3 : ")

        if sel == '1' :
            print("사전에 단어를 등록합니다. 원하는 단어 수 만큼 등록이 가능합니다.")
            # 사전 등록 함수
            eng.const_dict()

        elif sel == '2' :
            print("단어 1개에 대하여 검색합니다.")
            # 사전 검색 전 필터링 함수
            eng.search()

        else :
            print("사전 프로그램을 종료 합니다.")
            eng.save_dict() # 사전을 파일로 저장하는 함수
            break
