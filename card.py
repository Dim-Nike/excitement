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












