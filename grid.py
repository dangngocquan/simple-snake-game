import pygame
from setting import *

WIDTH = SETTING2['SCREEN']['WIDTH']
HEIGHT = SETTING2['SCREEN']['HEIGHT']
NUMBER_ROWS = SETTING2['SCREEN']['NUMBER_ROWS']
NUMBER_COLUMNS = SETTING2['SCREEN']['NUMBER_COLUMNS']
CELL_SIZE = SETTING2['SCREEN']['CELL_SIZE']
GRAY = SETTING2['COLOR']['GRAY']

###########   CLASS GRID   ##################################################################################
class Grid:
    ###########   Constructor   #############################################################################
    def __init__(self, x, y):
        ###########   Create surface and coordiante topLeft   ###############################################
        self.surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (x, y)
        ###########   Draw lines   ##########################################################################
        for row in range(NUMBER_ROWS):
            pygame.draw.line(self.surface, GRAY, (0, row*CELL_SIZE), 
                             (WIDTH, row*CELL_SIZE))
        for column in range(NUMBER_COLUMNS):
            pygame.draw.line(self.surface, GRAY, (column*CELL_SIZE, 0), 
                             (column*CELL_SIZE, HEIGHT))
    
    ###########   Update status of Grid   ###################################################################
    def update(self):
        pass
    
    ###########   Draw Grid on another surface   ############################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)