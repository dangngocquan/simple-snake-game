import pygame
from setting import *
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



###########  CLASS ABOUT GAME MENU  ##########################################################################
class AboutGameMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        ########### Buttons in Play Game Menu  ##############################################################
        self.titleNewGame = Button("NEW GAME", MEDIUM_FONT, width//2, height*4//12)
        self.titleContinueGame = Button("CONTINUE GAME", MEDIUM_FONT, width//2, height*6//12)
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*8//12)
        
    ###########   Update cursor and buttons status in Play Game Menu   ######################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleNewGame.isChosen = True
            self.titleContinueGame.isChosen = False
            self.titleBack.isChosen = False
            self.titleNewGame.update('NEW GAME', MEDIUM_FONT_HORVED)
            self.titleContinueGame.update('CONTINUE GAME', MEDIUM_FONT)
            self.titleBack.update('BACK', MEDIUM_FONT)
        elif self.cursor == 1:
            self.titleNewGame.isChosen = False
            self.titleContinueGame.isChosen = True
            self.titleBack.isChosen = False
            self.titleNewGame.update('NEW GAME', MEDIUM_FONT)
            self.titleContinueGame.update('CONTINUE GAME', MEDIUM_FONT_HORVED)
            self.titleBack.update('BACK', MEDIUM_FONT)
        elif self.cursor == 2:
            self.titleNewGame.isChosen = False
            self.titleContinueGame.isChosen = False
            self.titleBack.isChosen = True
            self.titleNewGame.update('NEW GAME', MEDIUM_FONT)
            self.titleContinueGame.update('CONTINUE GAME', MEDIUM_FONT)
            self.titleBack.update('BACK', MEDIUM_FONT_HORVED)
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
        self.titleNewGame.draw(self.surface)
        self.titleContinueGame.draw(self.surface)
        self.titleBack.draw(self.surface)
    
    ###########  Draw PlayGame Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)