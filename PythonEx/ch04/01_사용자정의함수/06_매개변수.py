# 매개 변수 (parameter)
# 함수로 전달되는 값을 받는 변수
#
# 인수 (argument)
# 함수에게 실제로 전달되는 값

# 매개변수가 있는 함수
# 이름을 전달받아 출력하는 함수 show_name
def show_name(name) :
    print(name)

# 호출 테스트
# TypeError: show_name() missing 1 required positional argument: 'name'
# show_name()
show_name('홍길동')

# 여러개의 매개변수가 있는 함수
# 3과목의 점수를 전달받아 평균을 구해서 반환하는 함수 get_average()
def get_average(k,e,m) : # 매개변수 k,e,m
    return (k+e+m) / 3

# 함수 test
print("평균 : %.2f" % get_average(90,80,65))

# 함수 test2
kor = int(input("국어 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))
math = int(input("수학 점수 입력 : "))
print("평균 : %.2f" % get_average(kor,eng,math))
