# 공백 제거
# strip() : 양쪽 공백 제거
# lstrip() : 왼쪽 공백 제거
# rstrip() : 오른쪽 공백 제거

s1 = "   hell o   "
print(s1)
print(s1.strip())   # 원본에 반영되지 않는다.
print(s1.lstrip())
print(s1.rstrip())

ID = "sun"
input_id = input("아이디 입력 : ")

if ID == input_id.strip() :
    print('로그인 성공')
else :
    print("로그인 실패")
