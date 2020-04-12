import pygame


class Ship():
    def __init__(self, ai_setting, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_setting = ai_setting
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/kissbmp.bmp')
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        self.center = float(self.rect.centerx)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_setting.ship_speed_factor

    def blitme(self):
        self.screen.blit(self.image, self.rect)
