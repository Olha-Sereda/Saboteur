
actionCardType = ("ViewGold", "StoleCard")
blockCardType = ("Hammer", "Lamp", "Wagon")

class Card:
    def __init__(self, number: int, image: str):
        self.number = number
        self.image = image


class ActionCard(Card):
    def __init__(self, number: int, image: str, type_card: str):
        self.type_card = type_card
        super().__init__(number, image)


class BlockCard(Card):
    def __init__(self, number: int, image: str, type_card: str, block: bool):
        self.block = block
        self.type_card = type_card
        super().__init__(number, image)


class PathCard(Card):
    def __init__(self, number: int, image: str, entrances: tuple):
        self.entrances = entrances  # top, right, bottom, left
        self.rotated = False
        super().__init__(number, image)

    def rotate(self):
        self.rotated = not self.rotated
        new_entrances = (self.entrances[2],self.entrances[3],self.entrances[0],self.entrances[1])
        self.entrances = new_entrances


class FinishCard(PathCard):
    def __init__(self, number: int, image: str, image_hidden: str, entrances: tuple):
        self.hidden = True
        self.image_hidden = image_hidden
        super().__init__(number, image, entrances)

    def switch_images(self):
        self.image, self.image_hidden = self.image_hidden, self.image
        return True


startPathCard = PathCard(0, "1111_full.png", (1, 1, 1, 1))

blank_card = PathCard(68, "blank_card.png", (0, 0, 0, 0))

finishCard0 = FinishCard(72, "finishblankcard.png", "1111_finish_card_gold.png", (1, 1, 1, 1))
finishCard1 = FinishCard(73, "finishblankcard.png", "0110_finish_card_stone.png", (0, 1, 1, 0))
finishCard2 = FinishCard(74, "finishblankcard.png", "0011_finish_card_stone2.png",  (0, 0, 1, 1))

pathCard1 = PathCard(1, "1010_full.png", (1, 0, 1, 0))
pathCard2 = PathCard(2, "1010_full.png", (1, 0, 1, 0))
pathCard3 = PathCard(3, "1010_full.png", (1, 0, 1, 0))
pathCard4 = PathCard(4, "1010_full.png", (1, 0, 1, 0))

pathCard5 = PathCard(5, "1110_full.png", (1, 1, 1, 0))
pathCard6 = PathCard(6, "1110_full.png", (1, 1, 1, 0))
pathCard7 = PathCard(7, "1110_full.png", (1, 1, 1, 0))
pathCard8 = PathCard(8, "1110_full.png", (1, 1, 1, 0))
pathCard9 = PathCard(9, "1110_full.png", (1, 1, 1, 0))

pathCard10 = PathCard(10, "1111_full.png", (1, 1, 1, 1))
pathCard11 = PathCard(11, "1111_full.png", (1, 1, 1, 1))
pathCard12 = PathCard(12, "1111_full.png", (1, 1, 1, 1))
pathCard13 = PathCard(13, "1111_full.png", (1, 1, 1, 1))
pathCard14 = PathCard(14, "1111_full.png", (1, 1, 1, 1))

pathCard15 = PathCard(15, "1101_full.png", (1, 1, 0, 1))
pathCard16 = PathCard(16, "1101_full.png", (1, 1, 0, 1))
pathCard17 = PathCard(17, "1101_full.png", (1, 1, 0, 1))
pathCard18 = PathCard(18, "1101_full.png", (1, 1, 0, 1))
pathCard19 = PathCard(19, "1101_full.png", (1, 1, 0, 1))

pathCard20 = PathCard(20, "0101_full.png", (0, 1, 0, 1))
pathCard21 = PathCard(21, "0101_full.png", (0, 1, 0, 1))
pathCard22 = PathCard(22, "0101_full.png", (0, 1, 0, 1))

pathCard23 = PathCard(23, "0110_full.png", (0, 1, 1, 0))
pathCard24 = PathCard(24, "0110_full.png", (0, 1, 1, 0))
pathCard25 = PathCard(25, "0110_full.png", (0, 1, 1, 0))
pathCard26 = PathCard(26, "0110_full.png", (0, 1, 1, 0))

pathCard27 = PathCard(27, "1100_full.png", (1, 1, 0, 0))
pathCard28 = PathCard(28, "1100_full.png", (1, 1, 0, 0))
pathCard29 = PathCard(29, "1100_full.png", (1, 1, 0, 0))
pathCard30 = PathCard(30, "1100_full.png", (1, 1, 0, 0))
pathCard31 = PathCard(31, "1100_full.png", (1, 1, 0, 0))

pathCard32 = PathCard(32, "0100_cuted.png", (0, 1, 0, 0))

pathCard33 = PathCard(33, "1010_cuted.png", (1, 0, 1, 0))

pathCard34 = PathCard(34, "1100_cuted.png", (1, 1, 0, 0))

pathCard35 = PathCard(35, "1111_cuted.png", (1, 1, 1, 1))

pathCard36 = PathCard(36, "1101_cuted.png", (1, 1, 0, 1))

pathCard37 = PathCard(37, "0101_cuted.png", (0, 1, 0, 1))

pathCard38 = PathCard(38, "0110_cuted.png", (0, 1, 1, 0))

pathCard39 = PathCard(39, "1100_cuted.png", (1, 1, 0, 0))

pathCard40 = PathCard(40, "1000_cuted.png", (1, 0, 0, 0))

actionCard41 = ActionCard(41, "map.png", actionCardType[0])
actionCard42 = ActionCard(42, "map.png", actionCardType[0])
actionCard43 = ActionCard(43, "map.png", actionCardType[0])
actionCard44 = ActionCard(44, "map.png", actionCardType[0])
actionCard45 = ActionCard(45, "map.png", actionCardType[0])
actionCard46 = ActionCard(46, "map.png", actionCardType[0])

actionCard47 = ActionCard(47, "stole_card.png", actionCardType[1])
actionCard48 = ActionCard(48, "stole_card.png", actionCardType[1])
actionCard49 = ActionCard(49, "stole_card.png", actionCardType[1])

blockCard50 = BlockCard(50, "blockcard_hammer.png", blockCardType[0], True)
unblockCard51 = BlockCard(51, "unblockcard_hammer.png", blockCardType[0], False)
blockCard52 = BlockCard(52, "blockcard_hammer.png", blockCardType[0], True)
unblockCard53 = BlockCard(53, "unblockcard_hammer.png", blockCardType[0], False)
blockCard54 = BlockCard(54, "blockcard_hammer.png", blockCardType[0], True)
unblockCard55 = BlockCard(55, "unblockcard_hammer.png", blockCardType[0], False)

blockCard56 = BlockCard(56, "blockcard_lamp.png", blockCardType[1], True)
unblockCard57 = BlockCard(57, "unblockcard_lamp.png", blockCardType[1], False)
blockCard58 = BlockCard(58, "blockcard_lamp.png", blockCardType[1], True)
unblockCard59 = BlockCard(59, "unblockcard_lamp.png", blockCardType[1], False)
blockCard60 = BlockCard(60, "blockcard_lamp.png", blockCardType[1], True)
unblockCard61 = BlockCard(61, "unblockcard_lamp.png", blockCardType[1], False)

blockCard62 = BlockCard(62, "blockcard_wagon.png", blockCardType[2], True)
unblockCard63 = BlockCard(63, "unblockcard_wagon.png", blockCardType[2], False)
blockCard64 = BlockCard(64, "blockcard_wagon.png", blockCardType[2], True)
unblockCard65 = BlockCard(65, "unblockcard_wagon.png", blockCardType[2], False)
blockCard66 = BlockCard(66, "blockcard_wagon.png", blockCardType[2], True)
unblockCard67 = BlockCard(67, "unblockcard_wagon.png", blockCardType[2], False)


cardList = [startPathCard, pathCard1, pathCard2, pathCard3, pathCard4, pathCard5, pathCard6, pathCard7,
            pathCard8, pathCard9, pathCard10, pathCard11, pathCard12, pathCard13, pathCard14, pathCard15, pathCard16,
            pathCard17, pathCard18, pathCard19, pathCard20, pathCard21, pathCard22, pathCard23, pathCard24, pathCard25,
            pathCard26, pathCard27, pathCard28, pathCard29, pathCard30, pathCard31, pathCard32, pathCard33,
            pathCard34, pathCard35, pathCard36, pathCard37, pathCard38, pathCard39, pathCard40, actionCard41,
            actionCard42, actionCard43, actionCard44, actionCard45, actionCard46, actionCard47, actionCard48,
            actionCard49, blockCard50, unblockCard51, blockCard52, unblockCard53, blockCard54, unblockCard55,
            blockCard56, unblockCard57, blockCard58, unblockCard59, blockCard60, unblockCard61, blockCard62,
            unblockCard63, blockCard64, unblockCard65, blockCard66, unblockCard67]

finishCards = [finishCard0, finishCard1, finishCard2]