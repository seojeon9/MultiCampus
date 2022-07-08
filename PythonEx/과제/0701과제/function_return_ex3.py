#  다음의 함수를 포함하는 프로그램 작성
#  함수명 : order()
#  상품가격, 주문수량을 입력 받아서, 주문액을 구하여 반환

def order() :
    price = int(input("상품가격 입력 : "))
    qt = int(input("주문수량 입력 : "))
    return price,qt,price*qt

price, qt, amount = order()
print("상품가격 : %d원" % price)
print("주문수량 : %d개" % qt)
print("주문액 : %d원" % amount)