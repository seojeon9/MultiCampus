# 디폴트매개변수
# 매개변수에 기본값 지정하는 기능

# 해당 매개변수에 대응하는 값이 전달되면 전달된 값 사용, 전달되지 않으면 기본 값을 사용
def greet(name, msg) :
    print(name + ' ' + msg)

# 함수 호출
greet('홍길동','잘지내니?')
# greet('둘리')     #TypeError: greet() missing 1 required positional argument: 'msg'

# 디폴트 파라미터 msg
def greet_d(name, msg='안녕하세요') :
    print(name + ' ' + msg)

# 함수 호출
greet_d('홍길동','잘지내니?')
greet_d('둘리')   # 둘리 안녕하세요

# 디폴트 파라미터 주의 사항
# 디폴트 매개변수는 마지막에 위치해야함, 일반 파라미터보다 앞으로 갈 수 없다
# def greet_d1(msg='안녕하세요', name) :   #SyntaxError: non-default argument follows default argument
#     print(name + ' ' + msg)

# greet_d1('홍길동')

# 디톨트 매개변수는 여러개 사용할 수 잆음 단, 일반 파라미터 보다 위치적으로 뒤에 와야한다.
def greet_d2(name, msg='안녕하세요',d='2122/7/1', t = None) :
    print(name + ' ' + msg + d)

greet_d2('둘리','안녕','7월1일')
greet_d2('둘리','안녕')
greet_d2('둘리')
# greet_d2('둘리',,'7월1일') # SyntaxError: invalid syntax # 중간에 비워놓을 수 없고 순서대로 값을 줘야한다.