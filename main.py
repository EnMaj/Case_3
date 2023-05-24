import ru_local as ru
import random

action_15_int=[0,0,0,0,0,0]
action_15_print = [ru.ACTION_15_1,ru.ACTION_15_2,ru.ACTION_15_3,ru.ACTION_15_4,ru.ACTION_15_5,ru.ACTION_15_6]
random_events_15_9 = [ru.RANDOM_EVENT_15_9_1,ru.RANDOM_EVENT_15_9_2,ru.RANDOM_EVENT_15_9_3]
friendli_list = [ru.FRIENDS_1,ru.FRIENDS_2,ru.FRIENDS_3,ru.FRIENDS_4]
friendly_scale = [15,15,15,15]
romantic_scale = [-10,-10,-10,-10]

skill = [0,0,0,0,0,0]
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

computer = False

name = input(ru.NAME_MESSAGE)

print(ru.MESSAGE_CHOICE)
choice = int(input())
if choice == 1:
    computer = True
elif choice == 2:
    money+=500*factor_money
elif choice == 3:
    dancing += 10

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
random_events_or = random.randint(0, 100)
#random_events_or = 2
if random_events_or%2==0:
    random_events_number = random.randint(0, 10)
#    random_events_number = 8
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
else:
    print(ru.RANDOM_EVENT_NO)
health = 100 + action_15_int[4]*2 + action_15_int[5]
happiness = 50 + action_15_int[0]*2 + action_15_int[2]*2 + action_15_int[3]*3
money = 0

design = (design + action_15_int[2]*2)*(action_15_int[1]*0.5)
programming = 0
poetry = 0
dancing = 0 + action_15_int[5]
english = 0
music = 0

for i in range(4):
    friendly_scale[i]+=action_15_int[0]*2

print(ru.INF_MESSAGE_2)

while health>0 and happiness>0:
    for i in range(16,26):
        if health<0 or happiness<0:
            exit(0)
        action=12
        print(ru.MESSAGE_CHOICE)
        choice = int(input())
        if choice == 1:
            computer = True
        elif choice == 2:
            money += 500 * factor_money
        elif choice == 3:
            dancing += 10

        random_events_or = random.randint(0, 100)
        if random_events_or%11==0:
            random_events_number=random.randint(1,5)
            if random_events_number == 1:
                print(ru.RANDOM_EVENT_22_1)
                exit(0)
            if random_events_number == 2:
                print(ru.RANDOM_EVENT_22_2)
                friendly_scale.pop(3)
                friendli_list.pop(3)
                romantic_scale.pop(3)
            if random_events_number == 3:
                print(ru.RANDOM_EVENT_22_3)
                health-=20
            if random_events_number==4:
                print(ru.RANDOM_EVENT_22_4)
                health-=20
            if random_events_number == 5:
                print(ru.RANDOM_EVENT_22_5)
                money+=10000
        else:
            print(ru.RANDOM_EVENT_NO)

        while action>0 and health>0 and happiness>0:
            print(ru.INF_MESSAGE_3)
            if i>=18:
                print()
            number, quantity = map(int, input().split(" "))
            if quantity<=action:
                if number<7:
                    if quantity <= action:
                        skill[number - 1] += quantity*2
                        action -= quantity
                    else:
                        print(ru.ACTION_ERROR)
                        continue
                if number == 7:
                    health+=5
                    action += quantity
                if number == 8 and money>=500:
                    health+=10
                    action -= quantity
                    money-=500
                if number == 9:
                    health+=5
                    action-=quantity
                if number == 10:
                    print(ru.FRIENDSHIP)
                    for j in range (len(friendly_scale)):
                        print(str(j+1)+". "+friendli_list[j])
                    number_f, quantity = map(int, input().split(" "))
                    friendly_scale[number_f]+=quantity*2
                    action-=quantity
                if number == 11:
                    print(ru.ROMANTIC)
                    for j in range (len(friendly_scale)):
                        print(str(j+1)+". "+friendli_list[j])
                    number_f, quantity = map(int, input().split(" "))
                    romantic_scale[number_f]+=quantity*2
                    action-=quantity
                if number == 12:
                    health= health - 20*quantity
                if number == 13:
                    action-=3
                    happiness-=5
                    print(ru.JOBS)
                    jobs = int(input())
                    if jobs == 1:
                        money+=1000
                    elif jobs == 2:
                        money+=1000
                    elif jobs == 3:
                        money+=1500
                        health-=10
            else:
                print(ru.ACTION_ERROR)
                continue





print("Вы умерли. Игра закончилась. Поздравляю!")