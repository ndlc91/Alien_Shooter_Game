import pygame.font
from pygame.sprite import Group

from ship import Ship
from health_bar import HealthBar

class Scoreboard:
    # A class to report scoring information

    def __init__(self, a_s_game):
        # Init scorekeeping attributes

        self.a_s_game = a_s_game
        self.screen = a_s_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = a_s_game.settings
        self.stats = a_s_game.stats

        # Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image
        self.prep_score()
        self.prep_ships()
        self.prep_health()

    def prep_score(self):
        # Turn the score into a rendered image
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_ships(self):
        # Show how many ships are left
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            print("ship added")
            ship = Ship(self.a_s_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_health(self):
        self.healths = Group()
        for health_left in range(self.stats.ship_health):
            print("health added")
            health = HealthBar(self.a_s_game)
            health.rect.x = 10 + health_left * health.rect.width
            health.rect.y = 80
            self.healths.add(health)

    def show_score(self):
        # Draw the score to the screen
        self.screen.blit(self.score_image, self.score_rect)
        self.healths.draw(self.screen)
        self.ships.draw(self.screen)

