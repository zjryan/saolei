# -*- coding: utf-8 -*-
import pygame

from pygame.locals import *
from sys import exit
from init import game_init
from utils import log


def main():
    game_init()

    # game main loop
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

            if event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                log(pos)


if __name__ == '__main__':
    main()

