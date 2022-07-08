# 학생들의 수학점수를 입력받아 총점과 평균을 구하고 80점 이상인 학생의 수도 확인해서 출력할 것
# 입력받은 학생들의 점수를 높은 점수부터 출력되게 정렬할 것
# 학생 수는 사용자에게 입력받아서 사용자가 입력한 학생 수 만큼의 점수를 입력받을 것

# 학생들으 점수를 입력받아 저장할 빈 리스트 생성
scores = []
# 총점을 계산하기 위한 변수
sum_s = 0
# 80점 이상인 학생의 수를 count하기 위한 변수
count = 0

# 몇명의 점수 입력할 것인지 학생 수 입력받기
num_s = int(input("학생 수 입력 : "))

# 점수입력 받아 리스트에 저장
for i in range(num_s) :
    score = int(input("학생"+str(i+1)+" 점수 입력 : "))
    scores.append(score) # 학생 한명 점수 리스트에 추가
print(scores)

# 입력된 점수의 총점, 평균, 80점 이상 학생 수 구하기
# 평균은 총점 구하고 학생수로 나누어줌( 학생 수는 num_s에 저장, scores 리스트의 길이)
# 총점과 80점 이상 학생수는 리스트를 순회하면서 원소 하나씩 더하고 판단

# + 입력/ 출력/ 처리는 보통 따로 모듈로 나눠서 프로그래밍을 하는것이 원칙임
# 리스트내 점수 합계와 80점 이상인 학생 수 계산
for s in scores :
    sum_s += s
    if s>= 80 :
        count += 1

# 평균 계산
avg = sum_s / len(scores)

print("총점 : %d" % sum_s)
print("평균 : %.2f" % avg)
print("80점 이상 학생 : %d명" % count)

scores.sort(reverse=True)
print("점수 내림 차순 정렬 : ", scores)
