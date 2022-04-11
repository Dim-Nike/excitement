from time import sleep

from card import Casino
from chips import Chips
from play import Person
from room import Room
from table import Table

chips = Chips()
room = Room()

list_name = [
    'Иван'
]

list_playing = []

Room = Casino()
BigTable = Table()

for name in list_name:
    num = Person(name=name, chips=1000, room=True)
    list_playing.append(num)

for person in list_playing:
    room.number_person.append(person)


# for x in room.number_person:
#     print(f'Я {x.name} мое состояние в комнате: {x.inPlay}\nМои фишки - {x.chips}')

# while True:
#     print('---Игра началась---')
#     for name in list_playing:
#         room.check_room(name)
#
#     for person in list_playing:
#         person_cards = Room.give_cards(count_cycle=person.count_card)
#         person.get_card(cards=person_cards)
#
#     for person in list_playing:
#         person.place_bet(chips=int(input(f'Я {person.name} моя ставка... ')), room_chips=chips)
#
    # print(f'Ставка сделана. Общий банк - {chips.total_bank}')
    # table_cards = Room.give_cards(count_cycle=BigTable.start_count_card)
    # BigTable.get_total_card(cards=table_cards)
    # print('----------------Ход 1--------------------')
    # table_cards = Room.give_cards(count_cycle=BigTable.next_count_card)
    # BigTable.get_total_card(cards=table_cards)
    # print('----------------Ход 2--------------------')
    # table_cards = Room.give_cards(count_cycle=BigTable.next_count_card)
    # BigTable.get_total_card(cards=table_cards)
    # for exam in list_playing:
    #     exam.examination(table_card=BigTable.table_card)
    #     print('=======')
    #     exam.examination_pair()
    # for score in list_playing:
    #     chips.highest_mark(point=score.points, room=room)
    # # for win_person in list_playing:
    # #     chips.win_check(room=room, user=win_person)
    # chips.user_win(list_person=list_playing, room=room)
    # print(f'mark - {len(chips.points)}\nnumber_person - {len(room.number_person)}')
    # for user in list_playing:
    #     print(f'Я {user.name} у меня {user.chips} фишек!')
    # print(f'Всего фишек осталось - {chips.total_bank}\npoint_chips - {chips.points}')
    # print(f'Наивысший балл - {chips.highest_score}')
    # break


def place_bid(user):
    user_action = int(input('Что ты сделаешь?\n'
                            '1. Пропустить\n'
                            '2. Поднять ставку\n'
                            '3. Скинуть\n'))

    if user_action == 1:
        print(f'{user.name} пропустил ход')
        print(user)
    if user_action == 2:
        user.place_bet(chips=int(input('Сколько ставишь? ')), room_chips=chips)
        print(user)
    if user_action == 3:
        print(F'{user.name} покинул партию!')
        print(user)


def user_place_bet():
    for user_play in list_playing:
        person_cards = Room.give_cards(count_cycle=user_play.count_card)
        user_play.get_card(cards=person_cards)
        user_play.examination(table_card=BigTable.table_card)
        user_play.examination_pair()
        print(user_play)
        print(f'Карты стола - {BigTable.table_card}')
        place_bid(user=user_play)
        pr_sleep(0)
        print(f'--- Подводим итоги---')





def table_give_card(count_card):
    table_cards = Room.give_cards(count_cycle=count_card)
    BigTable.get_total_card(cards=table_cards)

def pr_sleep(n):
    sleep(n)
    print("\n" * 100)




print('--- Начало положено ---')
print(f'Встречайте наших игроков...\n')
for person in list_playing:
    print(f'Я {person.name}, мое состояние в комнате - {person.inPlay}\nмои фишки - {person.chips}')

pr_sleep(5)

while True:
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
    break



for score in list_playing:
    chips.highest_mark(score.points, room=room)
for user in list_playing:
    chips.win_check(room=room, user=user)
chips.win_check(list_playing, room)
for user in list_playing:
    print(f'---{user}---')