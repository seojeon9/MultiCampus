#  다음과 같이 프로그램 작성
#  상품번호 입력 시 1, 2 이외의 숫자 입력하면 프로그램 종료
#  할인액
#  주문액이 백만원 이상 - 10%
#  백만원 미만 5십만원 이상 - 5%
#  5십만원 미만 할인 없음


notebook = 1200000   #1
camera = 400000     #2

print("********상품 정보********\n"
      "1 노트북 : %s 원\n"
      "2 디지털카메라 : %s 원\n"
      "***********************" % (format(int(notebook),','), format(int(camera),',')))

no = int(input("상품번호 입력 : "))

if no == 1 or no ==2 :
    pass
else:
    print("잘못 입력하였습니다. 종료합니다.")
    quit()

num = int(input("주문 수량 입력 : "))

if no == 1:
    item = '노트북'
    price = notebook
elif no == 2:
    item = '디지털 카메라'
    price = camera
sum_price = price * num

if sum_price >= 1000000 :
    discount = (sum_price * 10) / 100
elif sum_price >= 500000 :
    discount = (sum_price * 5) / 100
else :
    discount = 0

print("********주문 내용********\n"
      "상품명 : %s\n" 
      "가격 : %s 원\n" 
      "주문 수량 : %d 원\n"
      "주문액 : %s 원\n"
      "할인액 : %s 원\n"
      "총지불액 : %s 원\n"
      "***********************" \
      % (item, format(int(price),','),num, format(int(sum_price),','), format(int(discount),','), format(int(sum_price-discount),',')))




