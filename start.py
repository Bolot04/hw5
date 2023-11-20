from casino import bet
from decouple import config

My_Money = config('MY_MONEY', cast=int)

while True:
    print(f'Ваш баланс - {My_Money}$')
    print("1 - начать\n"
          "2 - выйти")
    word = input("Выберите команду ")

    if word == '2':
        print("you exit")
        break
    elif word == '1':
        b = int(input('Загадайте число от 1 до 30: '))
        g = int(input("сколько вы хотите постаить: "))
        My_Money -= g
        My_Money += bet(b, g)
    else:
        print("Проверьте правильно ли написали ")
