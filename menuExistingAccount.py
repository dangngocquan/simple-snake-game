from turtle import position
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


###########  CLASS EXISTING ACCOUNTS MENU  ##################################################################
class ExistingAccountMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor   ######################################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 1
        self.positionMouse = (-100, -100)
        self.positionLeftMouse = (-100, -100)
        
        ##############################   In main surface   ##################################################
        self.container1 = pygame.Surface((width//4 + 30, height), pygame.SRCALPHA)
        self.container1Rect = self.container1.get_rect()
        self.container1Rect.topleft = (0, 0)
        
        self.container2 = pygame.Surface((width-self.container1Rect.width, height), pygame.SRCALPHA)
        self.container2Rect = self.container2.get_rect()
        self.container2Rect.topleft = (self.container1Rect.width, 0)
        
        #########################   In container 1   ########################################################
        self.selection1 = pygame.Surface(
            (self.container1Rect.width, self.container1Rect.height//8), pygame.SRCALPHA)
        self.selection1Rect = self.selection1.get_rect()
        self.selection1Rect.topleft = (0, 0)
        
        
        self.selection2 = pygame.Surface(
            (self.container1Rect.width, self.container1Rect.height//8), pygame.SRCALPHA)
        self.selection2Rect = self.selection2.get_rect()
        self.selection2Rect.topleft = (0, self.container1Rect.height//8)
        
        self.selection3 = pygame.Surface(
            (self.container1Rect.width, self.container1Rect.height//8), pygame.SRCALPHA)
        self.selection3Rect = self.selection3.get_rect()
        self.selection3Rect.topleft = (0, self.container1Rect.height//8 * 2)
        
        
        ########### In selection1   #########################################################################
        self.titleCurrentAccount = Button("CURRENT ACCOUNT", DESCRIPTION_FONT,
                                         self.selection1Rect.width//2, self.selection1Rect.height//2)
        ########### In selection2   #########################################################################
        self.titleOtherAccounts = Button("OTHER ACCOUNTS", DESCRIPTION_FONT,
                                            self.selection2Rect.width//2, self.selection2Rect.height//2)
        ########### In selection3   #########################################################################
        self.titleBack = Button("BACK", DESCRIPTION_FONT, 
                                self.selection3Rect.width//2, self.selection3Rect.height//2)
        
        #################   In container 2   ################################################################
        self.container22 = pygame.Surface((self.container2Rect.width//8*5, height), pygame.SRCALPHA)
        self.container22Rect = self.container22.get_rect()
        self.container22Rect.topleft = (0, 0)
        
        self.container21 = pygame.Surface((self.container2Rect.width - self.container22Rect.width, height), pygame.SRCALPHA)
        self.container21Rect = self.container21.get_rect()
        self.container21Rect.topleft = (0, 0)
        
    
    def updatePostionMouse(self, position):
        self.positionMouse = position
        
    def updatePositonLeftMouse(self):
        self.positionLeftMouse = self.positionMouse
        if self.isPointedAt(positionMouse=self.positionLeftMouse,
                            surfaceCheckRect=self.selection1Rect,
                            parent1SurfaceRect=self.container1Rect):
            self.cursor = 0
        elif self.isPointedAt(positionMouse=self.positionLeftMouse,
                            surfaceCheckRect=self.selection2Rect,
                            parent1SurfaceRect=self.container1Rect):
            self.cursor = 1
        elif self.isPointedAt(positionMouse=self.positionLeftMouse,
                            surfaceCheckRect=self.selection3Rect,
                            parent1SurfaceRect=self.container1Rect):
            self.cursor = 2
        self.positionLeftMouse = (-100, -100)
    
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
    
    def updateMousePoitedAt(self):
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.selection1Rect,
                            parent1SurfaceRect=self.container1Rect):
            self.titleCurrentAccount.isChosen = True
            self.titleOtherAccounts.isChosen = False
            self.titleBack.isChosen = False
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.selection2Rect,
                            parent1SurfaceRect=self.container1Rect):
            self.titleCurrentAccount.isChosen = False
            self.titleOtherAccounts.isChosen = True
            self.titleBack.isChosen = False
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.selection3Rect,
                            parent1SurfaceRect=self.container1Rect):
            self.titleCurrentAccount.isChosen = False
            self.titleOtherAccounts.isChosen = False
            self.titleBack.isChosen = True
        else:
            self.titleCurrentAccount.isChosen = False
            self.titleOtherAccounts.isChosen = False
            self.titleBack.isChosen = False
    
    
       
    ###########  Update cursor and button status in Accounts Setting Menu ###############################################
    def update(self):
        ###########  Update cursor and button of Accounts Setting menu  #################################################
        self.updateMousePoitedAt()
        
        # if self.cursor == 0:
        #     pass
        # elif self.cursor == 1:
        #     pass
        # elif self.cursor == 2:
        #     pass
        self.titleCurrentAccount.update("CURRENT ACCOUNT", DESCRIPTION_FONT, 'B')
        self.titleOtherAccounts.update("OTHER ACCOUNTS", DESCRIPTION_FONT, 'B')
        self.titleBack.update("BACK", DESCRIPTION_FONT, 'B')
        ###########  Remove old display  #############################################################
        self.surface.fill((0, 0, 0, 0))
        self.container1.fill((0, 0, 0, 0))
        self.selection1.fill((0, 0, 0, 0))
        self.selection2.fill((0, 0, 0, 0))
        self.selection3.fill((0, 0, 0, 0))
        if self.cursor == 0:
            self.selection1.fill((70, 70, 70))
        elif self.cursor == 1:
            self.selection2.fill((70, 70, 70))
        elif self.cursor == 2:
            self.selection3.fill((70, 70, 70))
        self.container2.fill((111, 111, 111))
        self.container21.fill((0, 111, 111))
        self.container22.fill((111, 0, 111))
        ###########  Draw new screen   ######################################################################
        self.titleCurrentAccount.draw(self.selection1)
        self.titleOtherAccounts.draw(self.selection2)
        self.titleBack.draw(self.selection3)
        self.container1.blit(self.selection1, self.selection1Rect)
        self.container1.blit(self.selection2, self.selection2Rect)
        self.container1.blit(self.selection3, self.selection3Rect)
        self.container2.blit(self.container21, self.container21Rect)
        self.container2.blit(self.container22, self.container22Rect)
        self.surface.blit(self.container1, self.container1Rect)
        self.surface.blit(self.container2, self.container2Rect)
        
    ###########  Draw Accounts Setting Menu in another surface  #########################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)