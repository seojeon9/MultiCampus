# 예외 처리 방법
# try ... except 문 사용
# try :
#     예외발생가능한 문장 1
# except 예외유형 :
#     예외처리 문장 2
# else :
#     예외 없을때 수행 문장 3
# finally:
#     예외 유무와 상관없이 실행되는 문장 4

# else ~ finally 생략가능
# 1번문장을 실행 - 오류발생(예외처리 되어 있는 오류면) 2번문장 수행 - 4번문장을 수행
# 1번문장을 실행 - 오류없으면 3번문장 수행 - 4번문장을 수행

# 에러 확인

# ZeroDivisionError: division by zero
# print(10/0)

# TypeError: can only concatenate str (not "int") to str
# print("나이 : " + 23 + "살")

# NameError: name 'b' is not defined
# print(b)

# ValueError: incomplete format
# c=100
# print("%d%" % c) # 퍼센트 : %%

# SyntaxError: expected ':'
# x = 100
# if x > 10
#     print('홍길동')

# IndexError: list index out of range
# a = [1,2,3,4]
# print(a[4])

#UnboundLocalError: local variable 'a' referenced before assignment
# def add() :
#     a = a+1
# add()

# ModuleNotFoundError: No module named 'mymodule'
# import mymodule

# FileNotFoundError: [Errno 2] No such file or directory: 'exception.txt'
# f=open("exception.txt",'r')
# data = f.read()
# print(data)

# OSError: [Errno 22] Invalid argument: 'c:\x0cile\\exception.txt'
f = open("c:\file\exception.txt",'w')
# 경로 지정시 \\ 쓰거나 / 를 사용
# PermissionError: [Errno 13] Permission denied: 'd:\x0cile\\exception.txt'