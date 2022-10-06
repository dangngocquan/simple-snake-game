import pygame
import random
from setting import *
import setting

###########   VARIABLE   ####################################################################################
WIDTH = SETTING2['SCREEN']['WIDTH']
HEIGHT = SETTING2['SCREEN']['HEIGHT']
NUMBER_ROWS = SETTING2['SCREEN']['NUMBER_ROWS']
NUMBER_COLUMNS = SETTING2['SCREEN']['NUMBER_COLUMNS']
CELL_SIZE = SETTING2['SCREEN']['CELL_SIZE']
FOOD = SETTING2['FOOD']


###########   Load data of foods from json file   ###########################################################
def loadPreviousFoodManager(numberPlayers=1):
    dict = None
    if numberPlayers == 1:
        with open('./data/player/onePlayer/food/food.json', 'r') as file:
            dict = json.load(file)
        file.close()
    elif numberPlayers == 2:
        with open('./data/player/twoPlayer/food/food.json', 'r') as file:
            dict = json.load(file)
        file.close()
    
    listFood = []
    for food in dict['FOODS']:
        listFood.append(Food(x=food['x'], y=food['y'], indexFrame=food['indexFrame']))
        
    return FoodManager(listFood=listFood)

###########   Save data of current foods to json file   #####################################################
def saveFoodManager(foodManager=[], numberPlayers=1):
    data = {
        'FOODS' : [
           
        ]
    }
    
    for food in foodManager.listFood:
        data['FOODS'].append(
            {
                'x' : food.x,
                'y' : food.y,
                'indexFrame' : food.indexFrame
            }
        )
    
    if numberPlayers == 1:
        with open('./data/player/onePlayer/food/food.json', 'w') as file:
            json.dump(data, file, indent=4)
        file.close()
    elif numberPlayers == 2:
        with open('./data/player/twoPlayer/food/food.json', 'w') as file:
            json.dump(data, file, indent=4)
        file.close()


###########  CLASS FOOD  ####################################################################################
class Food:
    ########### Constructor  ################################################################################
    def __init__(self, x, y, indexFrame=0):
        ###########  Create surface   #######################################################################
        self.surface = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (x, y)
        self.x = x
        self.y = y
        ###########  Default image food  ####################################################################
        self.surface.blit(FOOD[0], (0, 0))
        self.indexFrame = indexFrame
    
    ###########  Get coordinate of food  ####################################################################
    def coordinate(self):
        return [self.x, self.y]
    
    ###########  Update image of food  ######################################################################
    def update(self):
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
    def __init__(self, listFood=[]):
        ###########  Surface and coordinate #################################################################
        self.surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (0, 0)
        ###########  List food anf  number of foods  ########################################################
        self.listFood = listFood
        self.maxFood = SETTING1['FOOD']['MAX_FOOD']
        self.animationSpeed = SETTING1['FOOD']['ANIMATION_SPEED']
    
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
        
    ###########   Update animation of foods   ###############################################################
    def updateAnimation(self):
        ###########   Remove old images   ###################################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new images   #####################################################################
        for food in self.listFood:
            food.indexFrame = (food.indexFrame + 1) % 4
            food.update()
            food.draw(self.surface)
    
    ###########  Draw all foods on another surface  #########################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect) 