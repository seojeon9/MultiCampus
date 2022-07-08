# 주어진 문자열에서 키에 대응하는 숫자값만 추출해서 총 합계를 구하는 프로그램
str_data = "{a1:20},{a2:30},{a3:15},\
        {a4:50},{a5:-14},{a6:15},\
        {a7:20},{a8:70},{a9:-100}"

total = 0 # 합계를 위한 누적변수

# 쉼표(,)로 구분하여 각 아템으로 분리
str_data_split = str_data.split(',')
print(str_data_split)

print(str_data_split[0])
print(str_data_split[0].split(':')) # ['{a1', '20}']
print(str_data_split[0].split(':')[1].split('}'))   # ['20', '']
print(str_data_split[0].split(':')[1].split('}')[0])    # 20 (str)
print(int(str_data_split[0].split(':')[1].split('}')[0]))   # 20 (int)

# 숫자만 추출해서 총 합계 구하기
for i in range(0, len(str_data_split)):
    str_temp = str_data_split[i].split(':')[1].split('}')[0]    # 문자열
    total += int(str_temp)

print(total)