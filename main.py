name = input("Как вас зовут ? : ")
ball = 0
from random import randrange
def rand():
    global ball
    num1 = randrange(1,10)
    num2 = randrange(1,10)
    deystvie = randrange(0,2)
    otv = 0
    if ball >= 3:
        print("Поздравляю вы победили!")
    else:
        if deystvie == 0:
            deystvie = "-"
            otv = num1 - num2
        elif deystvie == 1:
            deystvie = "+"
            otv = num1 + num2
        # для повышения уровня сложности
        # elif deystvie == 2:
        #     deystvie = "/"
        #     otv = num1 / num2
        # elif deystvie == 3:
        #     deystvie = "*"
        #     otv = num1 * num2
        try:
            user_otv = float(input(f"{num1} {deystvie} {num2} = "))
        except:
            print("Пожалуста пишите ответ цифрами \nВаши баллы сбрасываються ")
            rand()
        if user_otv == otv:
            print("Правильно продалжайте в том же духе! ")
            ball += 1
            print(f"Правильных ответов  {ball}")
            rand()
        elif user_otv != otv:
            print(f"{name} Увы но ваш ответ не правильный \nВаши баллы сбрасываються ")
            ball = 0
            rand()
        
vopr = input('хотите ли вы поучаствовать в математической викторине : ')
vopr = vopr.lower().replace(" ","")
if vopr == "да":
    print("Что бы победить ответить на 3 вопроса подрять")
    rand()
elif vopr == "нет":
    print("Ну ладно")
else:
    print("Не понимаю но приму как 'да'")
    print("Что бы победить ответить на 3 вопроса подрять")
    rand()
