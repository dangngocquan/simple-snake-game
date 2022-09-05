import pygame


###########  SIZE, CAPTION, FPS SCREEN  #####################################################################
CELL_SIZE = 25
INGAME_WIDTH = 1000
INGAME_HEIGHT = 600
NUMBER_ROWS = INGAME_HEIGHT // CELL_SIZE
NUMBER_COLUMNS = INGAME_WIDTH // CELL_SIZE
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_CAPTION = "Simple Snake Gameeee"
FPS = 60


###########  MENU  ##########################################################################################
MENU_CHANGE_COLOR_SPEED = 5
pygame.font.init()
SIMPLE_SNAKE_FONT = pygame.font.SysFont('algerian', 96)
TITLE_FONT = pygame.font.SysFont('castellar', 48)
TITLE_FONT_HORVED = pygame.font.SysFont('castellar', 56)
TITLE_FONT2 = pygame.font.SysFont('chiller', 48)
MEDIUM_FONT = pygame.font.SysFont('castellar', 36)
MEDIUM_FONT2 = pygame.font.SysFont('chiller', 36)
SMALL_FONT = pygame.font.SysFont('castellar', 22)

###########  FOOD SETTING  ##################################################################################
DEFAULT_MAX_FOOD = 7
DEFAULT_FOOD_TRANSITION_SPEED = 6
FOOD = []
for i in range(4):
    img = pygame.image.load("./assets/images/food/food" + str(i) + ".png")
    img = pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))
    FOOD.append(img)
    

###########  SNAKE  #########################################################################################
DEFAULT_SNAKE_SPEED = 60
DEFAULT_SNAKE_DROP_SPEED = 12
DEFAULT_SNAKE_FRAME_TRANSITION_SPEED = 3
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

