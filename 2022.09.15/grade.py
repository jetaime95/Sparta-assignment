'''
사용자의 시험 점수를 입력받아 등급을 출력하는 코드를 만들어주세요
- 등급표
    - 91~100 : A
    - 81~90 : B
    - 71~80 : C
    - ~71 : F
'''

def get_grade(score):
    if score > 90:
        return 'A'
    elif score > 80:
        return 'B'
    elif score > 70:
        return 'C'
    elif score < 70:
        return 'F'

score = int(input())
grade = get_grade(score)
print(grade)