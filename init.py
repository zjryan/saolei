# -*- coding: utf-8 -*-
import pygame
import os

from pygame.locals import *
from sys import exit


UNIT_WIDTH = 30
UNIT_HEIGHT = 30

UNIT_WIDTH_NUM = 20
UNIT_HEIGHT_NUM = 20
TABLE_SIZE = (UNIT_WIDTH_NUM, UNIT_HEIGHT_NUM)
BOMB_NUM = 100

SCREEN_WIDTH = UNIT_WIDTH * UNIT_WIDTH_NUM
SCREEN_HEIGHT = UNIT_HEIGHT * UNIT_HEIGHT_NUM
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_CAPTION = 'SaoLei'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

unit_assets_map = {
}


def game_init():
    pygame.init()
    pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(SCREEN_CAPTION)
    for i in range(0, 9):
        path = os.path.join(ASSETS_DIR, str(i) + '.jpg')
        unit_assets_map[i] = pygame.image.load(path).convert()
    bomb_img_path = os.path.join(ASSETS_DIR, 'bomb.jpg')
    unit_assets_map['bomb'] = pygame.image.load(bomb_img_path).convert()
    unclick_img_path = os.path.join(ASSETS_DIR, 'unclick.jpg')
    unit_assets_map['unclick'] = pygame.image.load(unclick_img_path).convert()
    flag_img_path = os.path.join(ASSETS_DIR, 'flag.jpg')
    unit_assets_map['flag'] = pygame.image.load(flag_img_path).convert()
    error_img_path = os.path.join(ASSETS_DIR, 'error.jpg')
    unit_assets_map['error'] = pygame.image.load(error_img_path).convert()


def game_exit():
    exit()
