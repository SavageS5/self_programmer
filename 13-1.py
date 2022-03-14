# Создайте классы Rectangle и Square с методом
# calculate_perimeter, вычисляющим периметр фигур,
# которые эти классы представляют.
# Создайте объекты Rectangle и Square и вызовите
# в них этот метод
class Shape():                                  # Класс Shape() из третьего задания,он получился
    def __init__(self, w, l):                   # самый родительский. Его наследник- Rectangle(),
        self.width = w                          # а наследник Rectangle()- Square()
        self.len = l                            # Чтоб и у Rectangle() и у Square() был доступен
                                                # родительский метод what_am_i
    def what_am_i(self):
        return 'Я - фигура!'
    
class Rectangle(Shape):
    def calculate_perimeter(self):              # определение метода ВНУТРИ класса. Если def воткнуть
        return 2 * self.width + 2 * self.len    # на первую позицию в строке,то будет уже ГЛОБАЛЬНЫЙ


# Квадраты- дочерний класс прямоугольников
class Square(Rectangle):
# Класс дочерний,поэтому конструктор не пишется,удобно!
# А это-переназначение метода(считаем уже по другой формуле)
    def calculate_perimeter(self):
        return 4 * self.len
    def change_size(self, var):
        self.variable = var
        self.width = self.width +self.variable
        self.len = self.width
        return self.len

r1 = Rectangle(5, 3)
r2 = Rectangle(8, 2)
s1 = Square(5, 5)
s2 = Square(10, 10)
x1 = Shape(8, 7)
x2 = Shape(9, 12)

print('Прямоугольник 1 {} на {}' .format(r1.width, r1.len))
print('Прямоугольник 2 {} на {}' .format(r2.width, r2.len))
print('Периметр Прямоугольника 1 ',r1.calculate_perimeter())
print('Периметр Прямоугольника 2 ',r2.calculate_perimeter())
print('Квадрат 1 {} на {}'.format(s1.width, s1.len))
print('Квадрат 2 {} на {}'.format(s2.width, s2.len)) 
print('Периметр квадрата 1', s1.calculate_perimeter())
print('Периметр квадрата 2', s2.calculate_perimeter())
print('Квадрат 1 изменен', s1.change_size(5))
print('Квадрат 2 изменен', s2.change_size(-3))
print('Прямоугольник 1 из класса Rectangle() говорит:', r1.what_am_i())
print('Квадрат 2 из класса Square() говорит:', s2.what_am_i())
print('Прямоугольник 2 из класса Shape() говорит:', x2.what_am_i())
