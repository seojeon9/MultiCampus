# 중첩 if 문
# if문에 다른 if문 포함되어 있는 경우
# if(조건식1) :
#     if(조건식 2):
#         문장 A
#     else:
#         문장 B
# else:
#     문장 C

# 사과 구매 프로그램
# 입력된 사과 상태가 신선이면 구매함 그렇지 않으면 구매하지 않는다
# 사과를 구매하기로 결정되었을 때 사과가격을 입력받아 1000원 미만이면 10개를 사고, 아니면 5개를 산다.

apple_quality = input("사과 상태 입력 : ")

if apple_quality == '신선' :
    # 사과를 구매
    apple_price = int(input('r개당 사과 가격 입력 : '))
    if apple_price < 1000 :
        print("10개를 산다")
    else:
        print("5개를 산다")
else:
    print("사과를 사지 않는다.")

