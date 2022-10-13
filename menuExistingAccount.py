import pygame
from setting import *
import setting
from grid import *
from button import Button
from account import ACCOUNT_MANAGER
import account

###########   VARIABLE   ####################################################################################
ANIMATION_SPEED = SETTING1['MENU']['ANIMATION_SPEED']
BIG_FONT = SETTING2['MENU']['BIG_FONT']
MEDIUM_FONT = SETTING2['MENU']['MEDIUM_FONT']
MEDIUM_FONT_HORVED = SETTING2['MENU']['MEDIUM_FONT_HORVED']
MEDIUM_FONT_2 = SETTING2['MENU']['MEDIUM_FONT_2']
SMALL_FONT = SETTING2['MENU']['SMALL_FONT']
DESCRIPTION_FONT = SETTING2['MENU']['DESCRIPTION_FONT']
WHITE = SETTING2['COLOR']['WHITE']


###########  CLASS EXISTING ACCOUNTS MENU  ##################################################################
class ExistingAccountMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor   ######################################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        self.positionMouse = (-100, -100)
        self.positionLeftMouse = (-100, -100)
        self.tempIndexAccount = 2
        
        ##############################   In main surface   ##################################################
        self.container1 = pygame.Surface((width//4 + 30, height), pygame.SRCALPHA)
        self.container1Rect = self.container1.get_rect()
        self.container1Rect.topleft = (0, 0)
        
        self.container2 = pygame.Surface((width-self.container1Rect.width, height), pygame.SRCALPHA)
        self.container2Rect = self.container2.get_rect()
        self.container2Rect.topleft = (self.container1Rect.width, 0)
        
        #########################   In container 1   ########################################################
        self.selection1 = pygame.Surface(
            (self.container1Rect.width, self.container1Rect.height//8), pygame.SRCALPHA)
        self.selection1Rect = self.selection1.get_rect()
        self.selection1Rect.topleft = (0, 0)
        
        
        self.selection2 = pygame.Surface(
            (self.container1Rect.width, self.container1Rect.height//8), pygame.SRCALPHA)
        self.selection2Rect = self.selection2.get_rect()
        self.selection2Rect.topleft = (0, self.container1Rect.height//8)
        
        self.selection3 = pygame.Surface(
            (self.container1Rect.width, self.container1Rect.height//8), pygame.SRCALPHA)
        self.selection3Rect = self.selection3.get_rect()
        self.selection3Rect.topleft = (0, self.container1Rect.height//8 * 2)
        
        
        ########### In selection1   #########################################################################
        self.titleCurrentAccount = Button("CURRENT ACCOUNT", DESCRIPTION_FONT,
                                         self.selection1Rect.width//2, self.selection1Rect.height//2)
        ########### In selection2   #########################################################################
        self.titleOtherAccounts = Button("OTHER ACCOUNTS", DESCRIPTION_FONT,
                                            self.selection2Rect.width//2, self.selection2Rect.height//2)
        ########### In selection3   #########################################################################
        self.titleBack = Button("BACK", DESCRIPTION_FONT, 
                                self.selection3Rect.width//2, self.selection3Rect.height//2)
        
        #################   In container 2   ################################################################
        self.container22 = pygame.Surface((self.container2Rect.width//8*5, height), pygame.SRCALPHA)
        self.container22Rect = self.container22.get_rect()
        self.container22Rect.topleft = (0, 0)
        
        self.container21 = pygame.Surface((self.container2Rect.width - self.container22Rect.width - 20, 
                                           40*10), pygame.SRCALPHA)
        self.container21Rect = self.container21.get_rect()
        self.container21Rect.topleft = (0, self.selection1Rect.height)
        
        ######################   In container21   ############################################################
        self.subtractNumber = 0
        self.listCell = []
        self.listCellRect = []
        self.listTitleNameAccount = []
        for i in range(len(ACCOUNT_MANAGER.listAccount)):
            cell = pygame.Surface((self.container21Rect.width, 40), pygame.SRCALPHA)
            cellRect = cell.get_rect()
            cellRect.topleft = (0, 40*i - self.subtractNumber)
            titleName = Button(f"{ACCOUNT_MANAGER.listAccount[i].name}", DESCRIPTION_FONT_2, 20, 10, 'topLeft')
            self.listCell.append(cell)
            self.listCellRect.append(cellRect)
            self.listTitleNameAccount.append(titleName)
        
        ######################   In container22   ############################################################
        self.titleName = Button(f"{ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name}", MEDIUM_FONT,
                                         20, self.container22Rect.height//24*2, 'topLeft')
        self.titleCreatedTime = Button(
            f"Created time: {ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].createdTime}", DESCRIPTION_FONT_2,
                                         20, self.container22Rect.height//24*6, 'topLeft')
        self.titleWinMatch = Button(f"Number win match: {ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].winMatch}", 
                                    DESCRIPTION_FONT_2, 20, self.container22Rect.height//24*8, 'topLeft')
        self.titleLoseMatch = Button(f"Number loss match: {ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].loseMatch}", 
                                     DESCRIPTION_FONT_2, 20, self.container22Rect.height//24*10, 'topLeft')
        tempSeconds = ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].totalTimePlayed
        self.titleTotalTimePlayed = Button(f"Total time played: {tempSeconds//3600}h{(tempSeconds%3600)//60}m{tempSeconds%60}s", 
                                     DESCRIPTION_FONT_2, 20, self.container22Rect.height//24*12, 'topLeft')
        
        self.titlePlayThisAccount = Button("PLAY THIS ACCOUNT", DESCRIPTION_FONT, 20, self.container22Rect.height//24*16, 'topLeft')
        self.titleDeleteThisAccount = Button("DELETE THIS ACCOUNT", DESCRIPTION_FONT, 20, self.container22Rect.height//24*18, 'topLeft')
        
    
    def updatePostionMouse(self, position):
        self.positionMouse = position
        
    def updatePositonLeftMouse(self):
        self.positionLeftMouse = self.positionMouse
        if self.isPointedAt(positionMouse=self.positionLeftMouse,
                            surfaceCheckRect=self.selection1Rect,
                            parent1SurfaceRect=self.container1Rect):
            self.cursor = 0
        elif self.isPointedAt(positionMouse=self.positionLeftMouse,
                            surfaceCheckRect=self.selection2Rect,
                            parent1SurfaceRect=self.container1Rect):
            self.cursor = 1
        elif self.isPointedAt(positionMouse=self.positionLeftMouse,
                            surfaceCheckRect=self.selection3Rect,
                            parent1SurfaceRect=self.container1Rect):
            self.cursor = 2
        if self.cursor == 1:
            for i in range(len(ACCOUNT_MANAGER.listAccount)):
                if self.isPointedAt(positionMouse=self.positionMouse,
                                    surfaceCheckRect=self.listCellRect[i],
                                    parent1SurfaceRect=self.container21Rect,
                                    parent2SurfaceRect=self.container2Rect):
                    if (self.listCellRect[i].topleft[1] >= 0 
                        and self.listCellRect[i].topleft[1] <= 40*(10-1)):
                        self.tempIndexAccount = i
            if self.isPointedAt(positionMouse=self.positionLeftMouse,
                            surfaceCheckRect=self.titlePlayThisAccount.textRect,
                            parent1SurfaceRect=self.container22Rect,
                            parent2SurfaceRect=self.container2Rect):
                setting.replaceData(key1='ACCOUNT', key2='INDEX_ACCOUNT', newData=self.tempIndexAccount)
                setting.saveSetting()
                self.cursor = 2
            if self.isPointedAt(positionMouse=self.positionLeftMouse,
                            surfaceCheckRect=self.titleDeleteThisAccount.textRect,
                            parent1SurfaceRect=self.container22Rect,
                            parent2SurfaceRect=self.container2Rect):
                if self.tempIndexAccount > 0:
                    if self.tempIndexAccount == SETTING1['ACCOUNT']['INDEX_ACCOUNT']:
                        setting.replaceData(key1='ACCOUNT', key2='INDEX_ACCOUNT', newData=0)
                        setting.saveSetting()
                    ACCOUNT_MANAGER.removeAccount(indexAccount=self.tempIndexAccount)
                    self.tempIndexAccount -= 1
                    account.saveData(ACCOUNT_MANAGER.listAccount)
        self.positionLeftMouse = (-100, -100)
    
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
    
    def updateMousePoitedAt(self):
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.selection1Rect,
                            parent1SurfaceRect=self.container1Rect):
            self.titleCurrentAccount.isChosen = True
            self.titleOtherAccounts.isChosen = False
            self.titleBack.isChosen = False
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.selection2Rect,
                            parent1SurfaceRect=self.container1Rect):
            self.titleCurrentAccount.isChosen = False
            self.titleOtherAccounts.isChosen = True
            self.titleBack.isChosen = False
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.selection3Rect,
                            parent1SurfaceRect=self.container1Rect):
            self.titleCurrentAccount.isChosen = False
            self.titleOtherAccounts.isChosen = False
            self.titleBack.isChosen = True
        else:
            self.titleCurrentAccount.isChosen = False
            self.titleOtherAccounts.isChosen = False
            self.titleBack.isChosen = False
        if self.cursor == 1:
            for i in range(len(ACCOUNT_MANAGER.listAccount)):
                if self.isPointedAt(positionMouse=self.positionMouse,
                                    surfaceCheckRect=self.listCellRect[i],
                                    parent1SurfaceRect=self.container21Rect,
                                    parent2SurfaceRect=self.container2Rect):
                    self.listTitleNameAccount[i].isChosen = True
                else:
                    self.listTitleNameAccount[i].isChosen = False
            if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titlePlayThisAccount.textRect,
                            parent1SurfaceRect=self.container22Rect,
                            parent2SurfaceRect=self.container2Rect):
                self.titlePlayThisAccount.isChosen = True
            else:
                self.titlePlayThisAccount.isChosen = False
            if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleDeleteThisAccount.textRect,
                            parent1SurfaceRect=self.container22Rect,
                            parent2SurfaceRect=self.container2Rect):
                self.titleDeleteThisAccount.isChosen = True
            else:
                self.titleDeleteThisAccount.isChosen = False

    def increaseSubtractNumber(self):
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.container21Rect,
                            parent1SurfaceRect=self.container2Rect):
            if len(ACCOUNT_MANAGER.listAccount) > 10:
                self.subtractNumber += 40
                self.subtractNumber = min(len(ACCOUNT_MANAGER.listAccount)*40 - 400, self.subtractNumber)
        
    def decreaseSubtractNumber(self):
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.container21Rect,
                            parent1SurfaceRect=self.container2Rect):
            self.subtractNumber -= 40
            self.subtractNumber = max(0, self.subtractNumber)
        
    def updateAccountInfoShowing(self):
        if self.cursor == 0:
            self.titleName = Button(f"{ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name}", MEDIUM_FONT,
                                         20, self.container22Rect.height//24*2, 'topLeft')
            self.titleCreatedTime = Button(
                f"Created time: {ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].createdTime}", DESCRIPTION_FONT_2,
                                            20, self.container22Rect.height//24*6, 'topLeft')
            self.titleWinMatch = Button(f"Number win match: {ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].winMatch}", 
                                        DESCRIPTION_FONT_2, 20, self.container22Rect.height//24*8, 'topLeft')
            self.titleLoseMatch = Button(f"Number loss match: {ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].loseMatch}", 
                                        DESCRIPTION_FONT_2, 20, self.container22Rect.height//24*10, 'topLeft')
            tempSeconds = ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].totalTimePlayed
            self.titleTotalTimePlayed = Button(f"Total time played: {tempSeconds//3600}h{(tempSeconds%3600)//60}m{tempSeconds%60}s", 
                                        DESCRIPTION_FONT_2, 20, self.container22Rect.height//24*12, 'topLeft')
        elif self.cursor == 1:
            self.titleName = Button(f"{ACCOUNT_MANAGER.listAccount[self.tempIndexAccount].name}", MEDIUM_FONT,
                                         20, self.container22Rect.height//24*2, 'topLeft')
            self.titleCreatedTime = Button(
                f"Created time: {ACCOUNT_MANAGER.listAccount[self.tempIndexAccount].createdTime}", DESCRIPTION_FONT_2,
                                            20, self.container22Rect.height//24*6, 'topLeft')
            self.titleWinMatch = Button(f"Number win match: {ACCOUNT_MANAGER.listAccount[self.tempIndexAccount].winMatch}", 
                                        DESCRIPTION_FONT_2, 20, self.container22Rect.height//24*8, 'topLeft')
            self.titleLoseMatch = Button(f"Number loss match: {ACCOUNT_MANAGER.listAccount[self.tempIndexAccount].loseMatch}", 
                                        DESCRIPTION_FONT_2, 20, self.container22Rect.height//24*10, 'topLeft')
            tempSeconds = ACCOUNT_MANAGER.listAccount[self.tempIndexAccount].totalTimePlayed
            self.titleTotalTimePlayed = Button(f"Total time played: {tempSeconds//3600}h{(tempSeconds%3600)//60}m{tempSeconds%60}s", 
                                        DESCRIPTION_FONT_2, 20, self.container22Rect.height//24*12, 'topLeft')
       
    ###########  Update cursor and button status in Accounts Setting Menu ###############################################
    def update(self):
        ###########  Update cursor and button of Accounts Setting menu  #################################################
        if len(self.listCell) != len(ACCOUNT_MANAGER.listAccount):
            self.listCell = []
            self.listCellRect = []
            self.listTitleNameAccount = []
            for i in range(len(ACCOUNT_MANAGER.listAccount)):
                cell = pygame.Surface((self.container21Rect.width, 40), pygame.SRCALPHA)
                cellRect = cell.get_rect()
                cellRect.topleft = (0, 40*i - self.subtractNumber)
                titleName = Button(f"{ACCOUNT_MANAGER.listAccount[i].name}", DESCRIPTION_FONT_2, 20, 10, 'topLeft')
                self.listCell.append(cell)
                self.listCellRect.append(cellRect)
                self.listTitleNameAccount.append(titleName)
        for i in range(len(self.listCellRect)):
            self.listCellRect[i].topleft = (0, 40*i - self.subtractNumber)
        self.updateMousePoitedAt()
        for i in range(len(ACCOUNT_MANAGER.listAccount)):
            self.listTitleNameAccount[i].update(f"{ACCOUNT_MANAGER.listAccount[i].name}", DESCRIPTION_FONT_2, 'B')
        self.titleCurrentAccount.update("CURRENT ACCOUNT", DESCRIPTION_FONT, 'B')
        self.titleOtherAccounts.update("OTHER ACCOUNTS", DESCRIPTION_FONT, 'B')
        self.titleBack.update("BACK", DESCRIPTION_FONT, 'B')    
        self.updateAccountInfoShowing()
        
        self.titlePlayThisAccount.update("Play this account", DESCRIPTION_FONT, 'G')
        self.titleDeleteThisAccount.update("Delete this account", DESCRIPTION_FONT, 'R')
        ###########  Remove old display  #############################################################
        self.surface.fill((0, 0, 0, 0))
        self.container1.fill((0, 0, 0, 0))
        self.selection1.fill((0, 0, 0, 0))
        self.selection2.fill((0, 0, 0, 0))
        self.selection3.fill((0, 0, 0, 0))
        if self.cursor == 0:
            self.selection1.fill((70, 70, 70))
        elif self.cursor == 1:
            self.selection2.fill((70, 70, 70))
        elif self.cursor == 2:
            self.selection3.fill((70, 70, 70))
        self.container2.fill((111, 111, 111))
        self.container21.fill((90, 90, 90))
        for i in range(len(ACCOUNT_MANAGER.listAccount)):
                self.listCell[i].fill((90, 90, 90))
        self.container22.fill((111, 111, 111))
        ###########  Draw new screen   ######################################################################
        self.titleCurrentAccount.draw(self.selection1)
        self.titleOtherAccounts.draw(self.selection2)
        self.titleBack.draw(self.selection3)
        self.container1.blit(self.selection1, self.selection1Rect)
        self.container1.blit(self.selection2, self.selection2Rect)
        self.container1.blit(self.selection3, self.selection3Rect)
        
        self.container22.blit(self.titleName.text, self.titleName.textRect)
        self.container22.blit(self.titleCreatedTime.text, self.titleCreatedTime.textRect)
        self.container22.blit(self.titleWinMatch.text, self.titleWinMatch.textRect)
        self.container22.blit(self.titleLoseMatch.text, self.titleLoseMatch.textRect)
        self.container22.blit(self.titleTotalTimePlayed.text, self.titleTotalTimePlayed.textRect)
        if self.cursor == 0:
            self.container22Rect.topleft = (self.container2Rect.width//16*2, 0)
        elif self.cursor == 1:
            self.container22Rect.topleft = (self.container2Rect.width//8*3, 0)
            self.container22.blit(self.titlePlayThisAccount.text, self.titlePlayThisAccount.textRect)
            if self.tempIndexAccount > 0:
                self.container22.blit(self.titleDeleteThisAccount.text, self.titleDeleteThisAccount.textRect)
            for i in range(len(ACCOUNT_MANAGER.listAccount)):
                self.listCell[i].blit(self.listTitleNameAccount[i].text, self.listTitleNameAccount[i].textRect)
                self.container21.blit(self.listCell[i], self.listCellRect[i])
            self.container2.blit(self.container21, self.container21Rect)    
        self.container2.blit(self.container22, self.container22Rect)
        self.surface.blit(self.container1, self.container1Rect)
        self.surface.blit(self.container2, self.container2Rect)
        
    ###########  Draw Accounts Setting Menu in another surface  #########################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)