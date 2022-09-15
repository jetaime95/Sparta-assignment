'''
도형 넓이 계산기
- 인스턴스를 선언할 때 가로, 세로 길이를 받을 수 있는 클래스를 선언해 주세요
- 인스턴스에서 사각형, 삼각형, 원의 넓이를 구하는 메소드를 생성해주세요
    - 원의 넓이를 계산할 때는 세로 길이는 무시하고, 가로 길이를 원의 지름이라 가정하고 계산해 주세요
'''

class Area:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def square(self):
        result = self.x * self.y
        return result
    
    def triangle(self):
        result = self.x * self.y / 2
        return result
    
    def circle(self):
        radius = self.x / 2
        result = radius * radius * 3.14
        return result
    
area = Area(10, 20)
print(area.square())
print(area.triangle())
print(area.circle())