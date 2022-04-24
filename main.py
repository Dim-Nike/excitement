from time import sleep
from random import randint

from card import Casino
from chips import Chips
from play import Person
from room import Room
from table import Table

chips = Chips()
room = Room()

list_name = [
    'Иван', "Игорь"
]

list_playing = []

Room = Casino()
BigTable = Table()

for name in list_name:
    num = Person(name=name, chips=1000, room=True)
    list_playing.append(num)

for person in list_playing:
    room.number_person.append(person)





def place_bid(user):
    while True:
        if chips.bid_check(user=user, list_users=list_playing, happening=1):
            action_1 = 'Пропустить'
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
                user.place_bet(chips=chips.bid_check(user=user, list_users=list_playing, happening=0), room_chips=chips)
                print(f'-=-=-=-=-=-=-=--=Моя ставка {user.bid}-=-=-=-=-=-=-=--=')
                print(user)
            break
        if user_action == 2:
            while True:
                higher_rate = int(input('Сколько поставить ставку?\n'))
                if chips.bid_check(user=user, list_users=list_playing, happening=1):
                    user.place_bet(chips=higher_rate, room_chips=chips)
                    print(f'{user.name} поставил {user.bid} фишек\n'
                          f'Ставка принята!')
                    print(user)
                    break
                else:
                    print(f'Тебе необходимо поставить больше, чем '
                          f'наивысшая ставка!')
                    continue
            break
        if user_action == 3:
            print(F'{user.name} покинул партию!')
            print(user)
            break
        else:
            print('Нет такого варианта!')
            continue



def user_place_bet():
    for user_play in list_playing:
        if user_play.card == {}:
            person_cards = Room.give_cards(count_cycle=user_play.count_card)
            user_play.get_card(cards=person_cards)
        user_play.examination(table_card=BigTable.table_card)
        user_play.examination_pair()
        print(user_play)
        print(f'Карты стола - {BigTable.table_card}')
        place_bid(user=user_play)
        pr_sleep(0)
    for user_play in list_playing:
        user_play.bid = 0






def table_give_card(count_card):
    table_cards = Room.give_cards(count_cycle=count_card)
    BigTable.get_total_card(cards=table_cards)

def pr_sleep(n):
    sleep(n)
    print("\n" * 10)


def round():
    for user in list_playing:
        room.check_room(person=user)
    user_place_bet()
    table_give_card(count_card=BigTable.start_count_card)
    pr_sleep(0)
    user_place_bet()
    table_give_card(count_card=BigTable.next_count_card)
    pr_sleep(0)
    user_place_bet()
    table_give_card(count_card=BigTable.next_count_card)
    pr_sleep(0)
    user_place_bet()

    for score in list_playing:
        chips.highest_mark(point=score, room=room)

    for user in list_playing:
        chips.win_check(room=room, user=user)

    for user in list_playing:
        print(f'---{user}---')
    chips.remove_values()
    BigTable.remove_card()
    print(f'Карты стола - {BigTable.table_card}')

count = 0

while True:
    count += 1
    print('--- Начало положено ---')
    print(f'Встречайте наших игроков...\n')
    for person in list_playing:
        print(f'Я {person.name}, мое состояние в комнате - {person.inPlay}\nмои фишки - {person.chips}')
    if count >= 2:
        break
    pr_sleep(0)
    round()
