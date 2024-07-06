import pygame

class Button:
    def __init__(self, image, x,y):
        self.image = image
        self.image = pygame.transform.scale(self.image , (50,50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def click(self):
        res = False
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                res = True
        return res