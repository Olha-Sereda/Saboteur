
actionCardsType = ("ViewGold", "StoleCard", "BlockCard", "UnblockCard")
class Card:
    def __init__(self, number: int, image: str):
        self.number = number
        self.image = image


class ActionCard(Card):
    def __init__(self, number: int, image: str, type_card: str):
        self.type_card = type_card
        super().__init__(number, image)


class BlockCard(Card):
    def __init__(self, number: int, image: str, type_card: str, block_id: int):
        self.block_id = block_id
        self.type_card = type_card
        super().__init__(number, image)


class PathCard(Card):
    def __init__(self, number: int, image: str, entrances: tuple):
        self.entrances = entrances  # top, right, bottom, left
        self.alignment = True
        super().__init__(number, image)


class GoldCard(Card):
    def __init__(self, number: int, image: str, hidden: bool, entrances: tuple):
        self.hidden = hidden
        self.entrances = entrances
        super().__init__(number, image)


startPathCard = PathCard(0, "1111_full.png", (1, 1, 1, 1))

blank_card = PathCard(68, "blank_card", (0, 0, 0, 0))

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

actionCard41 = ActionCard(41, "map.png", actionCardsType[0])
actionCard42 = ActionCard(42, "map.png", actionCardsType[0])
actionCard43 = ActionCard(43, "map.png", actionCardsType[0])
actionCard44 = ActionCard(44, "map.png", actionCardsType[0])
actionCard45 = ActionCard(45, "map.png", actionCardsType[0])
actionCard46 = ActionCard(46, "map.png", actionCardsType[0])

actionCard47 = ActionCard(47, "stole_card.png", actionCardsType[1])
actionCard48 = ActionCard(48, "stole_card.png", actionCardsType[1])
actionCard49 = ActionCard(49, "stole_card.png", actionCardsType[1])

blockCard50 = BlockCard(50, "blockcard_hammer.png", actionCardsType[2], 1)
unblockCard51 = BlockCard(51, "unblockcard_hammer.png", actionCardsType[3], 1)
blockCard52 = BlockCard(52, "blockcard_hammer.png", actionCardsType[2], 1)
unblockCard53 = BlockCard(53, "unblockcard_hammer.png", actionCardsType[3], 1)
blockCard54 = BlockCard(54, "blockcard_hammer.png", actionCardsType[2], 1)
unblockCard55 = BlockCard(55, "unblockcard_hammer.png", actionCardsType[3], 1)

blockCard56 = BlockCard(56, "blockcard_lamp.png", actionCardsType[2], 2)
unblockCard57 = BlockCard(57, "unblockcard_lamp.png", actionCardsType[3], 2)
blockCard58 = BlockCard(58, "blockcard_lamp.png", actionCardsType[2], 2)
unblockCard59 = BlockCard(59, "unblockcard_lamp.png", actionCardsType[3], 2)
blockCard60 = BlockCard(60, "blockcard_lamp.png", actionCardsType[2], 2)
unblockCard61 = BlockCard(61, "unblockcard_lamp.png", actionCardsType[3], 2)

blockCard62 = BlockCard(62, "blockcard_wagon.png", actionCardsType[2], 3)
unblockCard63 = BlockCard(63, "unblockcard_wagon.png", actionCardsType[3], 3)
blockCard64 = BlockCard(64, "blockcard_wagon.png", actionCardsType[2], 3)
unblockCard65 = BlockCard(65, "unblockcard_wagon.png", actionCardsType[3], 3)
blockCard66 = BlockCard(66, "blockcard_wagon.png", actionCardsType[2], 3)
unblockCard67 = BlockCard(67, "unblockcard_wagon.png", actionCardsType[3], 3)


cardList = [pathCard1, pathCard2, pathCard3, pathCard4, pathCard5, pathCard6, pathCard7, pathCard8,
            pathCard9, pathCard10, pathCard11, pathCard12, pathCard13, pathCard14, pathCard15, pathCard16,
            pathCard17, pathCard18, pathCard19, pathCard20, pathCard21, pathCard22, pathCard23, pathCard24, pathCard25,
            pathCard26, pathCard27, pathCard28, pathCard29, pathCard30, pathCard31, pathCard32, pathCard33,
            pathCard34, pathCard35, pathCard36, pathCard37, pathCard38, pathCard39, pathCard40]

