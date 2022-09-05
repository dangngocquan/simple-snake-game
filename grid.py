import pygame
from setting import *



###########   CLASS GRID   ##################################################################################
class Grid:
    ###########   Constructor   #############################################################################
    def __init__(self, x, y):
        ###########   Create surface and coordiante topLeft   ###############################################
        self.surface = pygame.Surface((INGAME_WIDTH, INGAME_HEIGHT), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (x, y)
        ###########   Draw lines   ##########################################################################
        for row in range(NUMBER_ROWS):
            pygame.draw.line(self.surface, GRAY, (0, row*CELL_SIZE), (INGAME_WIDTH, row*CELL_SIZE))
        for column in range(NUMBER_COLUMNS):
            pygame.draw.line(self.surface, GRAY, (column*CELL_SIZE, 0), (column*CELL_SIZE, INGAME_HEIGHT))
    
    ###########   Update status of Grid   ###################################################################
    def update(self):
        pass
    
    ###########   Draw Grid on another surface   ############################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)