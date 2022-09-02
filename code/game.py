import sys
import pygame

from mainMenu import MainMenu

###########  SCREEN SETTING  ####################################################
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_CAPTION = "Simple Snake Gameeee"
FPS = 60

###########  COLOR  #############################################################
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(SCREEN_CAPTION)
        self.clock = pygame.time.Clock()
        self.countTicks = 0
        self.running = True
        self.waiting = False
        self.runningMainMenu = True
        self.runningGame = False
        
        self.mainMenu = MainMenu(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT)
        
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.getEvents()
            for i in range(1000):
                self.countTicks = (self.countTicks + 1) % (FPS * 1000)
                self.update()
            self.display()
            
    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running =False
                pygame.quit()
                sys.exit()
            if self.runningMainMenu:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.mainMenu.cursor += 1
                        self.mainMenu.cursor %= 2
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.mainMenu.cursor -= 1
                        self.mainMenu.cursor %= 2
        
    def update(self):
        if self.countTicks % (FPS * 1000 // self.mainMenu.FPS):
            self.mainMenu.update()
        
    
    def display(self):
        self.screen.fill(BLACK)
        if self.runningMainMenu:
            self.mainMenu.draw(self.screen)
        pygame.display.update()