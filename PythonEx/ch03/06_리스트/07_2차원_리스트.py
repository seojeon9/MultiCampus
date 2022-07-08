# 2차원 테이블 형태의 리스트
table = [[1,2,3,4,5],
         [6,7,8,9,10],
         [11,12,13,14,15]]

print(table)

print("-------------------------------")

# 1행씩 출력
for row in table :
    print(row)

# 2차원 테이블의 행과 열
rows = len(table)   # 행의 수
cols = len(table[0])    # 열의 수

print("")
print("%d 행 %d 열" % (rows,cols))

for r in range(rows) :
    for c in range(cols) :
        print(table[r][c], end='\t')
    print()