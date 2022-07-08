# 사전 검색 모듈

# 필요 모듈 import
# from dict_var import ek_dic
# from dict_const import input_dict

# 실행되지만 다른 코드로 변경 (근데 나는 지금 dict를 찾지 못한다고 말함..)
# from dict.dict_var import ek_dic
# from dict.dict_const import input_dict

# .은 해당 모듈파일이 있는 위치가 기준 위치가 됨
from .dict_var import ek_dic
from .dict_const import input_dict

#################################################
# 검색 기능
# 1. 단어를 전달 받아 사전에 단어를 등록 : input_dict(eng)
def dict_search(eng) : # 단어가 사전에 있는 경우 호출
    print("%s의 뜻은 %s입니다. " % (eng, ek_dic[eng]))

# 2. 단어 하나 검색하는 함수
# - 단어 하나를 입력받아 입력 단어가 사전에 있으면 dict_search(eng)를 호출해서 뜻을 출력
# - 입력된 단어가 사전에 없으면 사전에 등록할 것인지 여부 확인
# - 등록하겠다고 하면
def search() :
    # 검색 단어 입력 받기
    eng = input("\n검색할 단어 입력 : ")

    if eng in ek_dic : # 사전에 있는 단어면
        dict_search(eng)
    else :
        print("%s는 사전에 없는 단어입니다. " % eng)
        # 사전 등록 여부
        answer = input('사전에 등록 하시겠습니까?(y/n)')
        if answer == 'y' :
            input_dict(eng)
            print("사전 등록 완료! 감사합니다!")
        print("\n 검색 종료 합니다.")
