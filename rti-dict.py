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
        my_list = []        
        r = 0
        if s == '':
            break

        for i in range(0, len(s)):
            if s[i] in my_dict:

                if s[i] == 'I' and (i + 1) < len(s) and s[i + 1] == 'V':
                    my_list.append(i)
                    my_list.append(i + 1)
                    r += my_dict['IV']

                elif s[i] == 'I' and (i + 1) < len(s) and s[i + 1] == 'X':
                    my_list.append(i)
                    my_list.append(i + 1)
                    r += my_dict['IX']      
                    
                elif s[i] == 'X' and (i + 1) < len(s) and s[i + 1] == 'L':
                    my_list.append(i)
                    my_list.append(i + 1)
                    r += my_dict['XL']
                    
                elif s[i] == 'X' and (i + 1) < len(s) and s[i + 1] == 'C':
                    my_list.append(i)
                    my_list.append(i + 1)
                    r += my_dict['XC']
                    
                elif s[i] == 'C' and (i + 1) < len(s) and s[i + 1] == 'D':
                    my_list.append(i)
                    my_list.append(i + 1)
                    r += my_dict['CD']

                elif s[i] == 'C' and (i + 1) < len(s) and s[i + 1] == 'M':
                    my_list.append(i)
                    my_list.append(i + 1)
                    r += my_dict['CM']

        for i in range(0, len(s)):
            if i in my_list:
                continue

            if s[i] == 'I': 
                r += 1   
            elif s[i] == 'V': 
                r += 5
            elif s[i] == 'X':
                r += 10
            elif s[i] == 'L':
                r += 50
            elif s[i] == 'C':
                r += 100
            elif s[i] == 'D': 
                r += 500
            elif s[i] == 'M': 
                r += 1000
                
        print('Вхождения исключений:', my_list)
        print(r)
rti(s)

    
