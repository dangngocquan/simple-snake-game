import pygame
from snake import Snake
from setting import *

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
    def __init__(self, text, font, x, y):
        self.text = font.render(text, True, WHITE, None)
        self.textRect = self.text.get_rect()
        self.textRect.center = (x, y)
        self.x = x
        self.y = y
        self.isChosen = False
        self.value = 255
        self.valueStatus = 1
    
    ###########  Update text, font, coordinate and color of Button  #########################################
    def update(self, text, font, color='G'):
        ###########  Update text, font, coordinate   ########################################################
        self.text = font.render(text, True, WHITE, None)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.x, self.y)
        ###########  Update color   #########################################################################
        if self.isChosen:
            if self.value == 255 or self.value == 55:
                self.valueStatus *= -1
            self.value += 50 * self.valueStatus
            if color == 'R':
                self.text = font.render(text, True, (255, self.value, self.value), None)
            elif color == 'G':
                self.text = font.render(text, True, (self.value, 255, self.value), None)
            elif color == 'B':
                self.text = font.render(text, True, (self.value, self.value, 255), None)
        else:
            self.value = 255
            self.valueStatus = 1
            self.text = font.render(text, True, (self.value, 255, self.value), None)
            
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
            self.titlePlayGame.update('PLAY GAME', MEDIUM_FONT_HORVED)
            self.titleOptions.update('OPTIONS', MEDIUM_FONT)
            self.titleQuitGame.update('QUIT GAME', MEDIUM_FONT)
        elif self.cursor == 1:
            self.titlePlayGame.isChosen = False
            self.titleOptions.isChosen = True
            self.titleQuitGame.isChosen = False
            self.titlePlayGame.update('PLAY GAME', MEDIUM_FONT)
            self.titleOptions.update('OPTIONS', MEDIUM_FONT_HORVED)
            self.titleQuitGame.update('QUIT GAME', MEDIUM_FONT)
        elif self.cursor == 2:
            self.titlePlayGame.isChosen = False
            self.titleOptions.isChosen = False
            self.titleQuitGame.isChosen = True
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
       

###########  CLASS CONTINUE GAME MENU  ##########################################################################
class ContinueGameMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        
        ########### Buttons in Continue Game Menu  ##############################################################
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*8//12)
        
    ###########   Update cursor and buttons status in Continue Game Menu   ######################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleBack.isChosen = True
            self.titleBack.update('BACK', MEDIUM_FONT_HORVED)
        
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
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
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*8//12)
        
    ###########   Update cursor and buttons status in Options Menu   ######################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleBack.isChosen = True
            self.titleBack.update('BACK', MEDIUM_FONT_HORVED)
        
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
        self.titleBack.draw(self.surface)
    
    ###########  Draw PlayGame Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
        
###########  CLASS GAME OVER MENU  ##########################################################################
class GameOverMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height, snake=Snake()):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        self.snake = snake
        
        ########### Buttons in Play Game Menu  ##############################################################
        self.titleGameOver = Button("GAME OVER", BIG_FONT, width//2, height*3//12)
        self.titleScore = Button(f"Your score: {self.snake.score}", MEDIUM_FONT_2, width//2, height*5//12)
        self.titlePlayAgain = Button("PLAY AGAIN", MEDIUM_FONT, width//2, height*7//12)
        self.titleBackMainMenu = Button("MAIN MENU", MEDIUM_FONT, width//2, height*9//12)
        
    
    ###########   Update cursor and buttons status in Game Over Menu   ######################################
    def update(self, type='UpdateTextAnimation'):
        if type == 'UpdateTextAnimation':
            ###########   Update cursor and buttons   ###########################################################
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
            
            ###########   Remove old button display   ###########################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ####################################################################
            self.titleScore.update(f"Your score: {self.snake.score}", MEDIUM_FONT_2)
            self.snake.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleScore.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        elif type == 'UpdateSnakeDrop':
            ###########   Remove old button display   ###########################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ####################################################################
            self.snake.drop()
            self.snake.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleScore.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        elif type == 'UpdateSnakeAnimation':
            ###########   Remove old button display   ###########################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ####################################################################
            self.snake.updateAnimation()
            self.snake.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleScore.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        
    ###########  Draw PlayGame Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
        
    
        
        
        