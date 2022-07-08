from menu_var import menu_list

# 1. 파일에서 음식명과 가격을 읽어온다
def read_menu() :
    data = open('menu.txt', 'r', encoding='utf-8')
    while True :
        menu = data.readline()
        if not menu : # 라인에 읽은 내용이 없으면
            break # 반복문 종료
        split_menu = menu.split(':')
        menu_list.append((split_menu[0],int(split_menu[1])))
        # print(split_menu, end='')
        # print(menu, end='')
    # print(menu_list)
    data.close()

# 2. 읽어 온 메뉴를 보여준다
def show_menu() :
    i = 1
    print("파이썬식당에 오신걸 환영합니다.")
    for menu in menu_list :
        print("%d. %s - %d원" % (i,menu[0],menu[1]))
        i += 1
