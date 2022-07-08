#  그림과 같이 예금액과 이자율을 입력 받아서
#  예금액, 이자율, 예금이자, 잔액 출력

deposits = float(input("예금액 입력 : "))
rate = float(input("이자율 입력(%) : "))

interest = int(deposits * rate) / 100
balance = deposits + interest

print("--------------------------------")
print("예금액 : %0.f 원" % deposits)
print("이자율 : %0.1f" % rate, r"%")
print("예금이자 : %d 원" % interest)
print("잔액 : %d 원" % balance)

print("--------------------------------")
print("예금액 : %s 원" % format(int(deposits),','))
print("이자율 : %0.1f" % rate, r"%")
print("예금이자 : %s 원" % format(int(interest),','))
print("잔액 : %s 원" % format(int(balance),','))
