class Table:
    def __init__(self):
        self.start_count_card = 3
        self.next_count_card = 1
        self.table_card = {}


    def total_card(self, cards):
        self.table_card = cards


        print(f'Я стол, мои карты: {self.table_card}')

