import pygame as pg

from settings import *

class Player:
    def __init__(self):
        self.hitbox = pg.Rect(0, 0, PLAYER_WIDTH, PLAYER_WIDTH)
        self.hitbox.center = (WIN_SIZE[0]/2, WIN_SIZE[1])

    def draw(self, screen):
        pg.draw.rect(screen, "red", self.hitbox)

    def update(self, inputs):
        if inputs.keys["left"].pressed: self.hitbox.x -= PLAYER_SPEED
        if inputs.keys["right"].pressed: self.hitbox.x += PLAYER_SPEED
        if inputs.keys["up"].pressed: self.hitbox.y -= PLAYER_SPEED
        if inputs.keys["down"].pressed: self.hitbox.y += PLAYER_SPEED