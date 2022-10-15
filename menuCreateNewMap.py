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
        
        self.positionMouse = (-100,-100)
        self.positionLeftMouse = (-100, -100)
        self.positionRightMouse = (-100, -100)
        
        self.cellBeingPoitedAt = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        self.cellBeingPoitedAt.fill(GRAY)
        self.cellBeingPoitedAtRect = self.cellBeingPoitedAt.get_rect()
        self.cellBeingPoitedAtRect.topleft = self.positionMouse
        
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
        if self.showingInstruction:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleStart.textRect):
                self.titleStart.isChosen = True
                self.titleStart.update('START', MEDIUM_FONT_HORVED)
            else:
                self.titleStart.isChosen = False
                self.titleStart.update('START', MEDIUM_FONT)
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleBack.textRect):
                self.titleBack.isChosen = True
                self.titleBack.update('BACK', MEDIUM_FONT_HORVED)
            else:
                self.titleBack.isChosen = False
                self.titleBack.update('BACK', MEDIUM_FONT)
        elif self.drawingNewMap:
            self.updateCellBeingPoitedAt()
    
    ###############     Update when player left-click    ####################################################
    def updatePositionLeftMouse(self):
        self.positionLeftMouse = self.positionMouse
        if self.showingInstruction:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleStart.textRect):
                self.cursor = 0
            elif self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleBack.textRect):
                self.cursor = 1
            else:
                self.cursor = 2
        elif self.drawingNewMap:
            self.addNewWallBlock()
        self.positionLeftMouse = (-100, -100)
        
    def updatePositionRightMouse(self):
        self.positionRightMouse = self.positionMouse
        if self.drawingNewMap:
            self.removeWallBlock()
        self.positionRightMouse = (-100, -100)
    
    def updateCellBeingPoitedAt(self):
        x = self.positionMouse[0]//CELL_SIZE*CELL_SIZE
        y = self.positionMouse[1]//CELL_SIZE*CELL_SIZE
        if [x, y] in (self.wallManager.coordinateWalls() 
                      + self.snake01.coordinateSnakeBlocks()
                      + self.snake02.coordinateSnakeBlocks()
                      + self.snake03.coordinateSnakeBlocks()):
            self.cellBeingPoitedAtRect.topleft = (-100, -100)
        else:
            self.cellBeingPoitedAtRect.topleft = (x, y)
    
    def addNewWallBlock(self):
        x = self.positionLeftMouse[0]//CELL_SIZE*CELL_SIZE
        y = self.positionLeftMouse[1]//CELL_SIZE*CELL_SIZE
        if [x, y] not in (self.wallManager.coordinateWalls()
                          + self.snake01.coordinateSnakeBlocks()
                          + self.snake02.coordinateSnakeBlocks()
                          + self.snake03.coordinateSnakeBlocks()
                          + [[-100, -100]]):
            self.wallManager.listWall.append(Wall(x, y))
        self.wallManager.updateImage()
        
    
    def removeWallBlock(self):
        x = self.positionRightMouse[0]//CELL_SIZE*CELL_SIZE
        y = self.positionRightMouse[1]//CELL_SIZE*CELL_SIZE
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
                                 createdTime=str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
    
    ###########   Update cursor and buttons status in Options Menu   ########################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        self.updateMousePoitedAt()
        if self.showingInstruction == True:
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