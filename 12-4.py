# Создайте класс Hexagon с методом calculate_perimeter,
# подсчитывающим и возвращающим периметр шестиугольника.
# Затем создайте объект Hexagon,вызовите в нем
# calculate_perimeter и выведите результат
#
# Оказывается, гексаген- правильный шестиугольник..
class Hexagon():
    def __init__(self, a):
        self.side1 = a
    def calculate_perimeter(self):
        return self.side1 * 6
    
hexagon1 = Hexagon(5)
print(hexagon1.calculate_perimeter())
