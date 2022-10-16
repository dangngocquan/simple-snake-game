import pygame
from snake import Snake
from setting import *
import setting
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
        self.positionMouse = (-100, -100)
        self.positionLeftMouse = (-100, -100)
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
                                surfaceCheckRect=self.titleGrid.textRect):
                self.titleGrid.isChosen = True
            else:
                self.titleGrid.isChosen = False
            self.titleGrid.update("Show grid", DESCRIPTION_FONT)
        if self.cursor != 1:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleGridOptions.textRect):
                self.titleGridOptions.isChosen = True
            else:
                self.titleGridOptions.isChosen = False
            self.titleGridOptions.update(f"{SETTING1['GRID']}", DESCRIPTION_FONT)
        if self.cursor != 2:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleSnakeMoveSpeed.textRect):
                self.titleSnakeMoveSpeed.isChosen = True
            else:
                self.titleSnakeMoveSpeed.isChosen = False
            self.titleSnakeMoveSpeed.update("Move speed", DESCRIPTION_FONT) 
        if self.cursor != 3:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleSnakeMoveSpeedOptions.textRect):
                self.titleSnakeMoveSpeedOptions.isChosen = True
            else:
                self.titleSnakeMoveSpeedOptions.isChosen = False
            self.titleSnakeMoveSpeedOptions.update(f"{SETTING1['SNAKE']['MOVE_SPEED']}", DESCRIPTION_FONT)
        if self.cursor != 4:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleSnakeDropSpeed.textRect):
                self.titleSnakeDropSpeed.isChosen = True
            else:
                self.titleSnakeDropSpeed.isChosen = False
            self.titleSnakeDropSpeed.update("Drop Speed", DESCRIPTION_FONT) 
        if self.cursor != 5:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleSnakeDropSpeedOptions.textRect):
                self.titleSnakeDropSpeedOptions.isChosen = True
            else:
                self.titleSnakeDropSpeedOptions.isChosen = False
            self.titleSnakeDropSpeedOptions.update(f"{SETTING1['SNAKE']['DROP_SPEED']}", DESCRIPTION_FONT) 
        if self.cursor != 6:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleSnakeAnimationSpeed.textRect):
                self.titleSnakeAnimationSpeed.isChosen = True
            else:
                self.titleSnakeAnimationSpeed.isChosen = False
            self.titleSnakeAnimationSpeed.update("Animation speed", DESCRIPTION_FONT)
        if self.cursor != 7:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleSnakeAnimationSpeedOptions.textRect):
                self.titleSnakeAnimationSpeedOptions.isChosen = True
            else:
                self.titleSnakeAnimationSpeedOptions.isChosen = False
            self.titleSnakeAnimationSpeedOptions.update(f"{SETTING1['SNAKE']['ANIMATION_SPEED']}", DESCRIPTION_FONT)
        if self.cursor != 8:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleFoodMax.textRect):
                self.titleFoodMax.isChosen = True
            else:
                self.titleFoodMax.isChosen = False
            self.titleFoodMax.update("Max food", DESCRIPTION_FONT) 
        if self.cursor != 9:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleFoodMaxOptions.textRect):
                self.titleFoodMaxOptions.isChosen = True
            else:
                self.titleFoodMaxOptions.isChosen = False
            self.titleFoodMaxOptions.update(f"{SETTING1['FOOD']['MAX_FOOD']}", DESCRIPTION_FONT) 
        if self.cursor != 10:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleFoodAnimationSpeed.textRect):
                self.titleFoodAnimationSpeed.isChosen = True
            else:
                self.titleFoodAnimationSpeed.isChosen = False
            self.titleFoodAnimationSpeed.update("Animation speed", DESCRIPTION_FONT) 
        if self.cursor != 11:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleFoodAnimationSpeedOptions.textRect):
                self.titleFoodAnimationSpeedOptions.isChosen = True
            else:
                self.titleFoodAnimationSpeedOptions.isChosen = False
            self.titleFoodAnimationSpeedOptions.update(f"{SETTING1['FOOD']['ANIMATION_SPEED']}", DESCRIPTION_FONT) 
        if self.cursor != 12:   
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
                            surfaceCheckRect=self.titleGrid.textRect):
            self.cursor = 0
            self.titleGrid.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleGridOptions.textRect):
            self.cursor = 1
            self.titleGridOptions.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleSnakeMoveSpeed.textRect):
            self.cursor = 2
            self.titleSnakeMoveSpeed.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleSnakeMoveSpeedOptions.textRect):
            self.cursor = 3
            self.titleSnakeMoveSpeedOptions.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleSnakeDropSpeed.textRect):
            self.cursor = 4
            self.titleSnakeDropSpeed.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleSnakeDropSpeedOptions.textRect):
            self.cursor = 5
            self.titleSnakeDropSpeedOptions.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleSnakeAnimationSpeed.textRect):
            self.cursor = 6
            self.titleSnakeAnimationSpeed.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleSnakeAnimationSpeedOptions.textRect):
            self.cursor = 7
            self.titleSnakeAnimationSpeedOptions.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleFoodMax.textRect):
            self.cursor = 8
            self.titleFoodMax.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleFoodMaxOptions.textRect):
            self.cursor = 9
            self.titleFoodMaxOptions.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleFoodAnimationSpeed.textRect):
            self.cursor = 10
            self.titleFoodAnimationSpeed.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleFoodAnimationSpeedOptions.textRect):
            self.cursor = 11
            self.titleFoodAnimationSpeedOptions.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleBack.textRect):
            self.cursor = 12
            self.titleBack.isChosen = True
        else:
            self.cursor = 13
        self.positionLeftMouse = (-100, -100)
    
      
    ###########   Update cursor and buttons status in Game Setting Menu   ###################################
    def update(self):
        self.updateMousePoitedAt()
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleGrid.update("Show grid", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Setup show grid 'on' or 'off'", DESCRIPTION_FONT, 'R')
        else:
            self.titleGrid.update("Show grid", DESCRIPTION_FONT, 'G')    
        if self.cursor == 1:
            self.titleGridOptions.update(f"{SETTING1['GRID']}", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Wheel-up or wheel-down to change your choice", 
                                        DESCRIPTION_FONT_2, 'R')
        else:
            self.titleGridOptions.update(f"{SETTING1['GRID']}", DESCRIPTION_FONT, 'G')
        if self.cursor == 2:
            self.titleSnakeMoveSpeed.update("Move speed", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Setup move speed of your snake", DESCRIPTION_FONT, 'R')
        else:
            self.titleSnakeMoveSpeed.update("Move speed", DESCRIPTION_FONT, 'G')
        if self.cursor == 3:
            self.titleSnakeMoveSpeedOptions.update(f"{SETTING1['SNAKE']['MOVE_SPEED']}", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Wheel-up or wheel-down to change your choice", 
                                        DESCRIPTION_FONT_2, 'R')
        else:
            self.titleSnakeMoveSpeedOptions.update(f"{SETTING1['SNAKE']['MOVE_SPEED']}", DESCRIPTION_FONT, 'G')
        if self.cursor == 4:
            self.titleSnakeDropSpeed.update("Drop speed", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Setup drop speed of your snake when game over.", DESCRIPTION_FONT_2, 'R')
        else:
            self.titleSnakeDropSpeed.update("Drop speed", DESCRIPTION_FONT, 'G')
        if self.cursor == 5:
            self.titleSnakeDropSpeedOptions.update(f"{SETTING1['SNAKE']['DROP_SPEED']}", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Wheel-up or wheel-down to change your choice", 
                                        DESCRIPTION_FONT_2, 'R')
        else:
            self.titleSnakeDropSpeedOptions.update(f"{SETTING1['SNAKE']['DROP_SPEED']}", DESCRIPTION_FONT, 'G')
        if self.cursor == 6:
            self.titleSnakeAnimationSpeed.update("Animation speed", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Setup Animation speed of your snake.", DESCRIPTION_FONT, 'R')
        else:
            self.titleSnakeAnimationSpeed.update("Animation speed", DESCRIPTION_FONT, 'G')
        if self.cursor == 7:
            self.titleSnakeAnimationSpeedOptions.update(f"{SETTING1['SNAKE']['ANIMATION_SPEED']}", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Wheel-up or wheel-down to change your choice", 
                                        DESCRIPTION_FONT_2, 'R')
        else:
            self.titleSnakeAnimationSpeedOptions.update(f"{SETTING1['SNAKE']['ANIMATION_SPEED']}", DESCRIPTION_FONT, 'G')
        if self.cursor == 8:
            self.titleFoodMax.update("Max food", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Setup the max food in game.", 
                                        DESCRIPTION_FONT_2, 'R')
        else:
            self.titleFoodMax.update("Max food", DESCRIPTION_FONT, 'G')
        if self.cursor == 9:
            self.titleFoodMaxOptions.update(f"{SETTING1['FOOD']['MAX_FOOD']}", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Wheel-up or wheel-down to change your choice", 
                                        DESCRIPTION_FONT_2, 'R')
        else:
            self.titleFoodMaxOptions.update(f"{SETTING1['FOOD']['MAX_FOOD']}", DESCRIPTION_FONT, 'G')
        if self.cursor == 10:
            self.titleFoodAnimationSpeed.update("Animation speed", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Setup the animation of food.", 
                                        DESCRIPTION_FONT_2, 'R')
        else:
            self.titleFoodAnimationSpeed.update("Animation speed", DESCRIPTION_FONT, 'G')
        if self.cursor == 11:
            self.titleFoodAnimationSpeedOptions.update(f"{SETTING1['FOOD']['ANIMATION_SPEED']}", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Wheel-up or wheel-down to change your choice", 
                                        DESCRIPTION_FONT_2, 'R')
        else:
            self.titleFoodAnimationSpeedOptions.update(f"{SETTING1['FOOD']['ANIMATION_SPEED']}", DESCRIPTION_FONT, 'G')
        if self.cursor == 12:
            self.titleBack.update("BACK", MEDIUM_FONT_HORVED, 'B')
            self.descriptionText.update("", DESCRIPTION_FONT, 'R')
        if self.cursor == 13:
            self.descriptionText.update("", DESCRIPTION_FONT, 'R')
            
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