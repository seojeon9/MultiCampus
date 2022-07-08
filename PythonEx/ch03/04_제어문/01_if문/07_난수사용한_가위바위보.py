# 랜덤숫자 생성을 위한 모듈 inport
from random import randint

# 1: 가위, 2: 바위, 3: 보
n = randint(1,3)

# 숫자-가위바위보 변환
if n == 1 :
    com = '가위'
elif n == 2 :
    com = '바위'
else :
    com = '보'

you = input("YOU 입력(가위/바위/보) : ")

# 'com'이 이기는 모든 경우의 수
if (com == '가위' and you == '보' or
    com == '바위' and you == '가위' or
    com == '보' and you == '바위') :
    print("컴퓨터가 이겼습니다.")
elif (com == you) :
    print("비겼습니다.")
else :
    print("당신이 이겼습니다.")

print("컴퓨터는 %s 입니다." % com)