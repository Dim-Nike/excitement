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
                            card_lady, card_ace],
                      'B': [card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10, card_jack,
                            card_lady, card_ace],
                      'W': [card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10, card_jack,
                            card_lady, card_ace],
                      'C': [card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10, card_jack,
                            card_lady, card_ace],
                      }
        self.total_bid = 0
        self.remainder = {
                      'P': [],
                      'B': [],
                      'W': [],
                      'С': [],
                      },
        self.testSelfCard = {}

    def do_bid(self, person_bid):
        self.total_bid += person_bid

    def getCard(self):
        for x in ['P', 'B', 'W', 'C']:
            print('-------------------------')
            for card in self.cards.get(x):
                print(f'{x} - {card}')

    def __str__(self):
        return f'Карты: {self.cards.get("")}'


num_1 = Casino()
num_1.getCard()

