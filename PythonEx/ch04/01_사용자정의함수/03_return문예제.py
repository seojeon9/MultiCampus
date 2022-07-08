# order()함수를 생성하시오
# order 함수 내부에서 상품가격, 주문수량을 입력받고 주문액을 계산해서, 상품가격, 주문수량, 주문액을 반환한다.
# 함수가 정상 동작하는지 호출 후 출력해서 확인하시오

def order() :
    pr = int(input("상품 가격 입력 : "))
    qt = int(input("주문 수량 입력 : "))
    amt = pr * qt
    return pr, qt, amt

# 함수 호출 test
# price, qty, amount = order()
# print("================================"
#       "\n상품가격 : ", price,
#       "\n주문 수량 : ", qty,
#       "\n주문액 : ", amount)

# result = order()
# print("================================"
#       "\n상품가격 : ", result[0],
#       "\n주문 수량 : ", result[1],
#       "\n주문액 : ", result[2])

print("================================"
      "\n상품가격 : ", order()[0],
      "\n주문 수량 : ", order()[1],
      "\n주문액 : ", order()[2])   # 세번의 호출이 일어남