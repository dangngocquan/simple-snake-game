import pygame
import menu
from menu import Button, GameOverMenu
import snake
from snake import SnakeBlock, Snake
import food
from food import Food, FoodManager
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
    def __init__(self, snake=Snake(), foodManager = FoodManager()):
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
        self.foodManager = foodManager
        self.descriptionTextScreenStart = Button("Press SPACE to start", menu.SMALL_FONT, WIDTH//2, HEIGHT*11//12)
        self.descriptionTextScreenStart.isChosen = True
        self.descriptionTextPauseGame = Button("Press SPACE to continue, Press K for a surprise, Press ESC to return main menu", 
                                               menu.SMALL_FONT, WIDTH//2, HEIGHT*11//12)
        self.descriptionTextPauseGame.isChosen = True
        self.scoreTextScreenRunning = Button(f"Score: {self.snake.score}", menu.SMALL_FONT, 3*SETTING2['SCREEN']['CELL_SIZE'], SETTING2['SCREEN']['CELL_SIZE'])
        self.scoreTextScreenRunning.isChosen = True
        
    ###########   Update screen    ##########################################################################
    def update(self, type='ProvideFoodsAndUpdateSnakeMove', tempCountTicks=0):
        self.snake.moveSpeed = SETTING1['SNAKE']['MOVE_SPEED']
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
                if SETTING1['GRID'] == 'ON':
                    self.grid.draw(self.surface)
                self.snake.draw(self.surface)
                self.descriptionTextScreenStart.draw(self.surface)
                self.descriptionTextScreenStart.update("Press SPACE to start", menu.SMALL_FONT, 'R')
            elif self.running:
                self.score = self.snake.score
                self.snake.updateLocation(self.foodManager.listFood)
                self.foodManager.supplementFood(self.snake.coordinateSnakeBlocks())
                self.scoreTextScreenRunning.update(f"Score: {self.snake.score}", menu.SMALL_FONT, 'R')
                if SETTING1['GRID'] == 'ON':
                    self.grid.draw(self.surface)
                if self.snake.currentDirection == None:
                    self.descriptionTextPauseGame.draw(self.surface)
                    if tempCountTicks % (SETTING2['SCREEN']['FPS'] * 1000 // SETTING1['MENU']['ANIMATION_SPEED']) == 0:
                        self.descriptionTextPauseGame.update("Press SPACE to continue, Press K for a surprise, Press ESC to return main menu",
                                                             menu.SMALL_FONT, 'R')
                self.foodManager.draw(self.surface)
                self.scoreTextScreenRunning.draw(self.surface)
                self.snake.draw(self.surface)
            elif self.waiting:
                pass
        ###########   Only update snake animation   #########################################################
        elif type == 'UpdateSnakeAnimation':
            if self.showingScreenStart:
                if SETTING1['GRID'] == 'ON':
                    self.grid.draw(self.surface)
                self.snake.updateAnimation()
                self.snake.draw(self.surface)
                self.descriptionTextScreenStart.draw(self.surface)
            elif self.running:
                self.snake.updateAnimation()
                if SETTING1['GRID'] == 'ON':
                    self.grid.draw(self.surface)
                self.foodManager.draw(self.surface)
                self.scoreTextScreenRunning.draw(self.surface)
                if self.snake.currentDirection == None:
                    self.descriptionTextPauseGame.draw(self.surface)
                self.snake.draw(self.surface)
            elif self.waiting:
                pass
        ###########   Only update food animation   ##########################################################
        elif type == 'UpdateFoodAnimation':
            if self.showingScreenStart:
                pass
            elif self.running:
                self.foodManager.updateAnimation()
                if SETTING1['GRID'] == 'ON':
                    self.grid.draw(self.surface)
                self.foodManager.draw(self.surface)
                self.scoreTextScreenRunning.draw(self.surface)
                if self.snake.currentDirection == None:
                    self.descriptionTextPauseGame.draw(self.surface)
                self.snake.draw(self.surface)
            elif self.waiting:
                pass
            

    ###########   Draw current screen on anthor surface  ####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
        
        