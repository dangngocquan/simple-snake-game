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
WALL = SETTING2['WALL']


###########   Load data of walls from json file   ###########################################################
def loadPreviousWallManager(path='./data/player/onePlayer/wall/wall.json'):
    dict = None

    with open(path, 'r') as file:
        dict = json.load(file)
    file.close()
    
    listWall = []
    for wall in dict['WALLS']:
        listWall.append(Wall(x=wall['x'], y=wall['y']))
        
    return WallManager(listWall=listWall)

###########   Load data of walls from list maps json file   #################################################
def loadWallManagerFromListMaps(path='./data/setting/map.json', indexMap=0):
    dict = None

    with open(path, 'r') as file:
        dict = json.load(file)
    file.close()
    
    listWall = []
    if indexMap >= len(dict['MAPS']):
        indexMap = 0
    for wall in dict['MAPS'][indexMap]['WALLS']:
        listWall.append(Wall(x=wall['x'], y=wall['y']))
        
    return WallManager(listWall=listWall)


###########   Save data of current walls to json file   #####################################################
def saveWallManager(wallManager, path='./data/player/onePlayer/wall/wall.json'):
    data = {
        'WALLS' : [
           
        ]
    }
    
    for wall in wallManager.listWall:
        data['WALLS'].append(
            {
                'x' : wall.x,
                'y' : wall.y,
            }
        )
    
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
    file.close()

###########   Save data of map   ############################################################################
def saveWallManagerToListMaps(wallManager, path='./data/setting/map.json'):
    map = {
        'WALLS' : [
           
        ]
    }
    
    for wall in wallManager.listWall:
        map['WALLS'].append(
            {
                'x' : wall.x,
                'y' : wall.y,
            }
        )
    
    dict = None
    with open(path, 'r') as file:
        dict = json.load(file)
    file.close()
    
    dict['MAPS'].append(map)
    
    with open(path, 'w') as file:
        json.dump(dict, file, indent=4)
    file.close()


###########  CLASS WALL  ####################################################################################
class Wall:
    ########### Constructor  ################################################################################
    def __init__(self, x, y):
        ###########  Create surface   #######################################################################
        self.surface = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (x, y)
        self.x = x
        self.y = y
        ###########  Default image wall  ####################################################################
        self.surface.blit(WALL[0], (0, 0))
    
    ###########  Get coordinate of wall  ####################################################################
    def coordinate(self):
        return [self.x, self.y]
    
    ###########  Update image of wall  ######################################################################
    def update(self):
        pass
    
    ###########  Draw wall on another surface  ##############################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        

###########  CLASS WALL MANAGER  ############################################################################
class WallManager:
    ###########  Constructor  ###############################################################################
    def __init__(self, listWall=[]):
        ###########  Surface and coordinate #################################################################
        self.surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (0, 0)
        ###########  List wall   ############################################################################
        self.listWall = listWall
        ###########   Draw images   #########################################################################
        for wall in self.listWall:
            wall.draw(self.surface)
    
    ###########  Get coordinate of all foods ################################################################
    def coordinateWalls(self):
        return [wall.coordinate() for wall in self.listWall]
    
    ###########  Draw all foods on another surface  #########################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect) 