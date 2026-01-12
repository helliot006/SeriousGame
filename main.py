import pygame as pg

from settings import *
from inputs import Inputs
from game import Game

pg.init()
pg.font.init()

screen = pg.display.set_mode(WIN_SIZE)
clock = pg.time.Clock()
inputs = Inputs()

game = Game(screen, clock, inputs)
game.run()














    



        