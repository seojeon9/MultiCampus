# 파일에 쓰기
# 쓰기모드(w)로 열고 파일 객체의 write()함수로 출력값을 파일에 기록
# f,write(데이터)
# open() - write() - close()

# data = "hi" # 영문은 엔코딩 문제가 없음
data = '안녕하세요'
# f = open("file2.txt","w") # 파일 열기, 한글 encoding 지정해주지 않으면 글자가 깨질 수 있다. (ANSI -> UTF-8)
# encoding='utf-8' 파일처리 중 한글 관련 encoding방식 설치
f = open('file2.txt','w',encoding='utf-8')
f.write(data) # 파일에 data 쓰기
f.close()