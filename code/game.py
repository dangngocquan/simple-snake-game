import sys
import pygame

from menu import MainMenu, PlayGameMenu

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
        self.runningPlayGameMenu = False
        self.runningNewGameMenu = False
        self.runningContinueGameMenu = False
        self.runningOptionsMenu = False
        self.runningGame = False
        
        self.mainMenu = MainMenu(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.playGameMenu = PlayGameMenu(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT)
        
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
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
                    elif event.key == pygame.K_RETURN:
                        if self.mainMenu.cursor == 0:
                            self.runningPlayGameMenu = True
                        elif self.mainMenu.cursor == 1:
                            self.runningOptionsMenu = True
                        self.runningMainMenu = False
            elif self.runningPlayGameMenu:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.playGameMenu.cursor += 1
                        self.playGameMenu.cursor %= 3
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.playGameMenu.cursor -= 1
                        self.playGameMenu.cursor %= 3
                    if event.key == pygame.K_RETURN:
                        if self.playGameMenu.cursor == 0:
                            self.runningNewGameMenu = True
                        elif self.playGameMenu.cursor == 1:
                            self.runningContinueGameMenu = True
                        elif self.playGameMenu.cursor == 2:
                            self.runningMainMenu = True
                        self.runningPlayGameMenu = False
            elif self.runningOptionsMenu:
                pass
            
                        
                        
        
    def update(self):
        if self.countTicks % (FPS * 1000 // self.mainMenu.FPS):
            if self.runningMainMenu:
                self.mainMenu.update()
            if self.runningPlayGameMenu:
                self.playGameMenu.update()
        
    
    def display(self):
        self.screen.fill(BLACK)
        if self.runningMainMenu:
            self.mainMenu.draw(self.screen)
        if self.runningPlayGameMenu:
            self.playGameMenu.draw(self.screen)
        pygame.display.update()