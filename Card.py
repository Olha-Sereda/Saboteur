class Card:
    def __init__(self, number: int):
        self.number = number

class ActionCard(Card):
    def __init__(self, type_card: str, number: int):
        self.type_card = type_card
        super().__init__(self, number)

class PathCard(Card):
    def __init__(self, number: int, entrances: tuple):
        self.entrances=entrances  #top, right, bottom, left
        self.aligment=True
        super().__init__(self, number)

class GoldCard(Card):
    def __init__(self, number: int, hidden: bool, entrances: tuple):
        self.hidden=hidden
        self.entrances=entrances
        super().__init__(self, number)

pathCard2 = PathCard(1,(1,0,1,0))
pathCard2 = PathCard(2,(1,0,1,0))
pathCard2 = PathCard(3,(1,0,1,0))
pathCard2 = PathCard(4,(1,0,1,0))

pathCard1 = PathCard(5, (1,1,1,0))
pathCard1 = PathCard(6, (1,1,1,0))
pathCard1 = PathCard(7, (1,1,1,0))
pathCard1 = PathCard(8, (1,1,1,0))
pathCard1 = PathCard(9, (1,1,1,0))

pathCard1 = PathCard(10, (1,1,1,1))
pathCard1 = PathCard(11, (1,1,1,1))
pathCard1 = PathCard(12, (1,1,1,1))
pathCard1 = PathCard(13, (1,1,1,1))
pathCard1 = PathCard(14, (1,1,1,1))

pathCard1 = PathCard(5, (1,1,0,1))
pathCard1 = PathCard(5, (1,1,0,1))
pathCard1 = PathCard(5, (1,1,0,1))
pathCard1 = PathCard(5, (1,1,0,1))
pathCard1 = PathCard(5, (1,1,0,1))

pathCard1 = PathCard(5, (0,1,0,1))
pathCard1 = PathCard(5, (0,1,0,1))
pathCard1 = PathCard(5, (0,1,0,1))

pathCard1 = PathCard(5, (0,1,1,0))
pathCard1 = PathCard(5, (0,1,1,0))
pathCard1 = PathCard(5, (0,1,1,0))
pathCard1 = PathCard(5, (0,1,1,0))

pathCard1 = PathCard(5, (0,0,1,1))
pathCard1 = PathCard(5, (0,0,1,1))
pathCard1 = PathCard(5, (0,0,1,1))
pathCard1 = PathCard(5, (0,0,1,1))
pathCard1 = PathCard(5, (0,0,1,1))

pathCard1 = PathCard(5, (0,0,1,0))

pathCard1 = PathCard(5, (1,0,1,0))

pathCard1 = PathCard(5, (1,1,0,0))

pathCard1 = PathCard(5, (1,1,1,1))

pathCard1 = PathCard(5, (1,1,0,1))

pathCard1 = PathCard(5, (0,1,0,1))

pathCard1 = PathCard(5, (0,1,1,0))

pathCard1 = PathCard(5, (0,0,1,1))

pathCard1 = PathCard(5, (0,0,0,1))
