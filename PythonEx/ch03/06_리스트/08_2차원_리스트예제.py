# 학생병 점수 리스트 생성
chulsu = [90,85,70]
younghee = [88,79,92]
young = [100,100,100]
min = [90,60,70]

# 전체 학생 점수 저장
students = [chulsu, younghee, young, min]

# 성적표 출력
print("-- 성적표 (점수, 총점 평균) --")
for scores in students :
    total = 0 #각 학생마다 총점 0으로 초기화

    for s in scores :
        total = total + s # 학생 1명의 총점
    avg = total / len(scores) # 학생 1명의 평균

    print(scores, ",", total, ",", round(avg,1)) # round : 반올림 round(값,표시자리수)