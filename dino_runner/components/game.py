import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, HEART, RUNNING, SMALL_CACTUS
from dino_runner.components.dinossaur import Dinossaur

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        #self.x_pos_cactus = 1100
        #self.y_pos_cactus = 320
        #self.player_gravity = 0
        self.player = Dinossaur()
    

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #if self.player_rect.collidepoint(event.pos):
                    #print("Colisão")
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_SPACE:
                    #self.player_gravity = -200

    def update(self):
       self.player.update()


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) # "#FFFFFF"
        self.draw_background()
        self.player()
        self.small_cactus()
        pygame.display.update()
        pygame.display.flip()


    #def player(self):
        #self.player_rect = RUNNING[0].get_rect(midbottom = (60, 395))  
        #self.player_gravity += 10        
        #self.player_rect.y += self.player_gravity 
       # self.screen.blit(RUNNING[0], self.player_rect)
             

    def small_cactus(self):
        self.cactus_rect = SMALL_CACTUS[0].get_rect(bottomright = (self.x_pos_cactus, 395))
        self.cactus_rect = SMALL_CACTUS[1].get_rect(bottomright = (self.x_pos_cactus, 395))
        self.cactus_rect = SMALL_CACTUS[2].get_rect(bottomright = (self.x_pos_cactus, 395))
        self.screen.blit(SMALL_CACTUS[0], self.cactus_rect)
        self.screen.blit(SMALL_CACTUS[1], self.cactus_rect)
        self.screen.blit(SMALL_CACTUS[2], self.cactus_rect)
        if self.x_pos_cactus <= -self.cactus_rect.right: 
            self.x_pos_cactus = SCREEN_WIDTH
        self.x_pos_cactus -= self.game_speed


    
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

