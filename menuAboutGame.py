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
        self.titleMusic = Button("MUSICS", MEDIUM_FONT_2, width//8, height*1//24, 'topLeft')
        self.titleLinkMusic01 = Button("MUSIC00: Sweden - C418", DESCRIPTION_FONT_2, width//8, height*3//24, 'topLeft')
        self.titleLinkMusic02 = Button("MUSIC01: BoyWithUke - Loafers", DESCRIPTION_FONT_2, width//8, height*4//24, 'topLeft')
        self.titleSound = Button("SOUNDS", MEDIUM_FONT_2, width//8, height*5//24, 'topLeft')
        self.titleLinkSound01 = Button("CHANGE BUTTON", DESCRIPTION_FONT_2, width//8, height*7//24, 'topLeft')
        self.titleLinkSound02 = Button("PRESS BUTTON", DESCRIPTION_FONT_2, width//8, height*8//24, 'topLeft')
        self.titleLinkSound03 = Button("SNAKE EAT FOOD", DESCRIPTION_FONT_2, width//8, height*9//24, 'topLeft')
        self.titleLinkSound04 = Button("GAME OVER", DESCRIPTION_FONT_2, width//8, height*10//24, 'topLeft')
        self.titleLinkSound05 = Button("WIN GAME", DESCRIPTION_FONT_2, width//8, height*11//24, 'topLeft')
        self.titleGraphic = Button("GRAPHICS", MEDIUM_FONT_2, width//8, height*12//24, 'topLeft')
        self.titleLinkGraphic01 = Button("SNAKE", DESCRIPTION_FONT_2, width//8, height*14//24, 'topLeft')
        self.titleLinkGraphic02 = Button("FOOD", DESCRIPTION_FONT_2, width//8, height*15//24, 'topLeft')
        self.titleLinkGraphic03 = Button("WALL", DESCRIPTION_FONT_2, width//8, height*16//24, 'topLeft')
        self.titleOthers = Button("OTHERS", MEDIUM_FONT_2, width//8, height*17//24, 'topLeft')
        self.titleLinkTutorialCreateButtonInYoutube = Button("TUTORIAL CREATE BUTTON IN PYGAME (YOUTUBE)", 
                                                             DESCRIPTION_FONT_2, width//8, height*19//24, 'topLeft')
        self.titleLinkSourceCode = Button("SOURCE CODE (IF YOU WANT)", DESCRIPTION_FONT_2, width//8, height*20//24, 'topLeft')
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*22//24)
        
    ###########   Update cursor and buttons status in Play Game Menu   ######################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            pass
        elif self.cursor == 1:
            pass
        elif self.cursor == 2:
            pass
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
        self.titleMusic.draw(self.surface)
        self.titleLinkMusic01.draw(self.surface)
        self.titleLinkMusic02.draw(self.surface)
        self.titleSound.draw(self.surface)
        self.titleLinkSound01.draw(self.surface)
        self.titleLinkSound02.draw(self.surface)
        self.titleLinkSound03.draw(self.surface)
        self.titleLinkSound04.draw(self.surface)
        self.titleLinkSound05.draw(self.surface)
        self.titleGraphic.draw(self.surface)
        self.titleLinkGraphic01.draw(self.surface)
        self.titleLinkGraphic02.draw(self.surface)
        self.titleLinkGraphic03.draw(self.surface)
        self.titleOthers.draw(self.surface)
        self.titleLinkTutorialCreateButtonInYoutube.draw(self.surface)
        self.titleLinkSourceCode.draw(self.surface)
        self.titleBack.draw(self.surface)
        self.titleBack.draw(self.surface)
    
    ###########  Draw PlayGame Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)