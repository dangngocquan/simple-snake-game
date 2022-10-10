import sys
import pygame
from food import NUMBER_COLUMNS, NUMBER_ROWS, FoodManager
import food
from menuMain import MainMenu
from menuPlayGame import PlayGameMenu
from menuOptions import OptionsMenu
from menuGamemodeSetting import GamemodeSettingMenu
from menuInGameSetting import GameSettingMenu
from menuSoundSetting import SoundSettingMenu
from menuMapSetting import MapSettingMenu
from menuExistingMaps import ExistingMapsMenu
from menuCreateNewMap import CreateNewMap
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
        ###########   Status in game   ######################################################################
        self.running = True
        self.runningMainMenu = True
        self.runningPlayGameMenu = False
        self.runningInGame = False
        self.runningInGame02 = False
        self.runningOptionsMenu = False
        self.runningGamemodeSettingMenu = False
        self.runningGameSettingMenu = False
        self.runningSoundSettingMenu = False
        self.runningMapSettingMenu = False
        self.runningExistingMapsMenu = False
        self.runningCreateNewMap = False
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
        self.optionsMenu = OptionsMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.gamemodeSettingMenu = GamemodeSettingMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.gameSettingMenu = GameSettingMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.soundSettingMenu = SoundSettingMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.mapSettingMenu = MapSettingMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.existingMapsMenu = ExistingMapsMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.createNewMap = CreateNewMap(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
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
            ###########   Get events when current screen is Main Menu   #####################################
            if self.runningMainMenu:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        SETTING2['SOUND']['CHANGE_BUTTON'].play()
                        self.mainMenu.cursor += 1
                        self.mainMenu.cursor %= 4
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        SETTING2['SOUND']['CHANGE_BUTTON'].play()
                        self.mainMenu.cursor -= 1
                        self.mainMenu.cursor %= 4
                    elif event.key == pygame.K_RETURN:
                        SETTING2['SOUND']['PRESS_BUTTON'].play()
                        self.runningMainMenu = False
                        if self.mainMenu.cursor == 0:
                            self.runningPlayGameMenu = True
                            self.playGameMenu.cursor = 0
                        elif self.mainMenu.cursor == 1:
                            self.runningOptionsMenu = True
                            self.optionsMenu.cursor = 0
                        elif self.mainMenu.cursor == 2:
                            self.runningAboutGameMenu = True
                            self.aboutGameMenu.cursor = 0
                        elif self.mainMenu.cursor == 3:
                            self.running = False
                            pygame.time.wait(500)
                            pygame.quit()
                            sys.exit()            
            ###########   Get events when current screen is Play Game Menu  #################################
            elif self.runningPlayGameMenu:
                if event.type == pygame.KEYDOWN:
                    ###########   Move the cursor   #########################################################
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        SETTING2['SOUND']['CHANGE_BUTTON'].play()
                        self.playGameMenu.cursor += 1
                        self.playGameMenu.cursor %= 3
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        SETTING2['SOUND']['CHANGE_BUTTON'].play()
                        self.playGameMenu.cursor -= 1
                        self.playGameMenu.cursor %= 3
                    ###########   Select the content that the cursor is pointing at   #######################
                    if event.key == pygame.K_RETURN:
                        SETTING2['SOUND']['PRESS_BUTTON'].play()
                        ###########   The cursor is pointing at "New Game"   ################################
                        if self.playGameMenu.cursor == 0:
                            if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                self.runningInGame = True
                                self.inGame.snake = Snake()
                                self.inGame.foodManager.removeAllFoods()
                                self.inGame.wallManager = wall.loadWallManagerFromListMaps(
                                    indexMap=SETTING1['MAP']['INDEX_MAP'])
                                self.inGame.showingScreenStart = True
                            elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                self.runningInGame02 = True
                                self.inGame02.snake01 = Snake(typeLocation=-1, typeColor='blue')
                                self.inGame02.snake02 = Snake(typeLocation=1, typeColor='green')
                                self.inGame02.foodManager.removeAllFoods()
                                self.inGame02.wallManager = wall.loadWallManagerFromListMaps(
                                    indexMap=SETTING1['MAP']['INDEX_MAP'])
                                self.inGame02.showingScreenStart = True
                        ###########   The cursor is pointing at "Continue Game"   ###########################
                        elif self.playGameMenu.cursor == 1:
                            if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                self.runningInGame = True
                                self.inGame.snake = snake.loadPreviousSnake()
                                self.inGame.foodManager = food.loadPreviousFoodManager()
                                self.inGame.wallManager = wall.loadPreviousWallManager()
                                self.inGame.showingScreenStart = True
                            elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                self.runningInGame02 = True
                                self.inGame02.snake01 = snake.loadPreviousSnake(path='./data/player/twoPlayer/snake/snake01.json')
                                self.inGame02.snake02 = snake.loadPreviousSnake(path='./data/player/twoPlayer/snake/snake02.json')
                                self.inGame02.foodManager = food.loadPreviousFoodManager(path='./data/player/twoPlayer/food/food.json')
                                self.inGame02.wallManager = wall.loadPreviousWallManager(path='./data/player/twoPlayer/wall/wall.json')
                                self.inGame02.showingScreenStart = True
                        ###########   The cursor is poiting at "Back"   #####################################
                        elif self.playGameMenu.cursor == 2:
                            self.runningMainMenu = True
                            self.mainMenu.cursor = 0
                        self.runningPlayGameMenu = False
            ###########   Get events when current screen is Options Menu  ###################################        
            elif self.runningOptionsMenu:
                if event.type == pygame.KEYDOWN:
                    ###########   Move the cursor   #########################################################
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        SETTING2['SOUND']['CHANGE_BUTTON'].play()
                        self.optionsMenu.cursor += 1
                        self.optionsMenu.cursor %= 5
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        SETTING2['SOUND']['CHANGE_BUTTON'].play()
                        self.optionsMenu.cursor -= 1
                        self.optionsMenu.cursor %= 5
                    ###########   Select the content that the cursor is pointing at   #######################
                    if event.key == pygame.K_RETURN:
                        SETTING2['SOUND']['PRESS_BUTTON'].play()
                        ###########   The cursor is pointing at "Gamemode setting"   ########################
                        if self.optionsMenu.cursor == 0:
                            self.runningGamemodeSettingMenu = True
                            self.gamemodeSettingMenu.cursor = 0
                        ###########   The cursor is pointing at "Game setting"   ############################
                        if self.optionsMenu.cursor == 1:
                            self.runningGameSettingMenu = True
                            self.gameSettingMenu.cursor = 0
                        ###########   The cursor is pointing at "Sound setting"   ###########################
                        elif self.optionsMenu.cursor == 2:
                            self.runningSoundSettingMenu = True
                        ###########   The cursor is pointing at "Map setting"   ###########################
                        elif self.optionsMenu.cursor == 3:
                            self.runningMapSettingMenu = True
                            self.mapSettingMenu.cursor = 0
                        ###########   The cursor is poiting at "Back"   #####################################
                        elif self.optionsMenu.cursor == 4:
                            self.runningMainMenu = True
                        self.runningOptionsMenu = False
            ###########   Get events when current screen is Options Menu  ###################################        
            elif self.runningAboutGameMenu:
                pass
            ###########   Get events when current screen is Gamemode Setting Menu   #########################
            elif self.runningGamemodeSettingMenu:
                if event.type == pygame.KEYDOWN:
                    ###########   Move the cursor   #########################################################
                    if self.gamemodeSettingMenu.cursor % 2 == 0:
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            if self.gamemodeSettingMenu.cursor == 8:
                                self.gamemodeSettingMenu.cursor += 1
                            else:
                                self.gamemodeSettingMenu.cursor += 2
                            self.gamemodeSettingMenu.cursor %= 9
                        elif event.key == pygame.K_UP or event.key == pygame.K_w:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            if self.gamemodeSettingMenu.cursor == 0:
                                self.gamemodeSettingMenu.cursor -= 1
                            else:
                                self.gamemodeSettingMenu.cursor -= 2
                            self.gamemodeSettingMenu.cursor %= 9
                        elif event.key == pygame.K_RETURN:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            if self.gamemodeSettingMenu.cursor == 8:
                                self.runningGamemodeSettingMenu = False
                                self.runningOptionsMenu = True
                            else:
                                self.gamemodeSettingMenu.cursor += 1
                    elif self.gamemodeSettingMenu.cursor % 2 != 0:
                        if self.gamemodeSettingMenu.cursor == 1:
                            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                    setting.replaceData(key1='GAMEMODE', key2='NUMBER_PLAYERS', newData=2)
                                elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                    setting.replaceData(key1='GAMEMODE', key2='NUMBER_PLAYERS', newData=1)
                            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                    setting.replaceData(key1='GAMEMODE', key2='NUMBER_PLAYERS', newData=2)
                                elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                    setting.replaceData(key1='GAMEMODE', key2='NUMBER_PLAYERS', newData=1)
                        elif self.gamemodeSettingMenu.cursor == 3:
                            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                if SETTING1['GAMEMODE']['AUTO_SPEED_UP'] == "OFF":
                                    setting.replaceData(key1='GAMEMODE', key2='AUTO_SPEED_UP', newData="ON")
                                elif SETTING1['GAMEMODE']['AUTO_SPEED_UP'] == "ON":
                                    setting.replaceData(key1='GAMEMODE', key2='AUTO_SPEED_UP', newData="OFF")
                            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                if SETTING1['GAMEMODE']['AUTO_SPEED_UP'] == "OFF":
                                    setting.replaceData(key1='GAMEMODE', key2='AUTO_SPEED_UP', newData="ON")
                                elif SETTING1['GAMEMODE']['AUTO_SPEED_UP'] == "ON":
                                    setting.replaceData(key1='GAMEMODE', key2='AUTO_SPEED_UP', newData="OFF")
                        elif self.gamemodeSettingMenu.cursor == 5:
                            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                if SETTING1['GAMEMODE']['TARGET_SCORE'] > 100:
                                    setting.replaceData(key1='GAMEMODE', key2='TARGET_SCORE', 
                                                        newData=SETTING1['GAMEMODE']['TARGET_SCORE']-100)
                            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                setting.replaceData(key1='GAMEMODE', key2='TARGET_SCORE', 
                                                        newData=SETTING1['GAMEMODE']['TARGET_SCORE']+100)
                        elif self.gamemodeSettingMenu.cursor == 7:
                            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                if SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'First-person view':
                                    setting.replaceData(key1='GAMEMODE', key2='VIEW_CONTROL', newData='Third-person view')
                                elif SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'Third-person view':
                                    setting.replaceData(key1='GAMEMODE', key2='VIEW_CONTROL', newData='First-person view')
                            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                if SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'First-person view':
                                    setting.replaceData(key1='GAMEMODE', key2='VIEW_CONTROL', newData='Third-person view')
                                elif SETTING1['GAMEMODE']['VIEW_CONTROL'] == 'Third-person view':
                                    setting.replaceData(key1='GAMEMODE', key2='VIEW_CONTROL', newData='First-person view')
                        if event.key  == pygame.K_RETURN:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.gamemodeSettingMenu.cursor -= 1
                ###########   Save current setting to json file   ###########################################
                setting.saveSetting()
                    
            ###########   Get events when current screen is Game Setting Menu   #############################
            elif self.runningGameSettingMenu:
                if event.type == pygame.KEYDOWN:
                    ###########   Move the cursor   #########################################################
                    ###########   If the cursor is pointing at "Show grid", "Move speed", "Drop speed",   ###
                    ###########   "Animation speed", "Max food"  ############################################
                    if self.gameSettingMenu.cursor % 2 == 0:
                        ###########   Move the cursor   #####################################################
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            if self.gameSettingMenu.cursor == 12:
                                self.gameSettingMenu.cursor += 1
                            else:
                                self.gameSettingMenu.cursor += 2
                            self.gameSettingMenu.cursor %= 13
                        elif event.key == pygame.K_UP or event.key == pygame.K_w:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            if self.gameSettingMenu.cursor == 0:
                                self.gameSettingMenu.cursor -= 1
                            else:
                                self.gameSettingMenu.cursor -= 2
                            self.gameSettingMenu.cursor %= 13
                        ###########   Select the content that cursor poiting at   ###########################
                        elif event.key == pygame.K_RETURN:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            if self.gameSettingMenu.cursor == 12:
                                self.runningGameSettingMenu = False
                                self.runningOptionsMenu = True
                            else:
                                self.gameSettingMenu.cursor += 1
                    ###########   If the cursor is not pointing at main content ("Show grid", "Move speed", #
                    ###########   "Drop speed", "Animation speed", "Max food")   ############################
                    elif self.gameSettingMenu.cursor % 2 != 0:
                        ###########   The cursor is poiting at sub options of "Show grid"   #################
                        if self.gameSettingMenu.cursor == 1:
                            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_DOWN, pygame.K_s, 
                                             pygame.K_a, pygame.K_d, pygame.K_RIGHT, pygame.K_LEFT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                if SETTING1['GRID'] == 'ON':
                                    setting.replaceData(key1='GRID', newData='OFF')
                                elif SETTING1['GRID'] == 'OFF':
                                    setting.replaceData(key1='GRID', newData='ON')
                        ###   The cursor is pointing at sub options of "Move speed" (of "Snake Setting")   ##
                        elif self.gameSettingMenu.cursor == 3:
                            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_d, pygame.K_RIGHT]:
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
                            elif event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_a, pygame.K_LEFT]:
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
                        ###   The cursor is pointing at sub options of "Drop speed" (of "Snake setting")   ###
                        elif self.gameSettingMenu.cursor == 5:
                            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_d, pygame.K_RIGHT]:
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
                            elif event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_a, pygame.K_LEFT]:
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
                        ### The cursor is pointing at sub options of "Animation speed" (of "Snake setting") #
                        elif self.gameSettingMenu.cursor == 7:
                            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_d, pygame.K_RIGHT]:
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
                            elif event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_a, pygame.K_LEFT]:
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
                        ###   The cursor is pointing at sub options of "Max food" (of "Food setting")   #####
                        elif self.gameSettingMenu.cursor == 9:
                            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_d, pygame.K_RIGHT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                setting.replaceData(key1='FOOD', key2='MAX_FOOD', 
                                                newData=(SETTING1['FOOD']['MAX_FOOD'] + 1) % 105)
                                
                                if SETTING1['FOOD']['MAX_FOOD'] == 0:
                                    setting.replaceData(key1='FOOD', key2='MAX_FOOD', newData=1)
                                if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                    self.inGame.foodManager.maxFood = SETTING1['FOOD']['MAX_FOOD']
                                elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                    self.inGame02.foodManager.maxFood = SETTING1['FOOD']['MAX_FOOD']
                            elif event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_a, pygame.K_LEFT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                setting.replaceData(key1='FOOD', key2='MAX_FOOD', 
                                                newData=(SETTING1['FOOD']['MAX_FOOD'] - 1) % 105)
                                
                                if SETTING1['FOOD']['MAX_FOOD'] == 0:
                                    setting.replaceData(key1='FOOD', key2='MAX_FOOD', newData=104)
                                if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                    self.inGame.foodManager.maxFood = SETTING1['FOOD']['MAX_FOOD']
                                elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                    self.inGame02.foodManager.maxFood = SETTING1['FOOD']['MAX_FOOD']
                        ### The cursor is pointing at sub options of "Animation food" (of "Food setting") ###
                        elif self.gameSettingMenu.cursor == 11:
                            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_d, pygame.K_RIGHT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                setting.replaceData(key1='FOOD', key2='ANIMATION_SPEED', 
                                                newData=(SETTING1['FOOD']['ANIMATION_SPEED'] + 1)%61)
                                if self.inGame.foodManager.animationSpeed == 0:
                                    setting.replaceData(key1='FOOD', key2='ANIMATION_SPEED', newData=1)
                                if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                    self.inGame.foodManager.animationSpeed = SETTING1['FOOD']['ANIMATION_SPEED']
                                elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                    self.inGame02.foodManager.animationSpeed = SETTING1['FOOD']['ANIMATION_SPEED']   
                            elif event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_a, pygame.K_LEFT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                setting.replaceData(key1='FOOD', key2='ANIMATION_SPEED', 
                                                newData=(SETTING1['FOOD']['ANIMATION_SPEED'] - 1)%61)
                                if self.inGame.foodManager.animationSpeed == 0:
                                    setting.replaceData(key1='FOOD', key2='ANIMATION_SPEED', newData=60 )
                                if SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 1:
                                    self.inGame.foodManager.animationSpeed = SETTING1['FOOD']['ANIMATION_SPEED']
                                elif SETTING1['GAMEMODE']['NUMBER_PLAYERS'] == 2:
                                    self.inGame02.foodManager.animationSpeed = SETTING1['FOOD']['ANIMATION_SPEED'] 
                        ###   Return to the main options if player press ENTER   ############################
                        if event.key == pygame.K_RETURN:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.gameSettingMenu.cursor -= 1
                ###########   Save current setting to json file   ###########################################
                setting.saveSetting()
            ###########   Get events when current screen is Sound Setting Menu   ############################
            elif self.runningSoundSettingMenu:
                if event.type == pygame.KEYDOWN:
                    if self.soundSettingMenu.cursor % 2 == 0:
                        if event.key in [pygame.K_s, pygame.K_DOWN]:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            if self.soundSettingMenu.cursor == 6:
                                self.soundSettingMenu.cursor = 0
                            else:
                                self.soundSettingMenu.cursor += 2
                            self.soundSettingMenu.cursor %= 7 
                        elif event.key in [pygame.K_w, pygame.K_UP]:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            if self.soundSettingMenu.cursor == 0:
                                self.soundSettingMenu.cursor = 6
                            else:
                                self.soundSettingMenu.cursor -= 2
                            self.soundSettingMenu.cursor %= 7
                        elif event.key == pygame.K_RETURN:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            if self.soundSettingMenu.cursor == 6:
                                self.runningSoundSettingMenu = False
                                self.runningOptionsMenu = True
                            else:
                                self.soundSettingMenu.cursor += 1
                    elif self.soundSettingMenu.cursor % 2 != 0:
                        if self.soundSettingMenu.cursor == 1:
                            if event.key in [pygame.K_w, pygame.K_UP, pygame.K_d, pygame.K_RIGHT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                pygame.mixer.music.unload()
                                setting.replaceData('SOUND', 'MUSIC_INDEX', 
                                                    (SETTING1['SOUND']['MUSIC_INDEX'] + 1) % len(SETTING2['SOUND']['MUSIC']))
                                pygame.mixer.music.load(
                                    SETTING2['SOUND']['MUSIC'][SETTING1['SOUND']['MUSIC_INDEX']])
                                pygame.mixer.music.play(-1)
                            elif event.key in [pygame.K_s, pygame.K_DOWN, pygame.K_a, pygame.K_LEFT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                pygame.mixer.music.unload()
                                setting.replaceData('SOUND', 'MUSIC_INDEX', 
                                                    (SETTING1['SOUND']['MUSIC_INDEX'] - 1) % len(SETTING2['SOUND']['MUSIC']))
                                pygame.mixer.music.load(
                                    SETTING2['SOUND']['MUSIC'][SETTING1['SOUND']['MUSIC_INDEX']])
                                pygame.mixer.music.play(-1)
                        elif self.soundSettingMenu.cursor == 3:
                            if event.key in [pygame.K_w, pygame.K_UP, pygame.K_d, pygame.K_RIGHT]:
                                setting.replaceData('SOUND', 'MUSIC_VOLUME', 
                                                    (SETTING1['SOUND']['MUSIC_VOLUME'] + 1) % 101)
                                pygame.mixer.music.set_volume(SETTING1['SOUND']['MUSIC_VOLUME'] / 100)
                            elif event.key in [pygame.K_s, pygame.K_DOWN, pygame.K_a, pygame.K_LEFT]:
                                setting.replaceData('SOUND', 'MUSIC_VOLUME', 
                                                    (SETTING1['SOUND']['MUSIC_VOLUME'] - 1) % 101)
                                pygame.mixer.music.set_volume(SETTING1['SOUND']['MUSIC_VOLUME'] / 100)
                        elif self.soundSettingMenu.cursor == 5:
                            if event.key in [pygame.K_w, pygame.K_UP, pygame.K_d, pygame.K_RIGHT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                setting.replaceData('SOUND', 'SOUND_VOLUME', 
                                                    (SETTING1['SOUND']['SOUND_VOLUME'] + 1) % 101)
                                setting.soundVolumeUpdate()
                            elif event.key in [pygame.K_s, pygame.K_DOWN, pygame.K_a, pygame.K_LEFT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                setting.replaceData('SOUND', 'SOUND_VOLUME', 
                                                    (SETTING1['SOUND']['SOUND_VOLUME'] - 1) % 101)
                                setting.soundVolumeUpdate()
                        if event.key == pygame.K_RETURN:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            setting.soundVolumeUpdate()
                            self.soundSettingMenu.cursor -= 1
                setting.saveSetting()
            ###########   Get events when current screen is Map Setting Menu   ##############################             
            elif self.runningMapSettingMenu:
                if event.type == pygame.KEYDOWN:
                    ###########   Move the cursor   #########################################################
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        SETTING2['SOUND']['CHANGE_BUTTON'].play()
                        self.mapSettingMenu.cursor += 1
                        self.mapSettingMenu.cursor %= 3
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        SETTING2['SOUND']['CHANGE_BUTTON'].play()
                        self.mapSettingMenu.cursor -= 1
                        self.mapSettingMenu.cursor %= 3
                    ###########   Select the content that the cursor is pointing at   #######################
                    if event.key == pygame.K_RETURN:
                        SETTING2['SOUND']['PRESS_BUTTON'].play()
                        ###########   The cursor is pointing at "Existing maps"   ###########################
                        if self.mapSettingMenu.cursor == 0:
                            self.runningExistingMapsMenu = True
                        ###########   The cursor is pointing at "Create new map"   ##########################
                        elif self.mapSettingMenu.cursor == 1:
                            self.runningCreateNewMap = True
                            self.createNewMap.cursor = 0
                            self.createNewMap.showingInstruction = True
                        ###########   The cursor is poiting at "Back"   #####################################
                        elif self.mapSettingMenu.cursor == 2:
                            self.runningOptionsMenu = True
                        self.runningMapSettingMenu = False
                        
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
                            
                setting.saveSetting()
            ###########   Get events when current screen is Existing Maps Menu   ############################
            elif self.runningCreateNewMap:
                if self.createNewMap.showingInstruction:
                    if event.type == pygame.KEYDOWN:
                        if event.key in [pygame.K_DOWN, pygame.K_LEFT, pygame.K_a, pygame.K_s]:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            self.createNewMap.cursor -= 1
                            self.createNewMap.cursor %= 2
                        elif event.key in [pygame.K_UP, pygame.K_RIGHT, pygame.K_d, pygame.K_w]:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            self.createNewMap.cursor += 1
                            self.createNewMap.cursor %= 2
                        if event.key == pygame.K_RETURN:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            ###########   The cursor is pointing at "START"   ###########################
                            if self.createNewMap.cursor == 0:
                                self.createNewMap.showingInstruction = False
                                self.createNewMap.drawingNewMap = True
                                self.createNewMap.wallManager = wall.loadPreviousWallManager(
                                    path='./data/creatingMap/creatingMap.json'
                                )
                            ###########   The cursor is poiting at "BACK"   #####################################
                            elif self.createNewMap.cursor == 1:
                                self.createNewMap.showingInstruction = False
                                self.runningCreateNewMap = False
                                self.runningMapSettingMenu = True
                elif self.createNewMap.drawingNewMap:
                    if event.type == pygame.MOUSEMOTION:
                        self.createNewMap.mouseMotionPosition = pygame.mouse.get_pos()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            self.createNewMap.mouseLeftClickPosition = pygame.mouse.get_pos()
                        elif event.button == 3:
                            self.createNewMap.mouseRightClickPosition = pygame.mouse.get_pos()
                    elif event.type == pygame.KEYDOWN:
                        if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5,
                                         pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                            keyString = pygame.key.name(event.key)
                            self.createNewMap.addNewRandomWallBlock(number=int(keyString))
                        elif event.key == pygame.K_d:
                            self.createNewMap.removeLastWallBlock()
                        elif event.key == pygame.K_c:
                            self.createNewMap.removeAllWallBlocks()
                        elif event.key == pygame.K_RETURN:
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
                                SETTING2['SOUND']['GAME_OVER'].play()
                                self.inGame02.running = False
                                self.runningInGame02 = False
                                self.runningGameOverMenu02 = True
                                self.gameOverMenu02 = GameOverMenu02(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT, 
                                                                 snake01=self.inGame02.snake01,
                                                                 snake02=self.inGame02.snake02, winner=0,
                                                                 wallManager=self.inGame02.wallManager)
                                if (len(self.inGame02.snake01.coordinateSnakeBlocks()) + 
                                    len(self.inGame02.snake02.coordinateSnakeBlocks())) > NUMBER_COLUMNS*NUMBER_ROWS//2:
                                    self.gameOverMenu02 = GameOverMenu02(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT, 
                                                                        snake01=self.inGame02.snake01, 
                                                                        snake02=self.inGame02.snake02, winner=3,
                                                                        wallManager=self.inGame02.wallManager)
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
                 if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        SETTING2['SOUND']['CHANGE_BUTTON'].play()
                        self.gameOverMenu.cursor += 1
                        self.gameOverMenu.cursor %= 2
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        SETTING2['SOUND']['CHANGE_BUTTON'].play()
                        self.gameOverMenu.cursor -= 1
                        self.gameOverMenu.cursor %= 2
                    elif event.key == pygame.K_RETURN:
                        SETTING2['SOUND']['PRESS_BUTTON'].play()
                        if self.gameOverMenu.cursor == 0:
                            self.runningInGame = True
                            self.inGame.showingScreenStart = True
                        elif self.gameOverMenu.cursor == 1:
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
                 if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        SETTING2['SOUND']['CHANGE_BUTTON'].play()
                        self.gameOverMenu02.cursor += 1
                        self.gameOverMenu02.cursor %= 2
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        SETTING2['SOUND']['CHANGE_BUTTON'].play()
                        self.gameOverMenu02.cursor -= 1
                        self.gameOverMenu02.cursor %= 2
                    elif event.key == pygame.K_RETURN:
                        SETTING2['SOUND']['PRESS_BUTTON'].play()
                        if self.gameOverMenu02.cursor == 0:
                            self.runningInGame02 = True
                            self.inGame02.showingScreenStart = True
                        elif self.gameOverMenu02.cursor == 1:
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
                if snakeDied:
                    SETTING2['SOUND']['GAME_OVER'].play()
                elif targetScoreReached:
                    SETTING2['SOUND']['WIN_GAME'].play()
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
            targetScoreReached01 = self.inGame02.snake01.score >= SETTING1['GAMEMODE']['TARGET_SCORE']
            targetScoreReached02 = self.inGame02.snake02.score >= SETTING1['GAMEMODE']['TARGET_SCORE']
            if (snake01Died or snake02Died or targetScoreReached01 or targetScoreReached02):
                if snake01Died or snake02Died:
                    SETTING2['SOUND']['GAME_OVER'].play()
                elif targetScoreReached01 or targetScoreReached02:
                    SETTING2['SOUND']['WIN_GAME'].play()
                self.inGame02.running = False
                self.runningInGame02 = False
                self.runningGameOverMenu02 = True
                self.gameOverMenu02 = GameOverMenu02(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT, 
                                                     snake01=self.inGame02.snake01, snake02=self.inGame02.snake02,
                                                     wallManager=self.inGame02.wallManager)
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
            if self.countTicks % (FPS * self.divisibility // self.inGame.snake.dropSpeed) == 0:
                self.gameOverMenu.update(type='UpdateSnakeDrop')
            if self.countTicks % (FPS * self.divisibility // self.inGame.snake.animationSpeed) == 0:
                self.gameOverMenu.update(type='UpdateSnakeAnimation')
            if self.countTicks % (FPS * self.divisibility // self.gameOverMenu.FPS) == 0:
                self.gameOverMenu.update()
        ###########   Update screen when Game Over 2 player   ###############################################
        elif self.runningGameOverMenu02:
            if self.countTicks % (FPS * self.divisibility // self.inGame02.snake01.dropSpeed) == 0:
                self.gameOverMenu02.update(type='UpdateSnakeDrop')
            if self.countTicks % (FPS * self.divisibility // self.inGame02.snake01.animationSpeed) == 0:
                self.gameOverMenu02.update(type='UpdateSnakeAnimation')
            if self.countTicks % (FPS * self.divisibility // self.gameOverMenu02.FPS) == 0:
                self.gameOverMenu02.update()        
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
        elif self.runningAboutGameMenu:
            self.aboutGameMenu.draw(self.screen)
        pygame.display.flip()