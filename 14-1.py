# Добавьте переменную square_list в класс Square
# так,чтобы всякий раз, когда вы создаете 
# новый объект Square, он добавлялся в список
#
# Измените класс Square так,чтобы при выводе объекта 
# Square выводилось сообщение с длинами всех четырех
# сторон фигуры. например,при создании квадрата вызовом
# Square(29), Питон должен вывести строку 29 на 29 на 29 на 29
#
# Напишите функцию, которая принимает два объекта в качестве
# параметров и возвращает True,если они являются одним и тем же
# объектом, и False в противном случае

class Square():
    square_list = []
    def __init__(self, side):
        self.side = side
        self.square_list.append(self.side)
        print('Создан квадрат {} на {} на {} на {}'.format(self.side,
                                                           self.side,
                                                           self.side,
                                                           self.side))
    def istf(address_one, address_two):
        if address_one == address_two:
            return True
        else:
            return False
        
s1 = Square(7)
s2 = Square(9)
s3 = Square(81)
s4 = Square(25)
s5 = Square(10)
some_s1 = s1
    
print('\nСоздавались объекты Square со сторонами:', Square.square_list)
print('\nАдрес s1     ', s1)
print('Адрес some_s1', some_s1)
print('Адрес s3     ', s3)
print('\nСравнение s1 и some_s1:', Square.istf(some_s1, s1))
print('Сравнение s1 и s3:     ', Square.istf(s1, s3))
        
