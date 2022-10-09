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
        self.cursor = 0
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
        self.titleTargetScore = Button("Auto speed up snake", SMALL_FONT, width//8, height*11//24, 'topLeft')
        self.titleTargetScoreOptions = Button(f"{SETTING1['GAMEMODE']['TARGET_SCORE']}", SMALL_FONT,
                                        width//12*8, height*11//24, 'topLeft')
        self.titleViewControlSetting = Button("VIEW CONTROL SETTING", MEDIUM_FONT_2, width//2, height*14//24)
        self.titleViewControl =  Button("View control", SMALL_FONT, width//8, height*16//24, 'topLeft')
        self.titleViewControlOptions = Button(f"{SETTING1['GAMEMODE']['VIEW_CONTROL']}", SMALL_FONT,
                                              width//12*8, height*16//24, 'topLeft')
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*19//24)
        
    ###########   Update cursor and buttons status in Gamemode setting Menu   ###############################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titlePlayerNumber.isChosen = True
            self.descriptionText.update("Press 'ENTER' to choose the number of players", DESCRIPTION_FONT, 'ALL')
        else:
            self.titlePlayerNumber.isChosen = False
        if self.cursor == 1:
            self.titlePlayerNumberOptions.isChosen = True
            self.descriptionText.update("Press W/S to change your choice, Press 'ENTER' to save your setting", 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titlePlayerNumberOptions.isChosen = False
        if self.cursor == 2:
            self.titleAutoSpeedUpSnake.isChosen = True
            self.descriptionText.update("Press 'ENTER' to set auto speed up snake", DESCRIPTION_FONT, 'ALL')
        else:
            self.titleAutoSpeedUpSnake.isChosen = False
        if self.cursor == 3:
            self.titleAutoSpeedUpSnakeOptions.isChosen = True
            self.descriptionText.update("Press W/S to change your choice, Press 'ENTER' to save your setting", 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titleAutoSpeedUpSnakeOptions.isChosen = False
        if self.cursor == 4:
            self.titleTargetScore.isChosen = True
            self.descriptionText.update("Press 'ENTER' to setup Target score", DESCRIPTION_FONT, 'ALL')
        else:
            self.titleTargetScore.isChosen = False
        if self.cursor == 5:
            self.titleTargetScoreOptions.isChosen = True
            self.descriptionText.update("Press W/S to change your choice, Press 'ENTER' to save your setting", 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titleTargetScoreOptions.isChosen = False
        if self.cursor == 6:
            self.titleViewControl.isChosen = True
            self.descriptionText.update("Press 'ENTER' to choose the view control", DESCRIPTION_FONT, 'ALL')
        else:
            self.titleViewControl.isChosen = False
        if self.cursor == 7:
            self.titleViewControlOptions.isChosen = True
            self.descriptionText.update("Press W/S to change your choice, Press 'ENTER' to save your setting", 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titleViewControlOptions.isChosen = False
        if self.cursor == 8:
            self.titleBack.isChosen = True
            self.titleBack.update("BACK", MEDIUM_FONT_HORVED)
            self.descriptionText.update("", DESCRIPTION_FONT, 'ALL')
        else:
            self.titleBack.isChosen = False
            self.titleBack.update("BACK", MEDIUM_FONT)
        
        self.titlePlayerNumber.update("Number of players", SMALL_FONT, 'B')
        self.titlePlayerNumberOptions.update(f"{SETTING1['GAMEMODE']['NUMBER_PLAYERS']}", SMALL_FONT, 'B')
        self.titleAutoSpeedUpSnake.update("Auto speed up snake", SMALL_FONT, 'B')
        self.titleAutoSpeedUpSnakeOptions.update(f"{SETTING1['GAMEMODE']['AUTO_SPEED_UP']}", SMALL_FONT, 'B')
        self.titleTargetScore.update("Target score", SMALL_FONT, 'B')
        self.titleTargetScoreOptions.update(f"{SETTING1['GAMEMODE']['TARGET_SCORE']}", SMALL_FONT, 'B')
        self.titleViewControl.update("View control", SMALL_FONT, 'B')
        self.titleViewControlOptions.update(f"{SETTING1['GAMEMODE']['VIEW_CONTROL']}", SMALL_FONT, 'B')
        
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
        
    ###########  Draw Options Menu in another surface  ######################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)