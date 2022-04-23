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
    # user_action = int(input('Что ты сделаешь?\n'
    #                         '1. Пропустить\n'
    #                         '2. Поднять ставку\n'
    #                         '3. Скинуть\n'))
    user_action = 2

    if user_action == 1:
        print(f'{user.name} пропустил ход')
        print(user)
    if user_action == 2:
        while True:
            user.place_bet(chips=int(input('Сколько поставить ставку?\n')), room_chips=chips)
            if chips.bid_check(user=user, list_users=list_playing, happening=2):
                print(f'{user.name} поставил {user.bid} фишек\n'
                      f'Ставка принята!')
                print(user)
                break
            else:
                print(f'Тебе необходимо поставить больше, чем '
                      f'наивысшая ставка!')
                continue
            # user.place_bet(chips=int(input('Сколько ставишь? ')), room_chips=chips)



    if user_action == 3:
        print(F'{user.name} покинул партию!')
        print(user)


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
