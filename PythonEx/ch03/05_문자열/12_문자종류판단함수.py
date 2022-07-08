# isalpha()
# 문자 여부 결과 반환 (True, False)
# isdigit()
# 숫자 여부 결과 반환 (True, False)
# isspace()
# 하나의 문자에 대해 공백 여부 결과 반환 (True, False)
# isalnum()
# 문자 또는 숫자 여부 결과 반환 (True, False)

phone = input("전화번호 입력하세요(구분기호 없이 숫자만 입력)")

if phone.isdigit() :
    pass
else :
    print("숫자만 입력하세요. ")

name = input("이름 입력 : ")

if name.isalpha() :
    pass
else:
    print("문자만 입력하세요")

# 위 코드와 동일한 결과
if not(name.isalpha()) :
    print("문자를 입력하세요.")

ID = input("ID 입력(문자와 숫자로만 구성) : ")
if not(ID.isalnum()) :
    print("문자와 숫자만 사용할 수 있습니다.")

###########################################
# isspace() : 스페이스 여부 확인(전체 문자가 공백인지 확인)
print(' '.isspace())
print(' c'.isspace())   # False
print('   '.isspace())  # True
