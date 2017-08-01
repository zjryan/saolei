# -*- coding: utf-8 -*-
import pygame

from pygame.locals import *
from sys import exit
from init import game_init, game_exit
from utils import log


def main():
    screen = game_init()
    screen = pygame.display.get_surface()
    # game main loop
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                game_exit()

            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                log(pos)

        pygame.display.update()


if __name__ == '__main__':
    main()

