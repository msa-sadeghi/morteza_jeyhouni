import pygame

class HealthBar:
    def __init__(self, x,y, health, max_health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health
        
        
    def update(self,screen, health):
        ratio = health/self.max_health
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 100, 20))
        pygame.draw.rect(screen, (0,0,255), (self.x, self.y, 100 * ratio, 20))
    