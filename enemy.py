import pygame

class Enemy:
    def __init__(self, vie, vitesse, pos):
        self.vie = vie 
        self.vitesse = vitesse 
        self.pos = pygame.Vector2(pos)

    def draw(self, screen):
        pygame.draw.circle(screen, "blue", self.pos, 40)