# задача про папин сейф из журнала The Code

import datetime
import numpy as np
matnp = np.array([0, 15, 0, 5,
                 17, 0, 11, 0,
                 0, 0, 0, 0,
                 14, 9, 0, 0]).reshape(4, 4)

# перебор грубой силой..
# напомню правила..вместо нулей нужно подставить числа от 6 до 20 
# числа не повторяются
# сумма любой строки, столбца, дивгоналей равна 50

# Нужно добавить мягкости..грубой силой перебирал целую ночь, 
# и не нашел решений..
#

# переписываем нули
c1 = matnp[0][0]
c2 = matnp[0][2]
c3 = matnp[1][1]
c4 = matnp[1][3]
c5 = matnp[2][0]
c6 = matnp[2][1]
c7 = matnp[2][2]
c8 = matnp[2][3]
c9 = matnp[3][2]
c10 = matnp[3][3]

# диапазон чисел, которые будем перебирать
ln = list(range(6, 21))

# из этого диапазона убираем те числа,что уже известны в матрице(уникальность!)
for i in matnp:
    for j in i:
        if j in ln:
            ln.remove(j)

diag_flag = True        # если каждая диагональ дает в сумме 50
lines_flag = True       # если каждая строка и колонка дает в сумме 50
r_flag = False          # результат найден!(пока нет)
bt = datetime.datetime.now() # время вхождения в первый for
for c1 in ln:                   
    if r_flag:              # если результат найден, выход из цикла
        break
    
    for c2 in ln:
        if r_flag:
            break
        s0 = sum(matnp[0]) + c1 + c2 # подбираем с1 и с2 так, чтобы сумма первой строки была равна 50
        if s0 < 50 or c2 == c1:     # если сумма меньше или с1 равно с2, перебираем дальше
            continue
        
        for c3 in ln:
            if r_flag:
                break
            if c3 == c2 or c3 == c1:
                continue
            
            for c4 in ln:
                if r_flag:
                    break
                s1 = sum(matnp[1]) + c3 + c4
                if s1 < 50 or c4 == c3 or c4 == c2 or c4 == c1:
                    continue
                
                for c5 in ln:
                    if r_flag:
                        break
                    if c5 == c4 or c5 == c3 or c5 == c2 or c5 == c1:
                        continue
                
                    for c6 in ln:       # с с6 вообще интересно,видно,что он равен 20 из условия
                        if r_flag:
                            break
                        if c6 == c5 or c6 == c4 or c6 == c3 or c6 == c2 or c6 == c1 or c6 < 20:
                            continue
                        
                        for c7 in ln:
                            if r_flag:
                                break
                            if c7 == c6 or c7 == c5 or c7 == c4 or c7 == c3 or c7 == c2 or c7 == c1:
                                continue
                        
                            for c8 in ln:
                                if r_flag:
                                    break

                                if c8 == c7 or c8 == c6 or c8 == c5 or c8 == c4 or c8 == c3 \
                                   or c8 == c2 or c8 == c1:
                                    continue

                                s2 = c5 + c6 + c7 +c8
                                if s2 < 50:
                                    continue
                                
                                for c9 in ln:
                                    if r_flag:
                                        break
                                    if c9 == c8 or c9 == c7 or c9 == c6 or c9 == c5 or c9 == c4 \
                                       or c9 == c3 or c9 == c2 or c9 == c1:
                                        continue
                                    
                                    for c10 in ln:
                                    
                                        if c10 == c9 or c10 == c8 or c10 == c7 or c10 == c6 \
                                           or c10 == c5 or c10 == c4 or c10 == c3 or c10 == c2 \
                                           or c10 == c1:
                                            continue
                                        diag_flag = True
                                        lines_flag = True
                                        matnp[0][0] = c1
                                        matnp[0][2] = c2
                                        matnp[1][1] = c3
                                        matnp[1][3] = c4
                                        matnp[2][0] = c5
                                        matnp[2][1] = c6
                                        matnp[2][2] = c7
                                        matnp[2][3] = c8
                                        matnp[3][2] = c9
                                        matnp[3][3] = c10
                                        print(sum(matnp[0]), sum(matnp[1]), sum(matnp[2]), \
                                              sum(matnp[3]),'|||', sum(matnp.diagonal()), \
                                              sum(np.flipud(matnp).diagonal()), '|||', \
                                              sum(matnp.T[0]), sum(matnp.T[1]), sum(matnp.T[2]), \
                                              sum(matnp.T[3]), '|||',  c1, c2, c3, c4, c5, c6,c7, \
                                              c8, c9, c10)

                                        # если сумма в каждой из диагоналей не равна 50,
                                        # фальшивим флаг диагоналей
                                        if sum(matnp.diagonal()) != 50 or \
                                           sum(np.flipud(matnp).diagonal()) != 50:
                                            diag_flag = False
                                            continue
                                                       
                                        # проверяем суммы строк и столбцов, если они не равны 50,
                                        # фальшивим флаг строк
                                        for j in range(4):
                                            if sum(matnp[j]) != 50 or sum(matnp.T[j]) != 50:
                                                lines_flag = False
                                                break
                                            
                                        # если флаг остался True, значит, мы нашли результат!
                                        # флаг результата на True
                                        if lines_flag == True:
                                            r_flag = True                                              
                                            break
                                        continue
                                                                                
if diag_flag and lines_flag: # если диагонали и строки и столбцы дают сумму 50 каждый
                            # уникальность проверили в циклах выше
                                        
    print('\nВот она!:')
    print(matnp)
    print('Время вхождения в первый for:', bt)
    print('Время окончания расчета:', datetime.datetime.now())
    print('Время расчета:',datetime.datetime.now() - bt)
                        
                                                
    
