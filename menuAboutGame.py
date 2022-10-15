import pygame
from setting import *
from grid import *
from button import Button
from menuGetInput import GetPasswordMenu

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
        
        self.passwordBox = GetPasswordMenu(width//2, height//2, width//2+40, height//2+20)
        self.isHiddenPasswordBox = True
        
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        self.positionMouse = (-100, -100)
        self.positionLeftMouse = (-100, -100)
        ########### Buttons in Play Game Menu  ##############################################################
        self.titleMusic = Button("MUSICS", MEDIUM_FONT_2, width//10, height*1//48, 'topLeft')
        self.titleLinkMusic01 = Button("MUSIC 0: BoyWithUke - Loafers", DESCRIPTION_FONT_2, width//8, height*5//48, 'topLeft')
        self.titleLinkMusic02 = Button("MUSIC 1: Sweden - C418", DESCRIPTION_FONT_2, width//8, height*8//48, 'topLeft')
        self.titleSound = Button("SOUNDS", MEDIUM_FONT_2, width//10, height*12//48, 'topLeft')
        self.titleLinkSound01 = Button("CHANGE BUTTON", DESCRIPTION_FONT_2, width//8, height*16//48, 'topLeft')
        self.titleLinkSound02 = Button("PRESS BUTTON", DESCRIPTION_FONT_2, width//8, height*19//48, 'topLeft')
        self.titleLinkSound03 = Button("SNAKE EAT FOOD", DESCRIPTION_FONT_2, width//8, height*22//48, 'topLeft')
        self.titleLinkSound04 = Button("GAME OVER", DESCRIPTION_FONT_2, width//8, height*25//48, 'topLeft')
        self.titleLinkSound05 = Button("WIN GAME", DESCRIPTION_FONT_2, width//8, height*28//48, 'topLeft')
        self.titleGraphic = Button("GRAPHICS", MEDIUM_FONT_2, width//10*6, height*12//48, 'topLeft')
        self.titleLinkGraphic01 = Button("SNAKE", DESCRIPTION_FONT_2, width//8*5, height*16//48, 'topLeft')
        self.titleLinkGraphic02 = Button("FOOD", DESCRIPTION_FONT_2, width//8*5, height*19//48, 'topLeft')
        self.titleLinkGraphic03 = Button("WALL", DESCRIPTION_FONT_2, width//8*5, height*22//48, 'topLeft')
        self.titleOthers = Button("OTHERS", MEDIUM_FONT_2, width//10, height*32//48, 'topLeft')
        self.titleLinkTutorialCreateButtonInYoutube = Button("TUTORIAL CREATE BUTTON IN PYGAME (YOUTUBE)", 
                                                             DESCRIPTION_FONT_2, width//8, height*36//48, 'topLeft')
        self.titleLinkSourceCode = Button("SOURCE CODE (IF YOU WANT)", DESCRIPTION_FONT_2, width//8, height*39//48, 'topLeft')
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*45//48)
        
    
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
        if self.isHiddenPasswordBox:
            if self.cursor != 0:
                if self.isPointedAt(positionMouse=self.positionMouse,
                                    surfaceCheckRect=self.titleLinkMusic01.textRect):
                    self.titleLinkMusic01.isChosen = True
                else:
                    self.titleLinkMusic01.isChosen = False
                self.titleLinkMusic01.update("MUSIC 0: BoyWithUke - Loafers", DESCRIPTION_FONT)
            if self.cursor != 1:
                if self.isPointedAt(positionMouse=self.positionMouse,
                                    surfaceCheckRect=self.titleLinkMusic02.textRect):
                    self.titleLinkMusic02.isChosen = True
                else:
                    self.titleLinkMusic02.isChosen = False
                self.titleLinkMusic02.update("MUSIC 1: Sweden - C418", DESCRIPTION_FONT)
            if self.cursor != 2:
                if self.isPointedAt(positionMouse=self.positionMouse,
                                    surfaceCheckRect=self.titleLinkSound01.textRect):
                    self.titleLinkSound01.isChosen = True
                else:
                    self.titleLinkSound01.isChosen = False
                self.titleLinkSound01.update("Change button", DESCRIPTION_FONT)
            if self.cursor != 3:
                if self.isPointedAt(positionMouse=self.positionMouse,
                                    surfaceCheckRect=self.titleLinkSound02.textRect):
                    self.titleLinkSound02.isChosen = True
                else:
                    self.titleLinkSound02.isChosen = False
                self.titleLinkSound02.update("Press button", DESCRIPTION_FONT)
            if self.cursor != 4:
                if self.isPointedAt(positionMouse=self.positionMouse,
                                    surfaceCheckRect=self.titleLinkSound03.textRect):
                    self.titleLinkSound03.isChosen = True
                else:
                    self.titleLinkSound03.isChosen = False
                self.titleLinkSound03.update("Snake eat food", DESCRIPTION_FONT)
            if self.cursor != 5:
                if self.isPointedAt(positionMouse=self.positionMouse,
                                    surfaceCheckRect=self.titleLinkSound04.textRect):
                    self.titleLinkSound04.isChosen = True
                else:
                    self.titleLinkSound04.isChosen = False
                self.titleLinkSound04.update("Game over", DESCRIPTION_FONT)
            if self.cursor != 6:
                if self.isPointedAt(positionMouse=self.positionMouse,
                                    surfaceCheckRect=self.titleLinkSound05.textRect):
                    self.titleLinkSound05.isChosen = True
                else:
                    self.titleLinkSound05.isChosen = False
                self.titleLinkSound05.update("Win game", DESCRIPTION_FONT)
            if self.cursor != 7:
                if self.isPointedAt(positionMouse=self.positionMouse,
                                    surfaceCheckRect=self.titleLinkGraphic01.textRect):
                    self.titleLinkGraphic01.isChosen = True
                else:
                    self.titleLinkGraphic01.isChosen = False
                self.titleLinkGraphic01.update("Snake", DESCRIPTION_FONT)
            if self.cursor != 8:
                if self.isPointedAt(positionMouse=self.positionMouse,
                                    surfaceCheckRect=self.titleLinkGraphic02.textRect):
                    self.titleLinkGraphic02.isChosen = True
                else:
                    self.titleLinkGraphic02.isChosen = False
                self.titleLinkGraphic02.update("Food", DESCRIPTION_FONT)
            if self.cursor != 9:
                if self.isPointedAt(positionMouse=self.positionMouse,
                                    surfaceCheckRect=self.titleLinkGraphic03.textRect):
                    self.titleLinkGraphic03.isChosen = True
                else:
                    self.titleLinkGraphic03.isChosen = False
                self.titleLinkGraphic03.update("Wall", DESCRIPTION_FONT)
            if self.cursor != 10:
                if self.isPointedAt(positionMouse=self.positionMouse,
                                    surfaceCheckRect=self.titleLinkTutorialCreateButtonInYoutube.textRect):
                    self.titleLinkTutorialCreateButtonInYoutube.isChosen = True
                else:
                    self.titleLinkTutorialCreateButtonInYoutube.isChosen = False
                self.titleLinkTutorialCreateButtonInYoutube.update(
                    "TUTORIAL CREATE BUTTON IN PYGAME (YOUTUBE)", DESCRIPTION_FONT)
            if self.cursor != 11:
                if self.isPointedAt(positionMouse=self.positionMouse,
                                    surfaceCheckRect=self.titleLinkSourceCode.textRect):
                    self.titleLinkSourceCode.isChosen = True
                else:
                    self.titleLinkSourceCode.isChosen = False
                self.titleLinkSourceCode.update("Source code (if you want)", DESCRIPTION_FONT)
            if self.cursor != 12:   
                if self.isPointedAt(positionMouse=self.positionMouse,
                                    surfaceCheckRect=self.titleBack.textRect):
                    self.titleBack.isChosen = True
                    self.titleBack.update('BACK', MEDIUM_FONT_HORVED, 'G')
                else:
                    self.titleBack.isChosen = False
                    self.titleBack.update('BACK', MEDIUM_FONT, 'G')
        elif not self.isHiddenPasswordBox:
            if self.passwordBox.cursor != 0:
                if self.isPointedAt(positionMouse=self.positionMouse,
                                    surfaceCheckRect=self.passwordBox.titleEnter.textRect,
                                    parent1SurfaceRect=self.passwordBox.surfaceRect):
                    self.passwordBox.titleEnter.isChosen = True
                    self.passwordBox.titleEnter.update("ENTER", MEDIUM_FONT_HORVED, 'G')
                else:
                    self.passwordBox.titleEnter.isChosen = False
                    self.passwordBox.titleEnter.update("ENTER", MEDIUM_FONT, 'G')
            if self.passwordBox.cursor != 1:
                if self.isPointedAt(positionMouse=self.positionMouse,
                                    surfaceCheckRect=self.passwordBox.titleCancer.textRect,
                                    parent1SurfaceRect=self.passwordBox.surfaceRect):
                    self.passwordBox.titleCancer.isChosen = True
                    self.passwordBox.titleCancer.update("CANCER", MEDIUM_FONT_HORVED, 'G')
                else:
                    self.passwordBox.titleCancer.isChosen = False
                    self.passwordBox.titleCancer.update("CANCER", MEDIUM_FONT)
    
    ###############     Update when player left-click    ####################################################
    def updatePositionLeftMouse(self):
        self.positionLeftMouse = self.positionMouse
        if self.isHiddenPasswordBox:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleLinkMusic01.textRect):
                self.cursor = 0
                self.titleLinkMusic01.isChosen = True
            elif self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleLinkMusic02.textRect):
                self.cursor = 1
                self.titleLinkMusic02.isChosen = True
            elif self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleLinkSound01.textRect):
                self.cursor = 2
                self.titleLinkSound01.isChosen = True
            elif self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleLinkSound02.textRect):
                self.cursor = 3
                self.titleLinkSound02.isChosen = True
            elif self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleLinkSound03.textRect):
                self.cursor = 4
                self.titleLinkSound03.isChosen = True
            elif self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleLinkSound04.textRect):
                self.cursor = 5
                self.titleLinkSound04.isChosen = True
            elif self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleLinkSound05.textRect):
                self.cursor = 6
                self.titleLinkSound05.isChosen = True
            elif self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleLinkGraphic01.textRect):
                self.cursor = 7
                self.titleLinkGraphic01.isChosen = True
            elif self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleLinkGraphic02.textRect):
                self.cursor = 8
                self.titleLinkGraphic02.isChosen = True
            elif self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleLinkGraphic03.textRect):
                self.cursor = 9
                self.titleLinkGraphic03.isChosen = True
            elif self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleLinkTutorialCreateButtonInYoutube.textRect):
                self.cursor = 10
                self.titleLinkTutorialCreateButtonInYoutube.isChosen = True
            elif self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleLinkSourceCode.textRect):
                self.cursor = 11
                self.titleLinkSourceCode.isChosen = True
            elif self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleBack.textRect):
                self.cursor = 12
                self.titleBack.isChosen = True
            else:
                self.cursor = 13
        elif not self.isHiddenPasswordBox:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.passwordBox.titleEnter.textRect,
                                parent1SurfaceRect=self.passwordBox.surfaceRect):
                self.passwordBox.cursor = 0
                self.passwordBox.titleEnter.isChosen = True
            elif self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.passwordBox.titleCancer.textRect,
                                parent1SurfaceRect=self.passwordBox.surfaceRect):
                self.passwordBox.cursor = 1
                self.passwordBox.titleCancer.isChosen = True
            else:
                self.passwordBox.cursor = 2
        self.positionLeftMouse = (-100, -100)    
        
        
    ###########   Update cursor and buttons status in Play Game Menu   ######################################
    def update(self):
        self.updateMousePoitedAt()
        if not self.isHiddenPasswordBox:
            self.passwordBox.update()
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
        if self.isHiddenPasswordBox:
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
        elif not self.isHiddenPasswordBox:
            self.passwordBox.draw(self.surface)
    
    ###########  Draw PlayGame Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)