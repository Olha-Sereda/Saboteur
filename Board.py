from flask import Flask, render_template, url_for

from Card import Card, PathCard, startPathCard, blank_card


class Board:
    def __init__(self):
        self.width = 9
        self.height = 5
        self.arr = [[0]]
        self.arr = [[blank_card]*self.width for i in range(self.height)]
        self.arr[2][0] = startPathCard

    def verifyCoords(self, coords: tuple):
        if coords[0] in range(self.height) and coords[1] in range(self.width):
            return True
        else:
            return False

    def matchPath(self, coords1: tuple, coords2: tuple, direction: int, card:PathCard):
        if direction == 0:
            self.opposite = 2
        if direction == 1:
            self.opposite = 3
        if direction == 2:
            self.opposite = 0
        if direction == 3:
            self.opposite = 1

        if card.entrances[direction] == 1 and self.arr[coords2[0]][coords2[1]].entrances[self.opposite]==1:
            return 1
        elif card.entrances[direction] == 0 and self.arr[coords2[0]][coords2[1]].entrances[self.opposite]==0:
            return 0
        else:
            return -1
    def verifyMove(self, card:PathCard, coords: tuple):
        self.coords = coords
        self.neighbourCards = 0
        self.count1 = 0
        if self.arr[coords[0]][coords[1]] != 0:
            return False
        if self.verifyCoords(coords)==False:
            return False
        if self.verifyCoords((coords[0]+1,coords[1])) and self.arr[coords[0]+1][coords[1]]!=0:
            self.neighbourCards = 1
            res = self.matchPath((coords[0], coords[1]), (coords[0] + 1, coords[1]), 0, card)
            if res == 1:
                self.count1+=1
            elif res == -1:
                return False

        if self.verifyCoords((coords[0]-1,coords[1])) and self.arr[coords[0]-1][coords[1]]==0:
            self.neighbourCards = 1
            res = self.matchPath((coords[0], coords[1]), (coords[0] - 1, coords[1]), 2, card)
            if res == 1:
                self.count1 += 1
            elif res == -1:
                return False
        if self.verifyCoords((coords[0],coords[1]+1)) and self.arr[coords[0]][coords[1]+1]==0:
            self.neighbourCards = 1
            res = self.matchPath((coords[0], coords[1]), (coords[0], coords[1]+1), 1, card)
            if res == 1:
                self.count1 += 1
            elif res == -1:
                return False
        if self.verifyCoords((coords[0],coords[1]-1)) and self.arr[coords[0]][coords[1]-1] == 0:
            self.neighbourCards = 1
            res = self.matchPath((coords[0], coords[1]), (coords[0], coords[1]-1), 3, card)
            if res == 1:
                self.count1 += 1
            elif res == -1:
                return False

        if self.neighbourCards == 0:
            return False
        if self.count1 == 0:
            return False

        self.arr[coords[0]][coords[1]] = card
        return True

    def get_board(self):
        return self.arr


