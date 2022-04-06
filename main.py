from card import Casino
from table import Table
from play import Person

list_name = [
    'Иван'
]
list_playing = []

Room = Casino()
BigTable = Table()

for name in list_name:
    num = Person(name=name, chips=1000, room=True)
    list_playing.append(num)

while True:
    print('---Игра началась---')
    for person in list_playing:
        person_cards = Room.give_cards(count_cycle=person.count_card)
        person.get_card(cards=person_cards)
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

    break









