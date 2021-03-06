class GameStats:
    # Track stats for A_S

    def __init__(self, a_s_game):
        # Init statistics
        self.settings = a_s_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        # Init stats that can change during the game
        self.ships_left = self.settings.ship_limit
        self.ship_health = self.settings.ship_health
        self.score = 0