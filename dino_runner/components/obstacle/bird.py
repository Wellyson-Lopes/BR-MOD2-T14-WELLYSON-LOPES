import random

from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.obstacle.obstacle import Obstacle

RUN_BIRD = [
    (BIRD, 220)
]

class Bird(Obstacle):

    def __init__(self):
        image, byrd_y_pos = RUN_BIRD[0]
        super().__init__(image[0])
        self.rect.y = byrd_y_pos
         
DOWN_BIRD = [
    (BIRD, 250)
]

class Down_Bird(Obstacle):

    def __init__(self):
        image, byrd_y_pos = DOWN_BIRD[0]
        super().__init__(image[1])
        self.rect.y = byrd_y_pos
         