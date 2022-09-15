'''
계산기 만들어보기(with class)
- 설정한 숫자를 계산해줄 클래스를 선언해주세요
- 메소드를 호출해서 num1, num2를 설정할 수 있도록 해주세요
- 입력된 숫자의 더하기, 빼기, 곱하기, 나누기 연산 결과를 구하는 메소드를 생성해주세요
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
        result = self.a / self.b
        return result
    
calc = Calc()
calc.set_number(20, 10)
print(calc.plus()) # 더한 값
print(calc.minus()) # 뺀 값
print(calc.multiple()) # 곱한 값
print(calc.divide()) # 나눈 값