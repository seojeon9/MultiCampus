# in / not in
# 문자열 안에 특정 문자열이 포함되어 있는지 여부를 반환
# True/False 결과 반환

string = "Python Programming"

print("Python" in string)
print("programming" in string)  # 대소문자 구별

if "python" in string :
    print("있음")
else :
    print("없음")

if "python" not in string :
    print("없음")
else :
    print("있음")

# in 연산자와 list
ids = ["sun", "flower", "moon", "sky"]
print("a" in ids)

ID = input("ID 입력 : ")

if ID in ids :
    print("로그인 성공")
else:
    print("로그인 실패")