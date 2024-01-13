from random import shuffle

from flask import Flask, render_template, url_for

from Card import Card, PathCard, startPathCard, blank_card, cardList, finishCards, ActionCard, FinishCard, isinstanceCard


class Board:
    def __init__(self):
        self.start = None
        self.width = 9
        self.height = 5
        self.arr = [[0]]
        self.arr = [[blank_card] * self.width for i in range(self.height)]
        self.arr[2][0] = startPathCard
        currentFinishCards = finishCards.copy()
        shuffle(currentFinishCards)
        print(str(currentFinishCards[0].gold_card))
        print(str(currentFinishCards[1].gold_card))
        print(str(currentFinishCards[2].gold_card))
        self.arr[0][8] = currentFinishCards[0]
        self.arr[2][8] = currentFinishCards[1]
        self.arr[4][8] = currentFinishCards[2]

    def verifyCoords(self, coords: tuple):
        if coords[0] in range(self.height) and coords[1] in range(self.width):
            return True
        else:
            return False

    def matchPath(self, coords1: tuple, coords2: tuple, direction: int, card: PathCard):
        # matchPath(where we put card, neighbour, direction, what card we want to put on first coords)
        #if self.arr[coords2[0]][coords2[1]].finish_card == True and self.arr[coords2[0]][coords2[1]].gold_card == False:
         #   return 1

        if direction == 0:
            self.opposite = 2
        if direction == 1:
            self.opposite = 3
        if direction == 2:
            self.opposite = 0
        if direction == 3:
            self.opposite = 1
        self.start += str(self.opposite)+"\n"
        self.start += str(card.entrances) + "\n"
        self.start += str(self.arr[coords2[0]][coords2[1]].entrances[self.opposite]) + "\n"
        if card.entrances[direction] == 1 and self.arr[coords2[0]][coords2[1]].entrances[self.opposite] == 1:
            return 1
        elif card.entrances[direction] == 0 and self.arr[coords2[0]][coords2[1]].entrances[self.opposite] == 0:
            return 0
        else:
            return -1

    def verifyMove(self, card: PathCard, coords: tuple):
        #сard - карта, яку ми хочемо поставити, coords -  координати куди
        self.start = "Verify move getting started\n"
        self.neighbourCards = 0 #the number of neigbours, that has the place we want to put our card to
        count1 = 0 #the number of the card, that matchPath returned succesfully
        if self.arr[coords[0]][coords[1]] != blank_card:
            self.start += "Here already is a card \n"
            return False
        if self.verifyCoords(coords) == False:
            self.start += "Such coords does not exist \n"
            return False

        self.start += "Starting verifying neiboughrs \n"
        neighbour_directions = [(coords[0] - 1, coords[1]), (coords[0], coords[1] + 1), (coords[0] + 1, coords[1]), (coords[0], coords[1]-1)]
        for idx, direction in enumerate(neighbour_directions):
            if self.verifyCoords(direction) and self.arr[direction[0]][direction[1]] != blank_card:

                self.start += "Direction Y="+str(direction[0]) + "; X=" + str(direction[1]) + "\n"
                self.neighbourCards = 1
                self.start += "We have a first neighbour from the downside \n"
                if isinstanceCard(self.arr[direction[0]][direction[1]], "FinishCard"):
                    res = 1
                else:
                    res = self.matchPath((coords[0], coords[1]), direction, idx, card)
                self.start += "Res=" + str(res) + "\n"
                #matchPath(where we put card, neighbour, direction, what card we want to put on first coords)
                if res == 1:
                    count1 += 1
                elif res == -1:
                    return False

        self.start += "Finished verifying neibours \n"

        if self.neighbourCards == 0:
            return False
        if count1 == 0:
            return False

        return True

    def make_move(self,  card: PathCard, coords: tuple):
        self.arr[coords[0]][coords[1]] = card
        self.start += "Puting a new card \n"
        return True


    def get_board(self):
        #self.verifyMove(cardList[20], (2, 1))
        return self.arr, self.start


    def path_finder(self):
        far_cells = [(2, 0)]
        far_future_cells = [(2, 0)]
        arr_finder = [[0]]    #масив де ми ставимо одинички на тих клітинках до яких ми дісталися
        arr_finder = [[0] * self.width for i in range(self.height)]
        arr_finder[2][0] = 1
        is_gold_card = 0
        is_finish_card = 0
        print("Path_finder works")
        while len(far_future_cells) > 0:
            far_cells = far_future_cells #від цих клітинок ми робимо пошук на поточній операції
            far_future_cells = [] #збираємо клітинки для наступної ітерації
            print(str(far_cells))
            for cell in far_cells:
                cell_directions = [(cell[0] - 1, cell[1]), (cell[0], cell[1] + 1), (cell[0] + 1, cell[1]), (cell[0], cell[1]-1)]
                for idx, direction in enumerate(cell_directions):
                    if self.verifyCoords(direction):
                        if (isinstanceCard(self.arr[direction[0]][direction[1]], "FinishCard") and self.arr[cell[0]][cell[1]].entrances[idx] == 1
                                and arr_finder[direction[0]][direction[1]] == 0):
                            arr_finder[direction[0]][direction[1]] = 1
                            print("You found finish card!")
                            is_finish_card = 1
                            #Make PathCard from FinishCard
                            make_path_card = self.arr[direction[0]][direction[1]]
                            self.arr[direction[0]][direction[1]] =    PathCard( make_path_card.number,
                                                                                make_path_card.image_hidden,
                                                                                make_path_card.entrances, False,
                                                                                make_path_card.gold_card )
                            if self.arr[direction[0]][direction[1]].gold_card == True:
                                print("FOUND GOLD!")
                                is_gold_card = 1
                            else:
                                if self.matchPath(cell, direction, idx, self.arr[cell[0]][cell[1]]) == 1:
                                    arr_finder[direction[0]][direction[1]] = 1
                                    far_future_cells.append(direction)

                        elif (self.verifyCoords(direction) and self.arr[direction[0]][direction[1]] != blank_card and
                                self.arr[direction[0]][direction[1]].cuted == False and arr_finder[direction[0]][direction[1]] == 0):

                            arr_finder[direction[0]][direction[1]] = 1
                            far_future_cells.append(direction)
        #Show the board
        for finder in arr_finder:
            print(finder)
        ###############

        if is_gold_card == 1:
            return 2
        elif is_finish_card == 1:

            return 1
        else:
            return 0


    def close_finish_cards(self):
        for row in self.arr:
            for card in row:
                if isinstanceCard(card, "FinishCard"):
                    card.temporary_show = False


