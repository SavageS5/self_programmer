# Создайте класс Triangle с методом area, подсчитывающим
# и возвращающим площадь треугольника. Затем создайте
# объект triangle, вызовите в нем area и выведите 
# результат
#
class Triangle():
    def __init__(self, b, h):
        self.basic = b
        self.height = h
    def area(self):
        return 0.5 * self.basic * self.height
triangle = Triangle(17, 7)
print('Площадь треугольника равна:', triangle.area())
