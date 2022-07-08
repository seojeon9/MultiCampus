#  현재 5명으로 고정된 학생수를 입력 받은 수 만큼 점수 입력하는 것으로 변경

list = []

num = int(input("학생 수 입력 : "))

for i in range(num) :
    score = int(input("학생%d 점수 입력 :" % (i+1)))
    list.append(score)

sum = 0
good_stu = 0

for i in range(num) :
    score = list[i]
    sum += score
    if score >= 80 :
        good_stu += 1

print("총점 : ",sum)
print("평균 : %.2f" % (sum/num))
print("80점 이상 학생 : ", good_stu,"명")