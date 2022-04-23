class Table:
    def __init__(self):
        self.start_count_card = 3
        self.next_count_card = 1
        self.table_card = {}


    def get_total_card(self, cards):
        if self.table_card != {}:
            for key in cards:
                for k in self.table_card:
                    if key == k:
                        for means in cards[key]:
                            self.table_card[k].append(means)
                        break
                    if key not in self.table_card.keys():
                        self.table_card[key] = cards.get(key)
                        break
        else:
            self.table_card = cards
        print(f'Я стол, мои карты: {self.table_card}')

    def remove_card(self):
        self.table_card = {}
