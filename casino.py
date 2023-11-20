import random
import time


def bet(b, g):
    print('Пожалуйста подождите...')
    time.sleep(2)
    choice = random.randint(1, 31)
    if choice == b:
        print("YOU WIN!!")
        return g * 2
    else:
        print("you lose")
        print(choice)
        print(f"-{g}$")
        return 0
