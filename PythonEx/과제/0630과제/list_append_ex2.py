#  학생 5명의 점수를 입력 받아서 list에 저장한 후 총점과 평균을 구하여 출력

list = []

for i in range(5) :
    score = int(input("학생%d 점수 입력 :" % (i+1)))
    list.append(score)

sum = 0
for i in range(5) :
    sum += list[i]

print("총점 : ",sum)
print("평균 : %.2f" % (sum/5))
