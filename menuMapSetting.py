import datetime
import random
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


###########  CLASS MAP SETTING MENU  ########################################################################
class MapSettingMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        ########### Buttons in Options Menu  ##############################################################
        self.titleExistingMap = Button("EXISTING MAPS", MEDIUM_FONT, width//2, height*3//12)
        self.titleCreateNewMap = Button("CREATE NEW MAP", MEDIUM_FONT, width//2, height*5//12)
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*7//12)
        
    ###########   Update cursor and buttons status in Options Menu   ########################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleExistingMap.isChosen = True
            self.titleCreateNewMap.isChosen = False
            self.titleBack.isChosen = False
            self.titleExistingMap.update('EXISTING MAPS', MEDIUM_FONT_HORVED)
            self.titleCreateNewMap.update('CREATE NEW MAP', MEDIUM_FONT)
            self.titleBack.update('BACK', MEDIUM_FONT)
        elif self.cursor == 1:
            self.titleExistingMap.isChosen = False
            self.titleCreateNewMap.isChosen = True
            self.titleBack.isChosen = False
            self.titleExistingMap.update('EXISTING MAPS', MEDIUM_FONT)
            self.titleCreateNewMap.update('CREATE NEW MAP', MEDIUM_FONT_HORVED)
            self.titleBack.update('BACK', MEDIUM_FONT)
        elif self.cursor == 2:
            self.titleExistingMap.isChosen = False
            self.titleCreateNewMap.isChosen = False
            self.titleBack.isChosen = True
            self.titleExistingMap.update('EXISTING MAPS', MEDIUM_FONT)
            self.titleCreateNewMap.update('CREATE NEW MAP', MEDIUM_FONT)
            self.titleBack.update('BACK', MEDIUM_FONT_HORVED)
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
        self.titleExistingMap.draw(self.surface)
        self.titleCreateNewMap.draw(self.surface)
        self.titleBack.draw(self.surface)
    
    ###########  Draw PlayGame Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)