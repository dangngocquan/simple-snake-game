import sys
import pygame
from food import FoodManager
from menu import MainMenu, PlayGameMenu, GameOverMenu, OptionsMenu
from inGame import InGame
from snake import Snake
import snake
from setting import *
import setting

###########   VARIABLE   ####################################################################################
WIDTH = SETTING2['SCREEN']['WIDTH']
HEIGHT = SETTING2['SCREEN']['HEIGHT']
CAPTION = SETTING2['SCREEN']['CAPTION']
FPS = SETTING2['SCREEN']['FPS']
BLACK = SETTING2['COLOR']['BLACK']

###########   CLASS GAME   ##################################################################################
class Game:
    ###########   Constructor   #############################################################################
    def __init__(self):
        ###########   Create window game, caption, clock   ##################################################
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()
        self.countTicks = 0
        ###########   Status in game   ######################################################################
        self.running = True
        self.runningMainMenu = True
        self.runningPlayGameMenu = False
        self.runningInGame = False
        self.runningOptionsMenu = False
        self.runningGameOverMenu = False
        ###########   Screens in game   #####################################################################
        self.mainMenu = MainMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.playGameMenu = PlayGameMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.inGame = InGame()
        self.gameOverMenu = GameOverMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT, self.inGame.snake)
        self.optionsMenu = OptionsMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        
    
    ###########   Main loop in game   #######################################################################
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.getEvents()
            for i in range(1000):
                self.countTicks = (self.countTicks + 1) % (FPS * 1000)
                self.update()
            self.display()
    
    ###########   Get events in current screen   ############################################################    
    def getEvents(self):
        for event in pygame.event.get():
            ###########   Quit game   #######################################################################
            if event.type == pygame.QUIT:
                ###########   Save data before quit game   ##################################################
                if self.runningInGame:
                    snake.saveSnake(self.inGame.snake)
                elif self.runningGameOverMenu:
                    snake.saveSnake(Snake())
                ###########   Quit   ########################################################################
                self.running = False
                pygame.quit()
                sys.exit()
            ###########   Get events when current screen is Main Menu   #####################################
            if self.runningMainMenu:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.mainMenu.cursor += 1
                        self.mainMenu.cursor %= 3
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.mainMenu.cursor -= 1
                        self.mainMenu.cursor %= 3
                    elif event.key == pygame.K_RETURN:
                        self.runningMainMenu = False
                        if self.mainMenu.cursor == 0:
                            self.runningPlayGameMenu = True
                            self.playGameMenu.cursor = 0
                        elif self.mainMenu.cursor == 1:
                            self.runningOptionsMenu = True
                        elif self.mainMenu.cursor == 2:
                            self.running = False
                            pygame.quit()
                            sys.exit()            
            ###########   Get events when current screen is Play Game Menu  #################################
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
                            self.inGame.snake = Snake()
                            self.inGame.showingScreenStart = True
                        elif self.playGameMenu.cursor == 1:
                            self.runningInGame = True
                            self.inGame.snake = snake.loadPreviousSnake()
                            self.inGame.showingScreenStart = True
                        elif self.playGameMenu.cursor == 2:
                            self.runningMainMenu = True
                            self.mainMenu.cursor = 0
                        self.runningPlayGameMenu = False
            ###########   Get events when current screen is Options Menu   ##################################
            elif self.runningOptionsMenu:
                if event.type == pygame.KEYDOWN:
                    if self.optionsMenu.cursor % 2 == 0:
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            if self.optionsMenu.cursor == 12:
                                self.optionsMenu.cursor += 1
                            else:
                                self.optionsMenu.cursor += 2
                            self.optionsMenu.cursor %= 13
                        elif event.key == pygame.K_UP or event.key == pygame.K_w:
                            if self.optionsMenu.cursor == 0:
                                self.optionsMenu.cursor -= 1
                            else:
                                self.optionsMenu.cursor -= 2
                            self.optionsMenu.cursor %= 13
                        elif event.key == pygame.K_RETURN:
                            if self.optionsMenu.cursor == 12:
                                self.runningOptionsMenu = False
                                self.optionsMenu.cursor = 12
                                self.runningMainMenu = True
                                self.mainMenu.cursor = 0
                            else:
                                self.optionsMenu.cursor += 1
                    elif self.optionsMenu.cursor % 2 != 0:
                        if self.optionsMenu.cursor == 1:
                            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_DOWN, pygame.K_s, 
                                             pygame.K_a, pygame.K_d, pygame.K_RIGHT, pygame.K_LEFT]:
                                if SETTING1['GRID'] == 'ON':
                                    setting.replaceData(key1='GRID', newData='OFF')
                                elif SETTING1['GRID'] == 'OFF':
                                    setting.replaceData(key1='GRID', newData='ON')
                        elif self.optionsMenu.cursor == 3:
                            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_d, pygame.K_RIGHT]:
                                self.inGame.snake.moveSpeed = SETTING1['SNAKE']['MOVE_SPEED'] + 1
                                self.inGame.snake.moveSpeed %= 61
                                if self.inGame.snake.moveSpeed == 0:
                                    self.inGame.snake.moveSpeed = 1
                            elif event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_a, pygame.K_LEFT]:
                                self.inGame.snake.moveSpeed = SETTING1['SNAKE']['MOVE_SPEED'] - 1
                                self.inGame.snake.moveSpeed %= 61
                                if self.inGame.snake.moveSpeed == 0:
                                    self.inGame.snake.moveSpeed = 60
                            setting.replaceData(key1='SNAKE', key2='MOVE_SPEED', 
                                                newData=self.inGame.snake.moveSpeed)
                        elif self.optionsMenu.cursor == 5:
                            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_d, pygame.K_RIGHT]:
                                self.inGame.snake.dropSpeed = SETTING1['SNAKE']['DROP_SPEED'] + 1
                                self.inGame.snake.dropSpeed %= 61
                                if self.inGame.snake.dropSpeed == 0:
                                    self.inGame.snake.dropSpeed = 1
                            elif event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_a, pygame.K_LEFT]:
                                self.inGame.snake.dropSpeed = SETTING1['SNAKE']['DROP_SPEED'] - 1
                                self.inGame.snake.dropSpeed %= 61
                                if self.inGame.snake.dropSpeed == 0:
                                    self.inGame.snake.dropSpeed = 60
                            setting.replaceData(key1='SNAKE', key2='DROP_SPEED', 
                                                newData=self.inGame.snake.dropSpeed)
                        elif self.optionsMenu.cursor == 7:
                            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_d, pygame.K_RIGHT]:
                                self.inGame.snake.animationSpeed = SETTING1['SNAKE']['ANIMATION_SPEED'] + 1
                                self.inGame.snake.animationSpeed %= 61
                                if self.inGame.snake.animationSpeed == 0:
                                    self.inGame.snake.animationSpeed = 1
                            elif event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_a, pygame.K_LEFT]:
                                self.inGame.snake.animationSpeed = SETTING1['SNAKE']['ANIMATION_SPEED'] - 1
                                self.inGame.snake.animationSpeed %= 61
                                if self.inGame.snake.animationSpeed == 0:
                                    self.inGame.snake.animationSpeed = 60
                            setting.replaceData(key1='SNAKE', key2='ANIMATION_SPEED', 
                                                newData=self.inGame.snake.animationSpeed)
                        elif self.optionsMenu.cursor == 9:
                            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_d, pygame.K_RIGHT]:
                                self.inGame.foodManager.maxFood = SETTING1['FOOD']['MAX_FOOD'] + 1
                                self.inGame.foodManager.maxFood %= 105
                                if self.inGame.foodManager.maxFood == 0:
                                    self.inGame.foodManager.maxFood = 1
                            elif event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_a, pygame.K_LEFT]:
                                self.inGame.foodManager.maxFood = SETTING1['FOOD']['MAX_FOOD'] - 1
                                self.inGame.foodManager.maxFood %= 105
                                if self.inGame.foodManager.maxFood == 0:
                                    self.inGame.foodManager.maxFood = 104
                            setting.replaceData(key1='FOOD', key2='MAX_FOOD', 
                                                newData=self.inGame.foodManager.maxFood)
                        elif self.optionsMenu.cursor == 11:
                            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_d, pygame.K_RIGHT]:
                                self.inGame.foodManager.animationSpeed = SETTING1['FOOD']['ANIMATION_SPEED'] + 1
                                self.inGame.foodManager.animationSpeed %= 61
                                if self.inGame.foodManager.animationSpeed == 0:
                                    self.inGame.foodManager.animationSpeed = 1
                            elif event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_a, pygame.K_LEFT]:
                                self.inGame.foodManager.animationSpeed = SETTING1['FOOD']['ANIMATION_SPEED'] - 1
                                self.inGame.foodManager.animationSpeed %= 61
                                if self.inGame.foodManager.animationSpeed == 0:
                                    self.inGame.foodManager.animationSpeed = 60
                            setting.replaceData(key1='FOOD', key2='ANIMATION_SPEED', 
                                                newData=self.inGame.foodManager.animationSpeed)
                        if event.key == pygame.K_RETURN:
                            self.optionsMenu.cursor -= 1
                setting.saveSetting('./data/setting/setting.json')          
            ###########   Get events when current screen is InGame (player controls snake)   ################
            elif self.runningInGame:
                ###########   Get events when current screen is Start InGame   ##############################
                if self.inGame.showingScreenStart:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.inGame.showingScreenStart = False
                            self.inGame.running = True
                ###########   Get events when snake moving   ################################################
                elif self.inGame.running:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_k:
                            if self.inGame.snake.currentDirection == None:
                                self.inGame.running = False
                                self.runningInGame = False
                                self.runningGameOverMenu = True
                                self.gameOverMenu = GameOverMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT, 
                                                                 self.inGame.snake)
                        elif event.key == pygame.K_SPACE:
                            if self.inGame.snake.currentDirection != None:
                                self.inGame.snake.previousDirection = self.inGame.snake.currentDirection
                                self.inGame.snake.currentDirection = None
                            else:
                                self.inGame.snake.currentDirection = self.inGame.snake.previousDirection
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
                ###########   Get events when game pause   ##################################################
                elif self.inGame.waiting:
                    pass
            ###########   Get event when current screen is Game Over Menu   #################################
            elif self.runningGameOverMenu:
                 if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.gameOverMenu.cursor += 1
                        self.gameOverMenu.cursor %= 2
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.gameOverMenu.cursor -= 1
                        self.gameOverMenu.cursor %= 2
                    elif event.key == pygame.K_RETURN:
                        if self.gameOverMenu.cursor == 0:
                            self.runningInGame = True
                            self.inGame.showingScreenStart = True
                        elif self.gameOverMenu.cursor == 1:
                            self.runningMainMenu = True
                        snake.saveSnake(Snake())
                        self.inGame.snake = Snake()
                        self.inGame.foodManager = FoodManager()
                        self.inGame.update()
                        self.runningGameOverMenu = False
                        
                                  
    ###########   Update screen with current status   #######################################################       
    def update(self):
        ###########   Update screen Main Menu   #############################################################
        if self.runningMainMenu:
            if self.countTicks % (FPS * 1000 // self.mainMenu.FPS) == 0:
                self.mainMenu.update()
        ###########   Update screen Play Game Menu   ########################################################
        elif self.runningPlayGameMenu:
            if self.countTicks % (FPS * 1000 // self.playGameMenu.FPS) == 0:
                self.playGameMenu.update()
        ###########   Update screen when player controlling snake   #########################################
            ###########   Check game over   #################################################################
            if self.inGame.snake.died():
                self.inGame.running = False
                self.runningInGame = False
                self.runningGameOverMenu = True
                self.gameOverMenu = GameOverMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT, self.inGame.snake)
            ###########   Update screen when showing screen start in Ingame   ###############################
                if self.countTicks % (FPS * 1000 // self.inGame.snake.animationSpeed) == 0:
                    self.inGame.update(type='UpdateSnakeAnimation')
                if self.countTicks % (FPS * 1000 // self.mainMenu.FPS) == 0:
                    self.inGame.update()
            ###########   Update screen when player is playing   ############################################
            elif self.inGame.running:
                if self.countTicks % (FPS * 1000 // self.inGame.snake.animationSpeed) == 0:
                    self.inGame.update(type='UpdateSnakeAnimation')
                if self.countTicks % (FPS * 1000 // self.inGame.foodManager.animationSpeed) == 0:
                    self.inGame.update(type='UpdateFoodAnimation')
                if self.countTicks % (FPS * 1000 // self.inGame.snake.moveSpeed) == 0:
                    self.inGame.update()
            ###########   Update screen when pause game   ###################################################
            elif self.inGame.waiting:
                pass
        ###########   Update screen when Game Over   ########################################################
        elif self.runningGameOverMenu:
            if self.countTicks % (FPS * 1000 // self.inGame.snake.dropSpeed) == 0:
                self.gameOverMenu.update(type='UpdateSnakeDrop')
            if self.countTicks % (FPS * 1000 // self.inGame.snake.animationSpeed) == 0:
                self.gameOverMenu.update(type='UpdateSnakeAnimation')
            if self.countTicks % (FPS * 1000 // self.gameOverMenu.FPS) == 0:
                self.gameOverMenu.update()
        ###########   Update screen when showing Options Menu   #############################################
        elif self.runningOptionsMenu:
            if self.countTicks % (FPS * 1000 // self.optionsMenu.FPS) == 0:
                self.optionsMenu.update()
            
        
    ###########   Draw screen with current status and show it   #############################################
    def display(self):
        ###########   Clear old images   ####################################################################
        self.screen.fill(BLACK)
        ###########   Draw new images   #####################################################################
        if self.runningInGame:
            self.inGame.draw(self.screen)
        elif self.runningMainMenu:
            self.mainMenu.draw(self.screen)
        elif self.runningPlayGameMenu:
            self.playGameMenu.draw(self.screen)
        elif self.runningGameOverMenu:
            self.gameOverMenu.draw(self.screen)
        elif self.runningOptionsMenu:
            self.optionsMenu.draw(self.screen)
        pygame.display.flip()