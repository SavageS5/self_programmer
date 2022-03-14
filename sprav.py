# Напишите программу,которая задает вопрос пользователю,
# и сохраняет ответ в файл
import csv
count = 'not space'
with open('sprav.csv', 'w') as rec:
    w = csv.writer(rec, delimiter = ',')
    w.writerow(['Имя', 'Фамилия', 'Страна', 'Модель'])
    while count != '':
        fname = input('Введите ваше имя:')
        if fname == '':
            count == ''
            break
        lname = input('Ваша фамилия:')
        country = input('Ваша страна:')
        phmod = input('Ваша модель телефона:')
        
        w.writerow([fname, lname, country, phmod])
        
        if count == '':
            break
    
    
               
               
               
        
