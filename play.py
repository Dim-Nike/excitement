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
        pari = 0
        two_pari = 0
        set = 0
        full_house = 0
        kare = 0

        count_pari = 0
        count_set = 0
        local_list = []
        result = Counter(self.total_without_suit_card)
        # print(result)
        for key in result:
            if result.get(key) == 4:
                local_list.append('Карэ')
                print(f'У меня карэ из {key}')
                kare += 1
            if result.get(key) == 3:
                local_list.append('Сет')
                print(f'У меня сет из {key}')
                set = 1
            elif result.get(key) == 2:
                local_list.append('Пара')
                print(f'У меня пара из {key}')
                pari = 1

        print(local_list)
        for combination in local_list:
            if combination == 'Пара':
                count_pari += 1
            if combination == 'Сет':
                count_set += 1

        if count_set == 1 and count_pari == 1 or count_set == 1 and count_pari == 2:
            full_house += 1
            print('У меня фулл хаус')
        if count_pari == 2 or count_pari == 3:
            two_pari += 1
            print('У меня две пары!')

        if kare == 1:
            self.points = 7
        elif full_house:
            self.points = 6
        elif set == 1:
            self.points = 3
        elif two_pari:
            self.points = 2
        elif pari == 1:
            self.points = 1
        print(f'Я {self.name} у меня {self.points} баллов!')







        # for count in result:
        #     local_list.append(result[count])
        #     print(local_list)
        # for mean in local_list:
        #     if mean == 4:
        #         print(f'Я {self.name} у меня карэ!')
        #     if mean == 3:
        #         print(f'Я {self.name} у меня сет!')
        #     if mean == 2:
        #         print(f'Я {self.name} у меня пара!')

        print(f'Общие карты у {self.name}: {self.total_without_suit_card}')

    def __str__(self):
        return f'I am {self.name}'





