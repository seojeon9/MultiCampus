# 현재 잔액 10,000원 있는 노래방 기계에 1곡에 2,000원이면 노래를 불렀을 때 몇곡째인지와 잔액을 표시하는 프로그램

song = 2000
money = 10000
count = 0

while money != 0 :
    count += 1
    money -= song

    print("노래를 " + str(count) + "곡 불렀습니다. 잔액 : " + str(money))