# 0부터 9까지 모두 더한 결과를 출력하시오

print(0+1+2+3+4+5+6+7+8+9)

sum = 0
for i in range(10) :
    # print(i)
    sum += i
    print(i, sum)
print(i, sum)


# 누적변수가 초기화되지 않으면 아래 에러가 남
# TypeError: unsupported operand type(s) for +=: 'builtin_function_or_method' and 'int'