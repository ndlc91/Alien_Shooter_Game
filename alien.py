import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    # A class to represent a single alien in the fleet

    def __init__(self, a_s_game):
        # Init the alien and set its starting point

        super().__init__()
        self.screen = a_s_game.screen
        self.settings = a_s_game.settings


        # Load the alien and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the mid right of the screen

        self.rect.x = (self.settings.screen_width - self.rect.width)
        self.rect.y = 0

        # Store the alien's exact vertical position
        self.y = float(self.rect.y)

    def check_edges(self):
        # Return True if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if self.rect.right < screen_rect.left:
            return True
            

    def update(self):
        # Move the alien across the screeen
        self.x -= self.settings.alien_speed
        self.rect.x = self.x

