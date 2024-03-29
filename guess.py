from random import *

guessTaken = 0  # переменная хранит значения попыток пользователя
myName = input('Привет! Как тебя зовут?  ')  # знакомимся с пользователем
number = randint(1, 100)
'''
Мы закончили с объявлением переменных.
Теперь мы можем приступить непосредственно к написанию кода программы.
'''
print(f'{myName}, я загадал число от 1 до 100. Твоя задача угадать это число.')

'''
Здесь мы делаем цикл с любым количеством повторений.
Чем меньше будет итераций, тем сложнее игроку будет угадать число.
По умолчанию у игрока 7 попыток, но вы можете это изменить.
'''

for guessTaken in range(7):  # считаем количество попыток
    print('Попробуй угадать!')
    guess = int(input('Вводи число: '))  # т.к. мы хотим получать только числа, сразу преобразуем тип данных

    '''
    Когда мы получили все необходимые данные,
    начинаем сравнивать то, что ввел пользователь,
    с загаданным числом. Делаем это через условия:
    '''

    if guess > number:
        print('Слишком много!')

    elif guess < number:
        print('Слишком мало!')

    elif guess == number:
        break

'''
С циклом мы закончили. Теперь напишем, что будет происходить,
если игрок угадал или не угадал число. Заметьте, что цикл завершает
свою работу как только введенное игроком число равно загаданному числу.
'''


if guess == number:
    print(f'Поздравляю, {myName}, ты угадал число за {guessTaken + 1} попыток.')

if guess != number:
    print('К сожалению, тебе не удалось угадать. Я загадал число: ', number, '.')
