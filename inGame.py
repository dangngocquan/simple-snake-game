import pygame
import menu
from menu import Button

###########  SETTING  ###########################################################
CELL_SIZE = 25
INGAME_WIDTH = 1000
INGAME_HEIGHT = 600
NUMBER_ROWS = INGAME_HEIGHT // CELL_SIZE
NUMBER_COLUMNS = INGAME_WIDTH // CELL_SIZE
DEFAULT_SNAKE_SPEED = 6


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


class Grid:
    def __init__(self, x, y):
        self.surface = pygame.Surface((INGAME_WIDTH, INGAME_HEIGHT), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (x, y)
        for row in range(NUMBER_ROWS):
            pygame.draw.line(self.surface, GRAY, (0, row*CELL_SIZE), (INGAME_WIDTH, row*CELL_SIZE))
        for column in range(NUMBER_COLUMNS):
            pygame.draw.line(self.surface, GRAY, (column*CELL_SIZE, 0), (column*CELL_SIZE, INGAME_HEIGHT))
        
    def update(self):
        pass
    
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)

###########  CLASS SNAKE BLOCK  #############################################################
class SnakeBlock:
    def __init__(self, image, x=NUMBER_COLUMNS//2 * CELL_SIZE, y=NUMBER_ROWS//2 * CELL_SIZE, 
                 direction='UU'):
        self.surface = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (x, y)
        self.surface.blit(image, (0, 0))
        self.x = x
        self.y = y
        self.direction = direction
    
    def coordinate(self):
        return [self.x, self.y]
    
    def setCoordinate(self, x, y):
        self.x = x
        self.y = y
        self.surfaceRect.topleft = (x, y)
        
    def update(self, part):
        ###### Clear old image #################################################################
        self.surface.fill((0, 0, 0, 0))
        ###### Add new image #################################################################
        img = SNAKE[part][self.direction][0]
        self.surface.blit(img, (0, 0))
    
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
###########  CLASS SNAKE  #############################################################
class Snake:
    def __init__(self, speed=DEFAULT_SNAKE_SPEED, currentDirection='UU'):
        self.surface = pygame.Surface((INGAME_WIDTH, INGAME_HEIGHT), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (0, 0)
        
        self.head = [SnakeBlock(SNAKE['HEAD']['UU'][0])]
        self.body = [SnakeBlock(SNAKE['BODY']['UU'][0], NUMBER_COLUMNS//2*CELL_SIZE, NUMBER_ROWS//2*CELL_SIZE + CELL_SIZE)]
        self.tail = [SnakeBlock(SNAKE['TAIL']['UU'][0], NUMBER_COLUMNS//2*CELL_SIZE, NUMBER_ROWS//2*CELL_SIZE + 2*CELL_SIZE)]
        self.head[0].draw(self.surface)
        self.body[0].draw(self.surface)
        self.tail[0].draw(self.surface)
        
        self.speed = speed
        self.currentDirection = currentDirection
        self.countTicks = 0
    
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
    
    def move(self):
        if self.currentDirection == None:
            return
        
        ###########  New Image of snakeBlocks  ##################################################################
           ########  Correct direction for snakeBlocks  #########################################
        self.head[0].direction = self.head[0].direction[1] + self.currentDirection[0]
        
        # if self.head[0].direction in ['LR', 'RL', 'DU', 'UD']:
        #     self.head[0].direction = self.head[0].direction[1] + self.head[0].direction[1]
        
        self.tail[0].direction = self.body[len(self.body) - 1].direction
        for index in range(len(self.body) - 1, 0, -1):
            self.body[index].coordinate = self.body[index-1].direction
        self.body[0].direction = self.head[0].direction
           #######  Update new image   #######################
        self.head[0].update('HEAD')
        for snakeBlock in self.body:
            snakeBlock.update('BODY')
        self.tail[0].update('TAIL')
        
        ###########  New Coordinate of snakeBlocks  #############################################################
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
            
        

            
    
    def update(self):
        self.move()
        self.surface.fill((0, 0, 0, 0))
        for snakeBlock in (self.tail + self.body + self.head):
            snakeBlock.draw(self.surface)
    
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        


###########  CLASS FOOD  #############################################################
class Food:
    def __init__(self):
        pass


###########  CLASS FOOD MANAGER  #############################################################
class FoodManager:
    def __init__(self):
        pass


###########  CLASS INGAME  #############################################################
class InGame:
    def __init__(self, snake=Snake(), foodManager = FoodManager()):
        self.surface = pygame.Surface((INGAME_WIDTH, INGAME_HEIGHT), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        
        self.showingScreenStart = False
        self.running = False
        self.waiting = False
        self.showingScreenEnd = False
        
        self.grid = Grid(0, 0)
        self.snake = snake
        self.foodManager = foodManager
        self.descriptionText = Button("Press SPACE to start", menu.TITLE_FONT2, INGAME_WIDTH//2, INGAME_HEIGHT*5//6)
        self.descriptionText.isChosen = True
        
        
    def update(self):
        self.surface.fill((0, 0, 0, 0))
        if self.showingScreenStart:
            self.snake.draw(self.surface)
            self.grid.draw(self.surface)
            self.descriptionText.draw(self.surface)
            self.descriptionText.update("Press SPACE to start", menu.TITLE_FONT2, 'R')
        elif self.running:
            self.snake.update()
            self.snake.draw(self.surface)
            self.grid.draw(self.surface)
        elif self.waiting:
            pass
        elif self.showingScreenEnd:
            pass
    
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
        
        