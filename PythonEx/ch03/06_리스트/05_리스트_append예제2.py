# 사용자로부터 회원의 이름을 입력받아 리스트에 저장하고 저장된 내용이 맞는 출력정보를 내보내는 프로그램

# 회원 이름을 입력받되 사용자가 종료 문구인 q를 입력할 때까지 명단을 입력받기
# 명단을 저장할 빈 리스트 생성
members = []

# 리스트에 추가(append())
while True :
    member = input("회원입력(입력의 종료는 'q') : ")
    if member == 'q' :
        break
    members.append(member)

# members 내용을 아래와 같은 형식으로 출력하시오.
# 회원명단 : 명단1, 명단2, 명단3

print("회원 명단 : ", end=" ")

for member in members :
    print(member, end=", ")