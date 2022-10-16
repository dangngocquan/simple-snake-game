from locale import currency
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


###########  CLASS GAMEMODE SETTING MENU  ######################################################################
class GamemodeSettingMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 9
        self.positionMouse = (-100, -100)
        self.positionLeftMouse = (-100, -100)
        ########### Buttons in Gamemode Setting Menu  #######################################################
        self.descriptionText = Button("", DESCRIPTION_FONT, width//2, height*1//12)
        self.descriptionText.isChosen = True
        self.titleModeSetting = Button("MODE SETTING", MEDIUM_FONT_2, width//2, height*5//24)
        self.titlePlayerNumber = Button("Number of players", SMALL_FONT, width//8, height*7//24, 'topLeft')
        self.titlePlayerNumberOptions = Button(f"{SETTING1['GAMEMODE']['NUMBER_PLAYERS']}", SMALL_FONT,
                                        width//12*8, height*7//24, 'topLeft')
        self.titleAutoSpeedUpSnake = Button("Auto speed up snake", SMALL_FONT, width//8, height*9//24, 'topLeft')
        self.titleAutoSpeedUpSnakeOptions = Button(f"{SETTING1['GAMEMODE']['AUTO_SPEED_UP']}", SMALL_FONT,
                                        width//12*8, height*9//24, 'topLeft')
        self.titleTargetScore = Button("Target score", SMALL_FONT, width//8, height*11//24, 'topLeft')
        self.titleTargetScoreOptions = Button(f"{SETTING1['GAMEMODE']['TARGET_SCORE']}", SMALL_FONT,
                                        width//12*8, height*11//24, 'topLeft')
        self.titleViewControlSetting = Button("VIEW CONTROL SETTING", MEDIUM_FONT_2, width//2, height*14//24)
        self.titleViewControl =  Button("View control", SMALL_FONT, width//8, height*16//24, 'topLeft')
        self.titleViewControlOptions = Button(f"{SETTING1['GAMEMODE']['VIEW_CONTROL']}", SMALL_FONT,
                                              width//12*8, height*16//24, 'topLeft')
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*19//24)
    
    
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
        if self.cursor != 0:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titlePlayerNumber.textRect):
                self.titlePlayerNumber.isChosen = True
            else:
                self.titlePlayerNumber.isChosen = False
            self.titlePlayerNumber.update("Number of players", DESCRIPTION_FONT)
        if self.cursor != 1:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titlePlayerNumberOptions.textRect):
                self.titlePlayerNumberOptions.isChosen = True
            else:
                self.titlePlayerNumberOptions.isChosen = False
            self.titlePlayerNumberOptions.update(f"{SETTING1['GAMEMODE']['NUMBER_PLAYERS']}", DESCRIPTION_FONT)
        if self.cursor != 2:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleAutoSpeedUpSnake.textRect):
                self.titleAutoSpeedUpSnake.isChosen = True
            else:
                self.titleAutoSpeedUpSnake.isChosen = False
            self.titleAutoSpeedUpSnake.update("Auto speed up snake", DESCRIPTION_FONT) 
        if self.cursor != 3:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleAutoSpeedUpSnakeOptions.textRect):
                self.titleAutoSpeedUpSnakeOptions.isChosen = True
            else:
                self.titleAutoSpeedUpSnakeOptions.isChosen = False
            self.titleAutoSpeedUpSnakeOptions.update(f"{SETTING1['GAMEMODE']['AUTO_SPEED_UP']}", DESCRIPTION_FONT)
        if self.cursor != 4:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleTargetScore.textRect):
                self.titleTargetScore.isChosen = True
            else:
                self.titleTargetScore.isChosen = False
            self.titleTargetScore.update("Target score", DESCRIPTION_FONT) 
        if self.cursor != 5:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleTargetScoreOptions.textRect):
                self.titleTargetScoreOptions.isChosen = True
            else:
                self.titleTargetScoreOptions.isChosen = False
            self.titleTargetScoreOptions.update(f"{SETTING1['GAMEMODE']['TARGET_SCORE']}", DESCRIPTION_FONT) 
        if self.cursor != 6:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleViewControl.textRect):
                self.titleViewControl.isChosen = True
            else:
                self.titleViewControl.isChosen = False
            self.titleViewControl.update("View control", DESCRIPTION_FONT)
        if self.cursor != 7:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleViewControlOptions.textRect):
                self.titleViewControlOptions.isChosen = True
            else:
                self.titleViewControlOptions.isChosen = False
            self.titleViewControlOptions.update(f"{SETTING1['GAMEMODE']['VIEW_CONTROL']}", DESCRIPTION_FONT) 
        if self.cursor != 8:   
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleBack.textRect):
                self.titleBack.isChosen = True
                self.titleBack.update('BACK', MEDIUM_FONT_HORVED, 'G')
            else:
                self.titleBack.isChosen = False
                self.titleBack.update('BACK', MEDIUM_FONT, 'G')
    
    ###############     Update when player left-click    ####################################################
    def updatePositionLeftMouse(self):
        self.positionLeftMouse = self.positionMouse
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titlePlayerNumber.textRect):
            self.cursor = 0
            self.titlePlayerNumber.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titlePlayerNumberOptions.textRect):
            self.cursor = 1
            self.titlePlayerNumberOptions.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleAutoSpeedUpSnake.textRect):
            self.cursor = 2
            self.titleAutoSpeedUpSnake.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleAutoSpeedUpSnakeOptions.textRect):
            self.cursor = 3
            self.titleAutoSpeedUpSnakeOptions.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleTargetScore.textRect):
            self.cursor = 4
            self.titleTargetScore.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleTargetScoreOptions.textRect):
            self.cursor = 5
            self.titleTargetScoreOptions.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleViewControl.textRect):
            self.cursor = 6
            self.titleViewControl.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleViewControlOptions.textRect):
            self.cursor = 7
            self.titleViewControlOptions.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleBack.textRect):
            self.cursor = 8
            self.titleBack.isChosen = True
        else:
            self.cursor = 9
        self.positionLeftMouse = (-100, -100)
    
    
    ###########   Update cursor and buttons status in Gamemode setting Menu   ###############################
    def update(self):
        self.updateMousePoitedAt()
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titlePlayerNumber.update("Number of players", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Setup the number of players", DESCRIPTION_FONT, 'R')
        else:
            self.titlePlayerNumber.update("Number of players", DESCRIPTION_FONT, 'G')    
        if self.cursor == 1:
            self.titlePlayerNumberOptions.update(f"{SETTING1['GAMEMODE']['NUMBER_PLAYERS']}", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Wheel-up or wheel-down to change your choice", 
                                        DESCRIPTION_FONT_2, 'R')
        else:
            self.titlePlayerNumberOptions.update(f"{SETTING1['GAMEMODE']['NUMBER_PLAYERS']}", DESCRIPTION_FONT, 'G')
        if self.cursor == 2:
            self.titleAutoSpeedUpSnake.update("Auto speed up snake", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Setup the snake auto speed up", DESCRIPTION_FONT, 'R')
        else:
            self.titleAutoSpeedUpSnake.update("Auto speed up snake", DESCRIPTION_FONT, 'G')
        if self.cursor == 3:
            self.titleAutoSpeedUpSnakeOptions.update(f"{SETTING1['GAMEMODE']['AUTO_SPEED_UP']}", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Wheel-up or wheel-down to change your choice", 
                                        DESCRIPTION_FONT_2, 'R')
        else:
            self.titleAutoSpeedUpSnakeOptions.update(f"{SETTING1['GAMEMODE']['AUTO_SPEED_UP']}", DESCRIPTION_FONT, 'G')
        if self.cursor == 4:
            self.titleTargetScore.update("Target score", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Setup Target score, you will win if your score >= target score", DESCRIPTION_FONT_2, 'R')
        else:
            self.titleTargetScore.update("Target score", DESCRIPTION_FONT, 'G')
        if self.cursor == 5:
            self.titleTargetScoreOptions.update(f"{SETTING1['GAMEMODE']['TARGET_SCORE']}", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Wheel-up or wheel-down to change your choice", 
                                        DESCRIPTION_FONT_2, 'R')
        else:
            self.titleTargetScoreOptions.update(f"{SETTING1['GAMEMODE']['TARGET_SCORE']}", DESCRIPTION_FONT, 'G')
        if self.cursor == 6:
            self.titleViewControl.update("View control", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Setup the view control", DESCRIPTION_FONT, 'R')
        else:
            self.titleViewControl.update("View control", DESCRIPTION_FONT, 'G')
        if self.cursor == 7:
            self.titleViewControlOptions.update(f"{SETTING1['GAMEMODE']['VIEW_CONTROL']}", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Wheel-up or wheel-down to change your choice", 
                                        DESCRIPTION_FONT_2, 'R')
        else:
            self.titleViewControlOptions.update(f"{SETTING1['GAMEMODE']['VIEW_CONTROL']}", DESCRIPTION_FONT, 'G')
        if self.cursor == 8:
            self.titleBack.update("BACK", MEDIUM_FONT_HORVED, 'B')
            self.descriptionText.update("", DESCRIPTION_FONT, 'R')
        if self.cursor == 9:
            self.descriptionText.update("", DESCRIPTION_FONT, 'R')
            
        
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
        self.descriptionText.draw(self.surface)
        self.titleModeSetting.draw(self.surface)
        self.titlePlayerNumber.draw(self.surface)
        self.titlePlayerNumberOptions.draw(self.surface)
        self.titleAutoSpeedUpSnake.draw(self.surface)
        self.titleAutoSpeedUpSnakeOptions.draw(self.surface)
        self.titleTargetScore.draw(self.surface)
        self.titleTargetScoreOptions.draw(self.surface)
        self.titleViewControlSetting.draw(self.surface)
        self.titleViewControl.draw(self.surface)
        self.titleViewControlOptions.draw(self.surface)
        self.titleBack.draw(self.surface)
        
    ###########  Draw Gamemode Setting Menu in another surface  ######################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)