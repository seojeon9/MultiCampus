#  다중 for 문을 사용하여 다음과 같이 출력

for i in range(1,10,4) :
    num = i
    for j in range(4) :
        print(num, end='\t')
        num += 1
    print("")

