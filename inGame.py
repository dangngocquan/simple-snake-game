import pygame
import menu
from menu import Button

###########  SETTING  ###########################################################
CELL_SIZE = 25
INGAME_WIDTH = 1000
INGAME_HEIGHT = 600
NUMBER_ROWS = INGAME_HEIGHT // CELL_SIZE
NUMBER_COLUMNS = INGAME_WIDTH // CELL_SIZE
DEFAULT_SNAKE_SPEED = 5
DEFAULT_SNAKE_CHANGE_COLOR_SPEED = 2
DEFAULT_MAX_FOOD = 7


###########  COLOR  ###########################################################
GRAY = (111, 111, 111)

###########  IMAGE  #############################################################
SNAKE = {
    'HEAD' : {},
    'BODY' : {},
    'TAIL' : {}
}
for direction in ['DD', 'DL', 'DR', 'LL', 'LD', 'LU', 'RR', 'RD', 'RU', 'UU', 'UL', 'UR']:
    SNAKE['HEAD'][direction] = []
    for i in range(7):
        img = pygame.image.load("./assets/images/snake/head/" + str(direction) 
                                + "/head" + str(direction) + "" + str(i) + ".png")
        img = pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))
        SNAKE['HEAD'][direction].append(img)
for direction in ['DD', 'DL', 'DR', 'LL', 'LD', 'LU', 'RR', 'RD', 'RU', 'UU', 'UL', 'UR']:
    SNAKE['BODY'][direction] = []
    for i in range(7):
        img = pygame.image.load("./assets/images/snake/body/" + str(direction)
                                + "/body" + str(direction) + "" + str(i) + ".png", )
        img = pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))
        SNAKE['BODY'][direction].append(img)
for direction in ['DD', 'DL', 'DR', 'LL', 'LD', 'LU', 'RR', 'RD', 'RU', 'UU', 'UL', 'UR']:
    SNAKE['TAIL'][direction] = []
    for i in range(7):
        img = pygame.image.load("./assets/images/snake/tail/" + str(direction)
                                + "/tail" + str(direction) + "" + str(i) + ".png")
        img = pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))
        SNAKE['TAIL'][direction].append(img)
FOOD = []
for i in range(4):
    img = pygame.image.load("./assets/images/food/food" + str(i) + ".png")
    img = pygame.transform.scale(img, (CELL_SIZE, CELL_SIZE))
    FOOD.append(img)

###########   CLASS GRID   ##################################################################################
class Grid:
    ###########   Constructor   #############################################################################
    def __init__(self, x, y):
        ###########   Create surface and coordiante topLeft   ###############################################
        self.surface = pygame.Surface((INGAME_WIDTH, INGAME_HEIGHT), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (x, y)
        ###########   Draw lines   ##########################################################################
        for row in range(NUMBER_ROWS):
            pygame.draw.line(self.surface, GRAY, (0, row*CELL_SIZE), (INGAME_WIDTH, row*CELL_SIZE))
        for column in range(NUMBER_COLUMNS):
            pygame.draw.line(self.surface, GRAY, (column*CELL_SIZE, 0), (column*CELL_SIZE, INGAME_HEIGHT))
    
    ###########   Update status of Grid   ###################################################################
    def update(self):
        pass
    
    ###########   Draw Grid on another surface   ############################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)

###########  CLASS SNAKE BLOCK  #############################################################################
class SnakeBlock:
    ###########   Constructor   #############################################################################
    def __init__(self, image, x=NUMBER_COLUMNS//2 * CELL_SIZE, y=NUMBER_ROWS//2 * CELL_SIZE, 
                 direction='UU'):
        self.surface = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (x, y)
        self.surface.blit(image, (0, 0))
        self.x = x
        self.y = y
        self.direction = direction
    
    ###########   Get coordinate of Snake Block with type List  #############################################
    def coordinate(self):
        return [self.x, self.y]
    
    ###########   Set up new coordinate for Snake Block   ###################################################
    def setCoordinate(self, x, y):
        self.x = x
        self.y = y
        self.surfaceRect.topleft = (x, y)
    
    ###########   Update new image for Snake Block   ########################################################
    def update(self, part, indexImg):
        ###### Clear old image ##############################################################################
        self.surface.fill((0, 0, 0, 0))
        ###### Add new image ################################################################################
        img = SNAKE[part][self.direction][indexImg]
        self.surface.blit(img, (0, 0))

    ###########   Draw SnakeBlock in another surface   ######################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
###########  CLASS SNAKE  ###################################################################################
class Snake:
    ###########   Constructor   #############################################################################
    def __init__(self, speed=DEFAULT_SNAKE_SPEED, currentDirection='UU'):
        ###########   Surface and coordinate   ##############################################################
        self.surface = pygame.Surface((INGAME_WIDTH, INGAME_HEIGHT), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (0, 0)
        
        ###########   Create first head, body anf tail for Snake   ##########################################
        self.head = [SnakeBlock(SNAKE['HEAD']['UU'][0])]
        self.body = [SnakeBlock(SNAKE['BODY']['UU'][0], NUMBER_COLUMNS//2*CELL_SIZE, NUMBER_ROWS//2*CELL_SIZE + CELL_SIZE)]
        self.tail = [SnakeBlock(SNAKE['TAIL']['UU'][0], NUMBER_COLUMNS//2*CELL_SIZE, NUMBER_ROWS//2*CELL_SIZE + 2*CELL_SIZE)]
        self.head[0].draw(self.surface)
        self.body[0].draw(self.surface)
        self.tail[0].draw(self.surface)
        
        ###########   Speed, Direction of Snake #############################################################
        self.speed = speed
        self.changeColorSpeed = DEFAULT_SNAKE_CHANGE_COLOR_SPEED
        self.currentDirection = currentDirection
        self.countTicks = 0

    ###########   Check if snake can move or not with next direction   ######################################
    def checkSnakeCanMove(self, aDirection):
        if aDirection == 'UU' and (self.head[0].y - CELL_SIZE) == self.body[0].y:
            return False
        elif aDirection == 'DD' and (self.head[0].y + CELL_SIZE) == self.body[0].y:
            return False
        elif aDirection == 'RR' and (self.head[0].x + CELL_SIZE) == self.body[0].x:
            return False
        elif aDirection == 'LL' and (self.head[0].x - CELL_SIZE) == self.body[0].x:
            return False
        return True
    
    ##   Update Coordinate and Direction of head, body and tail when snake move with current direction   ####
    def move(self):
        if self.currentDirection == None:
            return
        
        ########  Correct direction for head, body and tail  ################################################
        self.head[0].direction = self.head[0].direction[1] + self.currentDirection[0]
        self.tail[0].direction = self.body[len(self.body) - 1].direction
        for index in range(len(self.body) - 1, 0, -1):
            self.body[index].coordinate = self.body[index-1].direction
        self.body[0].direction = self.head[0].direction
        
        #######  Update new image for head, body and tail  ##################################################
        self.head[0].update('HEAD', self.countTicks)
        for snakeBlock in self.body:
            snakeBlock.update('BODY', self.countTicks)
        self.tail[0].update('TAIL', self.countTicks)
        
        ########  New Coordinate of snakeBlocks  ############################################################
        self.tail[0].setCoordinate(self.body[len(self.body)-1].x, self.body[len(self.body)-1].y)
        for index in range(len(self.body) - 1, 0, -1):
            self.body[index].setCoordinate(self.body[index-1].x, self.body[index-1].y)
        self.body[0].setCoordinate(self.head[0].x, self.head[0].y)
        if self.currentDirection[0] == 'U':
            self.head[0].setCoordinate(self.head[0].x, (self.head[0].y - CELL_SIZE) % INGAME_HEIGHT)
        elif self.currentDirection[0] == 'D':
            self.head[0].setCoordinate(self.head[0].x, (self.head[0].y + CELL_SIZE) % INGAME_HEIGHT)
        elif self.currentDirection[0] == 'R':
            self.head[0].setCoordinate((self.head[0].x + CELL_SIZE) % INGAME_WIDTH, self.head[0].y)
        elif self.currentDirection[0] == 'L':
            self.head[0].setCoordinate((self.head[0].x - CELL_SIZE) % INGAME_WIDTH, self.head[0].y)
            
    ###########   Update status of snake   ##################################################################
    def update(self):
        self.move()
        self.surface.fill((0, 0, 0, 0))
        for snakeBlock in (self.tail + self.body + self.head):
            snakeBlock.draw(self.surface)
    
    ###########   Draw snake on another surface   ###########################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)


###########  CLASS FOOD  ####################################################################################
class Food:
    def __init__(self, image, x, y):
        self.surface = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (x, y)
        
        self.surface.blit(image, (0, 0))
        
    def update(self):
        pass
    
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)


###########  CLASS FOOD MANAGER  ############################################################################
class FoodManager:
    def __init__(self):
        self.surface = pygame.Surface((INGAME_WIDTH, INGAME_HEIGHT), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (0, 0)
        self.listFood = []
        self.maxFood = DEFAULT_MAX_FOOD
    
    def update(self):
        pass
    
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)   


###########  CLASS INGAME  ##################################################################################
class InGame:
    ###########   Constructor   #############################################################################
    def __init__(self, snake=Snake(), foodManager = FoodManager(), score=0):
        ###########   Create surface and coordinate   #######################################################
        self.surface = pygame.Surface((INGAME_WIDTH, INGAME_HEIGHT), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (0, 0)
        
        ###########   Status screen    ######################################################################
        self.showingScreenStart = False
        self.running = False
        self.waiting = False
        self.showingScreenEnd = False
        
        ###########   Object in game    #####################################################################
        self.grid = Grid(0, 0)
        self.snake = snake
        self.foodManager = foodManager
        self.descriptionText = Button("Press SPACE to start", menu.TITLE_FONT2, INGAME_WIDTH//2, INGAME_HEIGHT*9//12)
        self.descriptionText.isChosen = True
        self.score = score
        self.scoreText = Button(f"Score: {self.score}", menu.SMALL_FONT, 3*CELL_SIZE, CELL_SIZE)
        self.scoreText.isChosen = True
        
    ###########   Update screen    ##########################################################################
    def update(self):
        ###########   Remove old screen   ###################################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new screen with current status   #################################################
        if self.showingScreenStart:
            self.snake.draw(self.surface)
            self.grid.draw(self.surface)
            self.descriptionText.draw(self.surface)
            self.descriptionText.update("Press SPACE to start", menu.TITLE_FONT2, 'R')
        elif self.running:
            self.snake.update()
            self.scoreText.update(f"Score: {self.score}", menu.SMALL_FONT, 'R')
            self.grid.draw(self.surface)
            self.scoreText.draw(self.surface)
            self.snake.draw(self.surface)
        elif self.waiting:
            pass
        elif self.showingScreenEnd:
            pass

    ###########   Draw current screen on anthor surface  ####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
        
        