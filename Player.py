class Player:
    def __init__(self, nickname: str):
        self.nickname = nickname
        self.flag_lamp = 0
        self.flag_truck = 0
        self.flag_hammer = 0
        self.card_in_hands = []

    def add_lamp(self):
        self.flag_lamp += 1


    def add_truck(self):
        self.flag_truck += 1


    def add_hammer(self):
        self.flag_hammer += 1


    def del_lamp(self):
        if self.flag_lamp > 0:
            self.flag_lamp -= 1
            return True
        return False


    def del_truck(self):
        if self.flag_truck > 0:
            self.flag_truck -= 1
            return True
        return False
    def del_hammer(self):
        if self.flag_truck > 0:
            self.flag_truck -= 1
            return True
        return False
