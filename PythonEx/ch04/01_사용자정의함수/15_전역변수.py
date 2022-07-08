# 15_전역변수.py
# 전역변수
# 함수 외부에서 정의된 변수
# 프로그램 내 모든 곳(함수내부 포함)에서 사용 가능
# 함수 내에서 전역변수 값을 변경(대입)하려면 : globl 사용

a=1 # 함수 밖에서 정의된 전역변수 a

# 함수 정의
def add() :
    c = a + b # 지역변수 c, 전역변수 a, 전역변수 b
    print("add()에서 출력")
    print(a)
    print(b)
    print(c)

def show() :
    print("show()에서 출력")
    print(a) #전역변수
    print(b) #전역변수

b = 2

# 함수 호출
add()
show()

# 함수 외부에서 전역 변수 사용
print("함수 외부에서 출력 : ")
print(a)
print(b)

# 함수 정의(전역변수 함수 내에서 변경)
def add1() :
    a=10 #지역변수 a
    a=a+1
    c=a+b #a,b가 전역변수, 지역변수 c
    print("add1()에서 출력")
    print(a)
    print(b)
    print(c)

def add2() :
    global a # 전역변수 a를 사용
    a=a+1 #a는 전역변수, 전역변수 a를 1 증가
    c=a+b #a,b가 전역변수, 지역변수 c
    print("add2()에서 출력")
    print(a)
    print(b)
    print(c)
    # print(d)    # NameError: name 'd' is not defined

add1()
add2()
# 함수 호출 후에 전역변수 d를 생성하면 호출 시 d변수를 인지할 수 없음

d = 10 # 전역변수 d 정의
print(a) # 전역변수 a 출력 - add2() 함수내에서 1 증가해서 2가 출력

# 전역변수를 함수 내에서 사용하려면 함수 호출전에 생성되어 있어야 함


