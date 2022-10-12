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


###########  CLASS ACCOUNTS SETTING MENU  ###############################################################################
class AccountsSettingMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor   ######################################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        ########### Buttons   ###############################################################################
        self.titleChangeAccount = Button("EXISTING ACCOUNT", MEDIUM_FONT, width//2, height*4//12)
        self.titleCreateNewAccount = Button("CREATE NEW ACCOUNT", MEDIUM_FONT, width//2, height*6//12)
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*8//12)
        
    ###########  Update cursor and button status in Accounts Setting Menu ###############################################
    def update(self):
        ###########  Update cursor and button of Accounts Setting menu  #################################################
        if self.cursor == 0:
            self.titleChangeAccount.isChosen = True
            self.titleCreateNewAccount.isChosen = False
            self.titleBack.isChosen = False
            self.titleChangeAccount.update('EXISTING ACCOUNT', MEDIUM_FONT_HORVED)
            self.titleCreateNewAccount.update('CREATE NEW ACCOUNT', MEDIUM_FONT)
            self.titleBack.update("BACK", MEDIUM_FONT)
        elif self.cursor == 1:
            self.titleChangeAccount.isChosen = False
            self.titleCreateNewAccount.isChosen = True
            self.titleBack.isChosen = False
            self.titleChangeAccount.update('EXISTING ACCOUNT', MEDIUM_FONT)
            self.titleCreateNewAccount.update('CREATE NEW ACCOUNT', MEDIUM_FONT_HORVED)
            self.titleBack.update("BACK", MEDIUM_FONT)
        elif self.cursor == 2:
            self.titleChangeAccount.isChosen = False
            self.titleCreateNewAccount.isChosen = False
            self.titleBack.isChosen = True
            self.titleChangeAccount.update('EXISTING ACCOUNT', MEDIUM_FONT)
            self.titleCreateNewAccount.update('CREATE NEW ACCOUNT', MEDIUM_FONT)
            self.titleBack.update("BACK", MEDIUM_FONT_HORVED)
        ###########  Remove old button display  #############################################################
        self.surface.fill((0, 0, 0, 0))
        ###########  Draw new button   ######################################################################
        self.titleChangeAccount.draw(self.surface)
        self.titleCreateNewAccount.draw(self.surface)
        self.titleBack.draw(self.surface)    
        
    ###########  Draw Accounts Setting Menu in another surface  #########################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)