#  노래방 기계: 1곡에 2,000원
#  현재 잔액: 10,000원

song = 2000
money = 10000
count = 0

while money != 0 :
    count += 1
    money -= song

    print("노래를 " + str(count) + "곡 불렀습니다.")
    if money != 0 :
        print("현재 " + str(money) + "원 남았습니다.")
    else :
        print("잔액이 없습니다. 종료합니다.")
