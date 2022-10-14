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
        self.positionMouse = (-100, -100)
        self.positionLeftMouse = (-100, -100)
        ########### Buttons   ###############################################################################
        self.titleExistingAccount = Button("EXISTING ACCOUNT", MEDIUM_FONT, width//2, height*4//12)
        self.titleCreateNewAccount = Button("CREATE NEW ACCOUNT", MEDIUM_FONT, width//2, height*6//12)
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*8//12)
    
    
    ##################    Update current position of mouse    ###############################################
    def updatePositionMouse(self, position):
        self.positionMouse = position
    
    
    #############   Check if the mouse is poited at a surfaceRect   #########################################
    def isPointedAt(self, positionMouse=(0, 0), parent3SurfaceRect=None, 
                    parent2SurfaceRect=None, parent1SurfaceRect=None, surfaceCheckRect=None):
        if surfaceCheckRect == None:
            return False
        x0 = positionMouse[0]
        y0 = positionMouse[1]
        x1 = 0
        y1 = 0
        if parent3SurfaceRect != None:
            x1 += parent3SurfaceRect.topleft[0]
            y1 += parent3SurfaceRect.topleft[1]
        if parent2SurfaceRect != None:
            x1 += parent2SurfaceRect.topleft[0]
            y1 += parent2SurfaceRect.topleft[1]
        if parent1SurfaceRect != None:
            x1 += parent1SurfaceRect.topleft[0]
            y1 += parent1SurfaceRect.topleft[1]
        x1 += surfaceCheckRect.topleft[0]
        y1 += surfaceCheckRect.topleft[1]
        x2 = x1 + surfaceCheckRect.width
        y2 = y1 + surfaceCheckRect.height
        
        return (x1 < x0 and x0 < x2 and y1 < y0 and y0 < y2)
    
    #############   Update text, button is horved by mouse   ################################################
    def updateMousePoitedAt(self):
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleExistingAccount.textRect):
            self.titleExistingAccount.isChosen = True
            self.titleExistingAccount.update('EXISTING ACCOUNT', MEDIUM_FONT_HORVED)
        else:
            self.titleExistingAccount.isChosen = False
            self.titleExistingAccount.update('EXISTING ACCOUNT', MEDIUM_FONT)
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleCreateNewAccount.textRect):
            self.titleCreateNewAccount.isChosen = True
            self.titleCreateNewAccount.update("CREATE NEW ACCOUNT", MEDIUM_FONT_HORVED)
        else:
            self.titleCreateNewAccount.isChosen = False
            self.titleCreateNewAccount.update("CREATE NEW ACCOUNT", MEDIUM_FONT)
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleBack.textRect):
            self.titleBack.isChosen = True
            self.titleBack.update('BACK', MEDIUM_FONT_HORVED)
        else:
            self.titleBack.isChosen = False
            self.titleBack.update('BACK', MEDIUM_FONT)
    
    ###############     Update when player left-click    ####################################################
    def updatePositionLeftMouse(self):
        self.positionLeftMouse = self.positionMouse
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleExistingAccount.textRect):
            self.cursor = 0
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleCreateNewAccount.textRect):
            self.cursor = 1
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleBack.textRect):
            self.cursor = 2
        else:
            self.cursor = 3
        self.positionLeftMouse = (-100, -100)
    
    
    ###########  Update cursor and button status in Accounts Setting Menu ###############################################
    def update(self):
        ###########  Update cursor and button of Accounts Setting menu  #################################################
        self.updateMousePoitedAt()
        ###########  Remove old button display  #############################################################
        self.surface.fill((0, 0, 0, 0))
        ###########  Draw new button   ######################################################################
        self.titleExistingAccount.draw(self.surface)
        self.titleCreateNewAccount.draw(self.surface)
        self.titleBack.draw(self.surface)    
        
    ###########  Draw Accounts Setting Menu in another surface  #########################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)