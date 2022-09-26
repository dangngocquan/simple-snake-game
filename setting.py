import json
import pygame

###########  SETTING CAN BE CHANGED BY PLAYER  ##############################################################
SETTING1 = {}

###########   Function load setting for game from json file   ###############################################
def loadSetting(path):
    global SETTING1
    with open(path, 'r') as file:
        SETTING1 = json.load(file)
    file.close()

###########   Function save current setting of game to json file   ##########################################
def saveSetting(path):
    global SETTING1
    with open('./data/setting/setting.json', 'w') as file:
        json.dump(SETTING1, file, indent=4)
    file.close()

###########   Function change data of setting file   ########################################################
def replaceData(key1=None, key2=None, newData=''):
    global SETTING1
    if key1 == None:
        return
    if key2 == None:
        SETTING1[key1] = newData
    else:
        SETTING1[key1][key2] = newData

###########   Load file setting   ###########################################################################
loadSetting('./data/setting/setting.json')

###########  RESOURCE  ######################################################################################
###########  SIZE  ##########################################################################################
CELL_SIZE = 25

###########  MENU  ##########################################################################################
pygame.font.init()
BIG_FONT = pygame.font.SysFont('algerian', 96)
MEDIUM_FONT = pygame.font.SysFont('castellar', 48)
MEDIUM_FONT_HORVED = pygame.font.SysFont('castellar', 56)
MEDIUM_FONT_2 = pygame.font.SysFont('chiller', 48)
SMALL_FONT = pygame.font.SysFont('chiller', 36)
DESCRIPTION_FONT = pygame.font.SysFont('castellar', 22)

###########  FOOD SETTING  ##################################################################################
DEFAULT_MAX_FOOD = 5
DEFAULT_FOOD_TRANSITION_SPEED = 6
FOOD = []
for i in range(4):
    img = pygame.image.load("./assets/images/food/food" + str(i) + ".png")
    img = pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))
    FOOD.append(img)
    

###########  SNAKE  #########################################################################################
SNAKE = {
    'HEAD' : {},
    'BODY' : {},
    'TAIL' : {}
}
for direction in ['DD', 'DL', 'DR', 'LL', 'LD', 'LU', 'RR', 'RD', 'RU', 'UU', 'UL', 'UR']:
    SNAKE['HEAD'][direction] = []
    for i in range(7):
        img = pygame.image.load("./assets/images/snake/head/" + direction 
                                + "/head" + direction + "" + str(i) + ".png")
        img = pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))
        SNAKE['HEAD'][direction].append(img)
for direction in ['DD', 'DL', 'DR', 'LL', 'LD', 'LU', 'RR', 'RD', 'RU', 'UU', 'UL', 'UR']:
    SNAKE['BODY'][direction] = []
    for i in range(7):
        img = pygame.image.load("./assets/images/snake/body/" + direction
                                + "/body" + direction + "" + str(i) + ".png", )
        img = pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))
        SNAKE['BODY'][direction].append(img)
for direction in ['DD', 'DL', 'DR', 'LL', 'LD', 'LU', 'RR', 'RD', 'RU', 'UU', 'UL', 'UR']:
    SNAKE['TAIL'][direction] = []
    for i in range(7):
        img = pygame.image.load("./assets/images/snake/tail/" + direction
                                + "/tail" + direction + "" + str(i) + ".png")
        img = pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))
        SNAKE['TAIL'][direction].append(img)

###########  COLOR  #########################################################################################
GRAY = (111, 111, 111)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


###########  SOUND  #########################################################################################
pygame.mixer.init()
PRESS_BUTTON = pygame.mixer.Sound('./assets/sounds/button/pressButton.wav')
CHANGE_BUTTON = pygame.mixer.Sound('./assets/sounds/button/changeButton.wav')
SNAKE_EAT_FOOD = pygame.mixer.Sound('./assets/sounds/snake/eatFood.wav')
GAME_OVER = pygame.mixer.Sound('./assets/sounds/snake/died.wav')

###########  SETTING CAN'T BE CHANGED BY PLAYER  ############################################################
SETTING2 = {
    'SCREEN' : {
        'CELL_SIZE' : CELL_SIZE,
        'WIDTH' : 1000,
        'HEIGHT' : 600,
        'NUMBER_ROWS' : 24,
        'NUMBER_COLUMNS' : 40,
        'CAPTION' : 'Simple Snake Game',
        'FPS' : 60
    },
    'MENU' : {
        'BIG_FONT' : BIG_FONT,
        'MEDIUM_FONT' : MEDIUM_FONT,
        'MEDIUM_FONT_HORVED' : MEDIUM_FONT_HORVED,
        'MEDIUM_FONT_2' : MEDIUM_FONT_2,
        'SMALL_FONT' : SMALL_FONT,
        'DESCRIPTION_FONT' : DESCRIPTION_FONT
    },
    'COLOR' : {
        'BLACK' : BLACK,
        'WHITE' : WHITE,
        'GRAY' : GRAY
    },
    'SNAKE' : SNAKE,
    'FOOD' : FOOD,
    'SOUND' : {
        'PRESS_BUTTON' : PRESS_BUTTON,
        'CHANGE_BUTTON' : CHANGE_BUTTON,
        'SNAKE_EAT_FOOD' : SNAKE_EAT_FOOD,
        'GAME_OVER' : GAME_OVER,
        'MUSIC' : './assets/sounds/game/BoyWithUkeLoafers.wav'
    }
}