# -*- coding: utf-8 -*-
import pygame
import os

from pygame.locals import *
from sys import exit


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_CAPTION = 'SaoLei'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')

bg_img_path = os.path.join(ASSETS_DIR, 'saolei.png')


def game_init():
    pygame.init()
    pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption(SCREEN_CAPTION)


def game_exit():
    exit()
