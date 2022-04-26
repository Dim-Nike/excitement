from time import sleep
from random import randint

from card import Casino
from chips import Chips
from play import Person
from room import Room
from table import Table

chips = Chips()
room = Room()


list_user_in_play = [
    'Иван', "Игорь", 'Артем'

]

list_playing = []

Room = Casino()
BigTable = Table()

for name in list_user_in_play:
    num = Person(name=name, chips=1000, room=True)
    list_playing.append(num)


def check_user_room(room):
    for person in list_playing:
        if person.inPlay:
            if person not in room.number_person:
                room.number_person.append(person)
                print(f'-=-=-=-=-=-=-Игрок {person.name} добавился!-=-=-=-=-=-=-')
            else:
                print(f'-=-=-=-=-=-=-Игрок {person.name} был в игре и остается в ней!-=-=-=-=-=-=-')
        else:
            if person in room.number_person:
                room.number_person.remove(person)
                print(f'-=-=-=-=-=-=-Игрок {person.name} раннее был в игре, теперь ушел!-=-=-=-=-=-=-')
    print(f'В комнате всего {len(room.number_person)} человек')


def place_bid(user):
    while True:
        if chips.bid_check(user=user, number_person=room.number_person, happening=1):
            action_1 = 'Пропустить'
        elif chips.bid_check(user=user, number_person=room.number_person, happening=4):
            action_1 = 'Ва-банк!'
        else:
            action_1 = 'Сравнять'
        action_2 = 'Повысить'
        action_3 = 'Поставить все!'
        action_4 = 'Сбросить'
        print(f'1. {action_1}\n'
              f'2. {action_2}\n'
              f'3. {action_3}\n'
              f'4. {action_4}')

        user_action = int(input(f'Твой ход!\n'))
        if user_action == 1:
            if action_1 == 'Пропустить':
                print(f'{user.name} пропустил ход')
                print(user)

            elif action_1 == 'Сравнять':
                if chips.bid_check(user=user, number_person=room.number_person, happening=2, higher_rate_user=user.chips):
                    user.place_bet(chips=chips.bid_check(user=user, number_person=room.number_person, happening=0) - user.bid, room_chips=chips)
                    print(f'{user.name} поставил {user.bid}')
                    print(user)
                else:
                    print(f'У {user.name} недостаточно фишек!\nИгрок поставил - {user.bid}\nУ игрока - {user.chips} фишек')
                    bid = user.chips
                    user.place_bet(chips=bid, room_chips=chips)
            elif action_1 == 'Ва-банк!':
                print(f'Игрок поставил все!')
                bid = user.chips
                user.place_bet(chips=bid, room_chips=chips)
                break
            break
        if user_action == 2:
            if action_1 != 'Ва-банк!':
                while True:
                    higher_rate = int(input('Сколько поставить ставку?\n'))
                    if user.chips >= higher_rate:
                        if user.bid < higher_rate:
                            if chips.bid_check(user=user, number_person=room.number_person, happening=2, higher_rate_user=higher_rate):
                                user.place_bet(chips=higher_rate, room_chips=chips)
                                print(f'{user.name} поставил {user.bid} фишек\n'
                                      f'Ставка принята!')
                                print(user)
                                break
                            else:
                                print(f'Тебе необходимо поставить больше, чем'
                                      f'наивысшая ставка!')
                                continue
                        else:
                            print(f'У {user.name}  не хватает фишек!')
                            continue
                    else:
                        print('Недостаточно фишек!')
                        continue
                break

            else:
                print('Недостаточно фишек!')
                continue
        if user_action == 3:
            bid = user.chips
            user.place_bet(chips=bid, room_chips=chips)
            print(f'Игрок поставил {bid} фишек')
            break

        if user_action == 4:
            user.inPlay = False
            print(F'{user.name} покинул партию!')
            print(user)
            break
        else:
            print('Нет такого варианта!')
            continue



def user_place_bet(room):
    for user_play in room.number_person:
        if user_play.card == {}:
            person_cards = Room.give_cards(count_cycle=user_play.count_card)
            user_play.get_card(cards=person_cards)
        user_play.examination(table_card=BigTable.table_card)
        user_play.examination_pair()
        print(user_play)
        print(f'Карты стола - {BigTable.table_card}')
        place_bid(user=user_play)
        pr_sleep(0)
    number = 0
    for user in room.number_person:
        if not chips.bid_check(user=user, number_person=room.number_person, happening=1):
            print(user)
            number = + 1
            place_bid(user)
            print(f'Попытка - {number}')
            pr_sleep(0)

    for user_play in room.number_person:
        user_play.bid = 0


def table_give_card(count_card):
    table_cards = Room.give_cards(count_cycle=count_card)
    BigTable.get_total_card(cards=table_cards)


def pr_sleep(n):
    sleep(n)
    print("\n" * 10)


def round():
    user_place_bet(room=room)
    check_user_room(room=room)
    table_give_card(count_card=BigTable.start_count_card)
    pr_sleep(0)
    user_place_bet(room=room)
    check_user_room(room=room)
    table_give_card(count_card=BigTable.next_count_card)
    pr_sleep(0)
    user_place_bet(room=room)
    check_user_room(room=room)
    table_give_card(count_card=BigTable.next_count_card)
    pr_sleep(0)
    user_place_bet(room=room)
    check_user_room(room=room)
    chips.check_win(room=room)
    for user in list_playing:
        print(f'---{user}---')
    chips.remove_values()
    BigTable.remove_card()
    print(f'Карты стола - {BigTable.table_card}')


count = 0
print('--- Начало положено ---')
print(f'Встречайте наших игроков...\n')
while True:
    check_user_room(room=room)
    count += 1
    print(f'Раунд {count}')
    for person in list_playing:
        print(f'Я {person.name}, мое состояние в комнате - {person.inPlay}\nМои фишки - {person.chips}')
    if count >= 4:
        break
    pr_sleep(0)
    round()
    pr_sleep(5)
    room.check_room(list_users=list_playing)


# from termcolor  import cprint
#
# list_components_for_plane = {'Полетный контроллер': 50,
#                    'Бесколекторный двигатель': 23,
#                    'Пропеллер 5.8дм': 17,
#                    'Видеопередатчик': 30,
#                    'PV видеокамера': 35,
#                    'GPS модуль': 40,
#                    'Регулятор оборотов': 13,
#                    'Сервы': 30,
#                    'Литионовые батареи': 7,
#                    'Пульт управления': 0,
#                    'Антена': 10,
#                    'Приемник радиоуправления': 45,
#                    'Пищалка': 5}
#
# list_components_for_cv = {'Полетный контроллер': 50,
#                    'Бесколекторный двигатель': 20*4,
#                    'Рама': 30,
#                    'Видеопередатчик': 30,
#                    'PV видеокамера': 35,
#                    'GPS модуль': 30,
#                    'Регулятор оборотов': 13*4,
#                    'Батарея': 7,
#                    'Пульт управления': 0,
#                    'Антена': 10,
#                    'Приемник радиоуправления': 45,
#                    'Пищалка': 5,
#                    'Пропеллер': 10}
#
#
# all_price_for_cv = 0
# dollar = 74.8
# slide = '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
#
# def plane():
#     all_price_for_plane = 0
#     for element, value in list_components_for_plane.items():
#         all_price_for_plane += value
#         if value >= 40:
#             cprint(f'{element} - {value}$', 'red')
#         elif value >= 20:
#             cprint(f'{element} - {value}$', 'yellow')
#         else:
#             cprint(f'{element} - {value}$', 'green')
#     print(slide)
#     print(f'Всего - {all_price_for_plane * dollar} Р ')
#     return all_price_for_plane * dollar
#
#
# def cv():
#     all_price_for_plane = 0
#     for element, value in list_components_for_cv.items():
#         all_price_for_plane += value
#         if value >= 40:
#             cprint(f'{element} - {value}$', 'red')
#         elif value >= 20:
#             cprint(f'{element} - {value}$', 'yellow')
#         else:
#             cprint(f'{element} - {value}$', 'green')
#     print(slide)
#     print(f'Всего - {all_price_for_plane * dollar} Р ')
#     return all_price_for_cv * dollar
#
# plan = plane()
# cvv = cv()
# print(slide*2)
# if plan > cvv:
#     cprint(f'Самолет дороже на {plan - cvv}', 'cyan')
# if cvv > plan:
#     cprint(f'Квадрик дороже на {cvv - plan}', 'cyan')




