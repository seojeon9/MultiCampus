# 주어진 num 변수의 저장된 숫자가 음수/양수/0인지를 판단하는 프로그램

num = 10

# 사용자가 입력하는 숫자가 음수/양수/0인지를 판단하는 프로그램
num = int(input("정수만 입력하세요 : "))

if num < 0 :
    print("음수")
elif num > 0 :
    print("양수")
else :
    print("0")