# break 문
# continue 문

# continue문 예제
x = 0
while x < 10 :
    x += 1
    if x % 2 == 0 : # 짝수이면
        continue    # 현재 시점의 반복을 중단하고
    print(x)    # if조건이 참이면 continue문을 만나서 이 문장은 수행되지 않음

# continue와 break 차이점
x = 0
while x < 10 :
    x += 1
    if x % 2 == 0 : # 짝수이면
        break    # 모든 반복을 강제 종료하고 반복문을 벗어남
    print(x)