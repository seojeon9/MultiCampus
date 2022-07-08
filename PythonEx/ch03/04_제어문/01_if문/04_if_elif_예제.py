# 사용자로부터 정수 3개를 입력받아서 가장 큰수를 출력하는 프로그램

num1 = int(input("정수1을 입력하세요 : "))
num2 = int(input("정수2을 입력하세요 : "))
num3 = int(input("정수3을 입력하세요 : "))

if((num1 > num2) and (num1 > num3)) : #num1이 가장 큰 경우
    maxNum = num1
elif(num2 > num3) : #num2이 가장 큰 경우
    maxNum = num2
else :  #num3이 가장 큰 경우
    maxNum = num3

print("제일 큰 수 : ", maxNum)