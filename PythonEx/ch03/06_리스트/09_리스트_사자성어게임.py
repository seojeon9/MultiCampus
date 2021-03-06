# 사자성어 게임
import random

# 문제와 답의 각각 리스트 생성 - 문제의 인덱스와 답의 인덱스를 동일하게 생성
words = ["개과천선", "구사일생", "군계일학", "무용지물", "동고동락",
         "유비무환", "입신양명", "괄목상대", "막역지우", "고장난명"]

Q = ["잘못을 고치고 옳은 길에 들어섬",
     "죽일 고비를 여러 번 겪으며 살아나다",
     "평범한 사람 가운데 뛰어난 사람",
     "아무짝에나 쓸모 없는 것",
     "고통과 즐거움을 함께 한다",
     "미리 준비해두면 근심 걱정이 없다",
     "사회적으로 인정받고 출세하여 이름을 세상에 드날림",
     "다른 사람의 학식이나 업적이 크게 진보한 것을 말함",
     "생사를 같이 할 수 있는 친밀한 벗",
     "상대 없이 혼자서는 어떤 일을 이룰 수 없다"]

print("사자성어 맞추기 게임을 시작합니다.")
print('--------------------------------------')

# 문제를 랜덤하게 생성하기 위해 random 패키지 사용
# 문제 리스트(Q)의 문제 중 랜덤하게 문제를 출제하기 위해 범위 (0~9)의 랜덤 숫자 발생
# 문제 인덱스 생성
i = random.randrange(len(Q))    # 0~9까지 범위 만들고 범위안에서 난수 발생

# 문제 출제 : 맞출때 까지 무한 반복
while True :
    print(Q[i]) # 문제 출제
    answer = input("위 내용에 맞는 사자성어를 쓰시오. ")

    # answer에 입력된 사자성어가 정답인지 확인 : 정답은 words 리스트 안에 있음
    if answer == words[i] : # 정답
        print()
        print("맞습니다. 게임을 종료합니다. ")
        break
    else :
        print()
        print("틀렸습니다. 다시도전!!!")
        print()










