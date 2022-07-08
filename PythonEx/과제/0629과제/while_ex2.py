#  1부터 사용자가 입력한 숫자 까지의 홀수의 합을 구하는 프로그램을 while 문으로 작성하시오

num = int(input("마지막 숫자를 입력하세요 : "))
i = 1
sum = 0

while i <= num :
    if i % 2 == 1 :
        sum += i
    i += 1

print("1부터 %d 까지의 홀수의 합은 %d 입니다." % (num,sum))