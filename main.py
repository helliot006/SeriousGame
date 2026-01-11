import pygame
from sys import exit

from player import Player
from enemy import Enemy

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 1280))
        self.clock = pygame.time.Clock()


    def run(self):
        player_start_pos = self.screen.get_width() / 2, self.screen.get_height() / 2
        self.player = Player(5, 3, player_start_pos)
        enemy_start_pos = self.screen.get_width() / 3, self.screen.get_height() / 2
        self.enemy = Enemy(1, 2, enemy_start_pos)

        while True:
            self.handle_events()
            self.update_sprites()
            self.update_screen()
            self.clock.tick(60)
        pygame.quit()

    def update_screen(self):
        self.screen.fill("white")
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_z]:
            self.player.pos.y -= 1
        if keys[pygame.K_s]:
            self.player.pos.y += 1
        if keys[pygame.K_q]:
            self.player.pos.x -= 1
        if keys[pygame.K_d]:
            self.player.pos.x += 1

    def update_sprites(self):
        pass


main = Main()
main.run()














    



        