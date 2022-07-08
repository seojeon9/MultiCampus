#  숫자 10개를 입력 받아서 양, 음, 0의 개수 출력

pos_num = 0     #양수
neg_num = 0     #음수
zero_num = 0    #0

for i in range(1,11) :
    num = int(input("숫자%d입력 : " % i))
    if num > 0 :
        pos_num += 1
    elif num < 0 :
        neg_num += 1
    else :
        zero_num += 1

print("---------------------")
print("양의 개수 : %d" % pos_num)
print("음의 개수 : %d" % neg_num)
print("0의 개수 : %d" % zero_num)