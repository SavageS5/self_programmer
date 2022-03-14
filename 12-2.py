# Создайте класс Circle с методом area, подсчитывающим
# и возвращающим площадь круга. Затем создайте объект 
# Circle, вызовите в нем метод area и выведите результат
# Воспользуйтесь функцией pi из встроенного в Python
# модуля math
#
#
import math

class Circle():
    def __init__(self, r):
        self.radius = r
    def area(self):
        return math.pi * self.radius ** 2
# Создаем объект класса Circle и радиусом 3
a = Circle(3)
print('Площадь круга равна:', a.area())
