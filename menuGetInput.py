import pygame
from setting import *
import setting
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


###########  CLASS GET PASSWORD MENU  ###############################################################################
class GetPasswordMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor   ######################################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        ########### Buttons   ###############################################################################
        self.titlePassword = Button("PASSWORD", MEDIUM_FONT, width//2, 0)
        self.titlePassword.isChosen = True
        self.titleCancer = Button("CANCER", MEDIUM_FONT, width//4, height)
        self.titleEnter = Button("ENTER", MEDIUM_FONT, width//4*3, height)
        
    ###########  Update cursor and button status in Main Menu ###############################################
    def update(self):
        ###########  Update cursor and button of main menu  #################################################
        if self.cursor == 0:
            self.titleEnter.isChosen = True
            self.titleCancer.isChosen = False
            self.titleEnter.update('ENTER', MEDIUM_FONT_HORVED, 'G')
            self.titleCancer.update('CANCER', MEDIUM_FONT, 'G')
        elif self.cursor == 1:
            self.titleEnter.isChosen = False
            self.titleCancer.isChosen = True
            self.titleEnter.update('ENTER', MEDIUM_FONT, 'G')
            self.titleCancer.update('CANCER', MEDIUM_FONT_HORVED, 'G')
        self.titlePassword.update("PASSWORD", MEDIUM_FONT, 'ALL')
        ###########  Remove old button display  #############################################################
        self.surface.fill((255, 255, 255))
        ###########  Draw new button   ######################################################################
        self.titlePassword.draw(self.surface)
        self.titleEnter.draw(self.surface)
        self.titleCancer.draw(self.surface)
        
    
    ###########  Draw Main Menu in another surface  #########################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)