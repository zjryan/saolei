# -*- coding: utf-8 -*-
import pygame
import random
from copy import deepcopy


UNIT_WIDTH = 20
UNIT_HEIGHT = 20


class Unit(object):

    def __init__(self, status):
        self.status = status
        self.clicked = False

    def __repr__(self):
        c = 'T' if self.clicked else 'F'
        return str(self.status) + ' ' + c

    def set_status(self, status):
        self.status = status

    def click(self):
        self.clicked = True

    def get_status(self):
        return self.status

    def is_bomb(self):
        return self.status == 9

    @staticmethod
    def blit(unit, screen, x, y):
        if unit.clicked:
            pass
        else:
            pass


class Table(object):

    def __init__(self, table_size, bomb_num):
        assert isinstance(table_size, tuple) or \
               isinstance(table_size, list) and \
               len(table_size) == 2
        self.width, self.height = table_size
        self.table_square = [[Unit(0) for x in range(self.width)] for y in range(self.height)]
        self.drop_bomb(bomb_num)
        self.cal_square()

    def __repr__(self):
        return '\n'.join([str(l) for l in self.table_square])

    def set_unit(self, x, y, status):
        self.table_square[x][y].set_status(status)

    def drop_bomb(self, bomb_num):
        while bomb_num > 0:
            j = random.randint(0, self.width - 1)
            i = random.randint(0, self.height - 1)
            if self.table_square[i][j].get_status() == 9:
                continue
            else:
                self.set_unit(i, j, 9)
                bomb_num -= 1

    def cal_square(self):
        aux_table = deepcopy(self.table_square)
        for row in aux_table:
            row.insert(0, Unit(0))
            row.append(Unit(0))
        aux_row = [Unit(0) for i in range(self.width + 2)]
        aux_table.append(aux_row)
        aux_table.insert(0, aux_row)

        for i in range(1, self.height + 1):
            for j in range(1, self.width + 1):
                if aux_table[i][j].get_status() == 9:
                    continue

                status = 0
                if aux_table[i - 1][j - 1].is_bomb():
                    status += 1
                if aux_table[i - 1][j].is_bomb():
                    status += 1
                if aux_table[i - 1][j + 1].is_bomb():
                    status += 1
                if aux_table[i][j - 1].is_bomb():
                    status += 1
                if aux_table[i][j + 1].is_bomb():
                    status += 1
                if aux_table[i + 1][j - 1].is_bomb():
                    status += 1
                if aux_table[i + 1][j].is_bomb():
                    status += 1
                if aux_table[i + 1][j + 1].is_bomb():
                    status += 1

                aux_table[i][j].set_status(status)

        for i in range(1, self.height + 1):
            self.table_square[i - 1] = aux_table[i][1: -1]
            print self.table_square[i - 1]

    def click(self, x, y, pressed=True):
        if not 0 <= x < self.width or not 0 <= y < self.height:
            return
        unit = self.table_square[y][x]

        if not pressed and unit.is_bomb():
            return

        if unit.clicked:
            return
        unit.click()

        if pressed and unit.is_bomb():
            print 'you lost'
            return

        # recurse
        self.click(x - 1, y, False)
        self.click(x + 1, y, False)
        self.click(x, y - 1, False)
        self.click(x, y + 1, False)





