import pygame
from setting import *
from grid import *
from button import Button
from menuGetInput import GetPasswordMenu

###########   VARIABLE   ####################################################################################
ANIMATION_SPEED = SETTING1['MENU']['ANIMATION_SPEED']
BIG_FONT = SETTING2['MENU']['BIG_FONT']
MEDIUM_FONT = SETTING2['MENU']['MEDIUM_FONT']
MEDIUM_FONT_HORVED = SETTING2['MENU']['MEDIUM_FONT_HORVED']
MEDIUM_FONT_2 = SETTING2['MENU']['MEDIUM_FONT_2']
SMALL_FONT = SETTING2['MENU']['SMALL_FONT']
DESCRIPTION_FONT = SETTING2['MENU']['DESCRIPTION_FONT']
WHITE = SETTING2['COLOR']['WHITE']


###########   Load data of Statistics from json file   ######################################################
def loadData(path='./data/statistics/statistics.json'):
    data = None
    with open(path, 'r') as file:
        data = json.load(file)
    file.close()
    return data

STATISTICS = loadData()

###########   Save data of Statistic to json file   #########################################################
def saveData(path='./data/statistics/statistics.json'):   
    with open(path, 'w') as file:
        json.dump(STATISTICS, file, indent=4)
    file.close()
   

###########  CLASS STATISTICS MENU  #########################################################################
class StatisticsMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        self.positionMouse = (-100, -100)
        self.positionLeftMouse = (-100, -100)
        ########### Buttons in Statistics Menu  ##############################################################
        self.title = Button("Statistics", MEDIUM_FONT, width//10, height*1//24, 'topLeft')
        self.titleHighestScore = Button(f"Highest score:    {STATISTICS['HIGHEST_SCORE']} - {STATISTICS['PLAYER_HAS_HIGHEST_SCORE']}", 
                                        DESCRIPTION_FONT, width//10, height*4//24, 'topLeft')
        self.titleTotalTimePlayed = Button(
            f"Total Time Played:    {STATISTICS['TOTAL_TIME_PLAYED']//3600:0>2}:{STATISTICS['TOTAL_TIME_PLAYED']%3600//60:0>2}:{STATISTICS['TOTAL_TIME_PLAYED']%60:0>2}", 
            DESCRIPTION_FONT, width//10, height*6//24, 'topLeft')
        self.titleNumberOfMatchesPlayed = Button(f"Number of matches played:    {STATISTICS['NUMBER_OF_MATCHES_PLAYED']}", 
                                                 DESCRIPTION_FONT, width//10, height*8//24, 'topLeft')
        self.titleNumberOfMatchesWon = Button(f"Number Of Matches Won:    {STATISTICS['NUMBER_OF_MATCHES_WON']}", 
                                              DESCRIPTION_FONT, width//10, height*10//24, 'topLeft')
        self.titleNumberOfMatchesLost = Button(f"Number of matches lost:    {STATISTICS['NUMBER_OF_MATCHES_LOST']}", 
                                               DESCRIPTION_FONT, width//10, height*12//24, 'topLeft')
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*22//24)
    
    ##################    Update current position of mouse    ###############################################
    def updatePostionMouse(self, position):
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
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleBack.textRect):
            self.cursor = 0
        else:
            self.cursor = 2
    
    ###############     Update when player left-click    ####################################################
    def updatePositionLeftMouse(self):
        self.positionLeftMouse = self.positionMouse
        if self.isPointedAt(positionMouse=self.positionLeftMouse,
                            surfaceCheckRect=self.titleBack.textRect):
            self.cursor = -1
        self.positionLeftMouse = (-100, -100)
    
    
    
    ###########   Update cursor and buttons status in Statistics Menu   #####################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        self.updateMousePoitedAt()
        if self.cursor == 0:
            self.titleBack.isChosen = True
            self.titleBack.update("BACK", MEDIUM_FONT_HORVED, 'G')
        else:
            self.titleBack.isChosen = False
            self.titleBack.update("BACK", MEDIUM_FONT, 'G')
            
        self.titleHighestScore.update(
            f"Highest score:    {STATISTICS['HIGHEST_SCORE']} - {STATISTICS['PLAYER_HAS_HIGHEST_SCORE']}", 
            DESCRIPTION_FONT) 
        self.titleTotalTimePlayed.update(
            f"Total Time Played:    {STATISTICS['TOTAL_TIME_PLAYED']//3600:0>2}:{STATISTICS['TOTAL_TIME_PLAYED']%3600//60:0>2}:{STATISTICS['TOTAL_TIME_PLAYED']%60:0>2}",
            DESCRIPTION_FONT)
        self.titleNumberOfMatchesPlayed.update(
            f"Number of matches played:    {STATISTICS['NUMBER_OF_MATCHES_PLAYED']}", DESCRIPTION_FONT)
        self.titleNumberOfMatchesWon.update(
            f"Number Of Matches Won:    {STATISTICS['NUMBER_OF_MATCHES_WON']}", DESCRIPTION_FONT)
        self.titleNumberOfMatchesLost.update(
            f"Number of matches lost:    {STATISTICS['NUMBER_OF_MATCHES_LOST']}", DESCRIPTION_FONT)
        
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
        self.title.draw(self.surface)
        self.titleHighestScore.draw(self.surface)
        self.titleTotalTimePlayed.draw(self.surface)
        self.titleNumberOfMatchesPlayed.draw(self.surface)
        self.titleNumberOfMatchesWon.draw(self.surface)
        self.titleNumberOfMatchesLost.draw(self.surface)
        self.titleBack.draw(self.surface)

    
    ###########  Draw Statistics Menu in another surface  ###################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)