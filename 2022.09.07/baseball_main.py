'''
숫자야구 게임 만들어보기
사용자의 입력을 받아 숫자야구 게임을 만들어주세요
- 프로그램이 시작되면 슷자야구 게임을 몇 자리 숫자로 할 건지 입력 받아 주세요
    - 3을 입력할 경우 해당 숫자야구 게임은 3자릿수로 진행, 최대 10자리
- 첫 번째 입력을 받은 자릿수 만큼 후 파이썬으로 중복 없는 랜덤한 수를 생성해 주세요
- 사용자가 숫자를 입력 했을 때 숫자야구 게임의 규칙에 맞게 ball / out count를 출력해 주세요
- 사용자가 정답을 맞춘 경우 아래 항목들을 출력해 주세요
    - 사용자가 정답을 맞추기까지 입력 한 횟수
    - 사용자가 게임을 시작해서 정답을 맞추기까지 소요된 시간
    - 정답을 맞춘 시점의 날짜/시간
- 게임을 진행하던 도중, “exit”을 입력할 경우 프로그램을 종료해 주세요
'''

from distutils.log import error
from sub import get_ball_count
from datetime import datetime
import time

player = input('플레이의 님의 닉네임을 입력해주세요. : ')
count = int(input('1 ~ 9 사이의 숫자를 입력해주세요. : '))
start_time = time.time()
input_number = 0
balls_count = get_ball_count(count)
# print(balls_count)

try:
    while True:
        strike_count = 0
        ball_count = 0
        my_count = list(map(int ,input('숫자 하나당 스페이스바 한번 추가해서 입력해주세요. : ').split()))
        input_number += 1
        if balls_count == my_count:
            now = datetime.now()
            string_datetime = datetime.strftime(now, '%y/%m/%d %H:%M:%S')
            end_time = time.time()
            print('!!! Congratulation !!!')
            print(f'{player}님은 총 {input_number}번 만에 성공 했습니다!')
            print(f'게임 실행 시간 : {end_time-start_time:.2f}초')
            print(f'현재 시간 : {string_datetime}')
            print('!!! Congratulation !!!')
            break
        
        else:
            for i in range(len(balls_count)):
                for j in range(len(balls_count)):
                    if balls_count[i] == my_count[j] and i == j:
                        strike_count += 1
                    elif balls_count[i] == my_count[j] and i != j:
                        ball_count += 1
        print(f'{strike_count} 스트라이크, {ball_count} 볼 입니다.')

except:
    print('게임을 종료하겠습니다.')
    error