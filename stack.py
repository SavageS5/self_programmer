# Класс Stack. LIFO- последний зашел - первый вышел
# Ассоциация со стопкой тарелок
#
#
# Интересно..если экземпляр класса объявить как, например
# q = Stack,то создвется не экземпляр, а ссылка, чтоли..
# Да, да..q будет показывать <class '__main__.Stack'>,
# но выполнение конструктора не происходит, и при попытке вызвать 
# атрибуты класса налетаем на ошибку..
# q.push(1)
# Traceback (most recent call last):
#   File "<pyshell#40>", line 1, in <module>
#    q.push(1)
# TypeError: Stack.push() missing 1 required positional argument: 'item'
#
# Правильно,ОКАЗЫВАЕТСЯ, создавать надо так: q = Stack()
# Тогда создается экземпляр уже как объект с конкретным адресом
# q = Stack()
# Создан экземпляр класса Stack
# q
# <__main__.Stack object at 0x000002113D902B90>
# и атрибуты начали работать!Однако..
#
class Stack():
    count = 0 # переменная класса
    def __init__(self):
        self.items = []
        Stack.count += 1 # считаем,сколько экземпляров класса было создано
        print('Создан экземпляр класса Stack')
        
# Стек пуст? True, если да
    def is_empty(self):
        return self.items == []

# Поместить элемент в вершину стека
    def push(self, item):
        self.items.append(item)

# Удалить элемент вершины стека и возвращает его
    def pop(self):
        return self.items.pop()

# Возвращает верхний элемент, но не удаляет его
    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

# Возвращает количество элементов в стеке
    def size(self):
        return len(self.items)

#
# Как реверснуть строку - вывести ее задом наперед
# при помощи стека

s = Stack()
rev = ''
for i in 'Позавчера было холодно':
    s.push(i)

for i in range(len(s.items)):
    rev += s.pop()

print('Прямой порядок: Позавчера было холодно')
print('Обратный порядок:', rev)

#
# реверснуть список [1, 2, 3, 4, 5]
#
my_list = []

for i in range(1,6):
    s.push(i)

for i in range(len(s.items)):
    my_list.append(s.pop())
print('\n')
print('Прямой список: [1, 2, 3, 4, 5]')
print('Обратный список:', my_list)
