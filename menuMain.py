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


###########  CLASS MAIN MENU  ###############################################################################
class MainMenu:
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
        self.titleSimpleSnake = Button("SIMPLE SNAKE", BIG_FONT, width//2, height//24*2)
        self.titleSimpleSnake.isChosen = True
        self.titlePlayGame = Button("PLAY GAME", MEDIUM_FONT, width//2, height*12//48)
        self.titleAccount = Button("ACCOUNT", MEDIUM_FONT, width//2, height*17//48)
        self.titleOptions = Button("OPTIONS", MEDIUM_FONT, width//2, height*22//48)
        self.titleStatistics = Button("STATISTICS", MEDIUM_FONT, width//2, height*27//48)
        self.titleHistory = Button("HISTORY", MEDIUM_FONT, width//2, height*32//48)
        self.titleAboutGame = Button("ABOUT GAME", MEDIUM_FONT, width//2, height*37//48)
        self.titleQuitGame = Button("QUIT GAME", MEDIUM_FONT, width//2, height*42//48)
    
    
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
                            surfaceCheckRect=self.titlePlayGame.textRect):
            self.titlePlayGame.isChosen = True
            self.titlePlayGame.update('PLAY GAME', MEDIUM_FONT_HORVED)
        else:
            self.titlePlayGame.isChosen = False
            self.titlePlayGame.update('PLAY GAME', MEDIUM_FONT)
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleAccount.textRect):
            self.titleAccount.isChosen = True
            self.titleAccount.update("ACCOUNT", MEDIUM_FONT_HORVED)
        else:
            self.titleAccount.isChosen = False
            self.titleAccount.update("ACCOUNT", MEDIUM_FONT)
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleOptions.textRect):
            self.titleOptions.isChosen = True
            self.titleOptions.update('OPTIONS', MEDIUM_FONT_HORVED)
        else:
            self.titleOptions.isChosen = False
            self.titleOptions.update('OPTIONS', MEDIUM_FONT)
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleStatistics.textRect):
            self.titleStatistics.isChosen = True
            self.titleStatistics.update("STATISTICS", MEDIUM_FONT_HORVED, 'G')
        else:
            self.titleStatistics.isChosen = False
            self.titleStatistics.update("STATISTICS", MEDIUM_FONT, 'G')
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleHistory.textRect):
            self.titleHistory.isChosen = True
            self.titleHistory.update("HISTORY", MEDIUM_FONT_HORVED, 'G')
        else:
            self.titleHistory.isChosen = False
            self.titleHistory.update("HISTORY", MEDIUM_FONT, 'G')
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleAboutGame.textRect):
            self.titleAboutGame.isChosen = True
            self.titleAboutGame.update("ABOUT GAME", MEDIUM_FONT_HORVED)
        else:
            self.titleAboutGame.isChosen = False
            self.titleAboutGame.update("ABOUT GAME", MEDIUM_FONT)
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleQuitGame.textRect):
            self.titleQuitGame.isChosen = True
            self.titleQuitGame.update('QUIT GAME', MEDIUM_FONT_HORVED)
        else:
            self.titleQuitGame.isChosen = False
            self.titleQuitGame.update('QUIT GAME', MEDIUM_FONT)
    
    ###############     Update when player left-click    ####################################################
    def updatePositionLeftMouse(self):
        self.positionLeftMouse = self.positionMouse
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titlePlayGame.textRect):
            self.cursor = 0
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleAccount.textRect):
            self.cursor = 1
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleOptions.textRect):
            self.cursor = 2
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleStatistics.textRect):
            self.cursor = 3
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleHistory.textRect):
            self.cursor = 4
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleAboutGame.textRect):
            self.cursor = 5
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleQuitGame.textRect):
            self.cursor = 6
        else:
            self.cursor = 7
        self.positionLeftMouse = (-100, -100)
    
      
    ###########  Update cursor and button status in Main Menu ###############################################
    def update(self):
        self.updateMousePoitedAt()
        ###########  Update cursor and button of main menu  #################################################
        self.titleSimpleSnake.update('SIMPLE SNAKE', BIG_FONT, 'ALL')
        ###########  Remove old button display  #############################################################
        self.surface.fill((0, 0, 0, 0))
        ###########  Draw new button   ######################################################################
        
        self.titleSimpleSnake.draw(self.surface)
        self.titlePlayGame.draw(self.surface)
        self.titleAccount.draw(self.surface)
        self.titleOptions.draw(self.surface)
        self.titleStatistics.draw(self.surface)
        self.titleHistory.draw(self.surface)
        self.titleAboutGame.draw(self.surface)
        self.titleQuitGame.draw(self.surface)
    
    ###########  Draw Main Menu in another surface  #########################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)