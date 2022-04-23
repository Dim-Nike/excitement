class Chips:
    def __init__(self, room=True):
        self.room = room
        self.total_bank = 0
        self.points = []
        self.highest_score = 0
        self.number_of_wins = 0
        self.some_wins_chips = 0

    def highest_mark(self, point, room):
        self.points.append(point.points)
        if len(self.points) == len(room.number_person):
            self.highest_score = max(self.points)
            print(f'---Наивысший балл - {self.highest_score}---')

    def win_check(self, room, user):
        for value in self.points:
            if self.highest_score == value:
                self.number_of_wins += 1

        self.some_wins_chips = self.total_bank
        if len(self.points) == len(room.number_person) and self.highest_score == user.points:
            user.chips += self.total_bank // self.number_of_wins
            print(f'Фишки передаются игроку с наивысшим баллом - {self.number_of_wins}\n'
                  f'Количество фишек - {self.total_bank}')
            some_wins_chips = self.total_bank
            self.total_bank -= some_wins_chips // self.number_of_wins
        self.number_of_wins = 0

    def user_win(self, list_person, room):
        for value in self.points:
            if self.highest_score == value:
                self.number_of_wins += 1

        for user in list_person:
            if len(self.points) == len(room.number_person) and self.highest_score == user.points:
                user.chips += self.total_bank // self.number_of_wins
                print(f'Всего победителей - {self.number_of_wins}\n')

        self.total_bank = 0




