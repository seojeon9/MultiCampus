# 정수 리터럴
a = 0b1010  # 2진수 (Binary)
b = 300
c = 0o123   # 8진수 (Octal)
d = 0x12    # 16진수 (Hexadecimal)

print(a, b, c, d)

# 실수 리터럴(정해진 숫자)
f1 = 3.24
f2 = -123.45
f3 = 1.234567e5
f4 = 1.234567e-5

print(f1, f2, f3, f4)

# 문자열 리터럴
str = '홍길동'
str2 = "py" \
        "thon"
str3 = '''파이썬'''
str4 = """프로그래밍"""
str5 = """여러줄로
나누어서
입력해도 됨
출력도 여러줄에 나타남"""

print(str5)
print(str2)

# 논리값 리터럴
t = True
f = False

print(t,f)

# 특수 리터럴
name = "홍길동"
phone = ''
print(name)
print(phone)
address = None
print(name)
print(phone, type(phone))   #<class 'str'>
print(address, type(address))   #None <class 'NoneType'>