# 다중 for 문

for y in range(3) : # 3번 반복
    for x in range(5) : # 바깥쪽 for문이 한번 반복할 때 마다 5번 반복을 실행
        print(x, end=" ") # 두번째 for문에 포함되는 문장, 실행은 15번 실행
    print() # 첫번째 for문에 포함되는 문장, 실행은 3번 실행

# 값을 1씩 증가하면서 출력
a = 0
for y in range(3) : # 3번 반복
    for x in range(5) : # 바깥쪽 for문이 한번 반복할 때 마다 5번 반복을 실행
        a += 1
        print(a, end=" ") # 두번째 for문에 포함되는 문장, 실행은 15번 실행
    print() # 첫번째 for문에 포함되는 문장, 실행은 3번 실행