from Card import Card
from Stat import Stat

PlayerRole = ("Dwarf", "Saboteur")
Roles =    {
            3: [PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[1]],
            4:  [PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[1]],
            5:  [PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[1], PlayerRole[1]],
            6:  [PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[1], PlayerRole[1]],
            7:  [PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[1], PlayerRole[1], PlayerRole[1]],
            8:  [PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[1], PlayerRole[1], PlayerRole[1]],
            9:  [PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[1], PlayerRole[1], PlayerRole[1]],
            10: [PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[0], PlayerRole[1], PlayerRole[1], PlayerRole[1]]
             }

class Player:
    def __init__(self, nickname: str, role: PlayerRole):
        self.nickname:str = nickname
        self.flag_lamp: bool = False
        self.flag_truck: bool = False
        self.flag_hammer: bool = False
        self.move_is_ended: bool = False
        self.card_in_hands = []
        self.playerRole = role
        self.playerStat = Stat()

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



