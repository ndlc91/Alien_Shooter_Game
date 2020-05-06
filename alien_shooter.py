import sys
from time import sleep

import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from random import randint

class AlienShooter: 

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("Alien Shooter")

        # Create an instance to store game statistics
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Set the background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        # Start the main loop for the game
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
                
    
    def _check_events(self):
        # Respond to keypresses and mouse events
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        # Respond to keypresses

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        # Respond to key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        # Create a new bullet and add it to the bullets group
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        # Create a fleet of aliens
        # Make an alien and find the number of aliens in a row
        # Spacing between each alien is equal to one alien width

        alien = Alien(self)

        # Determine the number of rows of aliens that fit on the screen

        fleet_size = self.settings.fleet_size
        alien_spawnpoint_x = self.settings.screen_width

        # Create the full fleet of aliens
        for alien in range(fleet_size):
            alien_spawnpoint_x = alien_spawnpoint_x + 600
            self._create_alien(alien_spawnpoint_x)


    def _create_alien(self, alien_spawnpoint_x):
        # Create an alien and place it in the row
        alien = Alien(self)
        alien_height = alien.rect.height
        alien.rect.y = randint(alien_height, self.settings.screen_height - alien_height)
        alien.y = alien.rect.y
        alien.x = alien_spawnpoint_x
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        # Respond appropriately if any aliens have reached the edge

        for alien in self.aliens.sprites():
            if alien.check_edges():
                alien.remove()

                #### Remove the ship from the fleet

    def _ship_hit(self):
        # Respond to the ship being hit by an alien

        # Decrement ships left
        self.stats.ships_left -= 1
                    

    
    def _update_aliens(self):
        # Update the positions of all aliens in the fleet
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
                self.aliens.remove(self.aliens)
                    


                        
    def _update_bullets(self):
        # Update position of bullets and get rid of old bullets
        # Update bullet positions
        self.bullets.update()

        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        # Respond to bullet alien collisions
        # Remove any bullets and aliens that have collided

        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()


    
    def _update_screen(self):
        # Update images on the screen and flip to the new screen
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet() 
            
            self.aliens.draw(self.screen)

            pygame.display.flip()




if __name__ == '__main__':
    # Make a game instance, and run the game
    a_s = AlienShooter()
    a_s.run_game()