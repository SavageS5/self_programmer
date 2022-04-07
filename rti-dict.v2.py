# rti - функция для преобразования римских цифр в арабские.
#
#
#
#

s = '' # переменная принимает римские цифры

# Сюда надо подумать написать еще одну функцию,чтоб не переписывать
# 6 раз обработку исключений..
#def eh(one, two, i):
#    if s[i] == 'I' and (i + 1) < len(s) and s[i + 1] == 'V':
#                    my_list.append(i)
#                    my_list.append(i + 1)
#                    r += my_dict['IV']

def rti(s):
    
    my_dict = { 'I' : 1,            # словарь римских цифр
                'V' : 5,
                'X' : 10,
                'L' : 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000,
                'IV' : 4,
                'IX' : 9,
                'XL' : 40,
                'XC' : 90,
                'CD' : 400,
                'CM' : 900
               }

    while True:
        print('Введите число или Enter для выхода:')
        s = input()
        my_list = []    # список адресов исключений (IV, IX, XL, XC, CD, CM)
        my_sbor = []    # список для словаря,по нему словарь считает результат
        r = 0           # результат
        if s == '':
            break

        for i in range(0, len(s)): 
            if s[i] in my_dict:

                if s[i] == 'I' and (i + 1) < len(s) and s[i + 1] == 'V': # обработка исключения 4
                    my_list.append(i)
                    my_list.append(i + 1)
                    my_sbor.append('IV')
                    
                elif s[i] == 'I' and (i + 1) < len(s) and s[i + 1] == 'X':
                    my_list.append(i)
                    my_list.append(i + 1)
                    my_sbor.append('IX')
                                        
                elif s[i] == 'X' and (i + 1) < len(s) and s[i + 1] == 'L':
                    my_list.append(i)
                    my_list.append(i + 1)
                    my_sbor.append('XL')
                    
                elif s[i] == 'X' and (i + 1) < len(s) and s[i + 1] == 'C':
                    my_list.append(i)
                    my_list.append(i + 1)
                    my_sbor.append('XC')
                    
                elif s[i] == 'C' and (i + 1) < len(s) and s[i + 1] == 'D':
                    my_list.append(i)
                    my_list.append(i + 1)
                    my_sbor.append('CD')

                elif s[i] == 'C' and (i + 1) < len(s) and s[i + 1] == 'M':
                    my_list.append(i)
                    my_list.append(i + 1)
                    my_sbor.append('CM')
    
                elif s[i] == 'I' and i not in my_list: # Обработка одноразрядных цифр, и проверка, 
                    my_sbor.append('I')                 # что они не начало или конец исключений,
                                                          # чтоб не считать их дважды
                elif s[i] == 'V' and i not in my_list:
                    my_sbor.append('V')
    
                elif s[i] == 'X' and i not in my_list:
                    my_sbor.append('X')
    
                elif s[i] == 'L' and i not in my_list:
                    my_sbor.append('L')
    
                elif s[i] == 'C' and i not in my_list:
                    my_sbor.append('C')
    
                elif s[i] == 'D' and i not in my_list:
                    my_sbor.append('D')
    
                elif s[i] == 'M' and i not in my_list:
                    my_sbor.append('M')
 
            else:           # если накосячили и ввели не цифры из словаря
                print('Ошибка ввода!')
                break

        for i in my_sbor:   # собственно,расчет. Берем сборный список, скармливаем его словарю
            if i in my_dict:
                r += my_dict[i]
                
        print('Вхождения исключений:', my_list)
        print('Полученный список:', my_sbor)
        print(r)
rti(s)

    
