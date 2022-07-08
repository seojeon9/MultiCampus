# 파일에 여러행 쓰기
# 여러행으로 표시될 \n이 포함된 문자열 하나를 쓴다
# write()는 여러번 사용

f = open('file3.txt', 'w', encoding='utf-8')
# 1.
# for i in range(1,11) :
#     data = '%d행\n' % i
#     f.write(data)

# 2.
data = ''
for i in range(1,11) :
    data = data + '%d행\n' % i
f.write(data)

f.close()