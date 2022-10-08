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


###########   Load list map from json file   ################################################################
def loadListMaps(path='./data/setting/map.json'):
    dict = None
    with open(path, 'r') as file:
        dict = json.load(file)
    file.close()
    
    listMap = []
    for dictMap in dict['MAPS']:
        listWall = []
        createdTime = dictMap['CREATED_TIME']
        for wall in dictMap['WALLS']:
            listWall.append(Wall(x=wall['x'], y=wall['y']))
        listMap.append({
            "WALLS" : listWall,
            "CREATED_TIME" : createdTime
        })
    return listMap

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
    listMap = loadListMaps(path)
    if indexMap >= len(listMap):
        indexMap = 0
    return WallManager(listWall=listMap[indexMap]['WALLS'])


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
        

################ LIST MAPS   ################################################################################       
LIST_MAP = loadListMaps()

################   Update new version of LIST MAPS   ########################################################
def updateListMaps():
    LIST_MAP = loadListMaps()
    
###########   Save data of map   ############################################################################
def addNewMapToListMaps(wallManager, createdTime, path='./data/setting/map.json'):
    newMap = {
        'WALLS' : [
           
        ],
        'CREATED_TIME' : createdTime
    }
    
    for wall in wallManager.listWall:
        newMap['WALLS'].append(
            {
                'x' : wall.x,
                'y' : wall.y,
            }
        )
    
    LIST_MAP.append(newMap)
    
    data = {
            "MAPS" : []
        }
    for map in LIST_MAP:
        WALLS = []
        createdTime = map['CREATED_TIME']
        for wall in map['WALLS']:
            WALLS.append({
                "x" : wall.x,
                "y" : wall.y
            })
        data['MAPS'].append({
            "WALLS" : WALLS,
            'CREATED_TIME' : createdTime
        })
    
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
    file.close()
    updateListMaps()


###########   Remove map from list maps  ####################################################################
def removeMapTFromListMaps(path='./data/setting/map.json', indexMap=0):
    if indexMap > 0:
        LIST_MAP.pop(indexMap)
        
        data = {
            "MAPS" : []
        }
        for map in LIST_MAP:
            WALLS = []
            createdTime = map['CREATED_TIME']
            for wall in map['WALLS']:
                WALLS.append({
                    "x" : wall.x,
                    "y" : wall.y
                })
            data['MAPS'].append({
                "WALLS" : WALLS,
                'CREATED_TIME' : createdTime
            })
        
        with open(path, 'w') as file:
            json.dump(data, file, indent=4)
        file.close()
        updateListMaps()