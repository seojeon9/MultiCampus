# 정수 2개를 입력 받아서 두 수 사이의 합을 구하는 프로그램을 작성(for문 사용)

# 두 수 입력 받기
print("숫자 1은 숫자 2보다 작아야 합니다.")
su1 = int(input("숫자 1 입력 : "))
su2 = int(input("숫자 2 입력 : "))

# 누적변수 초기화
sumx = 0

# 반복 실행
for x in range(su1, su2 + 1) :
    sumx += x

print("%d 부터 %d 까지의 합 : %d" % (su1, su2, sumx) )