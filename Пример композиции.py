# Пример композиции. Классы человек и собака.
# собака имеет хозяина. Объект класса человек
# хранится в переменной класса собака
class Dog():
    def __init__(self, name, breed, owner):
        self. name = name
        self.breed = breed
        self.owner = owner
class Person():
    def __init__(self, name):
        self.name = name
mick = Person('Mick Jagger')
sten = Dog('Stenly','Buldog',mick)
print(sten.name, sten.breed, sten.owner.name)

    
# Интересно,правда? создали человека переменной mick
# создали собаку переменной sten.
# sten.owner.name даст нам Mick Jagger
