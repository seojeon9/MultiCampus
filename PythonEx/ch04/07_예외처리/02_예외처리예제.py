# 에러 종류와 상관없이
# 에러가 발생하기만 하면 except 블록 수행
# 어떤 에러가 발생했는지 파악하기 위해서는 에러 메시지를 받아야 함

try :
    # print(10/0) # 오류발생
    print("나이" + 23)
except :
    print('오류발생') # 정상종료

# 최상위 에러인 Exception 적어도 됨
try :
    # print(10/0) # 오류발생
    print("나이" + 23)
except Exception :
    print('오류발생') # 정상종료

# # 에러 종류 명시
# try :
#     # print(10/0) # 오류발생
#     print("나이" + 23)
# except ZeroDivisionError: #0으로 나누는 에러만 예외처리
#     print('오류발생') # 정상종료

# 에러 종류 명시
try :
    print(10/0) # 오류발생하지만 예외처리 구문에서 처리해줌
    print("나이" + 23) # 위에서 에러가 발생해서 예외처리하고 종료 해버리기 때문에 이 문장은 실행되지 않음
except ZeroDivisionError: #0으로 나누는 에러만 예외처리
    print('오류발생') # 정상종료
