# Создайте модульCubed, содержащий функцию, которая
# в качестве параметра принимает число, возводит 
# его в куб и возвращает его. Импортируйте и вызовите 
# его из другого модуля.

def cubed(x):
    return(x ** 3)
# Если выполняется из программы,то будет диалог,
# а если модуль импортируется, то нет. НЕ забывать
if __name__ == '__main__':
    var = int(input('Введите целое число:'))
    print('Вы ввели:', var, '.Куб вашего числа:',cubed(var))