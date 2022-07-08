# read() 함수 : 내용 전체를 읽어서 1개의 문자열로 반환
f = open("test2.txt", 'r', encoding='utf-8')
data = f.read()
print(data)
print(type(data))

for ch in data : # 한문자씩 출력
    print(ch)

f.close()