from codecs import ignore_errors
import sys
import pygame

from menu import MainMenu, PlayGameMenu
from inGame import InGame

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
        self.runningInGame = False
        self.runningContinueGameMenu = False
        self.runningOptionsMenu = False
        
        self.mainMenu = MainMenu(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.playGameMenu = PlayGameMenu(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.inGame = InGame()
        
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
                            self.runningInGame = True
                            self.inGame.showingScreenStart = True
                        elif self.playGameMenu.cursor == 1:
                            self.runningContinueGameMenu = True
                        elif self.playGameMenu.cursor == 2:
                            self.runningMainMenu = True
                        self.runningPlayGameMenu = False
            elif self.runningOptionsMenu:
                pass
            elif self.runningInGame:
                if self.inGame.showingScreenStart:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.inGame.showingScreenStart = False
                            self.inGame.running = True
                elif self.inGame.running:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                            pass
                        elif event.key == pygame.K_UP or event.key == pygame.K_w:
                            if self.inGame.snake.currentDirection != 'DD' and self.inGame.snake.checkSnakeCanMove('UU'):
                                self.inGame.snake.currentDirection = 'UU'
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            if self.inGame.snake.currentDirection != 'UU' and self.inGame.snake.checkSnakeCanMove('DD'):
                                self.inGame.snake.currentDirection = 'DD'
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            if self.inGame.snake.currentDirection != 'LL' and self.inGame.snake.checkSnakeCanMove('RR'):
                                self.inGame.snake.currentDirection = 'RR'
                        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            if self.inGame.snake.currentDirection != 'RR' and self.inGame.snake.checkSnakeCanMove('LL'):
                                self.inGame.snake.currentDirection = 'LL'
                elif self.inGame.waiting:
                    pass
                elif self.inGame.showingScreenEnd:
                    pass
            elif self.runningContinueGameMenu:
                pass
                
                        
            
                        
                        
    def update(self):
        if self.runningInGame:
            if self.inGame.showingScreenStart or self.inGame.showingScreenEnd:
                if self.countTicks % (FPS * 1000 // self.mainMenu.FPS) == 0:
                    self.inGame.update()
            elif self.inGame.running or self.inGame.waiting:
                if self.countTicks % (FPS * 1000 // self.inGame.snake.changeColorSpeed) == 0:
                    self.inGame.snake.countTicks += 1
                    self.inGame.snake.countTicks %= 7
                if self.countTicks % (FPS * 1000 // self.inGame.snake.speed) == 0:
                    self.inGame.update()
        elif self.runningMainMenu:
            if self.countTicks % (FPS * 1000 // self.mainMenu.FPS) == 0:
                self.mainMenu.update()
        elif self.runningPlayGameMenu:
            if self.countTicks % (FPS * 1000 // self.mainMenu.FPS) == 0:
                self.playGameMenu.update()
        
    
    def display(self):
        self.screen.fill(BLACK)
        if self.runningInGame:
            self.inGame.draw(self.screen)
        elif self.runningMainMenu:
            self.mainMenu.draw(self.screen)
        elif self.runningPlayGameMenu:
            self.playGameMenu.draw(self.screen)
        pygame.display.flip()