# Создайте словарь, содержащий различные данные о вас:
# рост, любимый цвет, любимый актер и т.д.
#
basa = {}
name = 'Name'
i = 0
while name != '':
    i += 1
    name = input('Введите Ваше имя:')
    if name == '':
        break
    age = input('Введите Ваш возраст:')
    height = input('Ваш рост:')
    color = input('Ваш любимый цвет:')
    auto = input('у Вас есть автомобиль?')
    basa['Имя' + str(i) + ':'] = name
    basa['Возраст' + str(i) + ':'] = age
    basa['Рост' + str(i) +':'] = height
    basa['Цвет' + str(i) + ':'] = color
    basa[' Автомобиль' + str(i) + ':'] = auto
print(basa)
