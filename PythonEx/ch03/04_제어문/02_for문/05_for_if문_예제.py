# 아래와 같은 점수가 리스트로 주어졌을 때 해당 점수의 합격/불합격 여부를 판단하시오.
# 60점 이상이면 합격 미만이면 불합격

scores = [90,57,88,45,78]

for score in scores :
    if score >= 60 :
        print(score, "합격")
    else :
        print(score, "불합격")

num = 0
for score in scores :
    num += 1
    if score >= 60 :
        result = '합격'
    else :
        result = '불합격'
    print("%d번 %d점 %s" % (num,score, result))