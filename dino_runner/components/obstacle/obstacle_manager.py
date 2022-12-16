from dino_runner.components.obstacle.cactus import Cactus, Large_Cactus
from dino_runner.components.obstacle.bird import Bird, Down_Bird
import random

class Obstacle_Manager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            select_obstacle = random.randint(1, 4)
            if select_obstacle == 1:
                self.obstacles.append(Cactus())
            elif select_obstacle == 2:
                self.obstacles.append(Bird())
            elif select_obstacle == 3:
                self.obstacles.append(Large_Cactus())
            elif select_obstacle == 4:
                self.obstacles.append(Down_Bird())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                game.death_count += 1
                self.obstacles.remove(obstacle)
        
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
          