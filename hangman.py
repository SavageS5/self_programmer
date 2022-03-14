# Игра "Виселица"

def hangman(word):
    wrong = 0
    stages = ['',
              '_______       ',
              '|      |      ',
              '|      |      ',
              '|      O      ',
              '|     /|\     ',
              '|     / \     ',
              '|             '
              ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('У автора написано - добро пожаловать на казнь..')
    print('У меня будет - добро пожаловать в игру!)')
    
    while wrong < len(stages) - 1:
        print('\n')
        msg = 'Введите букву:'
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((''.join(board)))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('Вы выиграли!Было загадано слово:')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong]))
        print('Вы проиграли! Было загадано:{}.'.format(word))
hangman('собака')
    
