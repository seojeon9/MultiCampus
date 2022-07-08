# 변수(일반적인 의미)
# 값을 저장하기 위한 RAM 내의 기억장소

# 변수에 값 저장 형식
# 변수명 = 값(실제값, 변수명, 계산 결과)

x = 10  # x라는 변수를 생성 후 10을 저장
print(x)    # x변수에 접근해서 값을 추출(복사)한 후 화면에 전송

# 파이썬 변수 - 참조형 변수
# x변수에는 실제 값(객체)이 저장되어 있는 주소가 표시되어 있음
print(id(x))

#######################################################
# 변수에 값 저장 예제
result = 10 # 10 정수 저장
print(result)   # 10 정수 출력
print(type(result)) # <class 'int'>

result = 20.5   # 20.5 실수로 변수 값이 변경
print(result)   # 20.5 실수 출력
print(type(result)) # <class 'float'>

# 여러 개의 변수에 여러 개의 값 저장
a, b, c, d, = 1, 2, 3, 4
print(a, b, c, d)

# 여러 개의 변수에 한 개의 값 저장
a = b = c = 10
print(a)
print(b)
print(c)

# 두 변수의 값 교환(swap)
# 변수1, 변수2 = 10, 20
# 변수1, 변수2 = 변수2, 변수1
# 변수1, 변수2 = 20, 10
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

# 변수 삭제
# del 명령어 사용
# del 변수명
c = 100
print(c)
del c
# print(c) NameError: name 'c' is not defined