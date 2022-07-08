# 가위바위보 게임 함수구성
# 내가 낸 결과를 전달받아 컴퓨터와 게임을 진행 한 후 결과를 출력하는 함수 gbb_game()
# 랜덤숫자 생성을 위한 모듈 import
from random import randint

def gbb_game(you) :
    # 1: 가위, 2: 바위, 3: 보
    n = randint(1,3)

    # 숫자-가위바위보 변환
    if n == 1 :
        com = "가위"
    elif n == 2 :
        com = "바위"
    else :
        com = "보"

    # 'com'이 이기는 모든 경우의 수
    if ( com == "가위" and you == "보" or
         com == "바위" and you == "가위" or
         com == "보" and you == "바위") :
        print("컴퓨터가 이겼습니다.")
    elif (com == you) : # 비긴경우
        print("비겼습니다.")
    else :
        print("당신이 이겼습니다. ")

    print("컴퓨터는 %s 입니다. " % com)

################### 함수 사용
# 게임 진행
# 사용자가 원하는 만큼 게임 진행(무한루프)하도록 변경
# 엔터만 입력하면 게임 종료

while True :
    you = input("YOU 입력(가위/바위/보/종료시 엔터키만) : ")
    if you == "" :
        print("게임을 종료합니다")
        break
    gbb_game(you)