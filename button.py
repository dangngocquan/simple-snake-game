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