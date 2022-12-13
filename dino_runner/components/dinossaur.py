import pygame

from dino_runner.utils.constants import RUNNING

RUN_IMG = [RUNNING[0], RUNNING[1]]

class Dinossaur:
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.x_pos_dino = 0
        self.y_pos_dino = 0


    def run (self):
        self.step_index = 0
        if self.step_index < 5:
            self.image  = RUN_IMG[0]
            self.dino_rect.x = 80
            self.dino_rect.y = 310
        else:
            self.image  = RUN_IMG[1]
            self.dino_rect.x = 80
            self.dino_rect.y = 310            
        self.step_index += 1

    def update(self):
        self.run()
        if self.step_index >= 9:
            self.step_index = 0

    
    def draw (self, screen):
        screen.blit(self.image, ())
