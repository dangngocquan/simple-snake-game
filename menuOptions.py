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


###########  CLASS OPTIONS MENU  ##########################################################################
class OptionsMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        ########### Buttons in Options Menu  ##############################################################
        self.titleGamemodeSetting = Button("GAME MODE SETTING", MEDIUM_FONT, width//2, height*2//12)
        self.titleGameSetting = Button("GAME SETTING", MEDIUM_FONT, width//2, height*4//12)
        self.titleSoundSetting = Button("SOUND SETTING", MEDIUM_FONT, width//2, height*6//12)
        self.titleMapSetting = Button("MAP SETTING", MEDIUM_FONT, width//2, height*8//12)
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*10//12)
        
    ###########   Update cursor and buttons status in Options Menu   ########################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleGamemodeSetting.isChosen = True
            self.titleGamemodeSetting.update('GAME MODE SETTING', MEDIUM_FONT_HORVED, 'G')
            self.titleGameSetting.update('GAME SETTING', MEDIUM_FONT, 'G')
            self.titleSoundSetting.update('SOUND SETTING', MEDIUM_FONT, 'G')
            self.titleMapSetting.update('MAP SETTING', MEDIUM_FONT, 'G')
            self.titleBack.update('BACK', MEDIUM_FONT, 'G')
        else:
            self.titleGamemodeSetting.isChosen = False
        if self.cursor == 1:
            self.titleGameSetting.isChosen = True
            self.titleGamemodeSetting.update('GAME MODE SETTING', MEDIUM_FONT, 'G')
            self.titleGameSetting.update('GAME SETTING', MEDIUM_FONT_HORVED, 'G')
            self.titleSoundSetting.update('SOUND SETTING', MEDIUM_FONT, 'G')
            self.titleMapSetting.update('MAP SETTING', MEDIUM_FONT, 'G')
            self.titleBack.update('BACK', MEDIUM_FONT, 'G')
        else:
            self.titleGameSetting.isChosen = False
        if self.cursor == 2:
            self.titleSoundSetting.isChosen = True
            self.titleGamemodeSetting.update('GAME MODE SETTING', MEDIUM_FONT, 'G')
            self.titleGameSetting.update('GAME SETTING', MEDIUM_FONT, 'G')
            self.titleSoundSetting.update('SOUND SETTING', MEDIUM_FONT_HORVED, 'G')
            self.titleMapSetting.update('MAP SETTING', MEDIUM_FONT, 'G')
            self.titleBack.update('BACK', MEDIUM_FONT, 'G')
        else:
            self.titleSoundSetting.isChosen = False
        if self.cursor == 3:
            self.titleMapSetting.isChosen = True
            self.titleGamemodeSetting.update('GAME MODE SETTING', MEDIUM_FONT, 'G')
            self.titleGameSetting.update('GAME SETTING', MEDIUM_FONT, 'G')
            self.titleSoundSetting.update('SOUND SETTING', MEDIUM_FONT, 'G')
            self.titleMapSetting.update('MAP SETTING', MEDIUM_FONT_HORVED, 'G')
            self.titleBack.update('BACK', MEDIUM_FONT, 'G')
        else:
            self.titleMapSetting.isChosen = False
        if self.cursor == 4:
            self.titleBack.isChosen = True
            self.titleGamemodeSetting.update('GAME MODE SETTING', MEDIUM_FONT, 'G')
            self.titleGameSetting.update('GAME SETTING', MEDIUM_FONT, 'G')
            self.titleSoundSetting.update('SOUND SETTING', MEDIUM_FONT, 'G')
            self.titleMapSetting.update('MAP SETTING', MEDIUM_FONT, 'G')
            self.titleBack.update('BACK', MEDIUM_FONT_HORVED, 'G')
        else:
            self.titleBack.isChosen = False
        
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
        self.titleGamemodeSetting.draw(self.surface)
        self.titleGameSetting.draw(self.surface)
        self.titleSoundSetting.draw(self.surface)
        self.titleMapSetting.draw(self.surface)
        self.titleBack.draw(self.surface)
        
    ###########  Draw Gamemode settings Menu in another surface  ######################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)