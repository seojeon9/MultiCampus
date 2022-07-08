# range() 함수
# 특정 범위의 정수 생성

# 형식1. range(숫자1)

print(range(10))

# 형식2. range(start, stop) : start에서 stop-1까지의 정수
# 반복문을 통해서 범위의 원소 값 확인 가능
for i in range(0,10) : #범위 0~9까지 생성
    print(i, end=" ")

print()
# 형식3. range(start, stop, step) : start에서 stop-1까지 step 간격으로 정수 생성
for i in range(0,10,2) : # 범위 0~9까지 범위에 대해 2씩 증가하면서 정수 생성
    print(i, end=" ")

print()
for i in range(11, 21):  # 범위 11~20까지 생성
    print(i, end=" ")

print()
for i in range(1, 11, 2): # 1 3 5 7 9
    print(i, end=" ")

print()
for i in range(20, 11, -1): # 20 19 18 17 16 15 14 13 12
    print(i, end=" ")

# +range함수는 정수를 만들어내는 함수이다. 실수 안됨