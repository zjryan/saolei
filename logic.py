# -*- coding: utf-8 -*-
import pygame
import random
from copy import deepcopy
from init import (UNIT_WIDTH,
                  UNIT_HEIGHT,
                  unit_assets_map)


class Unit(object):

    def __init__(self, status):
        self.status = status
        self.clicked = False
        self.flagged = False
        self.error = False

    def __repr__(self):
        c = 'T' if self.clicked else 'F'
        f = '*' if self.flagged else '.'
        return str(self.status) + ' ' + c + ' ' + f

    def set_status(self, status):
        self.status = status

    def click(self):
        self.clicked = True

    def switch_flag(self):
        self.flagged = not self.flagged

    def set_error(self):
        self.error = True

    def get_status(self):
        return self.status

    def is_flagged(self):
        return self.flagged

    def is_error(self):
        return self.error

    def is_bomb(self):
        return self.status == 9

    @staticmethod
    def blit(unit, screen, x, y):
        draw_pos = (y * UNIT_WIDTH, x * UNIT_HEIGHT)

        if unit.is_error():
            asset = unit_assets_map['error']
        elif unit.is_flagged():
            asset = unit_assets_map['flag']
        elif not unit.clicked:
            asset = unit_assets_map['unclick']
        elif unit.is_bomb():
            asset = unit_assets_map['bomb']
        else:
            asset = unit_assets_map[unit.status]
        screen.blit(asset, draw_pos)


class Table(object):

    def __init__(self, table_size, bomb_num):
        assert isinstance(table_size, tuple) or \
               isinstance(table_size, list) and \
               len(table_size) == 2
        self.width, self.height = table_size
        assert self.width * self.height >= bomb_num
        self.table_square = [[Unit(0) for x in range(self.width)] for y in range(self.height)]
        self.drop_bomb(bomb_num)
        self.cal_square()
        self.is_game_lost = False
        self.is_game_win = False
        self.flag_num = bomb_num

    def __repr__(self):
        return '\n'.join([str(l) for l in self.table_square])

    def set_unit(self, x, y, status):
        self.table_square[x][y].set_status(status)

    def switch_flag(self, x, y):
        unit = self.table_square[y][x]
        if unit.clicked:
            return

        if unit.is_flagged():
            self.flag_num += 1
            unit.switch_flag()
        else:
            if self.flag_num > 0:
                self.flag_num -= 1
                unit.switch_flag()

    def drop_bomb(self, bomb_num):
        while bomb_num > 0:
            j = random.randint(0, self.width - 1)
            i = random.randint(0, self.height - 1)
            if self.table_square[i][j].get_status() == 9:
                continue
            else:
                self.set_unit(i, j, 9)
                bomb_num -= 1

    def game_lost(self):
        self.is_game_lost = True
        for row in self.table_square:
            for unit in row:
                if unit.is_bomb():
                    unit.click()
                if unit.is_flagged() and not unit.is_bomb():
                    unit.set_error()

    def game_win(self):
        if self.is_game_win:
            return self.is_game_win

        for row in self.table_square:
            for unit in row:
                if unit.is_bomb() and not unit.flagged:
                    return False
        self.is_game_win = True
        return True

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

    def click(self, x, y, pressed=True):
        if not 0 <= x < self.width or not 0 <= y < self.height:
            return
        unit = self.table_square[y][x]

        if pressed and unit.flagged:
            self.switch_flag(x, y)
            return

        if unit.flagged:
            return

        if not pressed and unit.is_bomb():
            return

        if unit.clicked:
            return
        unit.click()

        if pressed and unit.is_bomb():
            self.game_lost()
            return

        if unit.get_status() != 0:
            return
        else:
            # recurse
            self.click(x - 1, y, False)
            self.click(x + 1, y, False)
            self.click(x, y - 1, False)
            self.click(x, y + 1, False)

    def blit(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                unit = self.table_square[i][j]
                Unit.blit(unit, screen, i, j)
