# Создайте словарь, связывающий ваших любимых музыкантов
# со списком ваших любимых песен, написвнных ими
#
music = {}
groupname = 'Name'

while groupname != '':
    treklist = []
    trekname = 'La-La-La!'
    groupname = input('Введите название группы:')
    if groupname == '':
        break
    
    while trekname != '':
        trekname = input('Введите название песни:')
        treklist.append(trekname)
        if trekname == '':
            treklist.pop()
            break
        
    music[groupname] = treklist 
print(music)
