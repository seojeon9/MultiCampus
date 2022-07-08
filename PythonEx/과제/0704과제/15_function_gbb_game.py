#  가위 바위 보 게임 함수 작성
#  함수명 : gbb_game()
#  랜덤으로 COM 숫자를 생성해서
#  전달받은 YOU 숫자와 비교하여
#  결과 출력

from random import randint

def gbb_game(you) :
    # 1: 가위, 2: 바위, 3: 보
    com = randint(1,3)

    # 'com'이 이기는 모든 경우의 수
    if ( com == 1 and you == 3 or
         com == 2 and you == 1 or
         com == 3 and you == 2) :
        print("컴퓨터가 이겼습니다.")
    elif (com == you) : # 비긴경우
        print("비겼습니다.")
    else :
        print("당신이 이겼습니다. ")

    print("com : %d " % com)

you = int(input("YOU 입력(1:가위, 2:바위, 3:보) : "))
gbb_game(you)