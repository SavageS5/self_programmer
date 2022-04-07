mat = [[0, 15, 0, 5],
     [17, 0, 11, 0],
     [0, 0, 0, 0],
     [14, 9, 0, 0]]

#flag = False
ln = list(range(5, 21))
nln = []
#d0 = [ mat[3][0], mat[2][1], mat[1][2], mat[0][3]]
#d1 = [mat[0][0], mat[1][1], mat[2][2], mat[3][3]]
#r0 = 0
#c0 = 0
#sd0 = 0
#sd1 = 0
for i in mat:
    for j in ln:
        if j not in i:
            nln.append(j)
    ln = nln
    nln = []
print('Свободные числа:', ln)
print('Матрица:')
for i in mat:
    print(i)

#for i in mat:
#    r = 0
#    for j in i:
#        r += j
#    print('Сумма {} строки: {}'.format(i, r))

#for i in d0:
#    sd0 += i
#print('Сумма диагонали 1:', sd0)

#for i in d1:
#    sd1 += i
#print('Сумма диагонали 2:', sd1)

#print('Нулей в диагонали 1:', d0.count(0))
#print('Нулей в диагонали 2:', d1.count(0))
#print('Нулей в строке 1:', mat[0].count(0))
#print('Нулей в строке 2:', mat[1].count(0))
#print('Нулей в строке 3:', mat[2].count(0))
#print('Нулей в строке 4:', mat[3].count(0))
#print(mat[0].count(0))

#for i in d0:

# Проблема с диагональю.Если 0 один,находим, подбираем сумму из свободных чисел,
# меняем 20 в диагонали вместо 0.. а в матрице это значние не менятся. почему?
#cz = d0.count(0)
    
#if cz == 1:
#    for j in ln:
#        if sd0 + j == 50:
#            ln.remove(j)
#            #d0.index(0)
#            d0.insert(d0.index(0), j)
#            d0.remove(0)
#            print('j = ', j)
#            print(ln)
            
#elif cz == 2:
#    for j in ln:
#        #if sd0
#        pass
     


# счет строк
for i in mat:
    summ = 50
    flag = False
    for j in i:
        if flag:
            break
        if j == 0 and i.count(0) > 1:
            for x in range(len(ln)):
                ost = summ -sum(i)
                if ost == 0 or flag:
                    break 
                y = ln[x]
                for z in ln:
                    if z == y:
                        continue
                    if z + y == ost:
                        i.insert(i.index(0), y)
                        i.remove(0)
                        i.insert(i.index(0), z)
                        i.remove(0)
                        ln.remove(y)
                        ln.remove(z)
                        flag = True
                        break

if len(ln) == 4 and sum(ln) == 50:
    print('Свободные:', ln)
    for f in mat[2]:
        mat[2].insert(mat[2].index(0), ln[f])
        mat[2].remove(0)
        ln.remove(ln[f])

print('новая:','\n', mat[0], '\n', mat[1], '\n', mat[2], '\n', mat[3])
print('Свободные:', ln)

# обработка колонок
for a, b, c, d in zip(mat[0], mat[1], mat[2], mat[3]):
    print('Сумма колонок:',a + b + c + d)


