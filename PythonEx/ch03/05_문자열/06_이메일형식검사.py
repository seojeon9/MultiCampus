# @ 없는 경우
# . 없는 경우
# @과 . 위치가 바뀐 경우
# @과 . 사이에 문자가 없는 경우
# @ 앞에 문자가 없는 경우
# . 뒤에 문자가 없는 경우
# @ 두 번 이상 있는 경우
# . 두 번 이상 있는 경우

# 이메일 주소 입력받기
email = input("이메일 입력 : ")

if (email.find("@") == -1  or                   # @ 없는 경우
    email.find(".") == -1  or                   # . 없는 경우
    email.index("@") > email.index(".")  or     # @과 .의 위치가 바뀐 경우
    email.index(".")-email.index("@") < 2  or   # @과 .사이에 문자가 없는 경우
    len(email) - email.insex(".") <= 1  or      # . 뒤에 문자가 없는 경우
    email.count("@") >= 2  or                   # @ 두 번 이상 있는 경우
    email.count(".") >= 2 ) :                   # . 두 번 이상 있는 경우
    print("이메일 형식이 아닙니다.")

print("입력한 이메일 : ", email)