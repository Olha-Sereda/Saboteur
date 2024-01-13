from Card import Card

class Player:
    def __init__(self, nickname: str):
        self.nickname = nickname
        self.flag_lamp = False
        self.flag_truck = False
        self.flag_hammer = False
        self.move_is_ended = False
        self.card_in_hands = []

    def add_lamp(self):
        self.flag_lamp = True

    def add_truck(self):
        self.flag_truck = True

    def add_hammer(self):
        self.flag_hammer = True

    def del_lamp(self):
        self.flag_lamp = not self.flag_lamp

    def del_truck(self):
        self.flag_truck = not self.flag_truck

    def del_hammer(self):
        self.flag_hammer = not self.flag_hammer



