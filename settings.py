

class Settings:

    def __init__(self):
        # Init the game's settings

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 8
        self.ship_limit = 3
        self.ship_health = 3

        # Bullet settings
        self.bullet_speed = 20.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 8.0
        self.fleet_size = 30
        self.alien_points = 50

        # How quickly the game speeds up
        self.speedup_scale = 1.1


        