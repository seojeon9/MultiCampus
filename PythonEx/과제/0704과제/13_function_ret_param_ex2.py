#  다음의 함수를 포함하는 프로그램 작성
#  함수 이름 : get_interest()
#  예금액과 이자율을 전달받아서 이자액을 구하여 반환
#  deposit, int_rate, interest

def get_interest(deposit, int_rate) :
    return (deposit * int_rate) / 100

deposit = int(input("예금액 입력 : "))
int_rate = float(input("이자율 입력(%%) : "))

print("이자액 : %s원" % format(int((get_interest(deposit,int_rate))),','))