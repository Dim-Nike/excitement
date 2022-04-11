from card import Casino
from table import Table
from play import Person
from room import Room
from chips import Chips

chips = Chips()
room = Room()

list_name = [
    'Иван', 'Игорь'
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
#     print(f'Ставка сделана. Общий банк - {chips.total_bank}')
#     table_cards = Room.give_cards(count_cycle=BigTable.start_count_card)
#     BigTable.get_total_card(cards=table_cards)
#     print('----------------Ход 1--------------------')
#     table_cards = Room.give_cards(count_cycle=BigTable.next_count_card)
#     BigTable.get_total_card(cards=table_cards)
#     print('----------------Ход 2--------------------')
#     table_cards = Room.give_cards(count_cycle=BigTable.next_count_card)
#     BigTable.get_total_card(cards=table_cards)
#     for exam in list_playing:
#         exam.examination(table_card=BigTable.table_card)
#         print('=======')
#         exam.examination_pair()
#     for score in list_playing:
#         chips.highest_mark(point=score.points, room=room)
#     # for win_person in list_playing:
#     #     chips.win_check(room=room, user=win_person)
#     chips.user_win(list_person=list_playing, room=room)
#     print(f'mark - {len(chips.points)}\nnumber_person - {len(room.number_person)}')
#     for user in list_playing:
#         print(f'Я {user.name} у меня {user.chips} фишек!')
#     print(f'Всего фишек осталось - {chips.total_bank}\npoint_chips - {chips.points}')
#     print(f'Наивысший балл - {chips.highest_score}')
#     break


def place_bid(user):
    user_bid = len(input('Моя ставка... '))
    user_bid = len(input('Моя повышенная ставка... '))
    user_bid = 'Я скидываю...'
    user_action = len(input('Что ты сделаешь?\n'
                            '1. Пропустить\n'
                            '2. Поднять ставку\n'
                            '3. Скинуть'))
    if user_action == 1:
        print(f'{user.name} пропустил ход')
    elif user_action == 2:
        user.place_bet(chips=len(input('Сколько ставишь? ')), room_chips=chips)
        print(f'Ставка {user} - {user.bid}')
    elif user_action == 3:
        print(F'{user.name} покинул партию!')

print('--- Начало положено ---')
print(f'Встречайте наших игроков...\n')
for person in list_playing:
    print(f'Я {person.name}, мое состояние в комнате - {person.inPlay}\nмои фишки - {person.chips}')

while True:
    for user in list_playing:
        room.check_room(person=user)
    table_cards = Room.give_cards(count_cycle=BigTable.start_count_card)
    BigTable.get_total_card(cards=table_cards)
    for user_play in list_playing:
        person_cards = Room.give_cards(count_cycle=user_play.count_card)
        user_play.get_card(cards=person_cards)
        user_play.examination(table_card=BigTable.table_card)
        user_play.examination_pair()
        print(user_play)
        place_bid(user=user_play)
    break


















