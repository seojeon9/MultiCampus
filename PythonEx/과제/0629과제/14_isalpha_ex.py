#  그림과 같이 문장을 입력하고
#  알파벳, 숫자, 스페이스, 기타 개수 출력

string = input("문장을 입력하세요 : ")
alpha = 0
digit = 0
space = 0
etc = 0

for i in range(0,len(string)) :
    if string[i].isalpha() :
        alpha += 1
    elif string[i].isdigit() :
        digit += 1
    elif string[i].isspace() :
        space += 1
    else :
        etc += 1

print("알파벳 : %d개" % alpha)
print("숫자 : %d개" % digit)
print("스페이스 : %d개" % space)
print("기타 : %d개" % etc)