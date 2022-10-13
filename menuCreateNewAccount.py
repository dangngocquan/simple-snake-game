from datetime import datetime
from time import strftime
import pygame
from account import ACCOUNT_MANAGER, Account
from setting import *
import setting
from grid import *
from button import Button
from menuGetInput import GetInputStringMenu
import account

###########   VARIABLE   ####################################################################################
ANIMATION_SPEED = SETTING1['MENU']['ANIMATION_SPEED']
BIG_FONT = SETTING2['MENU']['BIG_FONT']
MEDIUM_FONT = SETTING2['MENU']['MEDIUM_FONT']
MEDIUM_FONT_HORVED = SETTING2['MENU']['MEDIUM_FONT_HORVED']
MEDIUM_FONT_2 = SETTING2['MENU']['MEDIUM_FONT_2']
SMALL_FONT = SETTING2['MENU']['SMALL_FONT']
DESCRIPTION_FONT = SETTING2['MENU']['DESCRIPTION_FONT']
WHITE = SETTING2['COLOR']['WHITE']


###########  CLASS MAIN MENU  ###############################################################################
class CreateNewAccountMenu:
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
        self.getInputStringMenu = GetInputStringMenu(WIDTH//2, HEIGHT//2, WIDTH//4*3, HEIGHT//2
                                                     , title="YOUR NAME")
    
    def updatePostionMouse(self, position):
        self.positionMouse = position
        
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
                            surfaceCheckRect=self.getInputStringMenu.titleCancer.textRect,
                            parent1SurfaceRect=self.getInputStringMenu.surfaceRect):
            self.getInputStringMenu.cursor = 1
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.getInputStringMenu.titleEnter.textRect,
                            parent1SurfaceRect=self.getInputStringMenu.surfaceRect):
            self.getInputStringMenu.cursor = 0
        else:
            self.getInputStringMenu.cursor = 2
    
    
    def updatePositionLeftMouse(self):
        self.positionLeftMouse = self.positionMouse
        if self.isPointedAt(positionMouse=self.positionLeftMouse,
                            surfaceCheckRect=self.getInputStringMenu.titleCancer.textRect,
                            parent1SurfaceRect=self.getInputStringMenu.surfaceRect):
            self.cursor = -1
        elif self.isPointedAt(positionMouse=self.positionLeftMouse,
                            surfaceCheckRect=self.getInputStringMenu.titleEnter.textRect,
                            parent1SurfaceRect=self.getInputStringMenu.surfaceRect):
            if len(self.getInputStringMenu.inputString) == 0:
                self.getInputStringMenu.titleDescription.update(
                    self.getInputStringMenu.textWhenIncorrect, DESCRIPTION_FONT_2, 'G')
            else:
                if ACCOUNT_MANAGER.addNewAccount(Account(name=self.getInputStringMenu.inputString,
                                                         createdTime=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))):
                    self.getInputStringMenu.titleDescription.update(
                    self.getInputStringMenu.textWhenCorrect, DESCRIPTION_FONT_2, 'G')
                    self.cursor = 1
                    account.saveData(ACCOUNT_MANAGER.listAccount)
                else:
                    self.getInputStringMenu.titleDescription.update(
                    self.getInputStringMenu.textWhenIncorrect, DESCRIPTION_FONT_2, 'G')
    
    ###########  Update cursor and button status in Main Menu ###############################################
    def update(self):
        ###########  Update cursor and button of main menu  #################################################
        self.updateMousePoitedAt()
        self.getInputStringMenu.update()
        ###########  Remove old button display  #############################################################
        self.surface.fill((0, 0, 0, 0))
        ###########  Draw new button   ######################################################################
        self.getInputStringMenu.draw(self.surface)
    
    ###########  Draw Main Menu in another surface  #########################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)