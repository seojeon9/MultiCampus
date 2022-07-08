#  80점 이상 학생의 수를 계산하여 출력

list = []

for i in range(5) :
    score = int(input("학생%d 점수 입력 :" % (i+1)))
    list.append(score)

sum = 0
good_stu = 0

for i in range(5) :
    score = list[i]
    sum += score
    if score >= 80 :
        good_stu += 1

print("총점 : ",sum)
print("평균 : %.2f" % (sum/5))
print("80점 이상 학생 : ", good_stu,"명")