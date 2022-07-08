# readlines() 함수를 이용해서 전체라인읽기

print("--------- 전체라인 읽고 출력 -----------")

f1 = open("test.txt", "r")
lines = f1.readline() # 전체 행을 읽어서 list로 반환
print(lines) # 1행이 한개의 리스트 요소 행 끝네 \n이 포함되어 있음(입력시 엔터키를 입력했기 때문)

f1.close()

print("--------- 전체라인 읽고 한행씩 출력 -----------")

f2 = open("test.txt", "r")
lines = f2.readline()

for line in lines: # 리스트 각 요소 출력(한행씩)
    print(line, end='')

f2.close()

print("\n--------- 전체라인 읽고 한행씩 출력 -----------")
f3 = open("test.txt", "r")

# for 반복문의 반복요소로 파일 객체 사용가능
for line in f3 : # f3.readlne() 함수가 자동 수행되면서
    print(line,end='') # 1행씩 읽어옴

f3.close()
