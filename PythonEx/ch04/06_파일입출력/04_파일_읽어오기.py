# readline() 함수를 이용해서 1개 라인 읽어오기
print("---------- 첫번째 행 읽기 ------------")

f1= open('test.txt', 'r') # 읽기모드 - txt 파일이기 때문에 파이썬 내부에서 한글처리 진행
# 읽어온 데이터으 한글이 깨지면
# f1= open('test.txt', 'r',encoding='utf-8')
line = f1.readline() # 첫번째 라인 읽기
print(line)
f1.close()

# readline() 이용해서 전체 라인 읽어오기
# 1행씩 읽고 출력
print("=========== 파일 전체 읽기 ============")
f2 = open('test.txt', 'r')

# 해당 파일의 총 라인수를 알 수 없으므로
while True :
    line = f2.readline() # 라인 1개 읽고
    if not line : # 라인에 읽은 내용이 없으면
        break # 반복문 종료
    # print(line) # 읽어온 line 출력
    # 출력 결과는 두줄 간격으로 출력 : 원 데이터에서 줄바꿈문자 + print()가 줄바꿈 = 2줄 간격
    print(line, end='') # print()의 줄바꿈은 하지 않음
    
f2.close()