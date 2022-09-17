import random
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH

class Power_Up(Sprite):
    def __init__(self, imagen, type):
        self.image = imagen
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(125, 175)

        self.star_time = 0
        self.width = self.image.get_width()

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)