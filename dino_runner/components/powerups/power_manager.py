import pygame
import random
from dino_runner.components.powerups.shild import Shild

class Power_Up_manager():
    def __init__(self):
        self.power_ups  = []
        self.when_apears = 0


    def generate_powe(self, score):
        if len(self.power_ups) == 0 and self.when_apears == score:
            self.when_apears += random.randint(200, 300)
            self.power_ups.append(Shild())


    def update(self, score, game_speed, player):
        for power_up  in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_ract.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.image_type = power_up.power_type
                player.has_power_uo = False
                player.shield = True
                player.shield_time_up = power_up.start_time + (power_up.duraction *100)
                self.power_ups.remove(power_up)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)


    def reset(self):
        self.power_ups = []
        self.when_apears = random.randint(200, 300)