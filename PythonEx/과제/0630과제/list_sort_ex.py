#  append() 연습문제2 (list_append_ex2.py) 복사해서
#  점수를 내림차순 정렬하여 출력

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

print("총점 : ", sum)
print("평균 : %.2f" % (sum/num))
print("80점 이상 학생 : ", good_stu,"명")

list.sort(reverse=True)
print("점수 내림차순 정렬 : ", list)