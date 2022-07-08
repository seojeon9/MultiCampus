#  다음과 같은 함수를 포함하는 프로그램 작성
#  함수명 : order()
#  상품 가격과 주문 수량을 전달 받아서
#  주문액, 할인액, 지불액을 계산하여 반환
#  price, qty, amount, discount, total
#  할인액
#  주문액이 10만원 이상이면 10% 할인
#  주문액이 5만원 이상 10미만이면 5% 할인
#  주문액이 5만원 미만이면 할인 없음

def order(price, qty) :
    amount = price * qty
    if amount >= 100000 :
        rate = 10
    elif amount >= 50000 :
        rate = 5
    else :
        rate = 0
    discount = (amount * rate) / 100
    total = amount - discount
    return amount,discount,total

price = int(input("상품 가격 입력 : "))
qty = int(input("주문 수량 입력 : "))
print("--------------------------------")

amount,discount,total = order(price, qty)

print("주문액 : %d원\n"
      "할인액 : %d원\n"
      "지불액 : %d원" % (amount,discount,total))