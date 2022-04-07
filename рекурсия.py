# Пример рекурсивного алгоритма..
# Функция вызывает сама себя,приближаясь к базомоу случаю.
# При наступлении базового случая(пива совсем нет), выполнение прерывается
#
import time

def bottles(bot):
    if bot < 1:
        print('Нет больше пива,совсем нет')
        return

    print('''{} бутылок стоят на столе, {} бутылок..Возьми одну,пусти по кругу!
            {} бутылок пива стоят на столе'''.format(bot, bot, bot - 1))
    bot -= 1
    time.sleep(1)
    bottles(bot)
bottles(10)
