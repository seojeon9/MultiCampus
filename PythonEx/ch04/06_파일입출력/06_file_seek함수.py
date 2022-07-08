print("------- 파일 내에서 검색 : seek() ---------")

f = open("test2.txt", 'r', encoding='utf-8')

# readlines()로 읽기
f.seek(0,0) # 시작위치 : 0행 0열
# 파일 전체 읽기(readlines())
lines = f.readlines()
print(lines) # 리스트 출력

# ------- 파일 내에서 검색 : seek() ---------
# ['01234\n', 'abcde\n', '가나다라마']

f.seek(1,0) # 시작위치 : 0행 1열에서 시작
lines = f.readlines()
print(lines)    # ['1234\n', 'abcde\n', '가나다라마']

f.seek(7, 0)  # 시작위치 : 0행 7열에서 시작
lines = f.readlines()
print(lines)    # ['abcde\n', '가나다라마']
# 엔터키 : \r\n => 2바이트를 차지함

# 한글은 2바이트 -> 현재는 3바이트?
f.seek(14, 0)  # 시작위치 : 0행 14열에서 시작
lines = f.readlines()
print(lines)
# ['가나다라마']

f.seek(17, 0)  # 시작위치 : 0행 17열에서 시작
lines = f.readlines()
print(lines)

f.close()