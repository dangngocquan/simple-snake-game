from datetime import datetime
import statistics
import sys
import webbrowser
import pygame
from account import ACCOUNT_MANAGER
import account
from food import NUMBER_COLUMNS, NUMBER_ROWS, FoodManager
import food
from menuMain import MainMenu
from menuPlayGame import PlayGameMenu
from menuAccountsSetting import AccountsSettingMenu
from menuExistingAccount import ExistingAccountMenu
from menuCreateNewAccount import CreateNewAccountMenu
from menuOptions import OptionsMenu
from menuGamemodeSetting import GamemodeSettingMenu
from menuInGameSetting import GameSettingMenu
from menuSoundSetting import SoundSettingMenu
from menuMapSetting import MapSettingMenu
from menuExistingMaps import ExistingMapsMenu
from menuCreateNewMap import CreateNewMap
from menuStatistics import STATISTICS, StatisticsMenu
import menuStatistics
from menuHistory import HISTORY, HistoryMenu
import menuHistory
from menuAboutGame import AboutGameMenu
from menuGameOver import GameOverMenu, GameOverMenu02
from inGame import InGame, InGame02
from snake import Snake
import snake
import wall
from wall import Wall, WallManager
from setting import *
import setting

###########   VARIABLE   ####################################################################################
WIDTH = SETTING2['SCREEN']['WIDTH']
HEIGHT = SETTING2['SCREEN']['HEIGHT']
CAPTION = SETTING2['SCREEN']['CAPTION']
FPS = SETTING2['SCREEN']['FPS']
BLACK = SETTING2['COLOR']['BLACK']

###########   CLASS GAME   ##################################################################################
class Game:
    ###########   Constructor   #############################################################################
    def __init__(self):
        ###########   Create window game, caption, clock   ##################################################
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(SETTING2['SOUND']['MUSIC'][SETTING1['SOUND']['MUSIC_INDEX']])
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(SETTING1['SOUND']['MUSIC_VOLUME'] / 100)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()
        self.countTicks = 0
        self.divisibility = 462
        self.startTimeOpen = datetime.now()
        self.startTimePlayThisAccount = datetime.now()
        ###########   Status in game   ######################################################################
        self.running = True
        self.runningMainMenu = True
        self.runningPlayGameMenu = False
        self.runningInGame = False
        self.runningInGame02 = False
        self.runningAccountsSetting = False
        self.runningExistingAccountMenu = False
        self.runningCreateNewAccountMenu = False
        self.runningOptionsMenu = False
        self.runningGamemodeSettingMenu = False
        self.runningGameSettingMenu = False
        self.runningSoundSettingMenu = False
        self.runningMapSettingMenu = False
        self.runningExistingMapsMenu = False
        self.runningCreateNewMap = False
        self.runningStatisticsMenu = False
        self.runningHistoryMenu = False
        self.runningAboutGameMenu = False
        self.runningGameOverMenu = False
        self.runningGameOverMenu02 = False
        ###########   Screens in game   #####################################################################
        self.mainMenu = MainMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.playGameMenu = PlayGameMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.inGame = InGame()
        self.inGame02 = InGame02()
        self.gameOverMenu = GameOverMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT, self.inGame.snake, 
                                         self.inGame.wallManager)
        self.gameOverMenu02 = GameOverMenu02(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT, self.inGame02.snake01,
                                             self.inGame02.snake02, self.inGame02.wallManager)
        self.accountsSetting = AccountsSettingMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.existingAccountMenu = ExistingAccountMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.createNewAccountMenu = CreateNewAccountMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.optionsMenu = OptionsMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.gamemodeSettingMenu = GamemodeSettingMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.gameSettingMenu = GameSettingMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.soundSettingMenu = SoundSettingMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.mapSettingMenu = MapSettingMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.existingMapsMenu = ExistingMapsMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.createNewMap = CreateNewMap(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.statisticsMenu = StatisticsMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.historyMenu = HistoryMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.aboutGameMenu = AboutGameMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
    
    ###########   Main loop in game   #######################################################################
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.getEvents()
            for i in range(self.divisibility):
                self.countTicks = (self.countTicks + 1) % (FPS * self.divisibility)
                self.update()
            self.display()
            
    
    ###########   Get events in current screen   ############################################################    
    def getEvents(self):
        for event in pygame.event.get():
            ###########   Quit game   #######################################################################
            if event.type == pygame.QUIT:
                ##############   Update statistics of game   ################################################
                STATISTICS['TOTAL_TIME_PLAYED'] += int((datetime.now() -self.startTimeOpen).total_seconds())
                menuStatistics.saveData()
                ####################   Update statistics of current player account   ########################
                ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].totalTimePlayed += int(
                    (datetime.now() - self.startTimePlayThisAccount).total_seconds())
                account.saveData(ACCOUNT_MANAGER.listAccount)
                ###########   Save data before quit game   ##################################################
                if self.runningInGame:
                    snake.saveSnake(self.inGame.snake)
                    food.saveFoodManager(foodManager=self.inGame.foodManager)
                    wall.saveWallManager(self.inGame.wallManager)
                elif self.runningGameOverMenu:
                    snake.saveSnake(Snake())
                    food.saveFoodManager(FoodManager())
                    wall.saveWallManager(wall.loadWallManagerFromListMaps(indexMap=SETTING1['MAP']['INDEX_MAP']))
                elif self.runningInGame02:
                    snake.saveSnake(self.inGame02.snake01, path='./data/player/twoPlayer/snake/snake01.json')
                    snake.saveSnake(self.inGame02.snake02, path='./data/player/twoPlayer/snake/snake02.json')
                    food.saveFoodManager(self.inGame02.foodManager, path='./data/player/twoPlayer/food/food.json')
                    wall.saveWallManager(self.inGame02.wallManager,
                                         path='./data/player/twoPlayer/wall/wall.json')
                elif self.runningGameOverMenu02:
                    self.inGame02.snake01 = Snake(typeLocation=-1, typeColor='blue')
                    self.inGame02.snake02 = Snake(typeLocation=1, typeColor='green')
                    self.inGame02.foodManager = FoodManager()
                    self.inGame02.update()
                    snake.saveSnake(self.inGame02.snake01, path='./data/player/twoPlayer/snake/snake01.json')
                    snake.saveSnake(self.inGame02.snake02, path='./data/player/twoPlayer/snake/snake02.json')
                    food.saveFoodManager(self.inGame02.foodManager, path='./data/player/twoPlayer/food/food.json')
                    wall.saveWallManager(wall.loadWallManagerFromListMaps(indexMap=SETTING1['MAP']['INDEX_MAP']),
                                         path='./data/player/twoPlayer/wall/wall.json')
                elif self.runningCreateNewMap:
                    wall.saveWallManager(self.createNewMap.wallManager,
                                                 path='./data/creatingMap/creatingMap.json')
                ###########   Quit   ########################################################################
                self.running = False
                pygame.quit()
                sys.exit()
            ###########   Get events when current screen is MAIN MENU   #####################################
            if self.runningMainMenu:
                self.mainMenu.updatePositionMouse(pygame.mouse.get_pos())
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.mainMenu.updatePositionLeftMouse()
                        ########   The cursor is "PLAY GAME"    #############################################
                        if self.mainMenu.cursor == 0:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningMainMenu = False
                            self.runningPlayGameMenu = True
                            self.playGameMenu.cursor = 0
                        ########   The cursor is "ACCOUNT"    ###############################################
                        elif self.mainMenu.cursor == 1:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningMainMenu = False
                            self.runningAccountsSetting = True
                            self.accountsSetting.cursor = 0
                        ########   The cursor is "OPTIONS"    ###############################################
                        elif self.mainMenu.cursor == 2:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningMainMenu = False
                            self.runningOptionsMenu = True
                            self.optionsMenu.cursor = 0
                        ########   The cursor is "STATISTICS"    ############################################
                        elif self.mainMenu.cursor == 3:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningMainMenu = False
                            self.runningStatisticsMenu = True
                            self.statisticsMenu.cursor = 0
                            ############   Update new data for statistics of game   #########################
                            STATISTICS['TOTAL_TIME_PLAYED'] += int(
                                (datetime.now() -self.startTimeOpen).total_seconds())
                            self.startTimeOpen = datetime.now()
                            menuStatistics.saveData()
                        ########   The cursor is "HISTORY"    ###############################################
                        elif self.mainMenu.cursor == 4:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningMainMenu = False
                            self.runningHistoryMenu = True
                            self.historyMenu.cursor = 0
                        ########   The cursor is "ABOUT GAME"    ############################################
                        elif self.mainMenu.cursor == 5:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningMainMenu = False
                            self.runningAboutGameMenu = True
                            self.aboutGameMenu.cursor = 13
                        ########   The cursor is "QUIT GAME"    #############################################
                        elif self.mainMenu.cursor == 6:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningMainMenu = False
                            self.running = False
                            ############    Update statistics of game before quit game   ####################
                            STATISTICS['TOTAL_TIME_PLAYED'] += int(
                                (datetime.now() -self.startTimeOpen).total_seconds())
                            menuStatistics.saveData()
                            pygame.time.wait(500)
                            pygame.quit()
                            sys.exit()            
            ###########   Get events when current screen is PLAY GAME MENU  #################################
            elif self.runningPlayGameMenu:
                self.playGameMenu.updatePositionMouse(pygame.mouse.get_pos())
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.playGameMenu.updatePositionLeftMouse()
                        ###########   The cursor is  "NEW GAME"   ###########################################
                        if self.playGameMenu.cursor == 0:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningPlayGameMenu = False
                            ########   If gamemode is 1 player   ############################################
                            if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                self.runningInGame = True
                                self.inGame.snake = Snake()
                                self.inGame.foodManager.removeAllFoods()
                                self.inGame.wallManager = wall.loadWallManagerFromListMaps(
                                    indexMap=SETTING1['MAP']['INDEX_MAP'])
                                self.inGame.showingScreenStart = True
                            #############   If gamemode is 2 player   #######################################
                            elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                self.runningInGame02 = True
                                self.inGame02.snake01 = Snake(typeLocation=-1, typeColor='blue')
                                self.inGame02.snake02 = Snake(typeLocation=1, typeColor='green')
                                self.inGame02.foodManager.removeAllFoods()
                                self.inGame02.wallManager = wall.loadWallManagerFromListMaps(
                                    indexMap=SETTING1['MAP']['INDEX_MAP'])
                                self.inGame02.showingScreenStart = True
                        ###########   The cursor is "CONTINUE GAME"   #######################################
                        elif self.playGameMenu.cursor == 1:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningPlayGameMenu = False
                            ############   If gamemode is 1 player   ########################################
                            if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                self.runningInGame = True
                                self.inGame.snake = snake.loadPreviousSnake()
                                self.inGame.foodManager = food.loadPreviousFoodManager()
                                self.inGame.wallManager = wall.loadPreviousWallManager()
                                self.inGame.showingScreenStart = True
                            ###########    If gamemode is 2 player   ########################################
                            elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                self.runningInGame02 = True
                                self.inGame02.snake01 = snake.loadPreviousSnake(
                                    path='./data/player/twoPlayer/snake/snake01.json')
                                self.inGame02.snake02 = snake.loadPreviousSnake(
                                    path='./data/player/twoPlayer/snake/snake02.json')
                                self.inGame02.foodManager = food.loadPreviousFoodManager(
                                    path='./data/player/twoPlayer/food/food.json')
                                self.inGame02.wallManager = wall.loadPreviousWallManager(
                                    path='./data/player/twoPlayer/wall/wall.json')
                                self.inGame02.showingScreenStart = True
                        ###########   The cursor is poiting at "BACK"   #####################################
                        elif self.playGameMenu.cursor == 2:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningPlayGameMenu = False
                            self.runningMainMenu = True
                            
            ###########   Get events when current screen is ACCOUNT SETTING MENU   ##########################
            elif self.runningAccountsSetting:
                self.accountsSetting.updatePositionMouse(pygame.mouse.get_pos())
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.accountsSetting.updatePositionLeftMouse()
                        #################    Cursor is "EXISTING ACCOUNTS"   ################################
                        if self.accountsSetting.cursor == 0:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningAccountsSetting = False
                            self.runningExistingAccountMenu = True
                            self.existingAccountMenu.cursor = 0
                            ###############   Update statistics of current player account   #################
                            ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].totalTimePlayed += int(
                                (datetime.now() - self.startTimePlayThisAccount).total_seconds())
                            account.saveData(ACCOUNT_MANAGER.listAccount)
                            self.startTimePlayThisAccount = datetime.now()
                        #################   Cursor is "CREATE NEW ACCOUNT"   ################################
                        elif self.accountsSetting.cursor == 1:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningAccountsSetting = False
                            self.runningCreateNewAccountMenu = True
                            self.createNewAccountMenu.cursor = 0
                            self.createNewAccountMenu.getInputStringMenu.removeAllChars()
                        ################   Cursor is "BACK"   ###############################################
                        elif self.accountsSetting.cursor == 2:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningAccountsSetting = False
                            self.runningMainMenu = True
            ###########   Get events when current screen is EXISTING ACCOUNT MENU   #########################
            elif self.runningExistingAccountMenu:
                self.existingAccountMenu.updatePostionMouse(pygame.mouse.get_pos())
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.existingAccountMenu.updatePositonLeftMouse()
                    elif event.button == pygame.BUTTON_WHEELDOWN:
                        self.existingAccountMenu.increaseSubtractNumber()
                    elif event.button == pygame.BUTTON_WHEELUP:
                        self.existingAccountMenu.decreaseSubtractNumber()
                ##################   When player left-click on title "BACK"   ###############################
                if self.existingAccountMenu.cursor == 2:
                    SETTING2['SOUND']['PRESS_BUTTON'].play()
                    self.runningExistingAccountMenu = False
                    self.runningAccountsSetting = True
                ##################   When player left-click on title 'Play this account'   ##################
                elif self.existingAccountMenu.cursor == 3:
                    SETTING2['SOUND']['PRESS_BUTTON'].play()
                    ########  Update statistic of current player account before change account   ############
                    ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].totalTimePlayed += int(
                        (datetime.now() - self.startTimePlayThisAccount).total_seconds())
                    account.saveData(ACCOUNT_MANAGER.listAccount)
                    self.startTimePlayThisAccount = datetime.now()
                    setting.replaceData(key1='ACCOUNT', key2='INDEX_ACCOUNT', 
                                        newData=self.existingAccountMenu.tempIndexAccount)
                    setting.saveSetting()
                    self.runningExistingAccountMenu = False
                    self.runningAccountsSetting = True
                ##################   When player left-click on title 'Delete this account'   ################
                elif self.existingAccountMenu.cursor == 4:
                    SETTING2['SOUND']['PRESS_BUTTON'].play()
                    ###########   Update statistics of current player account   #############################
                    ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].totalTimePlayed += int(
                        (datetime.now() - self.startTimePlayThisAccount).total_seconds())
                    account.saveData(ACCOUNT_MANAGER.listAccount)
                    self.startTimePlayThisAccount = datetime.now()
                    if self.existingAccountMenu.tempIndexAccount == SETTING1['ACCOUNT']['INDEX_ACCOUNT']:
                        setting.replaceData(key1='ACCOUNT', key2='INDEX_ACCOUNT', newData=0)
                        setting.saveSetting()
                    ##########   Remove account   ###########################################################
                    ACCOUNT_MANAGER.removeAccount(indexAccount=self.existingAccountMenu.tempIndexAccount)
                    self.existingAccountMenu.tempIndexAccount -= 1
                    account.saveData(ACCOUNT_MANAGER.listAccount)
                    self.existingAccountMenu.cursor = 1
            ###########   Get events when current screen is CREATE NEW ACCOUNT MENU   #######################
            elif self.runningCreateNewAccountMenu:
                self.createNewAccountMenu.updatePostionMouse(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.createNewAccountMenu.getInputStringMenu.removeChar()
                    else:
                        self.createNewAccountMenu.getInputStringMenu.addChar(pygame.key.name(event.key))
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.createNewAccountMenu.updatePositionLeftMouse()
                #########   Cursor is "CANCER"   ############################################################
                if self.createNewAccountMenu.cursor == -1:
                    SETTING2['SOUND']['PRESS_BUTTON'].play()
                    self.runningCreateNewAccountMenu = False
                    self.runningAccountsSetting = True
                ##########   Cursor is "ENTER" and create completed  ########################################
                elif self.createNewAccountMenu.cursor == 1:
                    SETTING2['SOUND']['PRESS_BUTTON'].play()
                    pygame.time.wait(500)
                    self.runningCreateNewAccountMenu = False
                    self.runningAccountsSetting = True
            ###########   Get events when current screen is Options Menu  ###################################        
            elif self.runningOptionsMenu:
                self.optionsMenu.updatePositionMouse(pygame.mouse.get_pos())
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.optionsMenu.updatePositionLeftMouse()
                        ###########   The cursor is pointing at "GAMEMODE SETTING"   ########################
                        if self.optionsMenu.cursor == 0:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningOptionsMenu = False
                            self.runningGamemodeSettingMenu = True
                            self.gamemodeSettingMenu.cursor = 9
                        ###########   The cursor is pointing at "GAME SETTING"   ############################
                        if self.optionsMenu.cursor == 1:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningOptionsMenu = False
                            self.runningGameSettingMenu = True
                            self.gameSettingMenu.cursor = 13
                        ###########   The cursor is pointing at "SOUND SETTING"   ###########################
                        elif self.optionsMenu.cursor == 2:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningOptionsMenu = False
                            self.runningSoundSettingMenu = True
                            self.soundSettingMenu.cursor = 7
                        ###########   The cursor is pointing at "MAP SETTING"   #############################
                        elif self.optionsMenu.cursor == 3:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningOptionsMenu = False
                            self.runningMapSettingMenu = True
                            self.mapSettingMenu.cursor = 3
                        ###########   The cursor is poiting at "BACK"   #####################################
                        elif self.optionsMenu.cursor == 4:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningOptionsMenu = False
                            self.runningMainMenu = True
            ###########   Get events when current screen is STATISTICS MENU   ###############################
            elif self.runningStatisticsMenu:
                self.statisticsMenu.updatePostionMouse(pygame.mouse.get_pos())
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.statisticsMenu.updatePositionLeftMouse()
                ###############   Cursor is "BACK"   ########################################################
                if self.statisticsMenu.cursor == -1:
                    SETTING2['SOUND']['PRESS_BUTTON'].play()
                    self.runningStatisticsMenu = False
                    self.runningMainMenu = True
            ###########   Get events when current screen is HISTORY MENU   ##################################
            elif self.runningHistoryMenu:
                self.historyMenu.updatePostionMouse(pygame.mouse.get_pos())
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.historyMenu.updatePositionLeftMouse()
                    elif event.button == pygame.BUTTON_WHEELDOWN:
                        self.historyMenu.increaseSubtractNumber()
                    elif event.button == pygame.BUTTON_WHEELUP:
                        self.historyMenu.decreaseSubtractNumber()
                    elif event.button == pygame.BUTTON_RIGHT:
                        self.historyMenu.addNewHistory()
                ###############   Cursor is "BACK"   ########################################################
                if self.historyMenu.cursor == -1:
                    SETTING2['SOUND']['PRESS_BUTTON'].play()
                    self.runningHistoryMenu = False
                    self.runningMainMenu = True
            ###########   Get events when current screen is ABOUT GAME MENU  ################################
            elif self.runningAboutGameMenu:
                self.aboutGameMenu.updatePositionMouse(pygame.mouse.get_pos())
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.aboutGameMenu.updatePositionLeftMouse()
                        if self.aboutGameMenu.isHiddenPasswordBox:
                            ###########   The cursor is pointing at "Music00: BoyWithUkey - Loafers"   ######
                            if self.aboutGameMenu.cursor == 0:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                webbrowser.open(
                                    url="https://www.youtube.com/watch?v=iGCE7nXfQK8&list=PLZQKIedkyIQ07V8CiKUc8KkBL_aekG77o&index=2")
                            ###########   The cursor is pointing at "Music01: Sweden - C418"   ##############
                            elif self.aboutGameMenu.cursor == 1:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                webbrowser.open(
                                    url="https://www.nhaccuatui.com/bai-hat/sweden-c418.ALubLN9LgFvf.html")
                            ###########   The cursor is pointing at "Change Button"   #######################
                            elif self.aboutGameMenu.cursor == 2:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                webbrowser.open(
                                    url="https://drive.google.com/file/d/1RV6iASyK85xAnvJ1OZl99khjsnmhi_0g/view?usp=sharing")
                            ###########   The cursor is pointing at "Press Button"   ########################
                            elif self.aboutGameMenu.cursor == 3:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                webbrowser.open(
                                    url="https://drive.google.com/file/d/1gu6LhBLcEVvN_x9rTD95nLLwzuWoVbdC/view?usp=sharing")
                            ###########   The cursor is pointing at "Snake eat food"   ######################
                            elif self.aboutGameMenu.cursor == 4:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                webbrowser.open(
                                    url="https://drive.google.com/file/d/1oeuZJTJYihGg22lgQX0hQaTSlDpNcrxw/view?usp=sharing")
                            ###########   The cursor is pointing at "Game Over"   ###########################
                            elif self.aboutGameMenu.cursor == 5:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                webbrowser.open(
                                    url="https://pixabay.com/sound-effects/search/gameover/?manual_search=1&order=None")
                            ###########   The cursor is pointing at "Win Game"   ############################
                            elif self.aboutGameMenu.cursor == 6:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                webbrowser.open(
                                    url="https://pixabay.com/sound-effects/search/win/?manual_search=1&order=None")
                            ###########   The cursor is pointing at "Snake"   ###############################
                            elif self.aboutGameMenu.cursor == 7:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                webbrowser.open(
                                    url="https://drive.google.com/drive/folders/1z1hBUdLROt_smwh3E25rmqYrmDptpaCn?usp=sharing")
                            ###########   The cursor is pointing at "Food"   ################################
                            elif self.aboutGameMenu.cursor == 8:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                webbrowser.open(
                                    url="https://drive.google.com/drive/folders/1IBQvUQiYWVVAU1Y_L3Q-yHZWRdFaY-pw?usp=sharing")
                            ###########   The cursor is pointing at "Wall"   ################################
                            elif self.aboutGameMenu.cursor == 9:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                webbrowser.open(
                                    url="https://drive.google.com/drive/folders/164DmyjPfnDHMxZZhz7OBMTfZXXnF5m4L?usp=sharing")
                            ##   The cursor is pointing at "Tutorial create button in pygame (youtube)"   ###
                            elif self.aboutGameMenu.cursor == 10:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                webbrowser.open(
                                    url="https://www.youtube.com/watch?v=G8MYGDf_9ho")
                            ###########   The cursor is pointing at "Source code (if you want)"   ###########
                            elif self.aboutGameMenu.cursor == 11:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                self.aboutGameMenu.isHiddenPasswordBox = False
                                self.aboutGameMenu.passwordBox.cursor = 2
                            ###########   The cursor is poiting at "Back"   #################################
                            elif self.aboutGameMenu.cursor == 12:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                self.runningMainMenu = True
                                self.runningAboutGameMenu = False
                        elif not self.aboutGameMenu.isHiddenPasswordBox:
                            ###########   The cursor is pointing at "ENTER"   ###############################
                            if self.aboutGameMenu.passwordBox.cursor == 0:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                if self.aboutGameMenu.passwordBox.checkPassword():
                                    self.aboutGameMenu.update()
                                    self.aboutGameMenu.draw(self.screen)
                                    self.display()
                                    pygame.time.wait(1000)
                                    webbrowser.open(url="https://github.com/dangngocquan/SimpleSnakeGame")
                                    self.aboutGameMenu.passwordBox.resetDefaultDescription()
                                    self.aboutGameMenu.passwordBox.removeAllDigits()
                                    self.aboutGameMenu.isHiddenPasswordBox = True
                            ###########   The cursor is pointing at "CANCER"   ##############################
                            elif self.aboutGameMenu.passwordBox.cursor == 1:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                self.aboutGameMenu.passwordBox.resetDefaultDescription()
                                self.aboutGameMenu.passwordBox.removeAllDigits()
                                self.aboutGameMenu.isHiddenPasswordBox = True
                                self.aboutGameMenu.cursor = 13
                            self.aboutGameMenu.passwordBox.cursor = 2
                elif event.type == pygame.KEYDOWN:
                    if not self.aboutGameMenu.isHiddenPasswordBox:
                        ###########   Get password from keyboard   ##########################################
                        if event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                                           pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                            self.aboutGameMenu.passwordBox.addDigit(pygame.key.name(event.key))
                            self.aboutGameMenu.passwordBox.resetDefaultDescription()
                        elif event.key == pygame.K_BACKSPACE:
                            self.aboutGameMenu.passwordBox.removeDigit()
                            self.aboutGameMenu.passwordBox.resetDefaultDescription()
                            
            ###########   Get events when current screen is GAMEMODE SETTING MENU   #########################
            elif self.runningGamemodeSettingMenu:
                self.gamemodeSettingMenu.updatePositionMouse(pygame.mouse.get_pos())
                ##############   The cursor is pointing at "BACK"    ########################################
                if self.gamemodeSettingMenu.cursor == 8:
                    SETTING2['SOUND']['PRESS_BUTTON'].play()
                    self.runningGamemodeSettingMenu = False
                    self.runningOptionsMenu = True  
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.gamemodeSettingMenu.cursor = 9
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.gamemodeSettingMenu.updatePositionLeftMouse()
                    elif event.button == pygame.BUTTON_WHEELDOWN:
                        ########   Cursor is Option of NUMBER PLAYER   ######################################
                        if self.gamemodeSettingMenu.cursor == 1:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                setting.replaceData(key1='GAMEMODE', key2='NUMBER_PLAYERS', newData=2)
                            elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                setting.replaceData(key1='GAMEMODE', key2='NUMBER_PLAYERS', newData=1)
                        ############    Setting AUTO SPEED UP SNAKE   #######################################
                        elif self.gamemodeSettingMenu.cursor == 3:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            if SETTING1['GAMEMODE']['AUTO_SPEED_UP'] == "OFF":
                                setting.replaceData(key1='GAMEMODE', key2='AUTO_SPEED_UP', newData="ON")
                            elif SETTING1['GAMEMODE']['AUTO_SPEED_UP'] == "ON":
                                setting.replaceData(key1='GAMEMODE', key2='AUTO_SPEED_UP', newData="OFF")
                        ############  Setting TARGET SCORE   ################################################
                        elif self.gamemodeSettingMenu.cursor == 5:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            if SETTING1['GAMEMODE']['TARGET_SCORE'] > 100:
                                setting.replaceData(key1='GAMEMODE', key2='TARGET_SCORE', 
                                                    newData=SETTING1['GAMEMODE']['TARGET_SCORE']-100)
                        #############   Setting control view of player   ####################################
                        elif self.gamemodeSettingMenu.cursor == 7:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            if SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'First-person view':
                                setting.replaceData(
                                    key1='GAMEMODE', key2='VIEW_CONTROL', newData='Third-person view')
                            elif SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'Third-person view':
                                setting.replaceData(
                                    key1='GAMEMODE', key2='VIEW_CONTROL', newData='First-person view')
                    elif event.button == pygame.BUTTON_WHEELUP:
                        #############   Setting number of player   ##########################################
                        if self.gamemodeSettingMenu.cursor == 1:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                setting.replaceData(key1='GAMEMODE', key2='NUMBER_PLAYERS', newData=2)
                            elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                setting.replaceData(key1='GAMEMODE', key2='NUMBER_PLAYERS', newData=1)
                        ############   Setting gamemode AUTO SPEED UP SNAKE   ###############################
                        elif self.gamemodeSettingMenu.cursor == 3:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            if SETTING1['GAMEMODE']['AUTO_SPEED_UP'] == "OFF":
                                setting.replaceData(key1='GAMEMODE', key2='AUTO_SPEED_UP', newData="ON")
                            elif SETTING1['GAMEMODE']['AUTO_SPEED_UP'] == "ON":
                                setting.replaceData(key1='GAMEMODE', key2='AUTO_SPEED_UP', newData="OFF")
                        ############   Setting TARGET SCORE   ###############################################
                        elif self.gamemodeSettingMenu.cursor == 5:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            setting.replaceData(key1='GAMEMODE', key2='TARGET_SCORE', 
                                                    newData=SETTING1['GAMEMODE']['TARGET_SCORE']+100)
                        ############   Setting view control of player   #####################################
                        elif self.gamemodeSettingMenu.cursor == 7:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            if SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'First-person view':
                                setting.replaceData(key1='GAMEMODE', key2='VIEW_CONTROL', newData='Third-person view')
                            elif SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'Third-person view':
                                setting.replaceData(key1='GAMEMODE', key2='VIEW_CONTROL', newData='First-person view')       
                ###########   Save current setting to json file   ###########################################
                setting.saveSetting()
                    
            ###########   Get events when current screen is GAME SETTING MENU   #############################
            elif self.runningGameSettingMenu:
                self.gameSettingMenu.updatePositionMouse(pygame.mouse.get_pos())
                ###############   Cursor is "BACK"   ########################################################
                if self.gameSettingMenu.cursor == 12:
                    SETTING2['SOUND']['PRESS_BUTTON'].play()
                    self.runningGameSettingMenu = False
                    self.runningOptionsMenu = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.gameSettingMenu.cursor = 13
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.gameSettingMenu.updatePositionLeftMouse()
                    elif event.button == pygame.BUTTON_WHEELDOWN:
                        ###########   Setting GRID   ########################################################
                        if self.gameSettingMenu.cursor == 1:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            if SETTING1['GRID'] == 'ON':
                                setting.replaceData(key1='GRID', newData='OFF')
                            elif SETTING1['GRID'] == 'OFF':
                                setting.replaceData(key1='GRID', newData='ON')
                        #########   Setting MOVE SPEED OF SNAKE   ###########################################
                        elif self.gameSettingMenu.cursor == 3:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            setting.replaceData(key1='SNAKE', key2='MOVE_SPEED', 
                                            newData=(SETTING1['SNAKE']['MOVE_SPEED'] - 1)%61)
                            if SETTING1['SNAKE']['MOVE_SPEED'] == 0:
                                setting.replaceData(key1='SNAKE', key2='MOVE_SPEED', newData=60)
                            if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                self.inGame.snake.moveSpeed = SETTING1['SNAKE']['MOVE_SPEED']
                            elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                self.inGame02.snake01.moveSpeed = SETTING1['SNAKE']['MOVE_SPEED']
                                self.inGame02.snake02.moveSpeed = SETTING1['SNAKE']['MOVE_SPEED']
                        #############   Setting DROP SPEED OF SNAKE when gameover   #########################
                        elif self.gameSettingMenu.cursor == 5:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            setting.replaceData(key1='SNAKE', key2='DROP_SPEED', 
                                            newData=(SETTING1['SNAKE']['DROP_SPEED'] - 1)%61)
                            if SETTING1['SNAKE']['DROP_SPEED'] == 0:
                                setting.replaceData(key1='SNAKE', key2='DROP_SPEED', newData=60)
                            if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                self.inGame.snake.dropSpeed = SETTING1['SNAKE']['DROP_SPEED']
                            elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                self.inGame02.snake01.dropSpeed = SETTING1['SNAKE']['DROP_SPEED']
                                self.inGame02.snake02.dropSpeed = SETTING1['SNAKE']['DROP_SPEED']
                        #############   Setting ANIMATION SPEED OF SNAKE   ##################################
                        elif self.gameSettingMenu.cursor == 7:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            setting.replaceData(key1='SNAKE', key2='ANIMATION_SPEED', 
                                            newData=(SETTING1['SNAKE']['ANIMATION_SPEED'] - 1)%61)
                            if self.inGame.snake.animationSpeed == 0:
                                setting.replaceData(key1='SNAKE', key2='ANIMATION_SPEED', newData=60)
                            if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                self.inGame.snake.animationSpeed = SETTING1['SNAKE']['ANIMATION_SPEED']
                            elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                self.inGame02.snake01.animationSpeed = SETTING1['SNAKE']['ANIMATION_SPEED']
                                self.inGame02.snake02.animationSpeed = SETTING1['SNAKE']['ANIMATION_SPEED']
                        #############   Setting MAX FOOD   ##################################################
                        elif self.gameSettingMenu.cursor == 9:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                setting.replaceData(key1='FOOD', key2='MAX_FOOD', 
                                                newData=(SETTING1['FOOD']['MAX_FOOD'] - 1) % 105)
                                if SETTING1['FOOD']['MAX_FOOD'] == 0:
                                    setting.replaceData(key1='FOOD', key2='MAX_FOOD', newData=104)
                                if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                    self.inGame.foodManager.maxFood = SETTING1['FOOD']['MAX_FOOD']
                                elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                    self.inGame02.foodManager.maxFood = SETTING1['FOOD']['MAX_FOOD']
                        ##############   Setting ANIMATION SPEED OF FOOD   ##################################
                        elif self.gameSettingMenu.cursor == 11:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                setting.replaceData(key1='FOOD', key2='ANIMATION_SPEED', 
                                                newData=(SETTING1['FOOD']['ANIMATION_SPEED'] - 1)%61)
                                if self.inGame.foodManager.animationSpeed == 0:
                                    setting.replaceData(key1='FOOD', key2='ANIMATION_SPEED', newData=60 )
                                if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                    self.inGame.foodManager.animationSpeed = SETTING1['FOOD']['ANIMATION_SPEED']
                                elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                    self.inGame02.foodManager.animationSpeed = SETTING1['FOOD']['ANIMATION_SPEED'] 
                    elif event.button == pygame.BUTTON_WHEELUP:
                        ###############   Setting GRID   ####################################################
                        if self.gameSettingMenu.cursor == 1:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            if SETTING1['GRID'] == 'ON':
                                setting.replaceData(key1='GRID', newData='OFF')
                            elif SETTING1['GRID'] == 'OFF':
                                setting.replaceData(key1='GRID', newData='ON')
                        ##############   Setting MOVE SPEED OF SNAKE   ######################################
                        elif self.gameSettingMenu.cursor == 3:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            setting.replaceData(key1='SNAKE', key2='MOVE_SPEED', 
                                            newData=(SETTING1['SNAKE']['MOVE_SPEED'] + 1)%61)
                            if SETTING1['SNAKE']['MOVE_SPEED'] == 0:
                                setting.replaceData(key1='SNAKE', key2='MOVE_SPEED', newData=1)
                            if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                self.inGame.snake.moveSpeed = SETTING1['SNAKE']['MOVE_SPEED']
                            elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                self.inGame02.snake01.moveSpeed = SETTING1['SNAKE']['MOVE_SPEED']
                                self.inGame02.snake02.moveSpeed = SETTING1['SNAKE']['MOVE_SPEED']
                        ##############   Setting DROP SPEED OF SNAKE   ######################################
                        elif self.gameSettingMenu.cursor == 5:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            setting.replaceData(key1='SNAKE', key2='DROP_SPEED', 
                                            newData=(SETTING1['SNAKE']['DROP_SPEED'] + 1)%61)
                            if SETTING1['SNAKE']['DROP_SPEED'] == 0:
                                setting.replaceData(key1='SNAKE', key2='DROP_SPEED', newData=1)
                            if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                self.inGame.snake.dropSpeed = SETTING1['SNAKE']['DROP_SPEED']
                            elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                self.inGame02.snake01.dropSpeed = SETTING1['SNAKE']['DROP_SPEED']
                                self.inGame02.snake02.dropSpeed = SETTING1['SNAKE']['DROP_SPEED']
                        ##############   Setting ANIMATION SPEED OF SNAKE   #################################
                        elif self.gameSettingMenu.cursor == 7:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            setting.replaceData(key1='SNAKE', key2='ANIMATION_SPEED', 
                                            newData=(SETTING1['SNAKE']['ANIMATION_SPEED'] + 1)%61)
                            if self.inGame.snake.animationSpeed == 0:
                                setting.replaceData(key1='SNAKE', key2='ANIMATION_SPEED', newData=1)
                            if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                self.inGame.snake.animationSpeed = SETTING1['SNAKE']['ANIMATION_SPEED']
                            elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                self.inGame02.snake01.animationSpeed = SETTING1['SNAKE']['ANIMATION_SPEED']
                                self.inGame02.snake02.animationSpeed = SETTING1['SNAKE']['ANIMATION_SPEED']
                        ##############   Setting MAX FOOD   #################################################
                        elif self.gameSettingMenu.cursor == 9:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            setting.replaceData(key1='FOOD', key2='MAX_FOOD', 
                                            newData=(SETTING1['FOOD']['MAX_FOOD'] + 1) % 105)
                            if SETTING1['FOOD']['MAX_FOOD'] == 0:
                                setting.replaceData(key1='FOOD', key2='MAX_FOOD', newData=1)
                            if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                self.inGame.foodManager.maxFood = SETTING1['FOOD']['MAX_FOOD']
                            elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                self.inGame02.foodManager.maxFood = SETTING1['FOOD']['MAX_FOOD']
                        ###########   Setting ANIMATION SPEED OF FOOD   #####################################
                        elif self.gameSettingMenu.cursor == 11:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            setting.replaceData(key1='FOOD', key2='ANIMATION_SPEED', 
                                            newData=(SETTING1['FOOD']['ANIMATION_SPEED'] + 1)%61)
                            if self.inGame.foodManager.animationSpeed == 0:
                                setting.replaceData(key1='FOOD', key2='ANIMATION_SPEED', newData=1)
                            if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                self.inGame.foodManager.animationSpeed = SETTING1['FOOD']['ANIMATION_SPEED']
                            elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                self.inGame02.foodManager.animationSpeed = SETTING1['FOOD']['ANIMATION_SPEED']   
                ###########   Save current setting to json file   ###########################################
                setting.saveSetting()
            ###########   Get events when current screen is SOUND SETTING MENU   ############################
            elif self.runningSoundSettingMenu:
                self.soundSettingMenu.updatePositionMouse(pygame.mouse.get_pos())
                ############   Cursor is "BACK"   ###########################################################
                if self.soundSettingMenu.cursor == 6:
                    SETTING2['SOUND']['PRESS_BUTTON'].play()
                    self.runningSoundSettingMenu = False
                    self.runningOptionsMenu = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.soundSettingMenu.cursor = 7
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.soundSettingMenu.updatePositionLeftMouse()
                    elif event.button == pygame.BUTTON_WHEELDOWN:
                        ##########   Setting MUSIC   ########################################################
                        if self.soundSettingMenu.cursor == 1:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            pygame.mixer.music.unload()
                            setting.replaceData('SOUND', 'MUSIC_INDEX', 
                                                (SETTING1['SOUND']['MUSIC_INDEX'] - 1) % len(SETTING2['SOUND']['MUSIC']))
                            pygame.mixer.music.load(
                                SETTING2['SOUND']['MUSIC'][SETTING1['SOUND']['MUSIC_INDEX']])
                            pygame.mixer.music.play(-1)
                        ##########   Setting MUSIC VOLUME   #################################################
                        elif self.soundSettingMenu.cursor == 3:
                            if SETTING1['SOUND']['MUSIC_VOLUME'] > 0:
                                setting.replaceData('SOUND', 'MUSIC_VOLUME', 
                                                    (SETTING1['SOUND']['MUSIC_VOLUME'] - 1) % 101)
                                pygame.mixer.music.set_volume(SETTING1['SOUND']['MUSIC_VOLUME'] / 100)
                        ##########   Setting SOUND VOLUME   #################################################
                        elif self.soundSettingMenu.cursor == 5:
                            if SETTING1['SOUND']['SOUND_VOLUME'] > 0:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                setting.replaceData('SOUND', 'SOUND_VOLUME', 
                                                    (SETTING1['SOUND']['SOUND_VOLUME'] - 1) % 101)
                                setting.soundVolumeUpdate()
                    elif event.button == pygame.BUTTON_WHEELUP:
                        ############    Setting MUSIC   #####################################################
                        if self.soundSettingMenu.cursor == 1:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            pygame.mixer.music.unload()
                            setting.replaceData('SOUND', 'MUSIC_INDEX', 
                                                (SETTING1['SOUND']['MUSIC_INDEX'] + 1) % len(SETTING2['SOUND']['MUSIC']))
                            pygame.mixer.music.load(
                                SETTING2['SOUND']['MUSIC'][SETTING1['SOUND']['MUSIC_INDEX']])
                            pygame.mixer.music.play(-1)
                        ############   Setting MUSIC VOLUME   ###############################################
                        elif self.soundSettingMenu.cursor == 3:
                            if SETTING1['SOUND']['MUSIC_VOLUME'] < 100:
                                setting.replaceData('SOUND', 'MUSIC_VOLUME', 
                                                    (SETTING1['SOUND']['MUSIC_VOLUME'] + 1) % 101)
                                pygame.mixer.music.set_volume(SETTING1['SOUND']['MUSIC_VOLUME'] / 100)
                        ############   Setting SOUND VOLUME   ###############################################
                        elif self.soundSettingMenu.cursor == 5:
                            if SETTING1['SOUND']['SOUND_VOLUME'] < 100:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                setting.replaceData('SOUND', 'SOUND_VOLUME', 
                                                    (SETTING1['SOUND']['SOUND_VOLUME'] + 1) % 101)
                                setting.soundVolumeUpdate()
                ######################   Save setting to json file     ######################################
                setting.saveSetting()
            ###########   Get events when current screen is Map Setting Menu   ##############################             
            elif self.runningMapSettingMenu:
                self.mapSettingMenu.updatePositionMouse(pygame.mouse.get_pos())
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.mapSettingMenu.updatePositionLeftMouse()
                        #########   Cursor is "EXISTING MAP"   ##############################################
                        if self.mapSettingMenu.cursor == 0:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningExistingMapsMenu = True
                            self.runningMapSettingMenu = False
                        ###########   The cursor is pointing at "CREATE NEW MAP"   ##########################
                        elif self.mapSettingMenu.cursor == 1:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningMapSettingMenu = False
                            self.runningCreateNewMap = True
                            self.createNewMap.cursor = 2
                            self.createNewMap.showingInstruction = True
                        ###########   The cursor is poiting at "BACK"   #####################################
                        elif self.mapSettingMenu.cursor == 2:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.runningMapSettingMenu = False
                            self.runningOptionsMenu = True
                        
            ###########   Get events when current screen is Existing Maps Menu   ############################
            elif self.runningExistingMapsMenu:
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_DOWN, pygame.K_LEFT, pygame.K_a, pygame.K_s]:
                        if SETTING1['MAP']['INDEX_MAP'] > 0:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            setting.replaceData(key1='MAP', key2='INDEX_MAP',
                                                newData=SETTING1['MAP']['INDEX_MAP']-1)
                    elif event.key in [pygame.K_UP, pygame.K_RIGHT, pygame.K_d, pygame.K_w]:
                        if SETTING1['MAP']['INDEX_MAP'] < len(wall.LIST_MAP) - 1:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            setting.replaceData(key1='MAP', key2='INDEX_MAP',
                                                newData=SETTING1['MAP']['INDEX_MAP']+1)
                    elif event.key == pygame.K_RETURN:
                        SETTING2['SOUND']['PRESS_BUTTON'].play()
                        self.runningExistingMapsMenu = False
                        self.runningMapSettingMenu = True
                    elif event.key == pygame.K_k:
                        if SETTING1['MAP']['INDEX_MAP'] > 0:
                            setting.replaceData(key1='MAP', key2='INDEX_MAP',
                                                newData=SETTING1['MAP']['INDEX_MAP']-1)
                            wall.removeMapTFromListMaps(indexMap=(SETTING1['MAP']['INDEX_MAP']+1))
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_WHEELDOWN:
                        if SETTING1['MAP']['INDEX_MAP'] > 0:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            setting.replaceData(key1='MAP', key2='INDEX_MAP',
                                                newData=SETTING1['MAP']['INDEX_MAP']-1)
                    elif event.button == pygame.BUTTON_WHEELUP:
                        if SETTING1['MAP']['INDEX_MAP'] < len(wall.LIST_MAP) - 1:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            setting.replaceData(key1='MAP', key2='INDEX_MAP',
                                                newData=SETTING1['MAP']['INDEX_MAP']+1)
                setting.saveSetting()
            ###########   Get events when current screen is EXISTING MAP Menu   #############################
            elif self.runningCreateNewMap:
                self.createNewMap.updatePositionMouse(pygame.mouse.get_pos())
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.createNewMap.updatePositionLeftMouse()
                        if self.createNewMap.showingInstruction:
                            ###########   The cursor is pointing at "START"   ###############################
                            if self.createNewMap.cursor == 0:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                self.createNewMap.showingInstruction = False
                                self.createNewMap.drawingNewMap = True
                                self.createNewMap.wallManager = wall.loadPreviousWallManager(
                                    path='./data/creatingMap/creatingMap.json'
                                )
                            ###########   The cursor is poiting at "BACK"   ##################################
                            elif self.createNewMap.cursor == 1:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                self.createNewMap.showingInstruction = False
                                self.runningCreateNewMap = False
                                self.runningMapSettingMenu = True
                    elif event.button == pygame.BUTTON_RIGHT:
                        self.createNewMap.updatePositionRightMouse()
                elif event.type == pygame.KEYDOWN:
                    if self.createNewMap.drawingNewMap:
                        if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                                         pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                            keyString = pygame.key.name(event.key)
                            self.createNewMap.addNewRandomWallBlock(number=int(keyString))
                        elif event.key == pygame.K_d:
                            self.createNewMap.removeLastWallBlock()
                        elif event.key == pygame.K_c:
                            self.createNewMap.removeAllWallBlocks()
                        elif event.key == pygame.K_RETURN:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.createNewMap.saveMap()
                            self.createNewMap.drawingNewMap = False
                            self.createNewMap.showingInstruction = True
                            self.createNewMap.update()
                            self.createNewMap.removeAllWallBlocks()
                            wall.saveWallManager(self.createNewMap.wallManager,
                                                 path='./data/creatingMap/creatingMap.json')
                            self.runningCreateNewMap = False
                            self.runningMapSettingMenu = True
                        elif event.key == pygame.K_ESCAPE:
                            wall.saveWallManager(self.createNewMap.wallManager,
                                                 path='./data/creatingMap/creatingMap.json')
                            self.createNewMap.drawingNewMap = False
                            self.createNewMap.showingInstruction = True
                            self.createNewMap.update()
                            self.runningCreateNewMap = False
                            self.runningMapSettingMenu = True
                            
                           
            ###########   Get events when current screen is InGame (player controls snake)   ################
            elif self.runningInGame:
                ###########   Get events when current screen is Start InGame   ##############################
                if self.inGame.showingScreenStart:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.inGame.showingScreenStart = False
                            self.inGame.running = True
                        elif event.key == pygame.K_ESCAPE:
                            snake.saveSnake(self.inGame.snake)
                            food.saveFoodManager(self.inGame.foodManager)
                            wall.saveWallManager(self.inGame.wallManager)
                            self.inGame.showingScreenStart = False
                            self.runningInGame = False
                            self.runningMainMenu = True
                ###########   Get events when snake moving   ################################################
                elif self.inGame.running:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_k:
                            if self.inGame.snake.currentDirection == None:
                                SETTING2['SOUND']['GAME_OVER'].play()
                                #########   Update statistics of game   #####################################
                                STATISTICS['NUMBER_OF_MATCHES_PLAYED'] += 1
                                STATISTICS['NUMBER_OF_MATCHES_LOST'] += 1
                                if self.inGame.snake.score > STATISTICS['HIGHEST_SCORE']:
                                    STATISTICS['HIGHEST_SCORE'] = self.inGame.snake.score
                                    STATISTICS['PLAYER_HAS_HIGHEST_SCORE'] = (
                                        ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name)
                                menuStatistics.saveData()
                                #########   Update statistics of Account   ##################################
                                ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].loseMatch += 1
                                account.saveData(ACCOUNT_MANAGER.listAccount)
                                #########   Update history of game   ########################################
                                self.historyMenu.addNewHistory(
                                    name=ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name,
                                    time=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                    score=self.inGame.snake.score,
                                    result="LOSE",
                                    typeGame="SINGLE MATCH"
                                )
                                self.inGame.running = False
                                self.runningInGame = False
                                self.runningGameOverMenu = True
                                self.gameOverMenu = GameOverMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT, 
                                                                 snake=self.inGame.snake,
                                                                 wallManager=self.inGame.wallManager)
                        elif event.key == pygame.K_SPACE:
                            if self.inGame.snake.currentDirection != None:
                                self.inGame.snake.previousDirection = self.inGame.snake.currentDirection
                                self.inGame.snake.currentDirection = None
                            else:
                                self.inGame.snake.currentDirection = self.inGame.snake.previousDirection
                        elif event.key == pygame.K_ESCAPE:
                            if self.inGame.snake.currentDirection != None:
                                self.inGame.snake.previousDirection = self.inGame.snake.currentDirection
                                self.inGame.snake.currentDirection = None
                            else:
                                snake.saveSnake(self.inGame.snake)
                                food.saveFoodManager(self.inGame.foodManager)
                                wall.saveWallManager(self.inGame.wallManager)
                                self.inGame.running = False
                                self.runningInGame = False
                                self.runningMainMenu = True
                        elif event.key == pygame.K_UP or event.key == pygame.K_w:
                            if SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'Third-person view':
                                if self.inGame.snake.currentDirection != 'DD' and self.inGame.snake.checkSnakeCanMove('UU'):
                                    if self.inGame.snake.currentDirection != None:
                                        self.inGame.snake.currentDirection = 'UU'
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            if SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'Third-person view':
                                if self.inGame.snake.currentDirection != 'UU' and self.inGame.snake.checkSnakeCanMove('DD'):
                                    if self.inGame.snake.currentDirection != None:
                                        self.inGame.snake.currentDirection = 'DD'
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            if SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'Third-person view':
                                if self.inGame.snake.currentDirection != 'LL' and self.inGame.snake.checkSnakeCanMove('RR'):
                                    if self.inGame.snake.currentDirection != None:
                                        self.inGame.snake.currentDirection = 'RR'
                            elif SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'First-person view':
                                if self.inGame.snake.currentDirection == 'UU' and self.inGame.snake.checkSnakeCanMove('RR'):
                                    if self.inGame.snake.currentDirection != None:
                                        self.inGame.snake.currentDirection = 'RR'
                                elif self.inGame.snake.currentDirection == 'RR' and self.inGame.snake.checkSnakeCanMove('DD'):
                                    if self.inGame.snake.currentDirection != None:
                                        self.inGame.snake.currentDirection = 'DD'
                                elif self.inGame.snake.currentDirection == 'DD' and self.inGame.snake.checkSnakeCanMove('LL'):
                                    if self.inGame.snake.currentDirection != None:
                                        self.inGame.snake.currentDirection = 'LL'
                                elif self.inGame.snake.currentDirection == 'LL' and self.inGame.snake.checkSnakeCanMove('UU'):
                                    if self.inGame.snake.currentDirection != None:
                                        self.inGame.snake.currentDirection = 'UU'        
                        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            if SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'Third-person view':
                                if self.inGame.snake.currentDirection != 'RR' and self.inGame.snake.checkSnakeCanMove('LL'):
                                    if self.inGame.snake.currentDirection != None:
                                        self.inGame.snake.currentDirection = 'LL'
                            elif SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'First-person view':
                                if self.inGame.snake.currentDirection == 'UU' and self.inGame.snake.checkSnakeCanMove('LL'):
                                    if self.inGame.snake.currentDirection != None:
                                        self.inGame.snake.currentDirection = 'LL'
                                elif self.inGame.snake.currentDirection == 'LL' and self.inGame.snake.checkSnakeCanMove('DD'):
                                    if self.inGame.snake.currentDirection != None:
                                        self.inGame.snake.currentDirection = 'DD'
                                elif self.inGame.snake.currentDirection == 'DD' and self.inGame.snake.checkSnakeCanMove('RR'):
                                    if self.inGame.snake.currentDirection != None:
                                        self.inGame.snake.currentDirection = 'RR'
                                elif self.inGame.snake.currentDirection == 'RR' and self.inGame.snake.checkSnakeCanMove('UU'):
                                    if self.inGame.snake.currentDirection != None:
                                        self.inGame.snake.currentDirection = 'UU'
                ###########   Get events when game pause   ##################################################
                elif self.inGame.waiting:
                    pass
            
            ###########   Get events when current screen is InGame02 (2 player controls 2 snake)   ##########
            elif self.runningInGame02:
                ###########   Get events when current screen is Start InGame   ##############################
                if self.inGame02.showingScreenStart:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.inGame02.showingScreenStart = False
                            self.inGame02.running = True
                        elif event.key == pygame.K_ESCAPE:
                            snake.saveSnake(self.inGame02.snake01, path='./data/player/twoPlayer/snake/snake01.json')
                            snake.saveSnake(self.inGame02.snake02, path='./data/player/twoPlayer/snake/snake02.json')
                            food.saveFoodManager(self.inGame02.foodManager, path='./data/player/twoPlayer/food/food.json')
                            wall.saveWallManager(self.inGame02.wallManager,
                                                 path='./data/player/twoPlayer/wall/wall.json')
                            self.inGame02.showingScreenStart = False
                            self.runningInGame02 = False
                            self.runningMainMenu = True
                ###########   Get events when snake moving   ################################################
                elif self.inGame02.running:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_k:
                            if self.inGame02.snake01.currentDirection == None:
                                self.inGame02.running = False
                                self.runningInGame02 = False
                                self.runningGameOverMenu02 = True
                                #############   Update statistics of game    ################################
                                STATISTICS['NUMBER_OF_MATCHES_PLAYED'] += 1
                                if self.inGame02.snake01.score > STATISTICS['HIGHEST_SCORE']:
                                        STATISTICS['HIGHEST_SCORE'] = self.inGame02.snake01.score
                                        STATISTICS['PLAYER_HAS_HIGHEST_SCORE'] = (
                                            ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name)
                                menuStatistics.saveData()
                                if (len(self.inGame02.snake01.coordinateSnakeBlocks()) + 
                                    len(self.inGame02.snake02.coordinateSnakeBlocks())) > NUMBER_COLUMNS*NUMBER_ROWS//2:
                                    SETTING2['SOUND']['WIN_GAME']
                                    self.gameOverMenu02 = GameOverMenu02(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT, 
                                                                        snake01=self.inGame02.snake01, 
                                                                        snake02=self.inGame02.snake02, winner=3,
                                                                        wallManager=self.inGame02.wallManager)
                                    ##########      Update statistics of current account player   ###########
                                    ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].winMatch += 1
                                    account.saveData(ACCOUNT_MANAGER.listAccount)
                                    ##########   Update statistics of game   ################################
                                    STATISTICS['NUMBER_OF_MATCHES_WON'] += 1
                                    menuStatistics.saveData()    
                                    #########   Update history of game   ########################################
                                    self.historyMenu.addNewHistory(
                                        name=ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name,
                                        time=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                        score=self.inGame02.snake01.score,
                                        result="WIN",
                                        typeGame="SOLO MATCH"
                                    )
                                else:
                                    SETTING2['SOUND']['GAME_OVER'].play()
                                    self.gameOverMenu02 = GameOverMenu02(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT, 
                                                                    snake01=self.inGame02.snake01,
                                                                    snake02=self.inGame02.snake02, winner=0,
                                                                    wallManager=self.inGame02.wallManager)
                                    ############   Update statistics of current account player   ############
                                    ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].loseMatch += 1
                                    account.saveData(ACCOUNT_MANAGER.listAccount)
                                    ############   Update statistics of game    #############################
                                    STATISTICS['NUMBER_OF_MATCHES_LOST'] += 1
                                    menuStatistics.saveData()
                                    #########   Update history of game   ########################################
                                    self.historyMenu.addNewHistory(
                                        name=ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name,
                                        time=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                        score=self.inGame02.snake01.score,
                                        result="LOSE",
                                        typeGame="SOLO MATCH"
                                    )
                        elif event.key == pygame.K_SPACE:
                            if self.inGame02.snake01.currentDirection != None:
                                self.inGame02.snake01.previousDirection = self.inGame02.snake01.currentDirection
                                self.inGame02.snake01.currentDirection = None
                            else:
                                self.inGame02.snake01.currentDirection = self.inGame02.snake01.previousDirection
                            if self.inGame02.snake02.currentDirection != None:
                                self.inGame02.snake02.previousDirection = self.inGame02.snake02.currentDirection
                                self.inGame02.snake02.currentDirection = None
                            else:
                                self.inGame02.snake02.currentDirection = self.inGame02.snake02.previousDirection
                        elif event.key == pygame.K_ESCAPE:
                            if self.inGame02.snake01.currentDirection != None:
                                self.inGame02.snake01.previousDirection = self.inGame02.snake01.currentDirection
                                self.inGame02.snake01.currentDirection = None
                                self.inGame02.snake02.previousDirection = self.inGame02.snake02.currentDirection
                                self.inGame02.snake02.currentDirection = None
                            else:
                                snake.saveSnake(self.inGame02.snake01, path='./data/player/twoPlayer/snake/snake01.json')
                                snake.saveSnake(self.inGame02.snake02, path='./data/player/twoPlayer/snake/snake02.json')
                                food.saveFoodManager(self.inGame02.foodManager, path='./data/player/twoPlayer/food/food.json')
                                wall.saveWallManager(self.inGame02.wallManager,
                                                 path='./data/player/twoPlayer/wall/wall.json')
                                self.inGame02.running = False
                                self.runningInGame02 = False
                                self.runningMainMenu = True
                        elif event.key == pygame.K_w:
                            if SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'Third-person view':
                                if self.inGame02.snake01.currentDirection != 'DD' and self.inGame02.snake01.checkSnakeCanMove('UU'):
                                    if self.inGame02.snake01.currentDirection != None:
                                        self.inGame02.snake01.currentDirection = 'UU'
                        elif event.key == pygame.K_s:
                            if SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'Third-person view':
                                if self.inGame02.snake01.currentDirection != 'UU' and self.inGame02.snake01.checkSnakeCanMove('DD'):
                                    if self.inGame02.snake01.currentDirection != None:
                                        self.inGame02.snake01.currentDirection = 'DD'
                        elif event.key == pygame.K_d:
                            if SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'Third-person view':
                                if self.inGame02.snake01.currentDirection != 'LL' and self.inGame02.snake01.checkSnakeCanMove('RR'):
                                    if self.inGame02.snake01.currentDirection != None:
                                        self.inGame02.snake01.currentDirection = 'RR'
                            elif SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'First-person view':
                                if self.inGame02.snake01.currentDirection == 'UU' and self.inGame02.snake01.checkSnakeCanMove('RR'):
                                    if self.inGame02.snake01.currentDirection != None:
                                        self.inGame02.snake01.currentDirection = 'RR'
                                elif self.inGame02.snake01.currentDirection == 'RR' and self.inGame02.snake01.checkSnakeCanMove('DD'):
                                    if self.inGame02.snake01.currentDirection != None:
                                        self.inGame02.snake01.currentDirection = 'DD'
                                elif self.inGame02.snake01.currentDirection == 'DD' and self.inGame02.snake01.checkSnakeCanMove('LL'):
                                    if self.inGame02.snake01.currentDirection != None:
                                        self.inGame02.snake01.currentDirection = 'LL'
                                elif self.inGame02.snake01.currentDirection == 'LL' and self.inGame02.snake01.checkSnakeCanMove('UU'):
                                    if self.inGame02.snake01.currentDirection != None:
                                        self.inGame02.snake01.currentDirection = 'UU'
                        elif event.key == pygame.K_a:
                            if SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'Third-person view':
                                if self.inGame02.snake01.currentDirection != 'RR' and self.inGame02.snake01.checkSnakeCanMove('LL'):
                                    if self.inGame02.snake01.currentDirection != None:
                                        self.inGame02.snake01.currentDirection = 'LL'
                            elif SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'First-person view':
                                if self.inGame02.snake01.currentDirection == 'UU' and self.inGame02.snake01.checkSnakeCanMove('LL'):
                                    if self.inGame02.snake01.currentDirection != None:
                                        self.inGame02.snake01.currentDirection = 'LL'
                                elif self.inGame02.snake01.currentDirection == 'LL' and self.inGame02.snake01.checkSnakeCanMove('DD'):
                                    if self.inGame02.snake01.currentDirection != None:
                                        self.inGame02.snake01.currentDirection = 'DD'
                                elif self.inGame02.snake01.currentDirection == 'DD' and self.inGame02.snake01.checkSnakeCanMove('RR'):
                                    if self.inGame02.snake01.currentDirection != None:
                                        self.inGame02.snake01.currentDirection = 'RR'
                                elif self.inGame02.snake01.currentDirection == 'RR' and self.inGame02.snake01.checkSnakeCanMove('UU'):
                                    if self.inGame02.snake01.currentDirection != None:
                                        self.inGame02.snake01.currentDirection = 'UU'
                        elif event.key == pygame.K_UP:
                            if SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'Third-person view':
                                if self.inGame02.snake02.currentDirection != 'DD' and self.inGame02.snake02.checkSnakeCanMove('UU'):
                                    if self.inGame02.snake02.currentDirection != None:
                                        self.inGame02.snake02.currentDirection = 'UU'
                        elif event.key == pygame.K_DOWN:
                            if SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'Third-person view':
                                if self.inGame02.snake02.currentDirection != 'UU' and self.inGame02.snake02.checkSnakeCanMove('DD'):
                                    if self.inGame02.snake02.currentDirection != None:
                                        self.inGame02.snake02.currentDirection = 'DD'
                        elif event.key == pygame.K_RIGHT:
                            if SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'Third-person view':
                                if self.inGame02.snake02.currentDirection != 'LL' and self.inGame02.snake02.checkSnakeCanMove('RR'):
                                    if self.inGame02.snake02.currentDirection != None:
                                        self.inGame02.snake02.currentDirection = 'RR'
                            elif SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'First-person view':
                                if self.inGame02.snake02.currentDirection == 'UU' and self.inGame02.snake02.checkSnakeCanMove('RR'):
                                    if self.inGame02.snake02.currentDirection != None:
                                        self.inGame02.snake02.currentDirection = 'RR'
                                elif self.inGame02.snake02.currentDirection == 'RR' and self.inGame02.snake02.checkSnakeCanMove('DD'):
                                    if self.inGame02.snake02.currentDirection != None:
                                        self.inGame02.snake02.currentDirection = 'DD'
                                elif self.inGame02.snake02.currentDirection == 'DD' and self.inGame02.snake02.checkSnakeCanMove('LL'):
                                    if self.inGame02.snake02.currentDirection != None:
                                        self.inGame02.snake02.currentDirection = 'LL'
                                elif self.inGame02.snake02.currentDirection == 'LL' and self.inGame02.snake02.checkSnakeCanMove('UU'):
                                    if self.inGame02.snake02.currentDirection != None:
                                        self.inGame02.snake02.currentDirection = 'UU'
                        elif event.key == pygame.K_LEFT:
                            if SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'Third-person view':
                                if self.inGame02.snake02.currentDirection != 'RR' and self.inGame02.snake02.checkSnakeCanMove('LL'):
                                    if self.inGame02.snake02.currentDirection != None:
                                        self.inGame02.snake02.currentDirection = 'LL'
                            elif SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'First-person view':
                                if self.inGame02.snake02.currentDirection == 'UU' and self.inGame02.snake02.checkSnakeCanMove('LL'):
                                    if self.inGame02.snake02.currentDirection != None:
                                        self.inGame02.snake02.currentDirection = 'LL'
                                elif self.inGame02.snake02.currentDirection == 'LL' and self.inGame02.snake02.checkSnakeCanMove('DD'):
                                    if self.inGame02.snake02.currentDirection != None:
                                        self.inGame02.snake02.currentDirection = 'DD'
                                elif self.inGame02.snake02.currentDirection == 'DD' and self.inGame02.snake02.checkSnakeCanMove('RR'):
                                    if self.inGame02.snake02.currentDirection != None:
                                        self.inGame02.snake02.currentDirection = 'RR'
                                elif self.inGame02.snake02.currentDirection == 'RR' and self.inGame02.snake02.checkSnakeCanMove('UU'):
                                    if self.inGame02.snake02.currentDirection != None:
                                        self.inGame02.snake02.currentDirection = 'UU'
                ###########   Get events when game pause   ##################################################
                elif self.inGame02.waiting:
                    pass
            
            ###########   Get event when current screen is Game Over Menu   #################################
            elif self.runningGameOverMenu:
                self.gameOverMenu.updatePositionMouse(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3,
                                     pygame.K_4, pygame.K_5, pygame.K_6]:
                        self.gameOverMenu.updateDropType(pygame.key.name(event.key))
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.gameOverMenu.updatePositionLeftMouse()
                        if self.gameOverMenu.cursor < 2:
                            if self.gameOverMenu.cursor == 0:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                self.runningInGame = True
                                self.inGame.showingScreenStart = True
                            elif self.gameOverMenu.cursor == 1:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                self.runningMainMenu = True
                            self.inGame.snake = Snake()
                            self.inGame.foodManager.removeAllFoods()
                            self.inGame.wallManager = wall.loadWallManagerFromListMaps(
                                indexMap=SETTING1['MAP']['INDEX_MAP']
                            )
                            self.inGame.update()
                            wall.saveWallManager(self.inGame.wallManager)
                            snake.saveSnake(self.inGame.snake)
                            food.saveFoodManager(self.inGame.foodManager)
                            self.inGame.update()
                            self.runningGameOverMenu = False
            
            ###########   Get event when current screen is Game Over Menu 02   ##############################
            elif self.runningGameOverMenu02:
                self.gameOverMenu02.updatePositionMouse(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3,
                                     pygame.K_4, pygame.K_5, pygame.K_6]:
                        self.gameOverMenu02.updateDropType(pygame.key.name(event.key))
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.gameOverMenu02.updatePositionLeftMouse()
                        if self.gameOverMenu02.cursor < 2:
                            if self.gameOverMenu02.cursor == 0:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                self.runningInGame02 = True
                                self.inGame02.showingScreenStart = True
                            elif self.gameOverMenu02.cursor == 1:
                                SETTING2['SOUND']['PRESS_BUTTON'].play()
                                self.runningMainMenu = True
                            self.inGame02.snake01 = Snake(typeLocation=-1, typeColor='blue')
                            self.inGame02.snake02 = Snake(typeLocation=1, typeColor='green')
                            self.inGame02.foodManager.removeAllFoods()
                            self.inGame02.wallManager = wall.loadWallManagerFromListMaps(
                                indexMap=SETTING1['MAP']['INDEX_MAP']
                            )
                            wall.saveWallManager(self.inGame02.wallManager,
                                            path='./data/player/twoPlayer/wall/wall.json')                           
                            snake.saveSnake(self.inGame02.snake01, path='./data/player/twoPlayer/snake/snake01.json')
                            snake.saveSnake(self.inGame02.snake02, path='./data/player/twoPlayer/snake/snake02.json')
                            food.saveFoodManager(self.inGame02.foodManager, path='./data/player/twoPlayer/food/food.json')
                            self.inGame02.update()
                            self.runningGameOverMenu02 = False
                        
                                  
    ###########   Update screen with current status   #######################################################       
    def update(self):
        ###########   Update screen Main Menu   #############################################################
        if self.runningMainMenu:
            if self.countTicks % (FPS * self.divisibility // self.mainMenu.FPS) == 0:
                self.mainMenu.update()
        ###########   Update screen Play Game Menu   ########################################################
        elif self.runningPlayGameMenu:
            if self.countTicks % (FPS * self.divisibility // self.playGameMenu.FPS) == 0:
                self.playGameMenu.update()
        ###########   Update screen when player controlling snake   #########################################
        elif self.runningInGame:
            ###########   Check game over   #################################################################
            snakeDied = self.inGame.snake.died(wallCoordinates=self.inGame.wallManager.coordinateWalls())
            targetScoreReached = self.inGame.snake.score >= SETTING1['GAMEMODE']['TARGET_SCORE']
            if (snakeDied or targetScoreReached):
                #################   Update statistics of game   #############################################
                STATISTICS['NUMBER_OF_MATCHES_PLAYED'] += 1
                if self.inGame.snake.score > STATISTICS['HIGHEST_SCORE']:
                    STATISTICS['HIGHEST_SCORE'] = self.inGame.snake.score
                    STATISTICS['PLAYER_HAS_HIGHEST_SCORE'] = (
                        ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name)
                menuStatistics.saveData()
                if snakeDied:
                    SETTING2['SOUND']['GAME_OVER'].play()
                    #############   Update statistics of game   #############################################
                    STATISTICS['NUMBER_OF_MATCHES_LOST'] += 1
                    menuStatistics.saveData()
                    #############   Update statistis of current account player   ############################
                    ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].loseMatch += 1
                    account.saveData(ACCOUNT_MANAGER.listAccount)
                    #########   Update history of game   ########################################
                    self.historyMenu.addNewHistory(
                        name=ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name,
                        time=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                        score=self.inGame.snake.score,
                        result="LOSE",
                        typeGame="SINGLE MATCH"
                    )
                elif targetScoreReached:
                    SETTING2['SOUND']['WIN_GAME'].play()
                    #################   Update statistics of game   #########################################
                    STATISTICS['NUMBER_OF_MATCHES_WON'] += 1
                    menuStatistics.saveData()
                    ##################   Update statistics of account player   ##############################
                    ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].winMatch += 1
                    account.saveData(ACCOUNT_MANAGER.listAccount)
                    #########   Update history of game   ####################################################
                    self.historyMenu.addNewHistory(
                        name=ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name,
                        time=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                        score=self.inGame.snake.score,
                        result="WIN",
                        typeGame="SINGLE MATCH"
                    )
                self.inGame.running = False
                self.runningInGame = False
                self.runningGameOverMenu = True
                self.gameOverMenu = GameOverMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT, 
                                                 snake=self.inGame.snake, wallManager=self.inGame.wallManager)
                
            ###########   Update screen when showing screen start in Ingame   ###############################
            if self.inGame.showingScreenStart:
                if self.countTicks % (FPS * self.divisibility // self.inGame.snake.animationSpeed) == 0:
                    self.inGame.update(type='UpdateSnakeAnimation')
                if self.countTicks % (FPS * self.divisibility // self.inGame.foodManager.animationSpeed) == 0:
                    self.inGame.update(type='UpdateFoodAnimation')
                if self.countTicks % (FPS * self.divisibility // self.mainMenu.FPS) == 0:
                    self.inGame.update()
            ###########   Update screen when player is playing   ############################################
            elif self.inGame.running:
                if self.countTicks % (FPS * self.divisibility // self.inGame.snake.animationSpeed) == 0:
                    self.inGame.update(type='UpdateSnakeAnimation')
                if self.countTicks % (FPS * self.divisibility // self.inGame.foodManager.animationSpeed) == 0:
                    self.inGame.update(type='UpdateFoodAnimation')
                if self.countTicks % (FPS * self.divisibility // self.inGame.snake.moveSpeed) == 0:
                    self.inGame.update(tempCountTicks=self.countTicks, divisibility=self.divisibility)
            ###########   Update screen when pause game   ###################################################
            elif self.inGame.waiting:
                pass
        ###########   Update screen when 2 player controlling 2 snake   #####################################
        elif self.runningInGame02:
            ###########   Check game over   #################################################################
            snake01Died = self.inGame02.snake01.died(otherCoordinateSnakeBlocks=self.inGame02.snake02.coordinateSnakeBlocks(),
                                                     wallCoordinates=self.inGame02.wallManager.coordinateWalls())
            snake02Died = self.inGame02.snake02.died(otherCoordinateSnakeBlocks=self.inGame02.snake01.coordinateSnakeBlocks(),
                                                     wallCoordinates=self.inGame02.wallManager.coordinateWalls())
            score1 = self.inGame02.snake01.score
            score2 = self.inGame02.snake02.score
            targetScoreReached01 = score1 >= SETTING1['GAMEMODE']['TARGET_SCORE']
            targetScoreReached02 = score2 >= SETTING1['GAMEMODE']['TARGET_SCORE']
            winner = -1
            if (snake01Died or snake02Died or targetScoreReached01 or targetScoreReached02):
                ###############    Update statistics of game   ##############################################
                STATISTICS['NUMBER_OF_MATCHES_PLAYED'] += 1
                if score1 > STATISTICS['HIGHEST_SCORE']:
                                        STATISTICS['HIGHEST_SCORE'] = score1
                                        STATISTICS['PLAYER_HAS_HIGHEST_SCORE'] = (
                                            ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name)
                menuStatistics.saveData()
                
                ###########   Who win?   ####################################################################
                if snake01Died or snake02Died:
                    SETTING2['SOUND']['GAME_OVER'].play()
                    if snake01Died and snake02Died:
                        if score1 > score2:
                            winner = 1
                        elif score1 == score2:
                            winner = 0
                        elif score1 < score2:
                            winner = 2
                    elif snake02Died:
                        winner = 1
                    elif snake01Died:
                        winner = 2
                elif targetScoreReached01 or targetScoreReached02:
                    SETTING2['SOUND']['WIN_GAME'].play()
                    if targetScoreReached01 and targetScoreReached02:
                        winner = 3
                    elif targetScoreReached01:
                        winner = 1
                    elif targetScoreReached02:
                        winner = 2
                
                if winner == 1 or winner == 3:
                    ###########    Update statistics of game   ##########################################
                    STATISTICS['NUMBER_OF_MATCHES_WON'] += 1
                    menuStatistics.saveData()
                    ############    Update statistics of current account player   #######################
                    ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].winMatch += 1
                    account.saveData(ACCOUNT_MANAGER.listAccount)
                    #########   Update history of game   ################################################
                    self.historyMenu.addNewHistory(
                        name=ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name,
                        time=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                        score=self.inGame02.snake01.score,
                        result="WIN",
                        typeGame="SOLO MATCH"
                    )
                elif winner == 0 or winner == 2:
                    ###########     Update statistics of game   #########################################
                    STATISTICS['NUMBER_OF_MATCHES_LOST'] += 1
                    menuStatistics.saveData()
                    ###########    Update statistics of account player   ################################
                    ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].loseMatch += 1
                    account.saveData(ACCOUNT_MANAGER.listAccount)
                    #########   Update history of game   ################################################
                    self.historyMenu.addNewHistory(
                        name=ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name,
                        time=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                        score=self.inGame02.snake01.score,
                        result="LOSE",
                        typeGame="SOLO MATCH"
                    )
                    
                self.inGame02.running = False
                self.runningInGame02 = False
                self.runningGameOverMenu02 = True
                self.gameOverMenu02 = GameOverMenu02(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT, 
                                                     snake01=self.inGame02.snake01, snake02=self.inGame02.snake02,
                                                     wallManager=self.inGame02.wallManager, winner=winner)
                
            ###########   Update screen when showing screen start in Ingame02   #############################
            if self.inGame02.showingScreenStart:
                if self.countTicks % (FPS * self.divisibility // self.inGame02.snake01.animationSpeed) == 0:
                    self.inGame02.update(type='UpdateSnakeAnimation')
                if self.countTicks % (FPS * self.divisibility // self.inGame02.foodManager.animationSpeed) == 0:
                    self.inGame02.update(type='UpdateFoodAnimation')
                if self.countTicks % (FPS * self.divisibility // self.mainMenu.FPS) == 0:
                    self.inGame02.update()
            ###########   Update screen when player is playing   ############################################
            elif self.inGame02.running:
                if self.countTicks % (FPS * self.divisibility // self.inGame02.snake01.animationSpeed) == 0:
                    self.inGame02.update(type='UpdateSnakeAnimation')
                if self.countTicks % (FPS * self.divisibility // self.inGame02.foodManager.animationSpeed) == 0:
                    self.inGame02.update(type='UpdateFoodAnimation')
                if self.countTicks % (FPS * self.divisibility // self.inGame02.snake01.moveSpeed) == 0:
                    self.inGame02.update(tempCountTicks=self.countTicks, snakeMove02=False, 
                                         divisibility=self.divisibility)
                if self.countTicks % (FPS * self.divisibility // self.inGame02.snake02.moveSpeed) == 0:
                    self.inGame02.update(tempCountTicks=self.countTicks, snakeMove01=False, 
                                         divisibility=self.divisibility)
            ###########   Update screen when pause game   ###################################################
            elif self.inGame02.waiting:
                pass
        ###########   Update screen when Game Over   ########################################################
        elif self.runningGameOverMenu:
            if self.gameOverMenu.dropType in ['2', '4', '5']:
                if self.countTicks % (FPS * self.divisibility // (self.inGame.snake.dropSpeed*10)) == 0:
                    self.gameOverMenu.update(type='UpdateSnakeDrop')
            if self.gameOverMenu.dropType in ['6']:
                if self.countTicks % (FPS * self.divisibility // (self.inGame.snake.dropSpeed*4)) == 0:
                    self.gameOverMenu.update(type='UpdateSnakeDrop')
            else:
                if self.countTicks % (FPS * self.divisibility // (self.inGame.snake.dropSpeed)) == 0:
                    self.gameOverMenu.update(type='UpdateSnakeDrop')
            if self.countTicks % (FPS * self.divisibility // self.inGame.snake.animationSpeed) == 0:
                self.gameOverMenu.update(type='UpdateSnakeAnimation')
            if self.countTicks % (FPS * self.divisibility // self.gameOverMenu.FPS) == 0:
                self.gameOverMenu.update()
        ###########   Update screen when Game Over 2 player   ###############################################
        elif self.runningGameOverMenu02:
            if self.gameOverMenu02.dropType in ['2', '4', '5']:
                if self.countTicks % (FPS * self.divisibility // (self.inGame02.snake01.dropSpeed*10)) == 0:
                    self.gameOverMenu02.update(type='UpdateSnakeDrop')
            if self.gameOverMenu02.dropType in ['6']:
                if self.countTicks % (FPS * self.divisibility // (self.inGame02.snake01.dropSpeed*4)) == 0:
                    self.gameOverMenu02.update(type='UpdateSnakeDrop')
            else:
                if self.countTicks % (FPS * self.divisibility // (self.inGame02.snake01.dropSpeed)) == 0:
                    self.gameOverMenu02.update(type='UpdateSnakeDrop')
            if self.countTicks % (FPS * self.divisibility // self.inGame02.snake01.animationSpeed) == 0:
                self.gameOverMenu02.update(type='UpdateSnakeAnimation')
            if self.countTicks % (FPS * self.divisibility // self.gameOverMenu02.FPS) == 0:
                self.gameOverMenu02.update()       
        ###########   Update screen when showing Accounts Setting Menu   ####################################
        elif self.runningAccountsSetting:
            if self.countTicks % (FPS * self.divisibility // self.accountsSetting.FPS) == 0:
                self.accountsSetting.update() 
        ###########   Update screen when showing Existing Account Menu   ####################################
        elif self.runningExistingAccountMenu:
            if self.countTicks % (FPS * self.divisibility // self.existingAccountMenu.FPS) == 0:
                self.existingAccountMenu.update()
        ###########   Update screen when showing Create New Account Menu   ####################################
        elif self.runningCreateNewAccountMenu:
            if self.countTicks % (FPS * self.divisibility // self.createNewAccountMenu.FPS) == 0:
                self.createNewAccountMenu.update() 
        ###########   Update screen when showing Options Menu   #############################################
        elif self.runningOptionsMenu:
            if self.countTicks % (FPS * self.divisibility // self.optionsMenu.FPS) == 0:
                self.optionsMenu.update()
        ###########   Update screen when showing Gamemode Setting Menu   ####################################
        elif self.runningGamemodeSettingMenu:
            if self.countTicks % (FPS * self.divisibility // self.gamemodeSettingMenu.FPS) == 0:
                self.gamemodeSettingMenu.update()
        ###########   Update screen when showing Game Setting Menu   ########################################
        elif self.runningGameSettingMenu:
            if self.countTicks % (FPS * self.divisibility // self.gameSettingMenu.FPS) == 0:
                self.gameSettingMenu.update()
        ###########   Update screen when showing Sound Setting Menu   #######################################
        elif self.runningSoundSettingMenu:
            if self.countTicks % (FPS * self.divisibility // self.soundSettingMenu.FPS) == 0:
                self.soundSettingMenu.update()
        ###########   Update screen when showing Map Setting Menu   #########################################
        elif self.runningMapSettingMenu:
            if self.countTicks % (FPS * self.divisibility // self.mapSettingMenu.FPS) == 0:
                self.mapSettingMenu.update()
        ###########   Update screen when showing Existing Maps Menu   #########################################
        elif self.runningExistingMapsMenu:
            if self.countTicks % (FPS * self.divisibility // self.existingMapsMenu.FPS) == 0:
                self.existingMapsMenu.update()
        ###########   Update screen when showing CreatNewMap   #########################################
        elif self.runningCreateNewMap:
            if self.countTicks % (FPS * self.divisibility // self.createNewMap.FPS) == 0:
                self.createNewMap.update()
        ###########   Update screen Statistics Menu   #######################################################
        elif self.runningStatisticsMenu:
            if self.countTicks % (FPS * self.divisibility // self.statisticsMenu.FPS) == 0:
                self.statisticsMenu.update()
        ###########   Update screen History Menu   #######################################################
        elif self.runningHistoryMenu:
            if self.countTicks % (FPS * self.divisibility // self.historyMenu.FPS) == 0:
                self.historyMenu.update()
        ###########   Update screen About Game Menu   #######################################################
        elif self.runningAboutGameMenu:
            if self.countTicks % (FPS * self.divisibility // self.aboutGameMenu.FPS) == 0:
                self.aboutGameMenu.update()
        
        
        
        
    ###########   Draw screen with current status and show it   #############################################
    def display(self):
        ###########   Clear old images   ####################################################################
        self.screen.fill(BLACK)
        ###########   Draw new images   #####################################################################
        if self.runningInGame:
            self.inGame.draw(self.screen)
        if self.runningInGame02:
            self.inGame02.draw(self.screen)
        elif self.runningMainMenu:
            self.mainMenu.draw(self.screen)
        elif self.runningPlayGameMenu:
            self.playGameMenu.draw(self.screen)
        elif self.runningGameOverMenu:
            self.gameOverMenu.draw(self.screen)
        elif self.runningGameOverMenu02:
            self.gameOverMenu02.draw(self.screen)
        elif self.runningAccountsSetting:
            self.accountsSetting.draw(self.screen)
        elif self.runningExistingAccountMenu:
            self.existingAccountMenu.draw(self.screen)
        elif self.runningCreateNewAccountMenu:
            self.createNewAccountMenu.draw(self.screen)
        elif self.runningOptionsMenu:
            self.optionsMenu.draw(self.screen)
        elif self.runningGamemodeSettingMenu:
            self.gamemodeSettingMenu.draw(self.screen)
        elif self.runningGameSettingMenu:
            self.gameSettingMenu.draw(self.screen)
        elif self.runningSoundSettingMenu:
            self.soundSettingMenu.draw(self.screen)
        elif self.runningMapSettingMenu:
            self.mapSettingMenu.draw(self.screen)
        elif self.runningExistingMapsMenu:
            self.existingMapsMenu.draw(self.screen)
        elif self.runningCreateNewMap:
            self.createNewMap.draw(self.screen)
        elif self.runningStatisticsMenu:
            self.statisticsMenu.draw(self.screen)
        elif self.runningHistoryMenu:
            self.historyMenu.draw(self.screen)
        elif self.runningAboutGameMenu:
            self.aboutGameMenu.draw(self.screen)
        pygame.display.flip()