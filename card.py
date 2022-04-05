import random


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
        self.remainder = {
                      'P': [],
                      'B': [],
                      'W': [],
                      'С': [],
                      },
        self.testSelfCard = {}
        self.get_two_card = {}
        self.suit = ['P', 'B', 'W', 'C']

    def do_bid(self, person_bid):
        self.total_bid += person_bid

    def getCard(self):
        for x in ['P', 'B', 'W', 'C']:
            print('-------------------------')
            for card in self.cards.get(x):
                print(f'{x} - {card}')


    def get_card_play(self):
        choice = random.randint(0, 52)
        count = 0
        for key in self.suit:
            for card in self.cards.get(key):
                count += 1
                if choice == count:
                    self.get_two_card[key] = [card]


                    return
                else:
                    continue






num_1 = Casino()
num_1.getCard()
num_1.get_card_play()
num_1.get_card_play()
print(num_1.get_two_card)

