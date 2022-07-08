# 등록된 ID와 비밀번호를 확인해서 로그인 성공 여부를 출력하는 프로그램
# ID : flower, 비밀번호 : 1234

ID = 'flower'
password = '1234'

input_id = input('아이디 입력 : ')
input_pass = input('비밀번호 입력 : ')

if((input_id == ID) and (input_pass == password)) :
    print("로그인 성공 ")
else :
    print("로그인 실패 ")