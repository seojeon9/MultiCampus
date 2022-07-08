# 사전 생성 모듈

# from dict_var import ek_dic # dict_var.py 파일이 동일한 경로에 존재하므로 바로 모듈명 사용
# ModuleNotFoundError: No module named 'dict_var'
# - 함수 호출 기준위치가 영어사전_모듈화.py
# 실행하고 있는 파일의 경로와 함수가 있는 파일의 경로가 달라서 나는 에러

# from dict.dict_var import ek_dic
from .dict_var import ek_dic

#################################################
# 사전 단어 등록 관련 함수
#################################################
# 1. 단어를 전달 받아 사전에 단어를 등록 : input_dict(eng)
def input_dict(eng) : # eng 매개변수 단어전달받기 위함
    # 단어에 해당하는 뜻 입력 받기
    kor = input(eng + " 뜻 입력 : ")
    # 사전에 등록
    ek_dic[eng] = kor
    # 반환값이 필요 없고 출력 값도 필요없음

# 사용자로부터 단어를 입력작아 사전에 단어가 있는지 검색 후
# - 단어가 없으면 input_dict(eng)함수 호출해서 뜻을 저장
# - 단어가 있으면 단어가 있다는 안내문구 내보냄
# - 단 사전등록을 사용자가 원하는 만큼 등록이 가능하게 할 것이므로 무한루프 사용
def const_dict() :
    while True : # 단 사전등록은 사용자가 원하는 만큼 등록이 간으하게 할 것이므로 무한루프 사용
        # 영어단어 입력 받기
        eng = input("\n영어 단어 입력 : (종료는 'q') : ")

        # 종료검사
        if eng == 'q' :
            print('단어 등록을 종료합니다. ')
            break # 반복 종료 (반복문 외에 함수에 다른 문장 없으므로 함수 종료)
        elif eng not in ek_dic : # 등록되지 않은 단어
            # 단어 등록 처리 함수 호출
            input_dict(eng)
        else :
            print("%s는 이미 등록된 단어입니다. " % eng)
