# 상수 : 값이 변경되지 않는 저장공간
# 파이썬에서는 별도의 상수가 없음
# 변수와 구분하기 위해 식별자를 대문자로 사용하기로 함
# 상수의 값을 변경해도 오류가 없음

# 원의 면적을 구하는 프로그램
PI = 3.141592

r = 10
area = r * r * PI
print(area)

###########################
#이자와 잔액을 구하는 프로그램
INT_RATE = 0.03

deposit = 10000
interest = deposit * INT_RATE
balance = deposit + interest

print(balance)
print(int(balance)) # 정수형으로 변환

# 천단위 구분 기호 사용
# foramt(수치데이터, ',')
print(format(int(balance),','))
print(type(format(int(balance),',')))