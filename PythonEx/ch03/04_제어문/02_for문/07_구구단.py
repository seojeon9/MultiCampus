# 구구단 출력

for dan in range(2,10) : # 2~9
    for n in range(1,10) : #1~9
        print("%d * %d = %2s" % (dan, n, str(dan*n)))    # %2s 문자열을 표시할 때 최소 2칸을 사용할 것 -> 오른쪽 정렬
    print()