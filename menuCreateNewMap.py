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