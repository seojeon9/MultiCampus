# 파이썬 내장함수
# 파이썬에 이미 만들어져 내장되어 있늖 함수들, 별도의 모듈을 import하지 않고 사용 가능
# 형식에 맞춰 함수 이름만 호출해서 사용
# print(), input(), type()

print("-------- abs() 함수 --------")
# abs(x) : x의 절대값 반환
print(abs(-10))

print("-------- all() 함수 --------")
# all(iterable) : 모든 요소가 참이면 True, 아니면 False 반환
# False : 0, True : 0이 아닌 모든 값
# 즉, 0이 하나라도 있으면 False 반환
# iterable : 반복 간으한 자료형, 각각의 요소를 하나씩 반환할 수 있는 형태
# for문으로 반복이 가능한 자료형 : 리스트, 튜플, 집합, 딕셔너리
print(all([1,2,3])) # True
print(all([0,1,2,3]))   # False

print("-------- any() 함수 --------")
# any(iterable) : 하나라도 참이면 True, 모두 거짓이면 False 반환
# False : 0, True : 0이 아닌 모든 값

print(any([0,0,0])) # False
print(any([0,1,2,3]))   # True
print(any([0,"",[]]))   # False
print(any([None,None])) # False

print("-------- chr() 함수 --------")
# chr(i) : 아스키 코드값에 해당하는 문자 반환
print(chr(97))  # a
print(chr(65))  # A
print(chr(13))  # enter

print("-------- ord() 함수 --------")
# 문자에 해당되는 아스키코드값 반환
print(ord('a')) # 97
print(ord('0')) # 48
print(ord('\n'))    # 10 (엔터가 아닌 new line)
print(ord(' '))    # 32
print(ord('\r'))    # 13 : enter

print("-------- divmod() 함수 --------")
# divmod(a,b) : a를 b로 나눈 몫과 나머지를 튜플형태로 반환
print(divmod(7,3)) # (2, 1)

print("-------- **enumerate() 함수 --------")
# enumerate(iterable, start = 0)
# 인덱스 값을 포함하는 enumerate 객체로 반환
print(enumerate(['kim','lee','park']))  # <enumerate object at 0x01BC8440>
# 반복 요소로 사용
for name in enumerate(['kim','lee','park']) :
    print(name)
    # (0, 'kim')
    # (1, 'lee')
    # (2, 'park')

for i, name in enumerate(['kim','lee','park']) :
    print(i, name)
    # 0
    # kim
    # 1
    # lee
    # 2
    # park

for i, name in enumerate(['kim','lee','park'], start=1) :
    print(i, name)
    # 1
    # kim
    # 2
    # lee
    # 3
    # park

# for문 처럼 반복되는 구간에서
# 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할 때
# 매우 유용

print("-------- filter() 함수 --------")
# 반복 가능한 자료형 요소들의 함수에 입력되었을 때 반환값이 참인것만 묶어서(걸러내서) 반환 -> 리스트 형태로 변환 후 사용
# filter(function명, iterable)
# 실습위한 함수 정의
def positive(x) :
    return x > 0  # True/false로 반환 / 양수만 반환

print(filter(positive, [0,-1,5,-7,10])) # <filter object at 0x01717150> -> filter객체
print(list(filter(positive, [0,-1,5,-7,10]))) # [5, 10]

def even_n(x) : # 짝수만 반환
    if x % 2 == 0 :
        return x
print(list(filter(even_n,[0.1,2,3,4,5,6,7,8])))   # [2, 4, 6, 8]

print("-------- hex() 함수 --------")
x = 0x569F # 16진수값 저장
# 점수를 0x 접두사가 붙은 소문자 16진수 문자열로 변환
# hex(7)
print(hex(7)) # 0x7
print(type(hex(7))) # <class 'str'>
print(hex(1234)) # 0x4d2

print("-------- **map() 함수 --------")
# map(fuction, iterable)
# iterable 각 요소를 함수에 전달해서 수행된 결과를 반환
# -> 여러개의 데이터를 함수에 적용시켜 한번에 반환받는 함수
def increase(x) : # x값을 전달받아 1증가 후 반환하는 함수
    return x + 1

print(map(increase,[1,2,3,4,5])) # <map object at 0x01E271F0>
print(list(map(increase,[1,2,3,4,5]))) # [2, 3, 4, 5, 6]

print("-------- open() 함수 --------")
# 파일 입출력과 관계있는 함수
# open(filename, [mode]) : mode 형식으로 파일 열기
# mode(읽기 방법) : 생략시 읽기 전용 모드(r)가 기본
# w, r, a, b
# 현재 디렉터리에 'my_file.txt'쓰기 모드로 생성
file_write = open('my_file.txt', 'w')   # file_write변수는 외부 파일인 my_file.txt을 사용할 수 있는 핸들러가 저장됨 (my_file.txt가 없으면 만들어서 열어라. 있으면 걍 열어라)
# 현재 디렉터리에 my_file.txt가 있는지 확인

print("-------- pow() 함수 --------")
# 제곱힌 결과값을 반환
print(pow(10,3))

print("-------- round() 함수 --------")
# 실수를 반올림하여 반환
# round(number,ndigits) ndigits : 표현할 소수 이하 자리수
print(round(3.141592,2))
print(round(3.141592,3))

print("-------- sum() 함수 --------")
# sum(iterable)
print(sum([1,2,3,4,5]))
print(sum((3,5,7,9)))

print("-------- zip() 함수 --------")
# zip(*iterable) : 긱 iterable에서 동일한 인덱스의 요소를 추출하여 묶어서 반환
# zip 객체로 반환하고 내부에 iterable 자료형으로 구성되어 있으므로 형변환해서 사용
print(zip([1,2,3],[4,5,6]))
print(list(zip([1,2,3],[4,5,6])))   # [(1, 4), (2, 5), (3, 6)]

# zip() 함수를 사용해서 튜플로부터 딕셔너리 생성
keys = ('apple','pear','peach')
vals = (300,250,400)
print(tuple(zip(keys,vals)))    # (('apple', 300), ('pear', 250), ('peach', 400))
result = dict(zip(keys,vals))
print(result) # {'apple': 300, 'pear': 250, 'peach': 400}

print("-------- **lambda식 함수 --------")
# 람다식 : lambda
# lambda :실행시(런타임)생성해서 사용할 수 있는 익명 함수
# 입력과 출력이 있는 간단한 한 행짜리 함숭를 만들 때 사용
# 같은 함수를 def 문으로 정의할때 보다 간결
# 형식 : lanbda 매개변수 : 표현식 (lambda 매개변수 : 리턴값)

# def로 정의한 함수
def add(a,b) :
    return a+b
print(add(3,5))

# 람다식으로 표현
print((lambda a,b:a+b)(3,5)) # 일회성 함수 -> 꼭 매개변수가 함수여야하는 함수가 있기 때문에 이와같은 일화성 함수 람다식이 필요함

# 람다식 재사용 : 변수에 할당해서 재사용 가능
lambda_add = lambda x,y : x+y
print(lambda_add(3,5))
print(lambda_add(6,7))  # 재사용을 할 것 같으면 def로 함수로 정의하는 것이 좋음(익명의 함수이기 때문, 하지만 요즘 개발자들은 간단한 함수의 경우 람다식으로 많이 사용함)



