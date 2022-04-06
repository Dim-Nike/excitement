import random
from play import Person
from table import Table

card_2 = 2
card_3 = 3
card_4 = 4
card_5 = 5
card_6 = 6
card_7 = 7
card_8 = 8
card_9 = 9
card_10 = 10
card_jack = 11
card_lady = 12
card_king = 13
card_ace = 14


class Casino:
    def __init__(self):
        self.circle = 0
        self.cards = {
                      'P': [card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10, card_jack,
                            card_lady, card_king, card_ace],
                      'B': [card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10, card_jack,
                            card_lady, card_king, card_ace],
                      'W': [card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10, card_jack,
                            card_lady, card_king, card_ace],
                      'C': [card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10, card_jack,
                            card_lady, card_king, card_ace],
                      }
        self.total_bid = 0
        self.save_card = {}


    def do_bid(self, person_bid):
        self.total_bid += person_bid

    def subtract_dict(self):
        for key in self.save_card:
            for k in self.cards:
                if key == k:
                    for meaning in self.save_card.get(k):
                        for m in self.cards.get(key):
                            if meaning == m:
                                self.cards.get(key).remove(meaning)
                            else:
                                continue
                else:
                    continue




    def show_all_cards(self):
        for x in ['P', 'B', 'W', 'C']:
            print('-------------------------')
            for card in self.cards.get(x):
                print(f'{x} - {card}')

    def give_cards(self, count_cycle):
        self.save_card = {}
        cycle = 0

        while cycle < count_cycle:
            choice = random.randint(1, 53)
            count = 0

            for key in self.cards:
                for card in self.cards.get(key):
                    count += 1
                    if choice == count:
                        if key in self.save_card:
                            self.save_card[key].append(card)
                            cycle += 1
                            self.subtract_dict()
                        else:
                            self.save_card[key] = [card]
                            cycle += 1
                            self.subtract_dict()
                    else:
                        continue
        return self.save_card

# Cas_1 = Casino()
#
# Room = Table()
# Cas_1.get_card(count_cycle=Room.start_count_card)
# table_cards = Cas_1.set_card
# print(table_cards)
# Room.total_card(cards=table_cards)
# Cas_1.get_card(count_cycle=Room.next_count_card)
# table_cards = Cas_1.set_card
# print(table_cards)
# Room.total_card(cards=table_cards)

# Cas_1.get_card(count_cycle=3)
# table_cards = Cas_1.set_card
# print(f'Казино дало карты: {table_cards}')
# Cas_1.get_card(count_cycle=1)
# Room.total_card(cards=table_cards)
# table_cards = Cas_1.set_card
# print(f'Казино дало карты: {table_cards}')
# Room.total_card(cards=table_cards)
#
#
# Ivan = Person(name='Иван', chips=1000, room=True)
# Sveta = Person(name='Света', chips=1000, room=True)
#
# Cas_1.get_card(Ivan.count_card)
# Ivan_card = Cas_1.set_card
# Cas_1.get_card(Sveta.count_card)
# Sveta_card = Cas_1.set_card

# Room = Casino()
# Big_table = Table()
#
# Ivan = Person(name='Иван', chips=1000, room=True)
# Sveta = Person(name='Света', chips=1000, room=True)
#
# Room.get_card(count_cycle=Big_table.start_count_card)
# table_card = Room.set_card
# Big_table.total_card(cards=table_card)
# Room.get_card(Ivan.count_card)
# ivan_card = Room.set_card
# Ivan.get_card(two_card=ivan_card)
# Room.get_card(Sveta.count_card)
# sveta_card = Room.set_card
# Sveta.get_card(two_card=sveta_card)
# Room.get_card(count_cycle=Big_table.next_count_card)
# table_card = Room.set_card
# print(f'Казино дало карты: {table_card}')
# Big_table.total_card(cards=table_card)
# print('-------------------------')
# print(f'Оставшиеся карты: {Room.getCard()}')











# Ivan.get_card(two_card=Ivan_card)
# Sveta.get_card(two_card=Sveta_card)
#
# print(Cas_1.getCard())
