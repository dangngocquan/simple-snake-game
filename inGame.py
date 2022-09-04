import pygame
import menu
from menu import Button
import snake
from snake import SnakeBlock, Snake
import food
from food import Food, FoodManager
import grid
from grid import Grid

###########  SETTING  #######################################################################################
CELL_SIZE = 25
INGAME_WIDTH = 1000
INGAME_HEIGHT = 600
NUMBER_ROWS = INGAME_HEIGHT // CELL_SIZE
NUMBER_COLUMNS = INGAME_WIDTH // CELL_SIZE


###########  COLOR  #########################################################################################
GRAY = (111, 111, 111)


###########  CLASS INGAME  ##################################################################################
class InGame:
    ###########   Constructor   #############################################################################
    def __init__(self, snake=Snake(), foodManager = FoodManager()):
        ###########   Create surface and coordinate   #######################################################
        self.surface = pygame.Surface((INGAME_WIDTH, INGAME_HEIGHT), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (0, 0)
        
        ###########   Status screen    ######################################################################
        self.showingScreenStart = False
        self.running = False
        self.waiting = False
        self.showingScreenEnd = False
        
        ###########   Object in game    #####################################################################
        self.grid = Grid(0, 0)
        self.snake = snake
        self.foodManager = foodManager
        self.descriptionText = Button("Press SPACE to start", menu.TITLE_FONT2, INGAME_WIDTH//2, INGAME_HEIGHT*9//12)
        self.descriptionText.isChosen = True
        self.scoreText = Button(f"Score: {self.snake.score}", menu.SMALL_FONT, 3*CELL_SIZE, CELL_SIZE)
        self.scoreText.isChosen = True
        
    ###########   Update screen    ##########################################################################
    def update(self):
        ###########   Remove old screen   ###################################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new screen with current status   #################################################
        if self.showingScreenStart:
            self.grid.draw(self.surface)
            self.snake.draw(self.surface)
            self.descriptionText.draw(self.surface)
            self.descriptionText.update("Press SPACE to start", menu.TITLE_FONT2, 'R')
        elif self.running:
            self.snake.updateDisplacement(self.foodManager.listFood)
            self.foodManager.update(self.snake.coordinateSnakeBlocks())
            self.scoreText.update(f"Score: {self.snake.score}", menu.SMALL_FONT, 'R')
            self.grid.draw(self.surface)
            self.foodManager.draw(self.surface)
            self.scoreText.draw(self.surface)
            self.snake.draw(self.surface)
        elif self.waiting:
            pass
        elif self.showingScreenEnd:
            self.grid.draw(self.surface)
            self.foodManager.draw(self.surface)
            self.snake.draw(self.surface)
            
    def updateOnlySnakeFrame(self):
        ###########   Remove old screen   ###################################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new screen with current status   #################################################
        if self.showingScreenStart:
            pass
        elif self.running:
            self.snake.updateFrame()
            self.grid.draw(self.surface)
            self.foodManager.draw(self.surface)
            self.scoreText.draw(self.surface)
            self.snake.draw(self.surface)
        elif self.waiting:
            pass
        elif self.showingScreenEnd:
            pass

    ###########   Draw current screen on anthor surface  ####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
        
        