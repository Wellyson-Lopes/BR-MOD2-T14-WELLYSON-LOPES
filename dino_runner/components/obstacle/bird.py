
import time
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.obstacle.obstacle import Obstacle

class Bird(Obstacle):

    def __init__(self):
        super().__init__(BIRD[0])
        self.step_index = 0
        self.rect.y = 230
        self.image = BIRD

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5],  self.rect)
        self.step_index += 1
        if self.step_index >= 9:
            self.step_index = 0
           

class Down_Bird(Obstacle):

    def __init__(self):
        super().__init__(BIRD[0])
        self.step_index = 0
        self.rect.y = 260
        self.image = BIRD

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5],  self.rect)
        self.step_index += 1
        if self.step_index >= 9:
            self.step_index = 0
           