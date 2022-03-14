#
# функция mean() модуля statistics возвращает примерное
# среднее арифметическое

import statistics
# создаем список квадратов чисел в диапазоне от 0 до 20
my_list = [x ** 2 for x in range(20)]
print(my_list)
# ищем среднее арифметическое
print('Среднее арифметическое:', statistics.mean(my_list))
