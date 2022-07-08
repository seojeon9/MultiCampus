def pay_bill(total) :
    try :
        print("\n총 금액은 %s원 입니다." % format(total,','))
        money = int(input("얼마를 지불하시겠습니까? : "))

        while True :
            if money < total :
                print("\n금액이 부족합니다. 다시 확인해주십시오.")
                money = int(input("얼마를 지불하시겠습니까? : "))
            else :
                break

        balance = money - total
        show_bill(total, money, balance)
    except ValueError:
        print("\n%%숫자를 입력해주세요%%")
        pay_bill(total)


def show_bill(total, money, balance) :
    print("\n=========================================================")
    print("=====================  결제    내역  =====================")
    print("전체 금액\t : %s" % format(total,','))
    print("지불한 금액\t : %s" % format(money,','))
    print("거스름돈\t : %s" % format(balance,','))
    print("=========================================================")
    print("=========================================================")

