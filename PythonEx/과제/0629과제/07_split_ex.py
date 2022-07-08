#  그림과 같이 입력 받고 split()을 사용하여 분리

birth = input("생일 입력 (연/원/일) : ")
birth_split = birth.split('/')

print("당신은 " + birth_split[0] + "에 태어났고\n"
    "생일은 " + birth_split[1] + "월 " + birth_split[2] + "일 이군요")