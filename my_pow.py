# как самому написать math.pow() ?
# math.pow() функция возведения
# одного числа в степень другого
def my_pow(x, y):
    return(x ** y)

if __name__ == '__main__':
    x = int(input('Введите число:'))
    y = int(input('Введите степень:'))
    print(x, 'в степени:', y , 'равно', my_pow(x,y))
