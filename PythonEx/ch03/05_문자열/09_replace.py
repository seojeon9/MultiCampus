# 전체 문자열에서 특정 문자열을 찾아 다른 문자열로 변경
# 전체문자열.replace(찾는 문자열, 변경할 문자열)
# 찾는 문자열이 존재하면 변경된 문자열 반환
# 찾는 문자열이 존재하지 않는 경우 변경된 내용이 없기 때문에 원래 문자열 반환

course = "Java Programming"

# Java 찾아서 Python으로 변경
print(course.replace("Java", "Python")) # 변경되어도 원본에 반영되지 않는다.
print(course)
course = course.replace("Java", "Python")   # 저장하면 변경된 문자열로 변수값이 다시 대입
print(course)
