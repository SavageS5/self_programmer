# Функция rti - преобразование римских цифр в арабские.
# Для справки: MMXXII - 2022(год) , а  MCMXC в названии
# первого альбома Энигмы - 1990
# Ограничения в задании:
# 1. при вводе римских цифр должны использоваться 
#    следуюшие символы: I, V, X, L, C, D, M
# 2. количество вводимых символов не должно быть больше 15
#
#
#
#
    
my_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
print('Вводите правильно римское число! Маска: MDCLXVI. M-1000, D-500, C-100, L-50, X-10, V-5, I-1.')
def rti(s:str) -> int:
    
    r = 0
    in4 = s.find('IV')
    in9 = s.find('IX')
    in40 = s.find('XL')
    in90 = s.find('XC')
    in400 = s.find('CD')
    in900 = s.find('CM')
    
    if in4 > -1:
        s = s[:in4] + s[in4 + 2:]
        r += 4
        print('in4', in4)
        if len(s) == 0:
            print(r)

    if in9 > -1:
        s = s[:in9] + s[in9 + 2:]
        r += 9
        print('in9', in9)
        if len(s) == 0:
            print(r)
            
    if in40 > -1:
        s = s[:in40] + s[in40 + 2:]
        r += 40
        print('in40', in40)
        if len(s) == 0:
            print(r)
            
    if in90 > -1:
        s = s[:in90] + s[in90 + 2:]
        r += 90
        print('in90', in90)
        if len(s) == 0:
            print(r)

    if in400 > -1:
        s = s[:in400] + s[in400 + 2:]
        r += 400
        print('in400', in400)
        if len(s) == 0:
            print(r)
            
    if in900 > -1:
        s = s[:in900] + s[in900 + 2:]
        r += 900
        print('in900', in900)
        if len(s) == 0:
            print(r)

                  
    for i in range(0, len(s)):
        
        if s[i] == 'M':
            r += 1000
        elif s[i] == 'D':
            r += 500
        elif s[i] == 'C':
            r += 100
        elif s[i] == 'L':
            r += 50
        elif s[i] == 'X':
            r += 10
        elif s[i] == 'V':
            r += 5
        elif s[i] == 'I':
            r += 1
        print(r)
            
            
while True:
    print('Введите число или Enter для выхода:')
    s = input()
    if s == '':
        print('Выходим..')
        break

    if len(s) > 15:
        print('Число, больше 15 знаков. Выходим..')
        break

    for i in range(0, len(s)):
        if s[i] not in my_list:
            print('Ошибка ввода!')
            break
            
        
    rti(s)
