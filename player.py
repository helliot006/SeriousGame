import pygame

class Player:
    def __init__(self, vie, vitesse, pos):
        self.vie = vie 
        self.vitesse = vitesse 
        self.pos = pygame.Vector2(pos)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.pos, 40)