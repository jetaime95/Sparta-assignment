'''
- 사용자의 입력을 받아 반복하는 프로그램을 만들어주세요
- 사용자가 숫자를 입력했을 경우 입력값에 2배를 곱한 수를 출력해주세요
- 사용자가 문자를 입력했을 경우 “입력한 문자는 {} 입니다.” 라는 문구를 출력해주세요
    - {} 자리에는 사용자가 입력한 문자가 들어가야 합니다.
- 사용자가 exit을 입력하거나 숫자가 5회 이상 입력됐을 경우 프로그램을 종료시켜주세요
'''

count = 0

while True:
    count += 1
    result = 0
    try:
        number = int(input())
        print(f'입력한 문자는 {number} 입니다.')
        if count <= 5:
            print(f'{number}의 두배는 {number * 2}입니다.')
        elif count >= 5:
            print(f'5회 이상 입력하여 종료합니다.')
            break
    except ValueError:
        print('종료합니다.')
        break