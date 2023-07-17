class area:
    def __init__(self, num1, num2=None):
        self.num1 = num1
        self.num2 = num2 

    def squar(self):
        area = self.num1 * self.num1
        return area

    def triangle(self):
        area = 0.5 * self.num1 * self.num2
        return area

area1 = area(3).squar()
print(area1)