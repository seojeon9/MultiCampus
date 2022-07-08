# 함수 정의
# 길동이으 이름과 나이를 출력해주는 함수
# 함수 정의 예약어 : def 함수명() :

def show_gildong() :
    print("성명 : 홍길동")
    print("나이 : 20")
    # 정의된 함수는 함수 자체의 실행으로는 작동하지 않는다.

# 길동이의 이름과 나이를 확인하기 위해 함수 호출
# 함수의 호출 : 함수명()
# show_gildong()
# sum_c() # NameError: name 'sum_c' is not defined

# sum() 함수를 아래 조건으로 생송하시오
# 함수 내부 문장에서 숫자 두개를 입력받아서 두 수의 합을 구하여 출력하는 함수
def sum_c() :
    num1 = eval(input("숫자 1을 입력하세요"))
    num2 = eval(input("숫자 2을 입력하세요"))
    total = num1 + num2
    print("두 수의 합은 ", total)

sum_c() # 호출
show_gildong()