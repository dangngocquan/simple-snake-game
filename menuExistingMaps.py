import pygame
from snake import Snake
from setting import *
import setting
from wall import Wall, WallManager
import wall
from grid import Grid
from grid import *
from button import Button

###########   VARIABLE   ####################################################################################
ANIMATION_SPEED = SETTING1['MENU']['ANIMATION_SPEED']
BIG_FONT = SETTING2['MENU']['BIG_FONT']
MEDIUM_FONT = SETTING2['MENU']['MEDIUM_FONT']
MEDIUM_FONT_HORVED = SETTING2['MENU']['MEDIUM_FONT_HORVED']
MEDIUM_FONT_2 = SETTING2['MENU']['MEDIUM_FONT_2']
SMALL_FONT = SETTING2['MENU']['SMALL_FONT']
DESCRIPTION_FONT = SETTING2['MENU']['DESCRIPTION_FONT']
WHITE = SETTING2['COLOR']['WHITE']



#############  CLASS EXISTING MAPS MENU  ######################################################################
class ExistingMapsMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        
        self.surfaceInfo1 = pygame.Surface((width//4-10, height//4*3+10), pygame.SRCALPHA)
        self.surfaceInfo1Rect = self.surfaceInfo1.get_rect()
        self.surfaceInfo1Rect.topleft = (0, 0)
        
        self.surfaceInfo2 = pygame.Surface((width, height//4-10), pygame.SRCALPHA)
        self.surfaceInfo2Rect = self.surfaceInfo2.get_rect()
        self.surfaceInfo2Rect.topleft = (0, height//4*3+10)
        
        self.grid = Grid(0, 0, widthLine=2)
        self.wallManager = WallManager(listWall=wall.LIST_MAP[SETTING1['MAP']['INDEX_MAP']]['WALLS'])
        self.picture = pygame.Surface((width, height), pygame.SRCALPHA)
        self.pictureRect = self.picture.get_rect()
        self.pictureRect.center = (x, y)
        
        self.surfaceViewMap = pygame.Surface((width//4*3+10, height//4*3+10), pygame.SRCALPHA)
        self.surfaceViewMapRect = self.surfaceViewMap.get_rect()
        self.surfaceViewMapRect.topleft = (width//4-10, 0)
        
        self.picture2 = pygame.Surface((width//4*3, height//4*3), pygame.SRCALPHA)
        self.picture2Rect = self.picture2.get_rect()
        self.picture2Rect.center = (self.surfaceViewMapRect.width//2, self.surfaceViewMapRect.height//2)
        
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        ########### Buttons in Existing Maps Menu  ##############################################################
        self.titleIndexMap = Button(f"MAP {SETTING1['MAP']['INDEX_MAP']+1:0>2}", 
                                    SMALL_FONT, self.surfaceInfo1Rect.width//2, 
                                    self.surfaceInfo1Rect.height//12*2)
        self.titleNumberOfMap = Button(f"NUMBER MAPS: {len(wall.LIST_MAP)}", 
                                    DESCRIPTION_FONT_2, self.surfaceInfo1Rect.width//8, 
                                    self.surfaceInfo1Rect.height//12*4, 'topLeft')
        self.titleCreatedTime = Button(f"Created Time:  {wall.LIST_MAP[SETTING1['MAP']['INDEX_MAP']]['CREATED_TIME']:0>2}", 
                                    DESCRIPTION_FONT, self.surfaceInfo2Rect.width//24, 
                                    self.surfaceInfo2Rect.height//10, 'topLeft')
        self.titleNumberOfWalls = Button(f"Number of Walls:  {len(wall.LIST_MAP[SETTING1['MAP']['INDEX_MAP']]['WALLS'])}", 
                                    DESCRIPTION_FONT, self.surfaceInfo2Rect.width//24, 
                                    self.surfaceInfo2Rect.height//10*3, 'topLeft')
        self.titleDescription = Button("", DESCRIPTION_FONT_2, self.surfaceInfo2Rect.width//24, 
                                    self.surfaceInfo2Rect.height//10*5, 'topLeft')
        self.titleDescription2 = Button("", DESCRIPTION_FONT_2, self.surfaceInfo2Rect.width//24, 
                                    self.surfaceInfo2Rect.height//10*7, 'topLeft')
        
        
        
    ###########   Update cursor and buttons status in Options Menu   ########################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleIndexMap.isChosen = True
        else:
            self.titleIndexMap.isChosen = False
        self.titleIndexMap.update(f"MAP {SETTING1['MAP']['INDEX_MAP']+1:0>2}", SMALL_FONT, 'B')
        self.titleNumberOfMap = Button(f"NUMBER MAPS: {len(wall.LIST_MAP)}", 
                                    DESCRIPTION_FONT_2, self.surfaceInfo1Rect.width//8, 
                                    self.surfaceInfo1Rect.height//12*4, 'topLeft')
        self.titleCreatedTime = Button(f"Created Time:  {wall.LIST_MAP[SETTING1['MAP']['INDEX_MAP']]['CREATED_TIME']:0>2}", 
                                    DESCRIPTION_FONT_2, self.surfaceInfo2Rect.width//24, 
                                    self.surfaceInfo2Rect.height//10, 'topLeft')
        self.titleNumberOfWalls = Button(f"Number of Walls:  {len(wall.LIST_MAP[SETTING1['MAP']['INDEX_MAP']]['WALLS'])}", 
                                    DESCRIPTION_FONT_2, self.surfaceInfo2Rect.width//24, 
                                    self.surfaceInfo2Rect.height//10*3, 'topLeft')
        if SETTING1['MAP']['INDEX_MAP'] > 0:
            self.titleDescription = Button("Press 'K' to delete this map.", 
                                           DESCRIPTION_FONT_2, self.surfaceInfo2Rect.width//24, 
                                    self.surfaceInfo2Rect.height//10*5, 'topLeft')
        else:
            self.titleDescription = Button("This is default map, you can't delete this map.", 
                                           DESCRIPTION_FONT_2, self.surfaceInfo2Rect.width//24, 
                                    self.surfaceInfo2Rect.height//10*5, 'topLeft')
        self.titleDescription2 = Button("Press A/W/D/S to change your map. Press 'Enter' to save your choice.", 
                                        DESCRIPTION_FONT_2, self.surfaceInfo2Rect.width//24, 
                                    self.surfaceInfo2Rect.height//10*7, 'topLeft')
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        self.surfaceInfo1.fill((0, 0, 0, 0))
        self.surfaceInfo2.fill((0, 0, 0, 0))
        self.picture.fill((0, 0, 0, 0))
        self.surfaceViewMap.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
        self.titleIndexMap.draw(self.surfaceInfo1)
        self.titleNumberOfMap.draw(self.surfaceInfo1)
        self.titleCreatedTime.draw(self.surfaceInfo2)
        self.titleNumberOfWalls.draw(self.surfaceInfo2)
        self.titleDescription.draw(self.surfaceInfo2)
        self.titleDescription2.draw(self.surfaceInfo2)
        
        self.wallManager = WallManager(listWall=wall.LIST_MAP[SETTING1['MAP']['INDEX_MAP']]['WALLS'])
        self.picture.fill((0, 0, 0))
        self.picture.blit(self.wallManager.surface, self.wallManager.surfaceRect)
        self.picture.blit(self.grid.surface, self.grid.surfaceRect)
        self.picture2 = pygame.transform.scale(self.picture, 
                                                     (self.surfaceRect.width//4*3, self.surfaceRect.height//4*3))
        self.picture2Rect = self.picture2.get_rect()
        self.picture2Rect.center = (self.surfaceViewMapRect.width//2, self.surfaceViewMapRect.height//2)
        self.surfaceViewMap.fill((199, 237, 203))
        self.surfaceViewMap.blit(self.picture2, self.picture2Rect)
        
        self.surface.blit(self.surfaceInfo1, self.surfaceInfo1Rect)
        self.surface.blit(self.surfaceInfo2, self.surfaceInfo2Rect)
        self.surface.blit(self.surfaceViewMap, self.surfaceViewMapRect)
        

    ###########  Draw PlayGame Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)