# Переменные класса и переменные экземпляра класса
class Rectangle():
    recs = []               # переменная класса создана вне модуля __init__
    def __init__(self, w, l):
        self.width = w      # а это уже переменные экземпляра класса,
        self.len = l        # те,что в конструкторе
        self.recs.append((self.width, self.len))

r1 = Rectangle(10, 20)
r2 = Rectangle(30, 40)
r3 = Rectangle(50, 60)
print(Rectangle.recs)       # печатать переменную класса 
