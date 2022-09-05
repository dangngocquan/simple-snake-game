import pygame
from snake import Snake
from setting import *



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
        self.FPS = MENU_CHANGE_COLOR_SPEED
        self.cursor = 0
        
        ########### Buttons   ###############################################################################
        self.titleSimpleSnake = Button("SIMPLE SNAKE", SIMPLE_SNAKE_FONT, width//2, height//6)
        self.titlePlayGame = Button("PLAY GAME", TITLE_FONT, width//2, height*5//12)
        self.titleOptions = Button("OPTIONS", TITLE_FONT, width//2, height*7//12)
        self.titleQuitGame = Button("QUIT GAME", TITLE_FONT, width//2, height*9//12)
        
    ###########  Update cursor and button status in Main Menu ###############################################
    def update(self):
        ###########  Update cursor and button of main menu  #################################################
        if self.cursor == 0:
            self.titlePlayGame.isChosen = True
            self.titleOptions.isChosen = False
            self.titleQuitGame.isChosen = False
            self.titlePlayGame.update('PLAY GAME', TITLE_FONT_HORVED)
            self.titleOptions.update('OPTIONS', TITLE_FONT)
            self.titleQuitGame.update('QUIT GAME', TITLE_FONT)
        elif self.cursor == 1:
            self.titlePlayGame.isChosen = False
            self.titleOptions.isChosen = True
            self.titleQuitGame.isChosen = False
            self.titlePlayGame.update('PLAY GAME', TITLE_FONT)
            self.titleOptions.update('OPTIONS', TITLE_FONT_HORVED)
            self.titleQuitGame.update('QUIT GAME', TITLE_FONT)
        elif self.cursor == 2:
            self.titlePlayGame.isChosen = False
            self.titleOptions.isChosen = False
            self.titleQuitGame.isChosen = True
            self.titlePlayGame.update('PLAY GAME', TITLE_FONT)
            self.titleOptions.update('OPTIONS', TITLE_FONT)
            self.titleQuitGame.update('QUIT GAME', TITLE_FONT_HORVED)
        
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
        self.FPS = MENU_CHANGE_COLOR_SPEED
        self.cursor = 0
        
        ########### Buttons in Play Game Menu  ##############################################################
        self.titleNewGame = Button("NEW GAME", TITLE_FONT, width//2, height*4//12)
        self.titleContinueGame = Button("CONTINUE GAME", TITLE_FONT, width//2, height*6//12)
        self.titleBack = Button("BACK", TITLE_FONT, width//2, height*8//12)
        
    ###########   Update cursor and buttons status in Play Game Menu   ######################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleNewGame.isChosen = True
            self.titleContinueGame.isChosen = False
            self.titleBack.isChosen = False
            self.titleNewGame.update('NEW GAME', TITLE_FONT_HORVED)
            self.titleContinueGame.update('CONTINUE GAME', TITLE_FONT)
            self.titleBack.update('BACK', TITLE_FONT)
        elif self.cursor == 1:
            self.titleNewGame.isChosen = False
            self.titleContinueGame.isChosen = True
            self.titleBack.isChosen = False
            self.titleNewGame.update('NEW GAME', TITLE_FONT)
            self.titleContinueGame.update('CONTINUE GAME', TITLE_FONT_HORVED)
            self.titleBack.update('BACK', TITLE_FONT)
        elif self.cursor == 2:
            self.titleNewGame.isChosen = False
            self.titleContinueGame.isChosen = False
            self.titleBack.isChosen = True
            self.titleNewGame.update('NEW GAME', TITLE_FONT)
            self.titleContinueGame.update('CONTINUE GAME', TITLE_FONT)
            self.titleBack.update('BACK', TITLE_FONT_HORVED)
        
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
        self.FPS = MENU_CHANGE_COLOR_SPEED
        self.cursor = 0
        
        ########### Buttons in Continue Game Menu  ##############################################################
        self.titleBack = Button("BACK", TITLE_FONT, width//2, height*8//12)
        
    ###########   Update cursor and buttons status in Continue Game Menu   ######################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleBack.isChosen = True
            self.titleBack.update('BACK', TITLE_FONT_HORVED)
        
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
        self.FPS = MENU_CHANGE_COLOR_SPEED
        self.cursor = 0
        
        ########### Buttons in Options Menu  ##############################################################
        self.titleBack = Button("BACK", TITLE_FONT, width//2, height*8//12)
        
    ###########   Update cursor and buttons status in Options Menu   ######################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleBack.isChosen = True
            self.titleBack.update('BACK', TITLE_FONT_HORVED)
        
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
        self.FPS = MENU_CHANGE_COLOR_SPEED
        self.cursor = 0
        self.snake = snake
        
        ########### Buttons in Play Game Menu  ##############################################################
        self.titleGameOver = Button("GAME OVER", SIMPLE_SNAKE_FONT, width//2, height*3//12)
        self.titleScore = Button(f"Your score: {self.snake.score}", MEDIUM_FONT2, width//2, height*5//12)
        self.titlePlayAgain = Button("PLAY AGAIN", TITLE_FONT, width//2, height*7//12)
        self.titleBackMainMenu = Button("MAIN MENU", TITLE_FONT, width//2, height*9//12)
        
    
    ###########   Update cursor and buttons status in Game Over Menu   ######################################
    def update(self, type='UpdateTextFrame'):
        if type == 'UpdateTextFrame':
            ###########   Update cursor and buttons   ###########################################################
            if self.cursor == 0:
                self.titlePlayAgain.isChosen = True
                self.titleBackMainMenu.isChosen = False
                self.titlePlayAgain.update("PLAY AGAIN", TITLE_FONT_HORVED)
                self.titleBackMainMenu.update("MAIN MENU", TITLE_FONT)
            elif self.cursor == 1:
                self.titlePlayAgain.isChosen = False
                self.titleBackMainMenu.isChosen = True
                self.titlePlayAgain.update("PLAY AGAIN", TITLE_FONT)
                self.titleBackMainMenu.update('MAIN MENU', TITLE_FONT_HORVED)
            
            ###########   Remove old button display   ###########################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ####################################################################
            self.titleScore.update(f"Your score: {self.snake.score}", MEDIUM_FONT2)
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
        elif type == 'UpdateSnakeFrame':
            ###########   Remove old button display   ###########################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ####################################################################
            self.snake.updateFrame()
            self.snake.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleScore.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        
    ###########  Draw PlayGame Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
        
    
        
        
        