#  카운트 다운 프로그램

num = int(input("시작 숫자를 입력하시오: "))

for i in range(num, 0, -1):
    print(i, end=' ')
print("발사")