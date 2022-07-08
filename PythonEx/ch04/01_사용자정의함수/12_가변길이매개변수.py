# 가변길이 매개 변수 : 1개의 매개변수로 개수가 정해지지 않은
# 여러개의 값을 전달 받을 때 사용
# 형태 : *매개변수 / ** 매개변수

def show_players(*players) :    # 튜플형태로 전달
    print(players)

def show_keywords(**kwords) :
    print(kwords)

# 호출 테스트
show_players('기성용', '박지성','이청용')
show_players()
show_players('둘리')

show_keywords(id='sum',name='kim',phone='010-1234-5678')    # key='value'
