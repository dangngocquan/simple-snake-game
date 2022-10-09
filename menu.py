import datetime
import random
import pygame
from snake import Snake
from setting import *
import setting
from wall import Wall, WallManager
import wall
from grid import Grid
from grid import *

###########   VARIABLE   ####################################################################################
ANIMATION_SPEED = SETTING1['MENU']['ANIMATION_SPEED']
BIG_FONT = SETTING2['MENU']['BIG_FONT']
MEDIUM_FONT = SETTING2['MENU']['MEDIUM_FONT']
MEDIUM_FONT_HORVED = SETTING2['MENU']['MEDIUM_FONT_HORVED']
MEDIUM_FONT_2 = SETTING2['MENU']['MEDIUM_FONT_2']
SMALL_FONT = SETTING2['MENU']['SMALL_FONT']
DESCRIPTION_FONT = SETTING2['MENU']['DESCRIPTION_FONT']
WHITE = SETTING2['COLOR']['WHITE']

###########  CLASS BUTTON  ##################################################################################
class Button:
    ###########  Constructor  ###############################################################################
    def __init__(self, text, font, x, y, typeLocation='center'):
        self.text = font.render(text, True, WHITE, None)
        self.textRect = self.text.get_rect()
        self.typeLocation = typeLocation
        if self.typeLocation == 'center':
            self.textRect.center = (x, y)
        elif self.typeLocation == 'topLeft':
            self.textRect.topleft = (x, y)
        self.x = x
        self.y = y
        self.isChosen = False
        self.valueR = 255
        self.valueG = 255
        self.valueB = 255
        self.valueRStatus = 1
        self.valueGStatus = 1
        self.valueBStatus = 1
    
    ###########  Update text, font, coordinate and color of Button  #########################################
    def update(self, text, font, color='G'):
        ###########  Update text, font, coordinate   ########################################################
        self.text = font.render(text, True, WHITE, None)
        self.textRect = self.text.get_rect()
        if self.typeLocation == 'center':
            self.textRect.center = (self.x, self.y)
        elif self.typeLocation == 'topLeft':
            self.textRect.topleft = (self.x, self.y)
        ###########  Update color   #########################################################################
        if self.isChosen:
            if color == 'R':
                self.valueG += 51 * self.valueGStatus
                self.valueB += 51 * self.valueBStatus
            elif color == 'G':
                self.valueR += 51 * self.valueRStatus
                self.valueB += 51 * self.valueBStatus
            elif color == 'B':
                self.valueR += 51 * self.valueRStatus
                self.valueG += 51 * self.valueGStatus
            elif color == 'ALL':
                self.valueR += random.randint(-25, 25)
                self.valueG += random.randint(-25, 25)
                self.valueB += random.randint(-25, 25)
            if self.valueR < 0:
                self.valueR = - self.valueR
                self.valueRStatus = 1
            elif self.valueR > 255:
                self.valueR = 510 - self.valueR
                self.valueRStatus = -1
            if self.valueG < 0:
                self.valueG = - self.valueG
                self.valueGStatus = 1
            elif self.valueG > 255:
                self.valueG = 510 - self.valueG
                self.valueGStatus = -1
            if self.valueB < 0:
                self.valueB = - self.valueB
                self.valueBStatus = 1
            elif self.valueB > 255:
                self.valueB = 510 - self.valueB
                self.valueBStatus = -1
                
            self.text = font.render(text, True, (self.valueR, self.valueG, self.valueB), None)
        else:
            self.valueR = 255
            self.valueG = 255
            self.valueB = 255
            self.text = font.render(text, True, (self.valueR, self.valueG, self.valueB), None)
            
    ###########  Draw button in another surface  ############################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.text, self.textRect)
  
        
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
        self.titlePlayGame = Button("PLAY GAME", MEDIUM_FONT, width//2, height*5//12)
        self.titleOptions = Button("OPTIONS", MEDIUM_FONT, width//2, height*7//12)
        self.titleQuitGame = Button("QUIT GAME", MEDIUM_FONT, width//2, height*9//12)
        
    ###########  Update cursor and button status in Main Menu ###############################################
    def update(self):
        ###########  Update cursor and button of main menu  #################################################
        if self.cursor == 0:
            self.titlePlayGame.isChosen = True
            self.titleOptions.isChosen = False
            self.titleQuitGame.isChosen = False
            self.titleSimpleSnake.update('SIMPLE SNAKE', BIG_FONT, 'ALL')
            self.titlePlayGame.update('PLAY GAME', MEDIUM_FONT_HORVED)
            self.titleOptions.update('OPTIONS', MEDIUM_FONT)
            self.titleQuitGame.update('QUIT GAME', MEDIUM_FONT)
        elif self.cursor == 1:
            self.titlePlayGame.isChosen = False
            self.titleOptions.isChosen = True
            self.titleQuitGame.isChosen = False
            self.titleSimpleSnake.update('SIMPLE SNAKE', BIG_FONT, 'ALL')
            self.titlePlayGame.update('PLAY GAME', MEDIUM_FONT)
            self.titleOptions.update('OPTIONS', MEDIUM_FONT_HORVED)
            self.titleQuitGame.update('QUIT GAME', MEDIUM_FONT)
        elif self.cursor == 2:
            self.titlePlayGame.isChosen = False
            self.titleOptions.isChosen = False
            self.titleQuitGame.isChosen = True
            self.titleSimpleSnake.update('SIMPLE SNAKE', BIG_FONT, 'ALL')
            self.titlePlayGame.update('PLAY GAME', MEDIUM_FONT)
            self.titleOptions.update('OPTIONS', MEDIUM_FONT)
            self.titleQuitGame.update('QUIT GAME', MEDIUM_FONT_HORVED)
        ###########  Remove old button display  #############################################################
        self.surface.fill((0, 0, 0, 0))
        ###########  Draw new button   ######################################################################
        self.titleSimpleSnake.draw(self.surface)
        self.titlePlayGame.draw(self.surface)
        self.titleOptions.draw(self.surface)
        self.titleQuitGame.draw(self.surface)
    
    ###########  Draw Main Menu in another surface  #########################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        

###########  CLASS PLAY GAME MENU  ##########################################################################
class PlayGameMenu:
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
       
        
###########  CLASS OPTIONS MENU  ##########################################################################
class OptionsMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        ########### Buttons in Options Menu  ##############################################################
        self.titleGamemodeSetting = Button("GAME MODE SETTING", MEDIUM_FONT, width//2, height*2//12)
        self.titleGameSetting = Button("GAME SETTING", MEDIUM_FONT, width//2, height*4//12)
        self.titleSoundSetting = Button("SOUND SETTING", MEDIUM_FONT, width//2, height*6//12)
        self.titleMapSetting = Button("MAP SETTING", MEDIUM_FONT, width//2, height*8//12)
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*10//12)
        
    ###########   Update cursor and buttons status in Options Menu   ########################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleGamemodeSetting.isChosen = True
            self.titleGamemodeSetting.update('GAME MODE SETTING', MEDIUM_FONT_HORVED, 'G')
            self.titleGameSetting.update('GAME SETTING', MEDIUM_FONT, 'G')
            self.titleSoundSetting.update('SOUND SETTING', MEDIUM_FONT, 'G')
            self.titleMapSetting.update('MAP SETTING', MEDIUM_FONT, 'G')
            self.titleBack.update('BACK', MEDIUM_FONT, 'G')
        else:
            self.titleGamemodeSetting.isChosen = False
        if self.cursor == 1:
            self.titleGameSetting.isChosen = True
            self.titleGamemodeSetting.update('GAME MODE SETTING', MEDIUM_FONT, 'G')
            self.titleGameSetting.update('GAME SETTING', MEDIUM_FONT_HORVED, 'G')
            self.titleSoundSetting.update('SOUND SETTING', MEDIUM_FONT, 'G')
            self.titleMapSetting.update('MAP SETTING', MEDIUM_FONT, 'G')
            self.titleBack.update('BACK', MEDIUM_FONT, 'G')
        else:
            self.titleGameSetting.isChosen = False
        if self.cursor == 2:
            self.titleSoundSetting.isChosen = True
            self.titleGamemodeSetting.update('GAME MODE SETTING', MEDIUM_FONT, 'G')
            self.titleGameSetting.update('GAME SETTING', MEDIUM_FONT, 'G')
            self.titleSoundSetting.update('SOUND SETTING', MEDIUM_FONT_HORVED, 'G')
            self.titleMapSetting.update('MAP SETTING', MEDIUM_FONT, 'G')
            self.titleBack.update('BACK', MEDIUM_FONT, 'G')
        else:
            self.titleSoundSetting.isChosen = False
        if self.cursor == 3:
            self.titleMapSetting.isChosen = True
            self.titleGamemodeSetting.update('GAME MODE SETTING', MEDIUM_FONT, 'G')
            self.titleGameSetting.update('GAME SETTING', MEDIUM_FONT, 'G')
            self.titleSoundSetting.update('SOUND SETTING', MEDIUM_FONT, 'G')
            self.titleMapSetting.update('MAP SETTING', MEDIUM_FONT_HORVED, 'G')
            self.titleBack.update('BACK', MEDIUM_FONT, 'G')
        else:
            self.titleMapSetting.isChosen = False
        if self.cursor == 4:
            self.titleBack.isChosen = True
            self.titleGamemodeSetting.update('GAME MODE SETTING', MEDIUM_FONT, 'G')
            self.titleGameSetting.update('GAME SETTING', MEDIUM_FONT, 'G')
            self.titleSoundSetting.update('SOUND SETTING', MEDIUM_FONT, 'G')
            self.titleMapSetting.update('MAP SETTING', MEDIUM_FONT, 'G')
            self.titleBack.update('BACK', MEDIUM_FONT_HORVED, 'G')
        else:
            self.titleBack.isChosen = False
        
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
        self.titleGamemodeSetting.draw(self.surface)
        self.titleGameSetting.draw(self.surface)
        self.titleSoundSetting.draw(self.surface)
        self.titleMapSetting.draw(self.surface)
        self.titleBack.draw(self.surface)
        
    ###########  Draw Gamemode settings Menu in another surface  ######################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
   


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
            self.descriptionText.update('Press ENTER to choose the number of players', DESCRIPTION_FONT, 'ALL')
        else:
            self.titlePlayerNumber.isChosen = False
        if self.cursor == 1:
            self.titlePlayerNumberOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titlePlayerNumberOptions.isChosen = False
        if self.cursor == 2:
            self.titleAutoSpeedUpSnake.isChosen = True
            self.descriptionText.update('Press ENTER to set auto speed up snake', DESCRIPTION_FONT, 'ALL')
        else:
            self.titleAutoSpeedUpSnake.isChosen = False
        if self.cursor == 3:
            self.titleAutoSpeedUpSnakeOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titleAutoSpeedUpSnakeOptions.isChosen = False
        if self.cursor == 4:
            self.titleTargetScore.isChosen = True
            self.descriptionText.update('Press ENTER to choose the view control', DESCRIPTION_FONT, 'ALL')
        else:
            self.titleTargetScore.isChosen = False
        if self.cursor == 5:
            self.titleTargetScoreOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titleTargetScoreOptions.isChosen = False
        if self.cursor == 6:
            self.titleViewControl.isChosen = True
            self.descriptionText.update('Press ENTER to choose the view control', DESCRIPTION_FONT, 'ALL')
        else:
            self.titleViewControl.isChosen = False
        if self.cursor == 7:
            self.titleViewControlOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
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


###########  CLASS GAME SETTING MENU  #######################################################################
class GameSettingMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 12
        ########### Buttons in Game Setting Menu  ###########################################################
        self.descriptionText = Button("", DESCRIPTION_FONT, width//2, height*1//17)
        self.descriptionText.isChosen = True
        self.titleGridSetting= Button("GRID SETTING", MEDIUM_FONT_2, width//2, height*3//17)
        self.titleGrid= Button("Show grid", SMALL_FONT, width//8, height*4//17, 'topLeft')
        self.titleGridOptions= Button(f"{SETTING1['GRID']}", SMALL_FONT, 
                                      width//16*13, height*4//17, 'topLeft')
        self.titleSnakeSetting= Button("SNAKE SETTING", MEDIUM_FONT_2, width//2, height*6//17)
        self.titleSnakeMoveSpeed = Button("Move Speed", SMALL_FONT, width//8, height*7//17, 'topLeft')
        self.titleSnakeMoveSpeedOptions = Button(f"{SETTING1['SNAKE']['MOVE_SPEED']}", SMALL_FONT, 
                                                 width//16*13, height*7//17, 'topLeft')
        self.titleSnakeDropSpeed = Button("Drop Speed (when snake died)", SMALL_FONT, 
                                          width//8, height*8//17, 'topLeft')
        self.titleSnakeDropSpeedOptions = Button(f"{SETTING1['SNAKE']['DROP_SPEED']}", SMALL_FONT, 
                                                 width//16*13, height*8//17, 'topLeft')
        self.titleSnakeAnimationSpeed = Button("Animation Speed", SMALL_FONT, 
                                               width//8, height*9//17, 'topLeft')
        self.titleSnakeAnimationSpeedOptions = Button(f"{SETTING1['SNAKE']['ANIMATION_SPEED']}", SMALL_FONT, 
                                                      width//16*13, height*9//17, 'topLeft')
        self.titleFoodSetting = Button("FOOD SETTING", MEDIUM_FONT_2, width//2, height*11//17)
        self.titleFoodMax = Button("Max Food", SMALL_FONT, width//8, height*12//17, 'topLeft')
        self.titleFoodMaxOptions = Button(f"{SETTING1['FOOD']['MAX_FOOD']}", SMALL_FONT, 
                                          width//16*13, height*12//17, 'topLeft')
        self.titleFoodAnimationSpeed = Button("Animation Speed", SMALL_FONT, 
                                              width//8, height*13//17, 'topLeft')
        self.titleFoodAnimationSpeedOptions = Button(f"{SETTING1['FOOD']['ANIMATION_SPEED']}", SMALL_FONT, 
                                                     width//16*13, height*13//17, 'topLeft')
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*15//17)
        
    ###########   Update cursor and buttons status in Game Setting Menu   ###################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleGrid.isChosen = True
            self.descriptionText.update('Press ENTER to setup the grid', DESCRIPTION_FONT, 'ALL')
        else:
            self.titleGrid.isChosen = False
        if self.cursor == 1:
            self.titleGridOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titleGridOptions.isChosen = False
        if self.cursor == 2:
            self.titleSnakeMoveSpeed.isChosen = True
            self.descriptionText.update('Press ENTER to setup the move speed of snake', DESCRIPTION_FONT, 'ALL')
        else:
            self.titleSnakeMoveSpeed.isChosen = False
        if self.cursor == 3:
            self.titleSnakeMoveSpeedOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titleSnakeMoveSpeedOptions.isChosen = False
        if self.cursor == 4:
            self.titleSnakeDropSpeed.isChosen = True
            self.descriptionText.update('Press ENTER to setup the drop speed of snake', DESCRIPTION_FONT, 'ALL')
        else:
            self.titleSnakeDropSpeed.isChosen = False
        if self.cursor == 5:
            self.titleSnakeDropSpeedOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titleSnakeDropSpeedOptions.isChosen = False
        if self.cursor == 6:
            self.titleSnakeAnimationSpeed.isChosen = True
            self.descriptionText.update('Press ENTER to setup the animation speed of snake', DESCRIPTION_FONT, 'ALL')
        else:
            self.titleSnakeAnimationSpeed.isChosen = False
        if self.cursor == 7:
            self.titleSnakeAnimationSpeedOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titleSnakeAnimationSpeedOptions.isChosen = False
        if self.cursor == 8:
            self.titleFoodMax.isChosen = True
            self.descriptionText.update('Press ENTER to setup the max number of food', DESCRIPTION_FONT, 'ALL')
        else:
            self.titleFoodMax.isChosen = False
        if self.cursor == 9:
            self.titleFoodMaxOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titleFoodMaxOptions.isChosen = False
        if self.cursor == 10:
            self.titleFoodAnimationSpeed.isChosen = True
            self.descriptionText.update('Press ENTER to setup the animation speed of food', DESCRIPTION_FONT, 'ALL')
        else:
            self.titleFoodAnimationSpeed.isChosen = False
        if self.cursor == 11:
            self.titleFoodAnimationSpeedOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titleFoodAnimationSpeedOptions.isChosen = False
        if self.cursor == 12:
            self.titleBack.isChosen = True
            self.titleBack.update('BACK', MEDIUM_FONT_HORVED)
            self.descriptionText.update('', DESCRIPTION_FONT, 'ALL')
        else:
            self.titleBack.isChosen = False
            self.titleBack.update('BACK', MEDIUM_FONT)
            
        self.titleGrid.update('Show grid', SMALL_FONT, 'B')
        self.titleGridOptions.update(f"{SETTING1['GRID']}", SMALL_FONT, 'B')
        self.titleSnakeMoveSpeed.update("Move speed", SMALL_FONT, 'B')
        self.titleSnakeMoveSpeedOptions.update(f"{SETTING1['SNAKE']['MOVE_SPEED']}", 
                                               SMALL_FONT, 'B')
        self.titleSnakeDropSpeed.update("Drop speed", SMALL_FONT, 'B')
        self.titleSnakeDropSpeedOptions.update(f"{SETTING1['SNAKE']['DROP_SPEED']}", 
                                               SMALL_FONT, 'B')
        self.titleSnakeAnimationSpeed.update('Animation speed', SMALL_FONT, 'B')
        self.titleSnakeAnimationSpeedOptions.update(f"{SETTING1['SNAKE']['ANIMATION_SPEED']}", 
                                                    SMALL_FONT, 'B')
        self.titleFoodMax.update('Max food', SMALL_FONT, 'B')
        self.titleFoodMaxOptions.update(f"{SETTING1['FOOD']['MAX_FOOD']}", SMALL_FONT, 'B')
        self.titleFoodAnimationSpeed.update('Animation speed', SMALL_FONT, 'B')
        self.titleFoodAnimationSpeedOptions.update(f"{SETTING1['FOOD']['ANIMATION_SPEED']}", 
                                                   SMALL_FONT, 'B')
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
        self.descriptionText.draw(self.surface)
        self.titleGridSetting.draw(self.surface)
        self.titleGrid.draw(self.surface)
        self.titleGridOptions.draw(self.surface)
        self.titleSnakeSetting.draw(self.surface)
        self.titleSnakeMoveSpeed.draw(self.surface)
        self.titleSnakeMoveSpeedOptions.draw(self.surface)
        self.titleSnakeDropSpeed.draw(self.surface)
        self.titleSnakeDropSpeedOptions.draw(self.surface)
        self.titleSnakeAnimationSpeed.draw(self.surface)
        self.titleSnakeAnimationSpeedOptions.draw(self.surface)
        self.titleFoodSetting.draw(self.surface)
        self.titleFoodMax.draw(self.surface)
        self.titleFoodMaxOptions.draw(self.surface)
        self.titleFoodAnimationSpeed.draw(self.surface)
        self.titleFoodAnimationSpeedOptions.draw(self.surface)
        self.titleBack.draw(self.surface)
    
    ###########  Draw Game Setting Menu in another surface  #################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
   
   
###########  CLASS SOUND SETTING MENU  ######################################################################
class SoundSettingMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        ########### Buttons in Options Menu  ##############################################################
        self.descriptionText = Button("", DESCRIPTION_FONT, width//2, height*1//12)
        self.descriptionText.isChosen = True
        self.titleMusicSetting = Button("MUSIC SETTING", MEDIUM_FONT_2, width//2, height*3//12)
        self.titleMusic = Button("Music", SMALL_FONT, width//8, height*4//12, 'topLeft')
        self.titleMusicOptions = Button(f"Music {SETTING1['SOUND']['MUSIC_INDEX']}", SMALL_FONT,
                                        width//16*13, height*4//12, 'topLeft')
        self.titleMusicVolume = Button("Music volume", SMALL_FONT, width//8, height*5//12, 'topLeft')
        self.titleMusicVolumeOptions = Button(f"{SETTING1['SOUND']['MUSIC_VOLUME']}", SMALL_FONT,
                                              width//16*13, height*5//12, 'topLeft')
        self.titleSoundSetting = Button("SOUND SETTING", MEDIUM_FONT_2, width//2, height*7//12)
        self.titleSoundVolume =  Button("Sound volume", SMALL_FONT, width//8, height*8//12, 'topLeft')
        self.titleSoundVolumeOptions = Button(f"{SETTING1['SOUND']['SOUND_VOLUME']}", SMALL_FONT,
                                              width//16*13, height*8//12, 'topLeft')
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*10//12)
        
    ###########   Update cursor and buttons status in Options Menu   ########################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleMusic.isChosen = True
            self.descriptionText.update('Press ENTER to choose the music for game', DESCRIPTION_FONT, 'ALL')
        else:
            self.titleMusic.isChosen = False
        if self.cursor == 1:
            self.titleMusicOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titleMusicOptions.isChosen = False
        if self.cursor == 2:
            self.titleMusicVolume.isChosen = True
            self.descriptionText.update('Press ENTER to set volume of music', DESCRIPTION_FONT, 'ALL')
        else:
            self.titleMusicVolume.isChosen = False
        if self.cursor == 3:
            self.titleMusicVolumeOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titleMusicVolumeOptions.isChosen = False
        if self.cursor == 4:
            self.titleSoundVolume.isChosen = True
            self.descriptionText.update('Press ENTER to set volume of sound', DESCRIPTION_FONT, 'ALL')
        else:
            self.titleSoundVolume.isChosen = False
        if self.cursor == 5:
            self.titleSoundVolumeOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titleSoundVolumeOptions.isChosen = False
        if self.cursor == 6:
            self.titleBack.isChosen = True
            self.titleBack.update("BACK", MEDIUM_FONT_HORVED)
            self.descriptionText.update("", DESCRIPTION_FONT, 'ALL')
        else:
            self.titleBack.isChosen = False
            self.titleBack.update("BACK", MEDIUM_FONT)
        
        self.titleMusic.update("Music", SMALL_FONT, 'B')
        self.titleMusicOptions.update(f"Music {SETTING1['SOUND']['MUSIC_INDEX']}", SMALL_FONT, 'B')
        self.titleMusicVolume.update("Music volume", SMALL_FONT, 'B')
        self.titleMusicVolumeOptions.update(f"{SETTING1['SOUND']['MUSIC_VOLUME']}", SMALL_FONT, 'B')
        self.titleSoundVolume.update("Sound volume", SMALL_FONT, 'B')
        self.titleSoundVolumeOptions.update(f"{SETTING1['SOUND']['SOUND_VOLUME']}", SMALL_FONT, 'B')
        
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
        self.descriptionText.draw(self.surface)
        self.titleMusicSetting.draw(self.surface)
        self.titleMusic.draw(self.surface)
        self.titleMusicOptions.draw(self.surface)
        self.titleMusicVolume.draw(self.surface)
        self.titleMusicVolumeOptions.draw(self.surface)
        self.titleSoundSetting.draw(self.surface)
        self.titleSoundVolume.draw(self.surface)
        self.titleSoundVolumeOptions.draw(self.surface)
        self.titleBack.draw(self.surface)
        
    ###########  Draw Sound setting Menu in another surface  ################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
  
  
###########  CLASS MAP SETTING MENU  ########################################################################
class MapSettingMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        ########### Buttons in Options Menu  ##############################################################
        self.titleExistingMap = Button("EXISTING MAPS", MEDIUM_FONT, width//2, height*3//12)
        self.titleCreateNewMap = Button("CREATE NEW MAP", MEDIUM_FONT, width//2, height*5//12)
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*7//12)
        
    ###########   Update cursor and buttons status in Options Menu   ########################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleExistingMap.isChosen = True
            self.titleCreateNewMap.isChosen = False
            self.titleBack.isChosen = False
            self.titleExistingMap.update('EXISTING MAPS', MEDIUM_FONT_HORVED)
            self.titleCreateNewMap.update('CREATE NEW MAP', MEDIUM_FONT)
            self.titleBack.update('BACK', MEDIUM_FONT)
        elif self.cursor == 1:
            self.titleExistingMap.isChosen = False
            self.titleCreateNewMap.isChosen = True
            self.titleBack.isChosen = False
            self.titleExistingMap.update('EXISTING MAPS', MEDIUM_FONT)
            self.titleCreateNewMap.update('CREATE NEW MAP', MEDIUM_FONT_HORVED)
            self.titleBack.update('BACK', MEDIUM_FONT)
        elif self.cursor == 2:
            self.titleExistingMap.isChosen = False
            self.titleCreateNewMap.isChosen = False
            self.titleBack.isChosen = True
            self.titleExistingMap.update('EXISTING MAPS', MEDIUM_FONT)
            self.titleCreateNewMap.update('CREATE NEW MAP', MEDIUM_FONT)
            self.titleBack.update('BACK', MEDIUM_FONT_HORVED)
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
        self.titleExistingMap.draw(self.surface)
        self.titleCreateNewMap.draw(self.surface)
        self.titleBack.draw(self.surface)
    
    ###########  Draw PlayGame Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
  
#############  CLASS EXISTING MAPS MENU  ######################################################################
class ExistingMapsMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        
        self.surfaceInfo1 = pygame.Surface((width//4-10, height//4*3+10), pygame.SRCALPHA)
        self.surfaceInfo1Rect = self.surfaceInfo1.get_rect()
        self.surfaceInfo1Rect.topleft = (0, 0)
        
        self.surfaceInfo2 = pygame.Surface((width, height//4-10), pygame.SRCALPHA)
        self.surfaceInfo2Rect = self.surfaceInfo2.get_rect()
        self.surfaceInfo2Rect.topleft = (0, height//4*3+10)
        
        self.grid = Grid(0, 0, widthLine=2)
        self.wallManager = WallManager(listWall=wall.LIST_MAP[SETTING1['MAP']['INDEX_MAP']]['WALLS'])
        self.picture = pygame.Surface((width, height), pygame.SRCALPHA)
        self.pictureRect = self.picture.get_rect()
        self.pictureRect.center = (x, y)
        
        self.surfaceViewMap = pygame.Surface((width//4*3+10, height//4*3+10), pygame.SRCALPHA)
        self.surfaceViewMapRect = self.surfaceViewMap.get_rect()
        self.surfaceViewMapRect.topleft = (width//4-10, 0)
        
        self.picture2 = pygame.Surface((width//4*3, height//4*3), pygame.SRCALPHA)
        self.picture2Rect = self.picture2.get_rect()
        self.picture2Rect.center = (self.surfaceViewMapRect.width//2, self.surfaceViewMapRect.height//2)
        
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        ########### Buttons in Existing Maps Menu  ##############################################################
        self.titleIndexMap = Button(f"MAP {SETTING1['MAP']['INDEX_MAP']+1:0>2}", 
                                    SMALL_FONT, self.surfaceInfo1Rect.width//2, 
                                    self.surfaceInfo1Rect.height//12*2)
        self.titleNumberOfMap = Button(f"NUMBER MAPS: {len(wall.LIST_MAP)}", 
                                    DESCRIPTION_FONT_2, self.surfaceInfo1Rect.width//8, 
                                    self.surfaceInfo1Rect.height//12*4, 'topLeft')
        self.titleCreatedTime = Button(f"Created Time:  {wall.LIST_MAP[SETTING1['MAP']['INDEX_MAP']]['CREATED_TIME']:0>2}", 
                                    DESCRIPTION_FONT, self.surfaceInfo2Rect.width//24, 
                                    self.surfaceInfo2Rect.height//10, 'topLeft')
        self.titleNumberOfWalls = Button(f"Number of Walls:  {len(wall.LIST_MAP[SETTING1['MAP']['INDEX_MAP']]['WALLS'])}", 
                                    DESCRIPTION_FONT, self.surfaceInfo2Rect.width//24, 
                                    self.surfaceInfo2Rect.height//10*3, 'topLeft')
        self.titleDescription = Button("", DESCRIPTION_FONT_2, self.surfaceInfo2Rect.width//24, 
                                    self.surfaceInfo2Rect.height//10*5, 'topLeft')
        self.titleDescription2 = Button("", DESCRIPTION_FONT_2, self.surfaceInfo2Rect.width//24, 
                                    self.surfaceInfo2Rect.height//10*7, 'topLeft')
        
        
        
    ###########   Update cursor and buttons status in Options Menu   ########################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleIndexMap.isChosen = True
        else:
            self.titleIndexMap.isChosen = False
        self.titleIndexMap.update(f"MAP {SETTING1['MAP']['INDEX_MAP']+1:0>2}", SMALL_FONT, 'B')
        self.titleNumberOfMap = Button(f"NUMBER MAPS: {len(wall.LIST_MAP)}", 
                                    DESCRIPTION_FONT_2, self.surfaceInfo1Rect.width//8, 
                                    self.surfaceInfo1Rect.height//12*4, 'topLeft')
        self.titleCreatedTime = Button(f"Created Time:  {wall.LIST_MAP[SETTING1['MAP']['INDEX_MAP']]['CREATED_TIME']:0>2}", 
                                    DESCRIPTION_FONT_2, self.surfaceInfo2Rect.width//24, 
                                    self.surfaceInfo2Rect.height//10, 'topLeft')
        self.titleNumberOfWalls = Button(f"Number of Walls:  {len(wall.LIST_MAP[SETTING1['MAP']['INDEX_MAP']]['WALLS'])}", 
                                    DESCRIPTION_FONT_2, self.surfaceInfo2Rect.width//24, 
                                    self.surfaceInfo2Rect.height//10*3, 'topLeft')
        if SETTING1['MAP']['INDEX_MAP'] > 0:
            self.titleDescription = Button("Press 'K' to delete this map.", 
                                           DESCRIPTION_FONT_2, self.surfaceInfo2Rect.width//24, 
                                    self.surfaceInfo2Rect.height//10*5, 'topLeft')
        else:
            self.titleDescription = Button("This is default map, you can't delete this map.", 
                                           DESCRIPTION_FONT_2, self.surfaceInfo2Rect.width//24, 
                                    self.surfaceInfo2Rect.height//10*5, 'topLeft')
        self.titleDescription2 = Button("Press A/W/D/S to change your map. Press 'Enter' to save your choice.", 
                                        DESCRIPTION_FONT_2, self.surfaceInfo2Rect.width//24, 
                                    self.surfaceInfo2Rect.height//10*7, 'topLeft')
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        self.surfaceInfo1.fill((0, 0, 0, 0))
        self.surfaceInfo2.fill((0, 0, 0, 0))
        self.picture.fill((0, 0, 0, 0))
        self.surfaceViewMap.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
        self.titleIndexMap.draw(self.surfaceInfo1)
        self.titleNumberOfMap.draw(self.surfaceInfo1)
        self.titleCreatedTime.draw(self.surfaceInfo2)
        self.titleNumberOfWalls.draw(self.surfaceInfo2)
        self.titleDescription.draw(self.surfaceInfo2)
        self.titleDescription2.draw(self.surfaceInfo2)
        
        self.wallManager = WallManager(listWall=wall.LIST_MAP[SETTING1['MAP']['INDEX_MAP']]['WALLS'])
        self.picture.fill((0, 0, 0))
        self.picture.blit(self.wallManager.surface, self.wallManager.surfaceRect)
        self.picture.blit(self.grid.surface, self.grid.surfaceRect)
        self.picture2 = pygame.transform.scale(self.picture, 
                                                     (self.surfaceRect.width//4*3, self.surfaceRect.height//4*3))
        self.picture2Rect = self.picture2.get_rect()
        self.picture2Rect.center = (self.surfaceViewMapRect.width//2, self.surfaceViewMapRect.height//2)
        self.surfaceViewMap.fill((199, 237, 203))
        self.surfaceViewMap.blit(self.picture2, self.picture2Rect)
        
        self.surface.blit(self.surfaceInfo1, self.surfaceInfo1Rect)
        self.surface.blit(self.surfaceInfo2, self.surfaceInfo2Rect)
        self.surface.blit(self.surfaceViewMap, self.surfaceViewMapRect)
        

    ###########  Draw PlayGame Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
        
#############  CLASS CREATE NEW MAP MENU  ######################################################################
class CreateNewMap:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        
        self.mouseMotionPosition = (-100,-100)
        self.mouseLeftClickPosition = (-100, -100)
        self.mouseRightClickPosition = (-100, -100)
        
        self.cellBeingPoitedAt = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        self.cellBeingPoitedAt.fill(GRAY)
        self.cellBeingPoitedAtRect = self.cellBeingPoitedAt.get_rect()
        self.cellBeingPoitedAtRect.topleft = self.mouseMotionPosition
        
        self.grid = Grid(0, 0)
        self.snake01 = Snake(typeLocation=-1, typeColor='blue')
        self.snake02 = Snake(typeLocation=0, typeColor='green')
        self.snake03 = Snake(typeLocation=1, typeColor='blue')
        self.wallManager = WallManager()
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        ################   Status in Create New Map   #######################################################
        self.showingInstruction = False
        self.drawingNewMap = False
        ########### Buttons in Create New Map  ##############################################################
        self.instruction1 = Button("Press left-click to add a new wall block.", DESCRIPTION_FONT, width//2, height*3//24)
        self.instruction2 = Button("Press right-click to remove a wall block.", DESCRIPTION_FONT, width//2, height*5//24)
        self.instruction3 = Button("Press 1/2/3/4/5/6/7/8/9 to add new random wall block.", DESCRIPTION_FONT, width//2, height*7//24)
        self.instruction4 = Button("Press 'D' to delete the last wall block you just added.", DESCRIPTION_FONT, width//2, height*9//24)
        self.instruction5 = Button("Press 'C' to clear all wall blocks.", DESCRIPTION_FONT, width//2, height*11//24)
        self.instruction6 = Button("Press 'ENTER' to save your map.", DESCRIPTION_FONT, width//2, height*13//24)
        self.instruction7 = Button("Press 'ESC' to return Map Setting.", DESCRIPTION_FONT, width//2, height*15//24)
        self.titleStart = Button("START", MEDIUM_FONT, width//2, height*18//24)
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*21//24)
    
    def updateCellBeingPoitedAt(self):
        x = self.mouseMotionPosition[0]//CELL_SIZE*CELL_SIZE
        y = self.mouseMotionPosition[1]//CELL_SIZE*CELL_SIZE
        if [x, y] in (self.wallManager.coordinateWalls() 
                      + self.snake01.coordinateSnakeBlocks()
                      + self.snake02.coordinateSnakeBlocks()
                      + self.snake03.coordinateSnakeBlocks()):
            self.cellBeingPoitedAtRect.topleft = (-100, -100)
        else:
            self.cellBeingPoitedAtRect.topleft = (x, y)
    
    def addNewWallBlock(self):
        x = self.mouseLeftClickPosition[0]//CELL_SIZE*CELL_SIZE
        y = self.mouseLeftClickPosition[1]//CELL_SIZE*CELL_SIZE
        if [x, y] not in (self.wallManager.coordinateWalls()
                          + self.snake01.coordinateSnakeBlocks()
                          + self.snake02.coordinateSnakeBlocks()
                          + self.snake03.coordinateSnakeBlocks()
                          + [[-100, -100]]):
            self.wallManager.listWall.append(Wall(x, y))
        self.wallManager.updateImage()
        
    
    def removeWallBlock(self):
        x = self.mouseRightClickPosition[0]//CELL_SIZE*CELL_SIZE
        y = self.mouseRightClickPosition[1]//CELL_SIZE*CELL_SIZE
        for wall in self.wallManager.listWall:
            if [x, y] == wall.coordinate():
                self.wallManager.listWall.remove(wall)
                self.wallManager.updateImage()
        
    def addNewRandomWallBlock(self, number=1):
        listCoordinateCanChoose = []
        for row in range(NUMBER_ROWS):
            for column in range(NUMBER_COLUMNS):
                if [column*CELL_SIZE, row*CELL_SIZE] not in (self.wallManager.coordinateWalls()
                                                             + self.snake01.coordinateSnakeBlocks()
                                                             + self.snake02.coordinateSnakeBlocks()
                                                             + self.snake03.coordinateSnakeBlocks()):
                    listCoordinateCanChoose.append([column*CELL_SIZE, row*CELL_SIZE])
        if (len(listCoordinateCanChoose)) > 0:
            coordinates = random.choices(listCoordinateCanChoose, k=number)
            for coordinate in coordinates:
                self.wallManager.listWall.append(Wall(coordinate[0], coordinate[1]))
            self.wallManager.updateImage()
    
    def removeLastWallBlock(self):
        numberWalls = len(self.wallManager.listWall)
        if numberWalls > 0:
            self.wallManager.listWall.pop(numberWalls-1)
            self.wallManager.updateImage()
            
    
    def removeAllWallBlocks(self):
        self.wallManager.listWall = []
        self.wallManager.updateImage()
        
    def saveMap(self):
        wall.addNewMapToListMaps(wallManager=self.wallManager,
                                 createdTime=str(datetime.datetime.now()))
    
    ###########   Update cursor and buttons status in Options Menu   ########################################
    def update(self):
        if self.showingInstruction == True:
            ###########   Update cursor and buttons   ###########################################################
            if self.cursor == 0:
                self.titleStart.isChosen = True
                self.titleBack.isChosen = False
                self.titleStart.update("START", MEDIUM_FONT_HORVED, 'G')
                self.titleBack.update("BACK", MEDIUM_FONT, 'G')
            elif self.cursor == 1:
                self.titleStart.isChosen = False
                self.titleBack.isChosen = True
                self.titleStart.update("START", MEDIUM_FONT, 'G')
                self.titleBack.update("BACK", MEDIUM_FONT_HORVED, 'G')
            ###########   Remove old button display   ###########################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ####################################################################
            self.instruction1.draw(self.surface)
            self.instruction2.draw(self.surface)
            self.instruction3.draw(self.surface)
            self.instruction4.draw(self.surface)
            self.instruction5.draw(self.surface)
            self.instruction6.draw(self.surface)
            self.instruction7.draw(self.surface)
            self.titleStart.draw(self.surface)
            self.titleBack.draw(self.surface)
            self.titleBack.draw(self.surface)
        elif self.drawingNewMap == True:
            ###########   Update   ###########################################################
            self.updateCellBeingPoitedAt()
            self.addNewWallBlock()
            self.removeWallBlock()
            self.mouseLeftClickPosition = (-100, -100)
            self.mouseRightClickPosition = (-100, -100)
            ###########   Remove old images   ###########################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new images   ####################################################################
            self.grid.draw(self.surface)
            self.snake01.draw(self.surface)
            self.snake02.draw(self.surface)
            self.snake03.draw(self.surface)
            self.wallManager.draw(self.surface)
            self.surface.blit(self.cellBeingPoitedAt, self.cellBeingPoitedAtRect)
    
    ###########  Draw PlayGame Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)


        
###########  CLASS GAME OVER MENU  ##########################################################################
class GameOverMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height, snake=Snake(), wallManager=WallManager()):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        self.snake = snake
        self.wallManager = wallManager
        ########### Buttons in Play Game Menu  ##############################################################
        if self.snake.score >= SETTING1['GAMEMODE']['TARGET_SCORE']:
            self.titleGameOver = Button("<< YOU WON >>", BIG_FONT, width//2, height*3//12)
        else:
            self.titleGameOver = Button("GAME OVER", BIG_FONT, width//2, height*3//12)
        self.titleGameOver.isChosen = True
        self.titleTargetScore = Button(f"Target score: {SETTING1['GAMEMODE']['TARGET_SCORE']}", 
                                       MEDIUM_FONT_2, width//2, height*5//12)
        self.titleScore = Button(f"Your score: {self.snake.score}", MEDIUM_FONT_2, width//2, height*6//12)
       
        self.titlePlayAgain = Button("PLAY AGAIN", MEDIUM_FONT, width//2, height*8//12)
        self.titleBackMainMenu = Button("MAIN MENU", MEDIUM_FONT, width//2, height*10//12)
        
    ###########   Update cursor and buttons status in Game Over Menu   ######################################
    def update(self, type='UpdateTextAnimation'):
        ###########   Update animation of text   ############################################################
        if type == 'UpdateTextAnimation':
            ###########   Update cursor and buttons   #######################################################
            if self.cursor == 0:
                self.titlePlayAgain.isChosen = True
                self.titleBackMainMenu.isChosen = False
                self.titlePlayAgain.update("PLAY AGAIN", MEDIUM_FONT_HORVED)
                self.titleBackMainMenu.update("MAIN MENU", MEDIUM_FONT)
            elif self.cursor == 1:
                self.titlePlayAgain.isChosen = False
                self.titleBackMainMenu.isChosen = True
                self.titlePlayAgain.update("PLAY AGAIN", MEDIUM_FONT)
                self.titleBackMainMenu.update('MAIN MENU', MEDIUM_FONT_HORVED)
            if self.snake.score >= SETTING1['GAMEMODE']['TARGET_SCORE']:
                self.titleGameOver.update("<< YOU WON >>", BIG_FONT, color = 'ALL')
            else:
                self.titleGameOver.update("GAME OVER", BIG_FONT, color = 'ALL')
            self.titleScore.update(f"Your score: {self.snake.score}", MEDIUM_FONT_2)
            ###########   Remove old button display   #######################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ################################################################
            self.wallManager.draw(self.surface)
            self.snake.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleTargetScore.draw(self.surface)
            self.titleScore.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        ###########   Update location of snake when snake drop   ############################################
        elif type == 'UpdateSnakeDrop':
            ###########   Remove old button display   #######################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ################################################################
            if self.snake.score < SETTING1['GAMEMODE']['TARGET_SCORE']:
                self.snake.drop(wallCoordinateBlocks=self.wallManager.coordinateWalls())
            self.wallManager.draw(self.surface)
            self.snake.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleTargetScore.draw(self.surface)
            self.titleScore.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        ###########   Update animation of snake   ###########################################################
        elif type == 'UpdateSnakeAnimation':
            ###########   Remove old button display   #######################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ################################################################
            self.snake.updateAnimation()
            self.wallManager.draw(self.surface)
            self.snake.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleTargetScore.draw(self.surface)
            self.titleScore.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        
    ###########  Draw PlayGame Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
        

###########  CLASS GAME OVER MENU 02 ########################################################################
class GameOverMenu02:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height, snake01=Snake(), 
                 snake02=Snake(), winner=-1, wallManager=WallManager()):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        self.snake01 = snake01
        self.snake02 = snake02
        self.wallManager = wallManager
        self.winner = winner
        snake01Died = self.snake01.died(otherCoordinateSnakeBlocks=self.snake02.coordinateSnakeBlocks(),
                                        wallCoordinates=self.wallManager.coordinateWalls())
        snake02Died = self.snake02.died(otherCoordinateSnakeBlocks=self.snake01.coordinateSnakeBlocks(),
                                        wallCoordinates=self.wallManager.coordinateWalls())
        targetScoreReach01 = self.snake01.score >= SETTING1['GAMEMODE']['TARGET_SCORE']
        targetScoreReach02 = self.snake02.score >= SETTING1['GAMEMODE']['TARGET_SCORE']
        if self.winner == -1:
            if targetScoreReach01 and targetScoreReach02:
                self.winner = 3
            elif targetScoreReach01:
                self.winner = 1
            elif targetScoreReach02:
                self.winner = 2
            elif snake01Died and snake02Died:
                if self.snake01.score == self.snake02.score:
                    self.winner = 0
                elif self.snake01.score > self.snake02.score:
                    self.winner = 1
                elif self.snake01.score < self.snake02.score:
                    self.winner = 2
            elif snake01Died:
                self.winner = 2
            elif snake02Died:
                self.winner = 1
        ########### Buttons in Play Game Menu  ##############################################################
        self.titleGameOver = Button("END MATCH", BIG_FONT, width//2, height*2//12)
        self.titleGameOver.isChosen = True
        self.titleStatusPlayer01 = None
        self.titleStatusPlayer02 = None
        if self.winner == 0:
            self.titleStatusPlayer01 = Button("LOSER", MEDIUM_FONT_2, width//4, height*4//12)
            self.titleStatusPlayer02 = Button("LOSER", MEDIUM_FONT_2, width//4*3, height*4//12)
        elif self.winner == 1:
            self.titleStatusPlayer01 = Button("WINNER", MEDIUM_FONT_2, width//4, height*4//12)
            self.titleStatusPlayer02 = Button("LOSER", MEDIUM_FONT_2, width//4*3, height*4//12)
        elif self.winner == 2:
            self.titleStatusPlayer01 = Button("LOSER", MEDIUM_FONT_2, width//4, height*4//12)
            self.titleStatusPlayer02 = Button("WINNER", MEDIUM_FONT_2, width//4*3, height*4//12)
        elif self.winner == 3:
            self.titleStatusPlayer01 = Button("WINNER", MEDIUM_FONT_2, width//4, height*4//12)
            self.titleStatusPlayer02 = Button("WINNER", MEDIUM_FONT_2, width//4*3, height*4//12)
        self.titlePlayer01 = Button("PLAYER 01", MEDIUM_FONT_2, width//4, height*21//48)
        self.titlePlayer02 = Button("PLAYER 02", MEDIUM_FONT_2, width//4*3, height*21//48)
        self.titleScore01 = Button(f"Score: {self.snake01.score}", DESCRIPTION_FONT, width//4, height*13//24)
        self.titleTargetScore = Button(f"Target Score: {SETTING1['GAMEMODE']['TARGET_SCORE']}", 
                                       DESCRIPTION_FONT, width//4*2, height*13//24)
        self.titleScore02 = Button(f"Score: {self.snake02.score}", DESCRIPTION_FONT, width//4*3, height*13//24)
        self.titlePlayAgain = Button("PLAY AGAIN", MEDIUM_FONT, width//2, height*16//24)
        self.titleBackMainMenu = Button("MAIN MENU", MEDIUM_FONT, width//2, height*19//24)
        
    ###########   Update cursor and buttons status in Game Over Menu   ######################################
    def update(self, type='UpdateTextAnimation'):
        ###########   Update animation of text   ############################################################
        if type == 'UpdateTextAnimation':
            ###########   Update cursor and buttons   #######################################################
            if self.cursor == 0:
                self.titlePlayAgain.isChosen = True
                self.titleBackMainMenu.isChosen = False
                self.titlePlayAgain.update("PLAY AGAIN", MEDIUM_FONT_HORVED)
                self.titleBackMainMenu.update("MAIN MENU", MEDIUM_FONT)
            elif self.cursor == 1:
                self.titlePlayAgain.isChosen = False
                self.titleBackMainMenu.isChosen = True
                self.titlePlayAgain.update("PLAY AGAIN", MEDIUM_FONT)
                self.titleBackMainMenu.update('MAIN MENU', MEDIUM_FONT_HORVED)
            self.titleGameOver.update("END MATCH", BIG_FONT, color='ALL')    
            ###########   Remove old button display   #######################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ################################################################
            self.wallManager.draw(self.surface)
            self.snake01.draw(self.surface)
            self.snake02.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleStatusPlayer01.draw(self.surface)
            self.titleStatusPlayer02.draw(self.surface)
            self.titlePlayer01.draw(self.surface)
            self.titlePlayer02.draw(self.surface)
            self.titleScore01.draw(self.surface)
            self.titleTargetScore.draw(self.surface)
            self.titleScore02.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        ###########   Update location of snake when snake drop   ############################################
        elif type == 'UpdateSnakeDrop':
            ###########   Remove old button display   #######################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ################################################################
            if self.winner == 0 or self.winner == 2:
                self.snake01.drop(otherSnakeCoordinateBlocks=self.snake02.coordinateSnakeBlocks(),
                                  wallCoordinateBlocks=self.wallManager.coordinateWalls())
            if self.winner == 0 or self.winner == 1:
                self.snake02.drop(otherSnakeCoordinateBlocks=self.snake01.coordinateSnakeBlocks(),
                                  wallCoordinateBlocks=self.wallManager.coordinateWalls())
            self.wallManager.draw(self.surface)
            self.snake01.draw(self.surface)
            self.snake02.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleStatusPlayer01.draw(self.surface)
            self.titleStatusPlayer02.draw(self.surface)
            self.titlePlayer01.draw(self.surface)
            self.titlePlayer02.draw(self.surface)
            self.titleScore01.draw(self.surface)
            self.titleTargetScore.draw(self.surface)
            self.titleScore02.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        ###########   Update animation of snake   ###########################################################
        elif type == 'UpdateSnakeAnimation':
            ###########   Remove old button display   #######################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ################################################################
            self.wallManager.draw(self.surface)
            self.snake01.updateAnimation()
            self.snake01.draw(self.surface)
            self.snake02.updateAnimation()
            self.snake02.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleStatusPlayer01.draw(self.surface)
            self.titleStatusPlayer02.draw(self.surface)
            self.titlePlayer01.draw(self.surface)
            self.titlePlayer02.draw(self.surface)
            self.titleScore01.draw(self.surface)
            self.titleTargetScore.draw(self.surface)
            self.titleScore02.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        
    ###########  Draw PlayGame Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
        
    
        
        
        