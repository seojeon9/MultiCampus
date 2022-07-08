#  음식명과 가격을 파일로 생성해 놓고 해당 파일을 읽어와 메뉴로 사용한다.
#  해당 메뉴를 화면에 출력 한 후 사용자가 주문하는 내용에 따라 금액을 지불
# 받고 지불받은 금액의 거스름돈을 계산하여 주문내용과 받은 돈 거스름돈을
# 출력하는 프로그램을 작성하라.
#  사용자는 여러 음식을 같이 주문 할 수 있습니다.(사용자가 필요한 만큼 주문
# 받도록 하세요)

######################################################################
# import문
from init_menu import *
from order import *
from pay import *

read_menu()
show_menu()

order()
total = show_order_list()

if total == 0:
    print("계산할 금액이 없습니다. 안녕히 가세요")
else :
    pay_bill(total)