import pygame
import random
from setting import *

WIDTH = SETTING2['SCREEN']['WIDTH']
HEIGHT = SETTING2['SCREEN']['HEIGHT']
NUMBER_ROWS = SETTING2['SCREEN']['NUMBER_ROWS']
NUMBER_COLUMNS = SETTING2['SCREEN']['NUMBER_COLUMNS']
CELL_SIZE = SETTING2['SCREEN']['CELL_SIZE']
FOOD = SETTING2['FOOD']
MAX_FOOD = SETTING1['FOOD']['MAX_FOOD']
ANIMATION_SPEED = SETTING1['FOOD']['ANIMATION_SPEED']

###########  CLASS FOOD  ####################################################################################
class Food:
    ########### Constructor  ################################################################################
    def __init__(self, x, y):
        ###########  Create surface   #######################################################################
        self.surface = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (x, y)
        self.x = x
        self.y = y
        
        ###########  Default image food  ####################################################################
        self.surface.blit(FOOD[0], (0, 0))
        self.indexFrame = 0
    
    ###########  Get coordinate of food  ####################################################################
    def coordinate(self):
        return [self.x, self.y]
    
    ###########  Update image of food  ######################################################################
    def update(self):
        # self.indexFrame = (self.indexFrame + 1) % 4
        ###########  Remove old image food  #################################################################
        self.surface.fill((0, 0, 0, 0))
        ###########  Draw new image food  ###################################################################
        self.surface.blit(FOOD[self.indexFrame], (0, 0))
    
    ###########  Draw Food on another surface  ##############################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)


###########  CLASS FOOD MANAGER  ############################################################################
class FoodManager:
    ###########  Constructor  ###############################################################################
    def __init__(self):
        ###########  Surface and coordinate #################################################################
        self.surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (0, 0)
        ###########  List food anf  number of foods  ########################################################
        self.listFood = []
        self.maxFood = MAX_FOOD
        self.animationSpeed = ANIMATION_SPEED
    
    ###########  Get coordinate of all foods ################################################################
    def coordinateFoods(self):
        return [food.coordinate() for food in self.listFood]
    
    ###########  Create a random Food  ######################################################################
    def createRandomValidFood(self, coordinateSnakeBlockss=[]):
        if len(self.listFood) + len(coordinateSnakeBlockss) >= NUMBER_ROWS * NUMBER_COLUMNS:
            return None
        randomX = random.randint(0, NUMBER_COLUMNS-1) * CELL_SIZE
        randomY = random.randint(0, NUMBER_ROWS-1) * CELL_SIZE
        while ([randomX, randomY] in (self.coordinateFoods() + coordinateSnakeBlockss)):
            randomX = random.randint(0, NUMBER_COLUMNS-1) * CELL_SIZE
            randomY = random.randint(0, NUMBER_ROWS-1) * CELL_SIZE
        return Food(randomX, randomY)
    
    ###########  Update status food man #####################################################################
    def supplementFood(self, coordinateSnakeBlockss):
        ###########  Supplement the Food Manager  ###########################################################
        while len(self.listFood) < self.maxFood:
            randomValidFood = self.createRandomValidFood(coordinateSnakeBlockss)
            if randomValidFood == None:
                break
            else:
                self.listFood.append(randomValidFood)
        ###########  Remove old image foods  ################################################################
        self.surface.fill((0, 0, 0, 0))
        ###########  Draw all new image foods  ##############################################################
        for food in self.listFood:
            food.update()
            food.draw(self.surface)
        
    
    def updateAnimation(self):
        self.surface.fill((0, 0, 0, 0))
        for food in self.listFood:
            food.indexFrame = (food.indexFrame + 1) % 4
            food.update()
            food.draw(self.surface)
    
    ###########  Draw all foods on another surface  #########################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect) 