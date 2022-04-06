from collections import Counter

class Person:
    def __init__(self, name, chips, room):
        self.name = name
        self.chips = chips
        self.room = room
        self.bid = 0
        self.inPlay = True
        self.card = {}
        self.count_card = 2
        self.points = 0
        self.total_without_suit_card = []
        self.total_with_suit_card = {}

    def up_ante(self, count):
        self.bid = count
        self.chips -= count

    def skip(self):
        self.bid = 0

    def throw_off(self):
        self.inPlay = False

    def get_card(self, cards):
        self.card = cards
        print(f'Я {self.name} у меня карты: {self.card}')

    def examination(self, table_card):
        for key in self.card:
            for mean in self.card[key]:
                self.total_without_suit_card.append(mean)
        for key in table_card:
            for mean in table_card[key]:
                self.total_without_suit_card.append(mean)

    def examination_pair(self):
        local_list = []
        result = Counter(self.total_without_suit_card)
        for count in result:
            local_list.append(result[count])
            print(local_list)
        for mean in local_list:
            if mean == 4:
                print(f'Я {self.name} у меня карэ!')
            if mean == 3:
                print(f'Я {self.name} у меня сет!')
            if mean == 2:
                print(f'Я {self.name} у меня пара!')

        print(f'Общие карты у {self.name}: {self.total_without_suit_card}')

    def __str__(self):
        return f'I am {self.name}'





