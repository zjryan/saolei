# -*- coding: utf-8 -*-
import pygame

from pygame.locals import *
from init import (game_init,
                  game_exit,
                  TABLE_SIZE,
                  BOMB_NUM,)
from logic import Table
from utils import log


def main():
    game_init()
    screen = pygame.display.get_surface()
    table = Table(TABLE_SIZE, BOMB_NUM)
    # game main loop
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                game_exit()
            if table.is_game_lost or table.is_game_win:
                break

            if event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                left, mid, right = pygame.mouse.get_pressed()
                x //= 30
                y //= 30
                if mid:
                    continue
                if left:
                    table.click(x, y)
                if right:
                    table.switch_flag(x, y)

                if table.game_win():
                    print 'you win'
                if table.is_game_lost:
                    print 'you lost'

        table.blit(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()

