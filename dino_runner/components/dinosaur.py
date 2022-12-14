import pygame

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DUCKING_SHIELD

RUN_IMG: list = [RUNNING[0], RUNNING[1]]
RUN_DUCK: list = [DUCKING[0], DUCKING[1]]
RUN_DUCK_SHILD = [DUCKING_SHIELD[0], DUCKING_SHIELD[1]]
X_POS: int = 80
Y_POS: int = 310
Y_POS_DUCK: int = 340
JUMP_VEL: float = 8.5

class Dinosaur:
    def __init__(self):
        self.image: list = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x: int = 0
        self.dino_rect.y: int = 0
        self.step_index: int = 0
        self.running: bool = False
        self.jump: bool = False
        self.jump_vel: float = JUMP_VEL
        self.dino_duck: bool = False
        self.dino_dick_shild: bool = False

    def update(self, user_input):
        if self.running:
             self.run()
        elif self.jump:
            self.dino_jump()
        elif self.dino_duck:
            self.duck()

        if user_input[pygame.K_UP] or user_input[pygame.K_SPACE] and not self.jump:
            self.running = False
            self.jump = True
        elif not self.jump:
            self.jump = False
            self.running = True

        if user_input[pygame.K_DOWN] or user_input[pygame.K_s]:#condition for dinosaur to duck
            self.running = False
            self.dino_duck = True

        if self.step_index >= 9:
           self.step_index = 0
        

    def run(self):
        if self.step_index < 5:
            self.image = RUN_IMG[0]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = X_POS
            self.dino_rect.y = Y_POS
        else:
            self.image = RUN_IMG[1]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = X_POS
            self.dino_rect.y = Y_POS
        
        self.step_index += 1

    def duck(self):
        if self.step_index < 5:
            self.image = RUN_DUCK[0]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = X_POS
            self.dino_rect.y = Y_POS_DUCK
        else:
            self.image = RUN_DUCK[1]
            self.dino_rect = self.image.get_rect()
            self.dino_rect.x = X_POS
            self.dino_rect.y = Y_POS_DUCK
        
        self.step_index += 1


    def dino_jump(self):
        self.image = JUMPING
        self.dino_rect.y -= self.jump_vel * 4
        self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            # self.dino_rect.y += self.jump_vel * 4
            # self.jump_vel += 1
            self.dino_rect.y = Y_POS
            self.jump = False
            self.jump_vel = JUMP_VEL
          

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
