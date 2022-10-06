import sys
import pygame
from food import FoodManager
import food
from menu import MainMenu, PlayGameMenu, GameOverMenu, OptionsMenu
from menu import GameSettingMenu, SoundSettingMenu, GamemodeSettingMenu
from inGame import InGame, InGame02
from snake import Snake
import snake
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
        self.numberPlayers = SETTING1['GAMEMODE']['NUMBER_PLAYERS']
        self.viewControl = SETTING1['GAMEMODE']['VIEW_CONTROL']
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
        self.runningGameOverMenu = False
        ###########   Screens in game   #####################################################################
        self.mainMenu = MainMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.playGameMenu = PlayGameMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.inGame = InGame()
        self.inGame02 = InGame02()
        self.gameOverMenu = GameOverMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT, self.inGame.snake)
        self.optionsMenu = OptionsMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.gamemodeSettingMenu = GamemodeSettingMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.gameSettingMenu = GameSettingMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
        self.soundSettingMenu = SoundSettingMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT)
    
    ###########   Main loop in game   #######################################################################
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.getEvents()
            for i in range(1000):
                self.countTicks = (self.countTicks + 1) % (FPS * 1000)
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
                    food.saveFoodManager(foodManager=self.inGame.foodManager, numberPlayers=self.numberPlayers)
                elif self.runningGameOverMenu:
                    snake.saveSnake(Snake())
                    food.saveFoodManager(FoodManager())
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
                        self.mainMenu.cursor %= 3
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        SETTING2['SOUND']['CHANGE_BUTTON'].play()
                        self.mainMenu.cursor -= 1
                        self.mainMenu.cursor %= 3
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
                            self.running = False
                            pygame.time.wait(1000)
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
                            self.runningInGame = True
                            self.inGame.snake = Snake()
                            self.inGame.foodManager = FoodManager()
                            self.inGame.showingScreenStart = True
                        ###########   The cursor is pointing at "Continue Game"   ###########################
                        elif self.playGameMenu.cursor == 1:
                            self.runningInGame = True
                            self.inGame.snake = snake.loadPreviousSnake()
                            self.inGame.foodManager = food.loadPreviousFoodManager(self.numberPlayers)
                            self.inGame.showingScreenStart = True
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
                        self.optionsMenu.cursor %= 4
                    elif event.key == pygame.K_UP or event.key == pygame.K_w:
                        SETTING2['SOUND']['CHANGE_BUTTON'].play()
                        self.optionsMenu.cursor -= 1
                        self.optionsMenu.cursor %= 4
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
                        ###########   The cursor is poiting at "Back"   #####################################
                        elif self.optionsMenu.cursor == 3:
                            self.runningMainMenu = True
                        self.runningOptionsMenu = False
            ###########   Get events when current screen is Gamemode Setting Menu   #########################
            elif self.runningGamemodeSettingMenu:
                if event.type == pygame.KEYDOWN:
                    ###########   Move the cursor   #########################################################
                    if self.gamemodeSettingMenu.cursor % 2 == 0:
                        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            if self.gamemodeSettingMenu.cursor == 4:
                                self.gamemodeSettingMenu.cursor += 1
                            else:
                                self.gamemodeSettingMenu.cursor += 2
                            self.gamemodeSettingMenu.cursor %= 5
                        elif event.key == pygame.K_UP or event.key == pygame.K_w:
                            SETTING2['SOUND']['CHANGE_BUTTON'].play()
                            if self.gamemodeSettingMenu.cursor == 0:
                                self.gamemodeSettingMenu.cursor -= 1
                            else:
                                self.gamemodeSettingMenu.cursor -= 2
                            self.gamemodeSettingMenu.cursor %= 5
                        elif event.key == pygame.K_RETURN:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            if self.gamemodeSettingMenu.cursor == 4:
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
                                self.inGame.snake.moveSpeed = SETTING1['SNAKE']['MOVE_SPEED'] + 1
                                self.inGame.snake.moveSpeed %= 61
                                if self.inGame.snake.moveSpeed == 0:
                                    self.inGame.snake.moveSpeed = 1
                            elif event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_a, pygame.K_LEFT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                self.inGame.snake.moveSpeed = SETTING1['SNAKE']['MOVE_SPEED'] - 1
                                self.inGame.snake.moveSpeed %= 61
                                if self.inGame.snake.moveSpeed == 0:
                                    self.inGame.snake.moveSpeed = 60
                            setting.replaceData(key1='SNAKE', key2='MOVE_SPEED', 
                                                newData=self.inGame.snake.moveSpeed)
                        ###   The cursor is pointing at sub options of "Drop speed" (of "Snake setting")   ###
                        elif self.gameSettingMenu.cursor == 5:
                            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_d, pygame.K_RIGHT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                self.inGame.snake.dropSpeed = SETTING1['SNAKE']['DROP_SPEED'] + 1
                                self.inGame.snake.dropSpeed %= 61
                                if self.inGame.snake.dropSpeed == 0:
                                    self.inGame.snake.dropSpeed = 1
                            elif event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_a, pygame.K_LEFT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                self.inGame.snake.dropSpeed = SETTING1['SNAKE']['DROP_SPEED'] - 1
                                self.inGame.snake.dropSpeed %= 61
                                if self.inGame.snake.dropSpeed == 0:
                                    self.inGame.snake.dropSpeed = 60
                            setting.replaceData(key1='SNAKE', key2='DROP_SPEED', 
                                                newData=self.inGame.snake.dropSpeed)
                        ### The cursor is pointing at sub options of "Animation speed" (of "Snake setting") #
                        elif self.gameSettingMenu.cursor == 7:
                            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_d, pygame.K_RIGHT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                self.inGame.snake.animationSpeed = SETTING1['SNAKE']['ANIMATION_SPEED'] + 1
                                self.inGame.snake.animationSpeed %= 61
                                if self.inGame.snake.animationSpeed == 0:
                                    self.inGame.snake.animationSpeed = 1
                            elif event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_a, pygame.K_LEFT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                self.inGame.snake.animationSpeed = SETTING1['SNAKE']['ANIMATION_SPEED'] - 1
                                self.inGame.snake.animationSpeed %= 61
                                if self.inGame.snake.animationSpeed == 0:
                                    self.inGame.snake.animationSpeed = 60
                            setting.replaceData(key1='SNAKE', key2='ANIMATION_SPEED', 
                                                newData=self.inGame.snake.animationSpeed)
                        ###   The cursor is pointing at sub options of "Max food" (of "Food setting")   #####
                        elif self.gameSettingMenu.cursor == 9:
                            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_d, pygame.K_RIGHT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                self.inGame.foodManager.maxFood = SETTING1['FOOD']['MAX_FOOD'] + 1
                                self.inGame.foodManager.maxFood %= 105
                                if self.inGame.foodManager.maxFood == 0:
                                    self.inGame.foodManager.maxFood = 1
                            elif event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_a, pygame.K_LEFT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                self.inGame.foodManager.maxFood = SETTING1['FOOD']['MAX_FOOD'] - 1
                                self.inGame.foodManager.maxFood %= 105
                                if self.inGame.foodManager.maxFood == 0:
                                    self.inGame.foodManager.maxFood = 104
                            setting.replaceData(key1='FOOD', key2='MAX_FOOD', 
                                                newData=self.inGame.foodManager.maxFood)
                        ### The cursor is pointing at sub options of "Animation food" (of "Food setting") ###
                        elif self.gameSettingMenu.cursor == 11:
                            if event.key in [pygame.K_UP, pygame.K_w, pygame.K_d, pygame.K_RIGHT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                self.inGame.foodManager.animationSpeed = SETTING1['FOOD']['ANIMATION_SPEED'] + 1
                                self.inGame.foodManager.animationSpeed %= 61
                                if self.inGame.foodManager.animationSpeed == 0:
                                    self.inGame.foodManager.animationSpeed = 1
                            elif event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_a, pygame.K_LEFT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                self.inGame.foodManager.animationSpeed = SETTING1['FOOD']['ANIMATION_SPEED'] - 1
                                self.inGame.foodManager.animationSpeed %= 61
                                if self.inGame.foodManager.animationSpeed == 0:
                                    self.inGame.foodManager.animationSpeed = 60
                            setting.replaceData(key1='FOOD', key2='ANIMATION_SPEED', 
                                                newData=self.inGame.foodManager.animationSpeed)
                        ###   Return to the main options if player press ENTER   ############################
                        if event.key == pygame.K_RETURN:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            self.gameSettingMenu.cursor -= 1
                ###########   Save current setting to json file   ###########################################
                setting.saveSetting('./data/setting/setting.json')
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
                                # self.optionsMenu.cursor = 0
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
                            elif event.key in [pygame.K_s, pygame.K_DOWN, pygame.K_a, pygame.K_LEFT]:
                                SETTING2['SOUND']['CHANGE_BUTTON'].play()
                                setting.replaceData('SOUND', 'SOUND_VOLUME', 
                                                    (SETTING1['SOUND']['SOUND_VOLUME'] - 1) % 101)
                        if event.key == pygame.K_RETURN:
                            SETTING2['SOUND']['PRESS_BUTTON'].play()
                            setting.soundVolumeUpdate()
                            self.soundSettingMenu.cursor -= 1
                setting.saveSetting()
                            
                                
            ###########   Get events when current screen is InGame (player controls snake)   ################
            elif self.runningInGame:
                ###########   Get events when current screen is Start InGame   ##############################
                if self.inGame.showingScreenStart:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.inGame.showingScreenStart = False
                            self.inGame.running = True
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
                                                                 self.inGame.snake)
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
                                self.inGame.running = False
                                self.runningInGame = False
                                self.runningMainMenu = True
                        elif event.key == pygame.K_UP or event.key == pygame.K_w:
                            if self.inGame.snake.currentDirection != 'DD' and self.inGame.snake.checkSnakeCanMove('UU'):
                                if self.inGame.snake.currentDirection != None:
                                    self.inGame.snake.currentDirection = 'UU'
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            if self.inGame.snake.currentDirection != 'UU' and self.inGame.snake.checkSnakeCanMove('DD'):
                                if self.inGame.snake.currentDirection != None:
                                    self.inGame.snake.currentDirection = 'DD'
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            if self.inGame.snake.currentDirection != 'LL' and self.inGame.snake.checkSnakeCanMove('RR'):
                                if self.inGame.snake.currentDirection != None:
                                    self.inGame.snake.currentDirection = 'RR'
                        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            if self.inGame.snake.currentDirection != 'RR' and self.inGame.snake.checkSnakeCanMove('LL'):
                                if self.inGame.snake.currentDirection != None:
                                    self.inGame.snake.currentDirection = 'LL'
                ###########   Get events when game pause   ##################################################
                elif self.inGame.waiting:
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
                        snake.saveSnake(Snake())
                        self.inGame.snake = Snake()
                        self.inGame.foodManager = FoodManager()
                        self.inGame.update()
                        self.runningGameOverMenu = False
                        
                                  
    ###########   Update screen with current status   #######################################################       
    def update(self):
        setting.soundVolumeUpdate()
        ###########   Update screen Main Menu   #############################################################
        if self.runningMainMenu:
            if self.countTicks % (FPS * 1000 // self.mainMenu.FPS) == 0:
                self.mainMenu.update()
        ###########   Update screen Play Game Menu   ########################################################
        elif self.runningPlayGameMenu:
            if self.countTicks % (FPS * 1000 // self.playGameMenu.FPS) == 0:
                self.playGameMenu.update()
        ###########   Update screen when player controlling snake   #########################################
        elif self.runningInGame:
            ###########   Check game over   #################################################################
            if self.inGame.snake.died():
                SETTING2['SOUND']['GAME_OVER'].play()
                self.inGame.running = False
                self.runningInGame = False
                self.runningGameOverMenu = True
                self.gameOverMenu = GameOverMenu(WIDTH//2, HEIGHT//2, WIDTH, HEIGHT, self.inGame.snake)
            ###########   Update screen when showing screen start in Ingame   ###############################
            if self.inGame.showingScreenStart:
                if self.countTicks % (FPS * 1000 // self.inGame.snake.animationSpeed) == 0:
                    self.inGame.update(type='UpdateSnakeAnimation')
                if self.countTicks % (FPS * 1000 // self.mainMenu.FPS) == 0:
                    self.inGame.update()
            ###########   Update screen when player is playing   ############################################
            elif self.inGame.running:
                if self.countTicks % (FPS * 1000 // self.inGame.snake.animationSpeed) == 0:
                    self.inGame.update(type='UpdateSnakeAnimation')
                if self.countTicks % (FPS * 1000 // self.inGame.foodManager.animationSpeed) == 0:
                    self.inGame.update(type='UpdateFoodAnimation')
                if self.countTicks % (FPS * 1000 // self.inGame.snake.moveSpeed) == 0:
                    self.inGame.update(tempCountTicks=self.countTicks)
            ###########   Update screen when pause game   ###################################################
            elif self.inGame.waiting:
                pass
        ###########   Update screen when Game Over   ########################################################
        elif self.runningGameOverMenu:
            if self.countTicks % (FPS * 1000 // self.inGame.snake.dropSpeed) == 0:
                self.gameOverMenu.update(type='UpdateSnakeDrop')
            if self.countTicks % (FPS * 1000 // self.inGame.snake.animationSpeed) == 0:
                self.gameOverMenu.update(type='UpdateSnakeAnimation')
            if self.countTicks % (FPS * 1000 // self.gameOverMenu.FPS) == 0:
                self.gameOverMenu.update()
        ###########   Update screen when showing Options Menu   #############################################
        elif self.runningOptionsMenu:
            if self.countTicks % (FPS * 1000 // self.optionsMenu.FPS) == 0:
                self.optionsMenu.update()
        ###########   Update screen when showing Gamemode Setting Menu   ########################################
        elif self.runningGamemodeSettingMenu:
            if self.countTicks % (FPS * 1000 // self.gamemodeSettingMenu.FPS) == 0:
                self.gamemodeSettingMenu.update()
        ###########   Update screen when showing Game Setting Menu   ########################################
        elif self.runningGameSettingMenu:
            if self.countTicks % (FPS * 1000 // self.gameSettingMenu.FPS) == 0:
                self.gameSettingMenu.update()
        ###########   Update screen when showing Sound Setting Menu   ########################################
        elif self.runningSoundSettingMenu:
            if self.countTicks % (FPS * 1000 // self.soundSettingMenu.FPS) == 0:
                self.soundSettingMenu.update() 
        
    ###########   Draw screen with current status and show it   #############################################
    def display(self):
        ###########   Clear old images   ####################################################################
        self.screen.fill(BLACK)
        ###########   Draw new images   #####################################################################
        if self.runningInGame:
            self.inGame.draw(self.screen)
        elif self.runningMainMenu:
            self.mainMenu.draw(self.screen)
        elif self.runningPlayGameMenu:
            self.playGameMenu.draw(self.screen)
        elif self.runningGameOverMenu:
            self.gameOverMenu.draw(self.screen)
        elif self.runningOptionsMenu:
            self.optionsMenu.draw(self.screen)
        elif self.runningGamemodeSettingMenu:
            self.gamemodeSettingMenu.draw(self.screen)
        elif self.runningGameSettingMenu:
            self.gameSettingMenu.draw(self.screen)
        elif self.runningSoundSettingMenu:
            self.soundSettingMenu.draw(self.screen)
        pygame.display.flip()