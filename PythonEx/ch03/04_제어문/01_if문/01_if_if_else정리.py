# if문 조건식이 참이면 주어진 문장 수행, 조건식이 거짓이면 다음 수행을 진행한다.
num = 100

if (num >= 100) :
    print("num은 100보다 큰 값이 저장되어 있습니다.") # if문에 포함되는 문장으로 if 조건식이 참이면 실행되는 문장

print("num은 100보다 작은 값입니다.")    # if 조건식과 상관없이 무조건 실행되는 문장

# if~else문
# 조건식이 참이면 if 문 수행 / 조건식이 거짓이면 else 문을 수행
# if문 뒤에는 조건식이 반드시 마와야 하고, else문 에는 어떤 조건식도 나오면 안된다.

num = 100
num = 90
if (num >= 100):
    print("num은 100이상 입니다.")    # 조건식이 참일 때 수행
else :
    print("num은 100 미만 입니다.")   # 조건식의 결과가 거짓일 때 수행

print("num의 값은", num, "입니다.")   # if문을 벗어나서 무조건 실행

password = input("패스워드를 입력하세요 : ")  #input으로 받은 결과값은 str

# 결정되어 있는 패스워드 1234
if password == '1234' :
    print("비밀번호 일치 로그인!!!")
else :
    print("비밀번호 확인하세요.")

# if 문의 구조
# if (조건식)
# 들여쓰기(-탭/스페이스 4칸) 조건식이 참일 때 수행 할 문장

if password == '1234' :
    print("비밀번호 일치 로그인!!!")
else :
    pass # else 구문에서 수행 할 내용이 없을 때 비워 놓으면 에러발생 - pass를 이용해 지나가도록 처리