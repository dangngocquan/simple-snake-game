import pygame


###########  FPS  ############################################################################
MENU_CHANGE_COLOR_SPEED = 5


###########  FONT  ############################################################################
pygame.font.init()
SIMPLE_SNAKE_FONT = pygame.font.SysFont('algerian', 96)
TITLE_FONT = pygame.font.SysFont('castellar', 48)
TITLE_FONT_HORVED = pygame.font.SysFont('castellar', 56)
TITLE_FONT2 = pygame.font.SysFont('chiller', 48)
SMALL_FONT = pygame.font.SysFont('curlz', 28)


###########  COLOR  ###########################################################################
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


###########  CLASS BUTTON  ####################################################################
class Button:
    def __init__(self, text, font, x, y):
        self.text = font.render(text, True, WHITE, None)
        self.textRect = self.text.get_rect()
        self.textRect.center = (x, y)
        self.x = x
        self.y = y
        self.isChosen = False
        self.value = 255
        self.valueStatus = 1
    
    def update(self, text, font, color='G'):
        self.text = font.render(text, True, WHITE, None)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.x, self.y)
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
            
    
    def draw(self, parentSurface):
        parentSurface.blit(self.text, self.textRect)
  
        
###########  CLASS MAIN MENU  #################################################################
class MainMenu:
    def __init__(self, x, y, width, height):
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = MENU_CHANGE_COLOR_SPEED
        self.cursor = 0
        
        self.titleSimpleSnake = Button("SIMPLE SNAKE", SIMPLE_SNAKE_FONT, width//2, height//6)
        self.titleSimpleSnake.draw(self.surface)
        
        self.titlePlayGame = Button("PLAY GAME", TITLE_FONT, width//2, height*5//12)
        self.titlePlayGame.draw(self.surface)
        
        self.titleOptions = Button("OPTIONS", TITLE_FONT, width//2, height*7//12)
        self.titleOptions.draw(self.surface)
        
        
    def update(self):
        if self.cursor == 0:
            self.titlePlayGame.isChosen = True
            self.titleOptions.isChosen = False
            self.titlePlayGame.update('PLAY GAME', TITLE_FONT_HORVED)
            self.titleOptions.update('OPTIONS', TITLE_FONT)
        elif self.cursor == 1:
            self.titlePlayGame.isChosen = False
            self.titleOptions.isChosen = True
            self.titlePlayGame.update('PLAY GAME', TITLE_FONT)
            self.titleOptions.update('OPTIONS', TITLE_FONT_HORVED)
        
        self.surface.fill((0, 0, 0, 0))
        self.titleSimpleSnake.draw(self.surface)
        self.titlePlayGame.draw(self.surface)
        self.titleOptions.draw(self.surface)
        
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        

###########  CLASS PLAY GAME MENU  ############################################################
class PlayGameMenu:
    def __init__(self, x, y, width, height):
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = MENU_CHANGE_COLOR_SPEED
        self.cursor = 0
        
        self.titleNewGame = Button("NEW GAME", TITLE_FONT, width//2, height*4//12)
        self.titleNewGame.draw(self.surface)
        
        self.titleContinueGame = Button("CONTINUE GAME", TITLE_FONT, width//2, height*6//12)
        self.titleContinueGame.draw(self.surface)
        
        self.titleBack = Button("BACK", TITLE_FONT, width//2, height*8//12)
        self.titleBack.draw(self.surface)
        
    
    def update(self):
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
            
        self.surface.fill((0, 0, 0, 0))
        self.titleNewGame.draw(self.surface)
        self.titleContinueGame.draw(self.surface)
        self.titleBack.draw(self.surface)
        
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
        
        
        
        