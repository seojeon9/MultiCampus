from menu_var import *

# 1. 주문 받기
def order() :
    for i in range(len(menu_list)) :
        order_list.append(0)    # 메뉴의 수만큼 주문리스트 크기 늘리기

    print("=========================================================")
    print('원하시는 메뉴의 번호를 입력해주세요(종료하고 싶으면 0을 입력해주세요)')

    while True :
        try :
            num = int(input('메뉴 번호 : '))
            if num == 0 :
                break
            elif num > len(menu_list) or num < 0 :
                print("잘못된 입력입니다.")
                continue
            qty = int(input('수량 : '))
            order_list[num-1] += qty
        except ValueError:
            print("\n%%숫자를 입력해주세요%%")
    # print(order_list)

# 2. 주문 내역 보여주기 + 총액 계산하기
def show_order_list() :
    total = 0
    print("\n=========================================================")
    print("=====================  주문    내역  =====================")
    for i in range(len(order_list)) :
        # print(i)
        qty = order_list[i]
        if qty != 0 :
            # print(menu_list[i])
            name = menu_list[i][0]
            price = menu_list[i][1]
            print("%s - %d개" % (name,qty))
            total += price * qty

    return total

