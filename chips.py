class Chips:
    def __init__(self, room=True):
        self.room = room
        self.total_bank = 0
        self.points = []
        self.highest_score = 0
        self.number_of_wins = 0
        self.max_bid = 0


    def highest_mark(self, point, room):
        self.points.append(point.points)
        if len(self.points) == len(room.number_person):
            self.highest_score = max(self.points)
            print(f'---Наивысший балл - {self.highest_score}---')

    def bid_check(self, user, list_users, happening=1):
        highest_bid = 0
        for playing in list_users:
            if playing.bid > highest_bid:
                highest_bid = playing.bid
        print(f'Наивысший балл - {highest_bid}')
        if happening == 0:
            return highest_bid
        if happening == 1:
            if highest_bid == user.bid:
                return True
        if happening == 2:
            if user.bid >= highest_bid:
                return True
        if happening == 3:
            if user.bid > highest_bid:
                return True



    def win_check(self, room, user):
        if self.highest_score == user.points:
            for value in self.points:
                if self.highest_score == value:
                    self.number_of_wins += 1
            user.chips += self.total_bank // self.number_of_wins
            print(f'Всего победителей - {self.number_of_wins}\n'
                  f'Фишки передаются игроку с наивысшим баллом - {self.highest_score}\n'
                  f'Количество фишек - {self.total_bank}')
        self.number_of_wins = 0


    def remove_values(self):
        self.highest_score = 0
        self.total_bank = 0
        self.number_of_wins = 0



    # def user_win(self, list_person, room):
    #     for value in self.points:
    #         if self.highest_score == value:
    #             self.number_of_wins += 1
    #
    #     for user in list_person:
    #         if len(self.points) == len(room.number_person) and self.highest_score == user.points:
    #             user.chips += self.total_bank // self.number_of_wins
    #             print(f'Всего победителей - {self.number_of_wins}\n')

        # self.total_bank = 0




