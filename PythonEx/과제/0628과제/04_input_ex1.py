#  점수를 입력 받아서 총점과 평균 출력

kor = int(input("국어 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))
math = int(input("수학 점수 입력 : "))

sum = kor + eng + math
avg = sum / 3

print("총점 : %d " % sum)
print("평균 : %0.2f" % avg)
