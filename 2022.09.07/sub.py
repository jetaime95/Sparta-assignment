import random

def get_ball_count(count): # 랜덤 번호 생성 함수
    result = []
    if count < 1: 
        print('1 이상의 값을 입력하시오.')
    else:
        ball_count = set() # 중복을 없애기 위해 set 지정
          
        while len(ball_count) < count: 
            ball_count.add(random.randint(1, 9))
        result = list(ball_count) #비교를 수월하기 위해, random.shuffle을 사용하기 위해 list로 변환
        random.shuffle(result) # 랜덤번호 출력시 작은 수 부터 순서대로 쌓여 무작위로 배열의 순서 섞기 위해 사용
    return result

