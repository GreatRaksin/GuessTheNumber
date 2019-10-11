from random import *
from colorama import Fore, init
init()

print(Fore.GREEN)
myName = input('Привет! Как тебя зовут?  ')  # знакомимся с пользователем
number = randint(1, 100)
guessTaken = 0  # переменная хранит значения попыток пользователя

print(Fore.CYAN, f'{myName}, я загадал число от 1 до 100. Твоя задача угадать это число.')


for guessTaken in range(7):  # считаем количество попыток
    print('Попробуй угадать.')
    guess = int(input('Вводи число: '))  # т.к. мы хотим получать только числа, сразу преобразуем тип данных

    if guess > number:
        print(guess, 'Слишком много!')
        print()

    if guess < number:
        print(guess, 'Слишком мало!')
        print()

    if guess == number:
        break


def getEnding(guessTaken):
    lastChars = guessTaken % 100

    if 2 <= lastChars <= 4:
        return 'ки'
    else:
        lastChars = guessTaken % 10
        if lastChars == 1:
            return 'ку'
        elif lastChars >= 5 <= 20:
            return 'ок'


if guess == number:
    print(f'Поздравляю, {myName}, ты угадал число за {guessTaken + 1} попыт{getEnding(guessTaken)}.')

if guess != number:
    print('К сожалению, тебе не удалось угадать. Я загадал число: ', number, '.')

