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


WIDTH = SETTING2['SCREEN']['WIDTH']
HEIGHT = SETTING2['SCREEN']['HEIGHT']
NUMBER_ROWS = SETTING2['SCREEN']['NUMBER_ROWS']
NUMBER_COLUMNS = SETTING2['SCREEN']['NUMBER_COLUMNS']
CELL_SIZE = SETTING2['SCREEN']['CELL_SIZE']

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
        # self.showingScreenEnd = False
        
        ###########   Object in game    #####################################################################
        self.grid = Grid(0, 0)
        self.snake = snake
        self.foodManager = foodManager
        self.descriptionTextScreenStart = Button("Press SPACE to start", menu.SMALL_FONT, WIDTH//2, HEIGHT*11//12)
        self.descriptionTextScreenStart.isChosen = True
        self.scoreTextScreenRunning = Button(f"Score: {self.snake.score}", menu.SMALL_FONT, 3*CELL_SIZE, CELL_SIZE)
        self.scoreTextScreenRunning.isChosen = True
        # self.gameOverMenu = GameOverMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT, self.snake.score)
        
    ###########   Update screen    ##########################################################################
    def update(self, type='ProvideFoodsAndUpdateSnakeMove'):
        ###########   Remove old screen   ###################################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new screen with current status   #################################################
        if type == 'ProvideFoodsAndUpdateSnakeMove':
            if self.showingScreenStart:
                self.grid.draw(self.surface)
                self.snake.draw(self.surface)
                self.descriptionTextScreenStart.draw(self.surface)
                self.descriptionTextScreenStart.update("Press SPACE to start", menu.SMALL_FONT, 'R')
            elif self.running:
                self.score = self.snake.score
                self.snake.updateDisplacement(self.foodManager.listFood)
                self.foodManager.supplementFood(self.snake.coordinateSnakeBlocks())
                self.scoreTextScreenRunning.update(f"Score: {self.snake.score}", menu.SMALL_FONT, 'R')
                self.grid.draw(self.surface)
                self.foodManager.draw(self.surface)
                self.scoreTextScreenRunning.draw(self.surface)
                self.snake.draw(self.surface)
            elif self.waiting:
                pass
        elif type == 'UpdateSnakeFrame':
            if self.showingScreenStart:
                self.grid.draw(self.surface)
                self.snake.updateFrame()
                self.snake.draw(self.surface)
                self.descriptionTextScreenStart.draw(self.surface)
            elif self.running:
                self.snake.updateFrame()
                self.grid.draw(self.surface)
                self.foodManager.draw(self.surface)
                self.scoreTextScreenRunning.draw(self.surface)
                self.snake.draw(self.surface)
            elif self.waiting:
                pass
        elif type == 'UpdateFoodFrame':
            if self.showingScreenStart:
                pass
            elif self.running:
                self.foodManager.updateFrameFoods()
                self.grid.draw(self.surface)
                self.foodManager.draw(self.surface)
                self.scoreTextScreenRunning.draw(self.surface)
                self.snake.draw(self.surface)
            elif self.waiting:
                pass
            

    ###########   Draw current screen on anthor surface  ####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
        
        