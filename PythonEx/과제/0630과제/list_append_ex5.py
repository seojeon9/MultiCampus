#  상품을 리스트에 추가 ‘’ “”
#  엔터키 누르면 입력 종료되고 등록된 상품 리스트 출력

products = []

while True :
    product = input("상품 등록(엔터키 누르면 종료) : ")
    if product == "" :
        break
    products.append(product)

print("등록된 상품 : ",end="\t")
for pt in products :
    print(pt ,end="\t")