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
    'Иван', "Игорь"
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
        action_3 = 'Сбросить'
        print(f'1. {action_1}\n'
              f'2. {action_2}\n'
              f'3. {action_3}')
        user_action = int(input(f'Твой ход!\n'))
        if user_action == 1:
            if action_1 == 'Пропустить':
                print(f'{user.name} пропустил ход')
                print(user)
            elif action_1 == 'Сравнять':
                if chips.bid_check(user=user, number_person=room.number_person, happening=2, higher_rate_user=user.chips):
                    user.place_bet(chips=chips.bid_check(user=user, number_person=room.number_person, happening=0), room_chips=chips)
                    print(user)
                else:
                    print(f'У {user.name} недостаточно фишек!\nИгрок поставил - {user.bid}\nУ игрока - {user.chips} фишек')
                    bid = user.chips
                    user.place_bet(chips=bid, room_chips=chips)
            break
        if user_action == 2:
            if action_1 != 'Ва-банк!':
                while True:
                    higher_rate = int(input('Сколько поставить ставку?\n'))
                    if user.chips > higher_rate:
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
        # for user in room.number_person:
        #     if not chips.bid_check(user=user, number_person=room.number_person, happening=1):
        #         place_bid(user)                !!!!!!!!!!Разобраться с этим!!!!!!!!!!
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



    for score in room.number_person:
        if score.inPlay:
            chips.highest_mark(point=score, room=room)

    for user in room.number_person:
        print('----------------Я отдаю фишки победителям!!!!!!!!!----------------')
        chips.win_check(room=room, user=user)

    for user in list_playing:
        print(f'---{user}---')
    chips.remove_values()
    BigTable.remove_card()
    print(f'Карты стола - {BigTable.table_card}')


count = 0

while True:
    check_user_room(room=room)
    count += 1
    print('--- Начало положено ---')
    print(f'Встречайте наших игроков...\n')
    for person in list_playing:
        print(f'Я {person.name}, мое состояние в комнате - {person.inPlay}\nМои фишки - {person.chips}')
    if count >= 4:
        break
    pr_sleep(0)
    round()
    pr_sleep(5)
    room.check_room(list_users=list_playing)



