import pygame
from account import ACCOUNT_MANAGER
import button
from button import Button
import snake
from snake import SnakeBlock, Snake
import food
from food import Food, FoodManager
from wall import Wall, WallManager
import wall
import grid
from grid import Grid
from setting import *
import setting

###########   VARIABLE   ####################################################################################
WIDTH = SETTING2['SCREEN']['WIDTH']
HEIGHT = SETTING2['SCREEN']['HEIGHT']
NUMBER_ROWS = SETTING2['SCREEN']['NUMBER_ROWS']
NUMBER_COLUMNS = SETTING2['SCREEN']['NUMBER_COLUMNS']

###########  CLASS INGAME  ##################################################################################
class InGame:
    ###########   Constructor   #############################################################################
    def __init__(self, snake=Snake(), foodManager = FoodManager(), wallManager = WallManager()):
        ###########   Create surface and coordinate   #######################################################
        self.surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (0, 0)
        ###########   Status screen    ######################################################################
        self.showingScreenStart = False
        self.running = False
        self.waiting = False
        ###########   Object in game    #####################################################################
        self.grid = Grid(0, 0)
        self.snake = snake
        self.wallManager = wallManager
        self.foodManager = foodManager
        self.descriptionTextScreenStart = Button("Press 'SPACE' to start, Press 'ESC' to return Main menu", 
                                                 button.DESCRIPTION_FONT_2, WIDTH//2, HEIGHT*11//12)
        self.descriptionTextScreenStart.isChosen = True
        self.descriptionTextPauseGame = Button("Press 'SPACE' to continue, Press 'K' for a surprise, Press 'ESC' to return Main menu", 
                                               button.DESCRIPTION_FONT_2, WIDTH//2, HEIGHT*11//12)
        self.descriptionTextPauseGame.isChosen = True
        self.scoreTextScreenRunning = Button(f"Score: {self.snake.score}", button.DESCRIPTION_FONT_2, 
                                             3*SETTING2['SCREEN']['CELL_SIZE'], SETTING2['SCREEN']['CELL_SIZE'])
        self.scoreTextScreenRunning.isChosen = True
        
    ###########   Update screen    ##########################################################################
    def update(self, type='ProvideFoodsAndUpdateSnakeMove', tempCountTicks=0, divisibility=462):
        if SETTING1['GAMEMODE']['AUTO_SPEED_UP'] == "OFF":
            self.snake.moveSpeed = SETTING1['SNAKE']['MOVE_SPEED']
        elif SETTING1['GAMEMODE']['AUTO_SPEED_UP'] == "ON":
            self.snake.moveSpeed = int((self.snake.score/5 + 1/4)**(1/2) + 3/2)
        self.snake.dropSpeed = SETTING1['SNAKE']['DROP_SPEED']
        self.snake.animationSpeed = SETTING1['SNAKE']['ANIMATION_SPEED']
        self.foodManager.maxFood = SETTING1['FOOD']['MAX_FOOD']
        self.foodManager.animationSpeed = SETTING1['FOOD']['ANIMATION_SPEED']
        ###########   Remove old screen   ###################################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new screen with current status   #################################################
        ###########   Update snake move and number of food   ################################################
        if type == 'ProvideFoodsAndUpdateSnakeMove':
            if self.showingScreenStart:
                self.wallManager.draw(self.surface)
                if SETTING1['GRID'] == 'ON':
                    self.grid.draw(self.surface)
                self.snake.draw(self.surface)
                self.foodManager.supplementFood(self.snake.coordinateSnakeBlocks(), self.wallManager.coordinateWalls())
                self.foodManager.draw(self.surface)
                self.descriptionTextScreenStart.draw(self.surface)
                self.descriptionTextScreenStart.update("Press 'SPACE' to start, Press 'ESC' to return Main menu", 
                                                       button.DESCRIPTION_FONT_2, 'R')
                self.scoreTextScreenRunning.update(f"Score: {self.snake.score}", button.DESCRIPTION_FONT_2, 'R')
                self.scoreTextScreenRunning.draw(self.surface)
            elif self.running:
                self.snake.updateLocation(self.foodManager.listFood)
                self.foodManager.supplementFood(self.snake.coordinateSnakeBlocks(), self.wallManager.coordinateWalls())
                self.scoreTextScreenRunning.update(f"Score: {self.snake.score}", button.DESCRIPTION_FONT_2, 'R')
                self.wallManager.draw(self.surface)
                if SETTING1['GRID'] == 'ON':
                    self.grid.draw(self.surface)
                self.foodManager.draw(self.surface)
                self.snake.draw(self.surface)
                self.scoreTextScreenRunning.draw(self.surface)
                if self.snake.currentDirection == None:
                    self.descriptionTextPauseGame.draw(self.surface)
                    if tempCountTicks % (SETTING2['SCREEN']['FPS'] * divisibility // SETTING1['MENU']['ANIMATION_SPEED']) == 0:
                        self.descriptionTextPauseGame.update(
                            "Press 'SPACE' to continue, Press 'K' for a surprise, Press 'ESC' to return Main menu",
                            button.DESCRIPTION_FONT_2, 'R')
            elif self.waiting:
                pass
        ###########   Only update snake animation   #########################################################
        elif type == 'UpdateSnakeAnimation':
            if self.showingScreenStart:
                self.wallManager.draw(self.surface)
                if SETTING1['GRID'] == 'ON':
                    self.grid.draw(self.surface)
                self.snake.updateAnimation()
                self.snake.draw(self.surface)
                self.foodManager.draw(self.surface)
                self.descriptionTextScreenStart.draw(self.surface)
                self.scoreTextScreenRunning.draw(self.surface)
            elif self.running:
                self.snake.updateAnimation()
                self.wallManager.draw(self.surface)
                if SETTING1['GRID'] == 'ON':
                    self.grid.draw(self.surface)
                self.foodManager.draw(self.surface)
                self.snake.draw(self.surface)
                self.scoreTextScreenRunning.draw(self.surface)
                if self.snake.currentDirection == None:
                    self.descriptionTextPauseGame.draw(self.surface)
            elif self.waiting:
                pass
        ###########   Only update food animation   ##########################################################
        elif type == 'UpdateFoodAnimation':
            if self.showingScreenStart:
                self.wallManager.draw(self.surface)
                if SETTING1['GRID'] == 'ON':
                    self.grid.draw(self.surface)
                self.foodManager.updateAnimation()
                self.snake.draw(self.surface)
                self.foodManager.draw(self.surface)
                self.descriptionTextScreenStart.draw(self.surface)
                self.scoreTextScreenRunning.draw(self.surface)
            elif self.running:
                self.foodManager.updateAnimation()
                self.wallManager.draw(self.surface)
                if SETTING1['GRID'] == 'ON':
                    self.grid.draw(self.surface)
                self.foodManager.draw(self.surface)
                self.snake.draw(self.surface)
                self.scoreTextScreenRunning.draw(self.surface)
                if self.snake.currentDirection == None:
                    self.descriptionTextPauseGame.draw(self.surface)
            elif self.waiting:
                pass
            

    ###########   Draw current screen on anthor surface  ####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        



###########  CLASS INGAME02  ################################################################################
class InGame02:
    ###########   Constructor   #############################################################################
    def __init__(self, snake01=Snake(typeLocation=-1, typeColor='blue'),
                 snake02=Snake(typeLocation=1, typeColor='green'),
                 foodManager = FoodManager(), wallManager=WallManager()):
        ###########   Create surface and coordinate   #######################################################
        self.surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (0, 0)
        ###########   Status screen    ######################################################################
        self.showingScreenStart = False
        self.running = False
        self.waiting = False
        ###########   Object in game    #####################################################################
        self.grid = Grid(0, 0)
        self.snake01 = snake01
        self.snake02 = snake02
        self.foodManager = foodManager
        self.wallManager = wallManager
        self.descriptionTextScreenStart = Button("Press 'SPACE' to start, Press 'ESC' to return Main menu", 
                                                 button.DESCRIPTION_FONT_2, WIDTH//2, HEIGHT*11//12)
        self.descriptionTextScreenStart.isChosen = True
        self.descriptionTextPauseGame = Button("Press 'SPACE' to continue, Press 'K' for a surprise, Press 'ESC' to return Main menu", 
                                               button.DESCRIPTION_FONT_2, WIDTH//2, HEIGHT*11//12)
        self.descriptionTextPauseGame.isChosen = True
        self.scoreTextScreenRunning01 = Button(
            f"{ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name}'s score: {self.snake01.score}", 
            button.DESCRIPTION_FONT_2, x=6*SETTING2['SCREEN']['CELL_SIZE'], y=SETTING2['SCREEN']['CELL_SIZE'])
        self.scoreTextScreenRunning01.isChosen = True
        self.scoreTextScreenRunning02 = Button(f"Other player's score: {self.snake02.score}", button.DESCRIPTION_FONT_2, 
                                               x=(NUMBER_COLUMNS-7)*SETTING2['SCREEN']['CELL_SIZE'], y=SETTING2['SCREEN']['CELL_SIZE'])
        self.scoreTextScreenRunning02.isChosen = True
        
    ###########   Update screen    ##########################################################################
    def update(self, type='ProvideFoodsAndUpdateSnakeMove', tempCountTicks=0, 
               snakeMove01=True, snakeMove02=True, divisibility=462):
        if SETTING1['GAMEMODE']['AUTO_SPEED_UP'] == "OFF":
            self.snake01.moveSpeed = SETTING1['SNAKE']['MOVE_SPEED']
            self.snake02.moveSpeed = SETTING1['SNAKE']['MOVE_SPEED']
        elif SETTING1['GAMEMODE']['AUTO_SPEED_UP'] == "ON":
            self.snake01.moveSpeed = int((self.snake01.score/5 + 1/4)**(1/2) + 3/2)
            self.snake02.moveSpeed = int((self.snake02.score/5 + 1/4)**(1/2) + 3/2)
        self.snake01.dropSpeed = SETTING1['SNAKE']['DROP_SPEED']
        self.snake01.animationSpeed = SETTING1['SNAKE']['ANIMATION_SPEED']
        self.snake02.dropSpeed = SETTING1['SNAKE']['DROP_SPEED']
        self.snake02.animationSpeed = SETTING1['SNAKE']['ANIMATION_SPEED']
        self.foodManager.maxFood = SETTING1['FOOD']['MAX_FOOD']
        self.foodManager.animationSpeed = SETTING1['FOOD']['ANIMATION_SPEED']
        ###########   Remove old screen   ###################################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new screen with current status   #################################################
        ###########   Update snake move and number of food   ################################################
        if type == 'ProvideFoodsAndUpdateSnakeMove':
            if self.showingScreenStart:
                self.wallManager.draw(self.surface)
                if SETTING1['GRID'] == 'ON':
                    self.grid.draw(self.surface)
                self.snake01.draw(self.surface)
                self.snake02.draw(self.surface)
                self.foodManager.supplementFood(self.snake01.coordinateSnakeBlocks() + self.snake02.coordinateSnakeBlocks(),
                                                self.wallManager.coordinateWalls())
                self.foodManager.draw(self.surface)
                self.descriptionTextScreenStart.draw(self.surface)
                if tempCountTicks % (SETTING2['SCREEN']['FPS'] * divisibility // SETTING1['MENU']['ANIMATION_SPEED']) == 0:
                    self.descriptionTextScreenStart.update(
                        "Press 'SPACE' to start, Press 'ESC' to return Main menu", button.DESCRIPTION_FONT_2, 'R')
                if snakeMove01 == True:
                    self.scoreTextScreenRunning01.update(
                        f"{ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name}'s score: {self.snake01.score}", 
                        button.DESCRIPTION_FONT_2, 'B')
                if snakeMove02 == True:
                    self.scoreTextScreenRunning02.update(
                        f"Other player's score: {self.snake02.score}", button.DESCRIPTION_FONT_2, 'G')
                self.scoreTextScreenRunning01.draw(self.surface)
                self.scoreTextScreenRunning02.draw(self.surface)
            elif self.running:
                if snakeMove01 == True:
                    self.snake01.updateLocation(self.foodManager.listFood)
                    self.scoreTextScreenRunning01.update(
                        f"{ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name}'s score: {self.snake01.score}", 
                        button.DESCRIPTION_FONT_2, 'B')
                if snakeMove02 == True:
                    self.snake02.updateLocation(self.foodManager.listFood)
                    self.scoreTextScreenRunning02.update(f"Other player's score: {self.snake02.score}", button.DESCRIPTION_FONT_2, 'G')
                self.foodManager.supplementFood(self.snake01.coordinateSnakeBlocks() + self.snake02.coordinateSnakeBlocks(),
                                                self.wallManager.coordinateWalls())
                self.wallManager.draw(self.surface)
                if SETTING1['GRID'] == 'ON':
                    self.grid.draw(self.surface)
                self.foodManager.draw(self.surface)
                self.scoreTextScreenRunning01.draw(self.surface)
                self.scoreTextScreenRunning02.draw(self.surface)
                self.snake01.draw(self.surface)
                self.snake02.draw(self.surface)
                if self.snake01.currentDirection == None or self.snake02.currentDirection == None:
                    self.descriptionTextPauseGame.draw(self.surface)
                    if tempCountTicks % (SETTING2['SCREEN']['FPS'] * divisibility // SETTING1['MENU']['ANIMATION_SPEED']) == 0:
                        self.descriptionTextPauseGame.update(
                            "Press 'SPACE' to continue, Press 'K' for a surprise, Press 'ESC' to return Main menu",
                            button.DESCRIPTION_FONT_2, 'R')
            elif self.waiting:
                pass
        ###########   Only update snake animation   #########################################################
        elif type == 'UpdateSnakeAnimation':
            if self.showingScreenStart:
                self.wallManager.draw(self.surface)
                if SETTING1['GRID'] == 'ON':
                    self.grid.draw(self.surface)
                self.snake01.updateAnimation()
                self.snake01.draw(self.surface)
                self.snake02.updateAnimation()
                self.snake02.draw(self.surface)
                self.foodManager.draw(self.surface)
                self.descriptionTextScreenStart.draw(self.surface)
                self.scoreTextScreenRunning01.draw(self.surface)
                self.scoreTextScreenRunning02.draw(self.surface)
            elif self.running:
                self.snake01.updateAnimation()
                self.snake02.updateAnimation()
                self.wallManager.draw(self.surface)
                if SETTING1['GRID'] == 'ON':
                    self.grid.draw(self.surface)
                self.foodManager.draw(self.surface)
                self.snake01.draw(self.surface)
                self.snake02.draw(self.surface)
                self.scoreTextScreenRunning01.draw(self.surface)
                self.scoreTextScreenRunning02.draw(self.surface)
                if self.snake01.currentDirection == None or self.snake02.currentDirection == None:
                    self.descriptionTextPauseGame.draw(self.surface)
            elif self.waiting:
                pass
        ###########   Only update food animation   ##########################################################
        elif type == 'UpdateFoodAnimation':
            if self.showingScreenStart:
                self.wallManager.draw(self.surface)
                if SETTING1['GRID'] == 'ON':
                    self.grid.draw(self.surface)
                self.foodManager.updateAnimation()
                self.snake01.draw(self.surface)
                self.snake02.draw(self.surface)
                self.foodManager.draw(self.surface)
                self.descriptionTextScreenStart.draw(self.surface)
                self.scoreTextScreenRunning01.draw(self.surface)
                self.scoreTextScreenRunning02.draw(self.surface)
            elif self.running:
                self.foodManager.updateAnimation()
                self.wallManager.draw(self.surface)
                if SETTING1['GRID'] == 'ON':
                    self.grid.draw(self.surface)
                self.foodManager.draw(self.surface)
                self.snake01.draw(self.surface)
                self.snake02.draw(self.surface)
                self.scoreTextScreenRunning01.draw(self.surface)
                self.scoreTextScreenRunning02.draw(self.surface)
                if self.snake01.currentDirection == None or self.snake01.currentDirection == None:
                    self.descriptionTextPauseGame.draw(self.surface)
            elif self.waiting:
                pass
            

    ###########   Draw current screen on anthor surface  ####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        