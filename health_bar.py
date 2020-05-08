import pygame
from pygame.sprite import Sprite

class HealthBar(Sprite):
    
    def __init__(self, a_s_game):
        super().__init__()
        self.screen = a_s_game.screen
        self.settings = a_s_game.settings
        self.screen_rect = a_s_game.screen.get_rect()

        
        # Load the image and get its rect
        self.image = pygame.image.load('images/health_bar.bmp')
        self.rect = self.image.get_rect()
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image, self.rect)
