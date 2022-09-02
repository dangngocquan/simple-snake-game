import pygame

MAIN_MENU_FPS = 40

###########  FONT  #############################################################
pygame.font.init()
SIMPLE_SNAKE_FONT = pygame.font.SysFont('algerian', 96)
TITLE_FONT = pygame.font.SysFont('castellar', 48)

###########  COLOR  ############################################################
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Button:
    def __init__(self, text, font, x, y):
        self.text = font.render(text, True, WHITE, None)
        self.textRect = self.text.get_rect()
        self.textRect.center = (x, y)
        self.isChosen = False
        self.valueRB = 255
        self.valueRBStatus = 1
    
    def update(self, text, font):
        if self.isChosen:
            if self.valueRB == 255 or self.valueRB == 55:
                self.valueRBStatus *= -1
            self.valueRB += 50 * self.valueRBStatus
            self.text = font.render(text, True, (self.valueRB, 255, self.valueRB), None)
        else:
            self.valueRB = 255
            self.valueRBStatus = 1
            self.text = font.render(text, True, (self.valueRB, 255, self.valueRB), None)
            
    
    def draw(self, parentSurface):
        parentSurface.blit(self.text, self.textRect)
        
    
    

class MainMenu:
    def __init__(self, x, y, width, height):
        self.surface = pygame.Surface((width, height))
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = MAIN_MENU_FPS
        
        self.titleSimpleSnake = Button("SIMPLE SNAKE", SIMPLE_SNAKE_FONT, width//2, height//6)
        self.titleSimpleSnake.draw(self.surface)
        
        self.titlePlayGame = Button("PLAY GAME", TITLE_FONT, width//2, height*5//12)
        self.titlePlayGame.draw(self.surface)
        
        self.titleOptions = Button("OPTIONS", TITLE_FONT, width//2, height*7//12)
        self.titleOptions.draw(self.surface)
        
        self.cursor = 0
    
    def update(self):
        if self.cursor == 0:
            self.titlePlayGame.isChosen = True
        else:
            self.titlePlayGame.isChosen = False
        if self.cursor == 1:
            self.titleOptions.isChosen = True
        else:
            self.titleOptions.isChosen = False    
            
        self.titlePlayGame.update('PLAY GAME', TITLE_FONT)
        self.titlePlayGame.draw(self.surface)
        
        
        self.titleOptions.update('OPTIONS', TITLE_FONT)
        self.titleOptions.draw(self.surface)
        
        

    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
        