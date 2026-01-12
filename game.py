import pygame as pg

from settings import *
from player import Player

class Game:
	def __init__(self, screen, clock, inputs):
		self.screen = screen
		self.clock = clock
		self.inputs = inputs

		self.player = Player()

	def run(self):
		while not self.inputs.quit:
			self.inputs.update()
			self.update_sprites()
			self.update_screen()
			self.clock.tick(MAX_FPS)

	def update_screen(self):
		self.screen.fill((0,0,0))
		self.player.draw(self.screen)
		pg.display.flip()

	def update_sprites(self):
		self.player.update(self.inputs)


if __name__ == "__main__":
	import main