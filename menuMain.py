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
        ########### Buttons   ###############################################################################
        self.titleSimpleSnake = Button("SIMPLE SNAKE", BIG_FONT, width//2, height//6)
        self.titleSimpleSnake.isChosen = True
        self.titlePlayGame = Button("PLAY GAME", MEDIUM_FONT, width//2, height*4//12)
        self.titleOptions = Button("OPTIONS", MEDIUM_FONT, width//2, height*6//12)
        self.titleAboutGame = Button("ABOUT GAME", MEDIUM_FONT, width//2, height*8//12)
        self.titleQuitGame = Button("QUIT GAME", MEDIUM_FONT, width//2, height*10//12)
        
    ###########  Update cursor and button status in Main Menu ###############################################
    def update(self):
        ###########  Update cursor and button of main menu  #################################################
        if self.cursor == 0:
            self.titlePlayGame.isChosen = True
            self.titleOptions.isChosen = False
            self.titleAboutGame.isChosen = False
            self.titleQuitGame.isChosen = False
            self.titleSimpleSnake.update('SIMPLE SNAKE', BIG_FONT, 'ALL')
            self.titlePlayGame.update('PLAY GAME', MEDIUM_FONT_HORVED)
            self.titleOptions.update('OPTIONS', MEDIUM_FONT)
            self.titleAboutGame.update("ABOUT GAME", MEDIUM_FONT)
            self.titleQuitGame.update('QUIT GAME', MEDIUM_FONT)
        elif self.cursor == 1:
            self.titlePlayGame.isChosen = False
            self.titleOptions.isChosen = True
            self.titleAboutGame.isChosen = False
            self.titleQuitGame.isChosen = False
            self.titleSimpleSnake.update('SIMPLE SNAKE', BIG_FONT, 'ALL')
            self.titlePlayGame.update('PLAY GAME', MEDIUM_FONT)
            self.titleOptions.update('OPTIONS', MEDIUM_FONT_HORVED)
            self.titleAboutGame.update("ABOUT GAME", MEDIUM_FONT)
            self.titleQuitGame.update('QUIT GAME', MEDIUM_FONT)
        elif self.cursor == 2:
            self.titlePlayGame.isChosen = False
            self.titleOptions.isChosen = False
            self.titleAboutGame.isChosen = True
            self.titleQuitGame.isChosen = False
            self.titleSimpleSnake.update('SIMPLE SNAKE', BIG_FONT, 'ALL')
            self.titlePlayGame.update('PLAY GAME', MEDIUM_FONT)
            self.titleOptions.update('OPTIONS', MEDIUM_FONT)
            self.titleAboutGame.update("ABOUT GAME", MEDIUM_FONT_HORVED)
            self.titleQuitGame.update('QUIT GAME', MEDIUM_FONT)
        elif self.cursor == 3:
            self.titlePlayGame.isChosen = False
            self.titleOptions.isChosen = False
            self.titleAboutGame.isChosen = False
            self.titleQuitGame.isChosen = True
            self.titleSimpleSnake.update('SIMPLE SNAKE', BIG_FONT, 'ALL')
            self.titlePlayGame.update('PLAY GAME', MEDIUM_FONT)
            self.titleOptions.update('OPTIONS', MEDIUM_FONT)
            self.titleAboutGame.update("ABOUT GAME", MEDIUM_FONT)
            self.titleQuitGame.update('QUIT GAME', MEDIUM_FONT_HORVED)
        ###########  Remove old button display  #############################################################
        self.surface.fill((0, 0, 0, 0))
        ###########  Draw new button   ######################################################################
        self.titleSimpleSnake.draw(self.surface)
        self.titlePlayGame.draw(self.surface)
        self.titleOptions.draw(self.surface)
        self.titleAboutGame.draw(self.surface)
        self.titleQuitGame.draw(self.surface)
    
    ###########  Draw Main Menu in another surface  #########################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)