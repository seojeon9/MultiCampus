# 함수의 반환값
# 함수 내부의 문장을 수행하고 돌려주는 결과값
# 결과값 반환 시 사용 문장 : return 문 사용
# 반환값은 함수가 호출된 곳으로 반환

# 두 수를 함수내에서 입력받아 더한 결과를 반환하는 함수를 생성 할 것
# def sum_c() :
#     num1 = eval(input("국어점수를 입력하세요"))
#     num2 = eval(input("수학점수를 입력하세요"))
#     total = num1 + num2
#     return total # 반환문

# print(sum_c() #이 자리로 결과값이 반환)
# print(sum_c())
# sum_c() 함수를 활용해서 5명의 학생의 국어 수학 점수를 입력받아 더한 total 점수를 리스트에 저장하시오
# tot_jumsu = []
# for n in range(5) :
#     tot_jumsu.append(sum_c())
#
# print(tot_jumsu)

################################
# 여러개의 값 반환하기
# 파이썬을 제외한 다른 프로그래밍 언너에서는 함수는 항상 하나의 값을 반환해야 함
# 파이썬은 함수가 여러개의 값을 반환 할 수 있음

def multi_return() :
    return 1,2,3

# 여러개의 값이 반환되는 함수를 호출 후 반환값을 변수에 저장
# 여러변수에 저장
a,b,c = multi_return() # 1,2,3
print(a,b,c)

# 변환값을 1개의 변수에 저장
d = multi_return()
print(d) # (1, 2, 3) : tuple

################################
def multi_return1() :
    return 1
    return 2    # 위쪽에서 return돼버려서 아래 return문은 실행되지 않음
    return 3

result = multi_return1()
print(result)   # 1

###########################################333
# 반환값이 없는 함수인 경우에 함수 호출 후 저장 하면
def test() :
    print('test')

res = test()
print(res) # None