name = input("Как тебя звать матиматик ? : ")
ball = 0
from random import randrange
def rand():
    num1 = randrange(1,100)
    num2 = randrange(1,100)
    deystvie = randrange(0,4)
    otv = 0
    if deystvie == 0:
        deystvie = "-"
        otv = num1 - num2
    elif deystvie == 1:
        deystvie = "+"
        otv = num1 + num2
    elif deystvie == 2:
        deystvie = "/"
        otv = num1 / num2
    elif deystvie == 3:
        deystvie = "*"
        otv = num1 * num2
    user_otv = int(input(f"{num1} {deystvie} {num2} = "))
    if user_otv == otv:
        print("Правильно!")
        global ball
        ball += 1
        print(f"Правильных ответов  {ball}")
        rand()
    elif user_otv != otv:
        print(f"{name} Ты что совсем тупой?!\n Твои баллы сбрасываються ")
        ball = 0
        rand()
rand()