#  다음과 같이 이름이 명단에 있는지 검색
#  ["홍길동", "이몽룡", "성춘향", "변학도"]

list = ['홍길동', '이몽룡', '성춘향', '변학도']

input_name = input("이름 입력 : ")
result = 0

for name in list:
    if(name == input_name) :
        print("명단에 있습니다.")
        result = 1
        break

if result == 0 :
    print("명단에 없습니다.")
