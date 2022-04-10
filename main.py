from card import Casino
from table import Table
from play import Person
from room import Room
from chips import Chips

chips = Chips()
room = Room()

list_name = [
    'Иван', 'Игорь', 'Ольга'
]

list_playing = []

Room = Casino()
BigTable = Table()

for name in list_name:
    num = Person(name=name, chips=1000, room=True)
    list_playing.append(num)

for person in list_playing:
    room.number_person.append(person)



for x in room.number_person:
    print(f'Я {x.name} мое состояние в комнате: {x.inPlay}\nМои фишки - {x.chips}')



while True:
    print('---Игра началась---')
    for name in list_playing:
        room.check_room(name)

    for person in list_playing:
        person_cards = Room.give_cards(count_cycle=person.count_card)
        person.get_card(cards=person_cards)

    for person in list_playing:
        person.place_bet(chips=int(input(f'Я {person.name} моя ставка... ')), room_chips=chips)

    print(f'Ставка сделана. Общий банк - {chips.total_bank}')
    table_cards = Room.give_cards(count_cycle=BigTable.start_count_card)
    BigTable.get_total_card(cards=table_cards)
    print('----------------Ход 1--------------------')
    table_cards = Room.give_cards(count_cycle=BigTable.next_count_card)
    BigTable.get_total_card(cards=table_cards)
    print('----------------Ход 2--------------------')
    table_cards = Room.give_cards(count_cycle=BigTable.next_count_card)
    BigTable.get_total_card(cards=table_cards)
    for exam in list_playing:
        exam.examination(table_card=BigTable.table_card)
        print('=======')
        exam.examination_pair()
    for score in list_playing:
        chips.win_check(point=score.points, room=room, user=score)
    for user in list_playing:
        print(f'Я {user.name} у меня {user.chips} фишек!')
    break









