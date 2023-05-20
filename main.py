import ru_local as ru
import random

action_15_int=[0,0,0,0,0,0]
action_15_print = [ru.ACTION_15_1,ru.ACTION_15_2,ru.ACTION_15_3,ru.ACTION_15_4,ru.ACTION_15_5,ru.ACTION_15_6]
random_events_15_9 = [ru.RANDOM_EVENT_15_9_1,ru.RANDOM_EVENT_15_9_2,ru.RANDOM_EVENT_15_9_3]

design = 0
programming = 0
poetry = 0
dancing = 0
english = 0
music = 0

action = 15
health = 100
happiness = 50
money = 0

factor_health = 0.2
factor_happiness = 0.2
factor_money = 0.2

name = input(ru.NAME_MESSAGE)
print(ru.INF_MESSAGE_1)

#Перечисление действий в первые 15 лет
for i in range(0,6):
    print(str(i+1) + ". " + str(action_15_print[i]))

#распределение очков действия за первые 15 лет
while action>0:
    number,quantity = map(int,input().split(" "))
    if quantity<=action:
        action_15_int[number-1] += quantity
        action -= quantity
    else:
        print(ru.ACTION_ERROR)
        continue

#Рандомные события за первые 15 лет
print(ru.INF_MESSAGE_RANDOM_1)
#random_events_or = random.randint(0, 100)
random_events_or = 2
if random_events_or%2==0:
#    random_events_number = random.randint(0, 10)
    random_events_number = 8

    if random_events_number == 10:
        print(ru.RANDOM_EVENT_15_11)
        exit(0)

    if random_events_number == 9:
        print(ru.RANDOM_EVENT_15_10)
        yes_no_flag = input(ru.RANDOM_EVENT_15_10_question)
        if yes_no_flag.upper() == "ДА":
            if random.randint(0,100)%2==0:
                print(ru.RANDOM_EVENT_15_10_3)
            elif random_events_number%5==0:
                print(ru.RANDOM_EVENT_15_10_2)
                health -=30
            elif random_events_number%3:
                print(ru.RANDOM_EVENT_15_10_1)
                health +=20

    if random_events_number == 8:
        print(ru.RANDOM_EVENT_15_9)
        for i in range(3):
            print(str(i+1) + ". " + random_events_15_9[i])
        number_flag = int(input(ru.RANDOM_EVENT_15_9_question))

    if random_events_number == 7:
        print(ru.RANDOM_EVENT_15_8)
        health -= 20

    if random_events_number == 6:
        print(ru.RANDOM_EVENT_15_7)
        factor_money = 0.5

    if random_events_number == 5:
        print(ru.RANDOM_EVENT_15_6)
        health -= 20

    if random_events_number == 4:
        print(ru.RANDOM_EVENT_15_5)
        health -= 20

    if random_events_number == 3:
        print(ru.RANDOM_EVENT_15_4)
        health += 20

    if random_events_number == 2:
        print(ru.RANDOM_EVENT_15_3)
        factor_money = 2

    if random_events_number == 1:
        print(ru.RANDOM_EVENT_15_2)
        health += 20

    if random_events_number == 0:
        print(ru.RANDOM_EVENT_15_1)
        factor_money = 3

health = 100
happiness = 50
money = 0

design = 0
programming = 0
poetry = 0
dancing = 0
english = 0
music = 0
