from constants import *
class Button:
    def __init__(self, image, x,y):
        self.image = image
        self.rect = self.image.get_rect(center=(x,y))
        self.clicked = False
        
        
    def draw(self):
        action = False
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                action = True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
            
        
                
        SCREEN.blit(self.image, self.rect)
        return action