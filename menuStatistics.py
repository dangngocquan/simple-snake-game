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


###########   Load data of Statistics from json file   ############################################################
def loadData(path='./data/statistics/statistics.json'):
    data = None
    with open(path, 'r') as file:
        data = json.load(file)
    file.close()
    return data

STATISTICS = loadData()

###########   Save data of Account Manager to json file   ############################################################
def saveData(path='./data/statistics/statistics.json'):   
    with open(path, 'w') as file:
        json.dump(STATISTICS, file, indent=4)
    file.close()
   

###########  CLASS STATISTICS MENU  ##########################################################################
class StatisticsMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        ########### Buttons in Statistics Menu  ##############################################################
        self.title = Button("Statistics", MEDIUM_FONT, width//10, height*1//24, 'topLeft')
        self.titleHighestScore = Button(f"Highest score: {STATISTICS['HIGHEST_SCORE']}", MEDIUM_FONT, width//10, 
                                        height*1//24, 'topLeft')
        self.titleTotalTimePlayed = Button(f"Total Time Played: {STATISTICS['TOTAL_TIME_PLAYED']}", MEDIUM_FONT, 
                                           width//10, height*1//24, 'topLeft')
        self.titleNumberOfMatchesPlayed = Button(f"Number of matches played: {STATISTICS['NUMBER_OF_MATCHES_PLAYED']}", 
                                                 MEDIUM_FONT, width//10, height*1//24, 'topLeft')
        self.titleNumberOfMatchesWon = Button(f"Number Of Matches Won: {STATISTICS['NUMBER_OF_MATCHES_WON']}", 
                                              MEDIUM_FONT, width//10, height*1//24, 'topLeft')
        self.titleNumberOfMatchesLost = Button(f"Number of matches lost: {STATISTICS['NUMBER_OF_MATCHES_LOST']}", MEDIUM_FONT, width//10, height*1//24, 'topLeft')
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*22//24)
        
    ###########   Update cursor and buttons status in Play Game Menu   ######################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleBack.isChosen = True
            self.titleBack.update("BACK", MEDIUM_FONT_HORVED, 'G')
        else:
            self.titleBack.isChosen = False
            self.titleBack.update("BACK", MEDIUM_FONT, 'G')
                
        
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

    
    ###########  Draw PlayGame Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)