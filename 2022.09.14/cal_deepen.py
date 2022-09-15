'''
- 클래스를 활용해 작성했던 계산기 코드를 활용해주세요
- 기존처럼 사용자의 입력을 받고 출력하되, try / except를 활용해 사용자의 입력을 검증하는 코드를 추가해주세요
    - 두 번쨰 숫자에 0을 입력하고 나누기를 시도할 경우 “0으로 나눌 수 없습니다” 문구를 출력해주세요
    - 숫자가 아닌 다른 값을 입력했을 경우 “숫자만 입력 가능합니다” 라는 문구를 출력해 주세요
'''
class Calc:
    def set_number(self, a, b):
        self.a = a
        self.b = b      
          
    def plus(self):
        result = self.a + self.b
        return result
    
    def minus(self):
        result = self.a - self.b
        return result
    
    def multiple(self):
        result = self.a * self.b
        return result
    
    def divide(self):
        try:
            result = self.a / self.b
            return result
        except ZeroDivisionError: # 0으로 나누면서 에러가 발생했을 때
            print("0으로는 나눌수 없습니다.")
    
while True:
    try:
        a, b = map(int,input('숫자를 입력해주세요 : ').split())
        break
    except ValueError:
        print("숫자만 입력 가능합니다.")
    
calc = Calc()
calc.set_number(a, b)
print(calc.plus()) # 더한 값
print(calc.minus()) # 뺀 값
print(calc.multiple()) # 곱한 값
print(calc.divide()) # 나눈 값