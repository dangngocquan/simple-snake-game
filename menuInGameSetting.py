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