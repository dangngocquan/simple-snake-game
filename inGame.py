import random
import pygame
import menu
from menu import Button

###########  SETTING  #######################################################################################
CELL_SIZE = 25
INGAME_WIDTH = 1000
INGAME_HEIGHT = 600
NUMBER_ROWS = INGAME_HEIGHT // CELL_SIZE
NUMBER_COLUMNS = INGAME_WIDTH // CELL_SIZE
DEFAULT_SNAKE_SPEED = 4
DEFAULT_SNAKE_CHANGE_FRAME_SPEED = 2
DEFAULT_MAX_FOOD = 7


###########  COLOR  #########################################################################################
GRAY = (111, 111, 111)

###########  IMAGE  #########################################################################################
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
                 direction='UU', indexFrame=0):
        self.surface = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (x, y)
        self.surface.blit(image, (0, 0))
        self.x = x
        self.y = y
        self.direction = direction
        self.indexFrame = indexFrame
    
    ###########   Get coordinate of Snake Block with type List  #############################################
    def coordinate(self):
        return [self.x, self.y]
    
    ###########   Set up new coordinate for Snake Block   ###################################################
    def setCoordinate(self, x, y):
        self.x = x
        self.y = y
        self.surfaceRect.topleft = (x, y)
    
    ###########   Update new image for Snake Block   ########################################################
    def update(self, part):
        ###### Clear old image ##############################################################################
        self.surface.fill((0, 0, 0, 0))
        ###### Add new image ################################################################################
        img = SNAKE[part][self.direction][self.indexFrame]
        self.surface.blit(img, (0, 0))

    ###########   Draw SnakeBlock in another surface   ######################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
###########  CLASS SNAKE  ###################################################################################
class Snake:
    ###########   Constructor   #############################################################################
    def __init__(self, speed=DEFAULT_SNAKE_SPEED, currentDirection='UU', score=0):
        ###########   Surface and coordinate   ##############################################################
        self.surface = pygame.Surface((INGAME_WIDTH, INGAME_HEIGHT), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (0, 0)
        
        ###########   Create first head, body anf tail for Snake   ##########################################
        self.head = [SnakeBlock(SNAKE['HEAD']['UU'][0], indexFrame=0)]
        self.body = [SnakeBlock(SNAKE['BODY']['UU'][0], NUMBER_COLUMNS//2*CELL_SIZE, 
                                NUMBER_ROWS//2*CELL_SIZE + CELL_SIZE, indexFrame=1)]
        self.tail = [SnakeBlock(SNAKE['TAIL']['UU'][0], NUMBER_COLUMNS//2*CELL_SIZE, 
                                NUMBER_ROWS//2*CELL_SIZE + 2*CELL_SIZE, indexFrame=2)]
        self.head[0].draw(self.surface)
        self.body[0].draw(self.surface)
        self.tail[0].draw(self.surface)
        
        ###########   Speed, Direction of Snake #############################################################
        self.speed = speed
        self.changeFrameSpeed = DEFAULT_SNAKE_CHANGE_FRAME_SPEED
        self.currentDirection = currentDirection
        self.score = score

    ###########  Get all coordinate of Snake Blocks #########################################################
    def coordinateSnakeBlocks(self):
        return [snakeBlock.coordinate() for snakeBlock in (self.head + self.body + self.tail)]
    
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
    
    ###########   Check if snake is eating food   ##########################################################
    def eatingFood(self, foodList):
        for food in foodList:
            if self.head[0].coordinate() == food.coordinate():
                foodList.remove(food)
                self.score += self.speed
                return True
        return False
    
    ##   Update Coordinate and Direction of head, body and tail when snake move with current direction   ####
    def onlyMove(self):
        if self.currentDirection == None:
            return
        
        ########  Correct direction for head, body and tail  ################################################
        self.head[0].direction = self.head[0].direction[1] + self.currentDirection[0]
        self.tail[0].direction = self.body[len(self.body) - 1].direction
        for index in range(len(self.body) - 1, 0, -1):
            self.body[index].direction = self.body[index-1].direction
        self.body[0].direction = self.head[0].direction
        
        #######  Update new image for head, body and tail  ##################################################
        self.head[0].update('HEAD')
        for snakeBlock in self.body:
            snakeBlock.update('BODY')
        self.tail[0].update('TAIL')
        
        ########  New Coordinate of snakeBlocks  ############################################################
        self.tail[0].setCoordinate(self.body[len(self.body)-1].x, self.body[len(self.body)-1].y)
        for index in range(len(self.body) - 1, 0, -1):
            self.body[index].setCoordinate(self.body[index-1].x, self.body[index-1].y)
        self.body[0].setCoordinate(self.head[0].x, self.head[0].y)
        if self.currentDirection == 'UU':
            self.head[0].setCoordinate(self.head[0].x, (self.head[0].y - CELL_SIZE) % INGAME_HEIGHT)
        elif self.currentDirection == 'DD':
            self.head[0].setCoordinate(self.head[0].x, (self.head[0].y + CELL_SIZE) % INGAME_HEIGHT)
        elif self.currentDirection == 'RR':
            self.head[0].setCoordinate((self.head[0].x + CELL_SIZE) % INGAME_WIDTH, self.head[0].y)
        elif self.currentDirection == 'LL':
            self.head[0].setCoordinate((self.head[0].x - CELL_SIZE) % INGAME_WIDTH, self.head[0].y)
            
    def moveAndGrowUp(self):
        if self.currentDirection == None:
            return
        
        ########  Correct direction for head, body and tail  ################################################
        self.head[0].direction = self.head[0].direction[1] + self.currentDirection[0]
        newSnakeBlockDirection = self.head[0].direction
        
        ########  New Coordinate of snakeBlocks  ############################################################
        newSnakeBlockCoordinate = [self.head[0].x, self.head[0].y]
        if self.currentDirection == 'UU':
            self.head[0].setCoordinate(self.head[0].x, (self.head[0].y - CELL_SIZE) % INGAME_HEIGHT)
        elif self.currentDirection == 'DD':
            self.head[0].setCoordinate(self.head[0].x, (self.head[0].y + CELL_SIZE) % INGAME_HEIGHT)
        elif self.currentDirection == 'RR':
            self.head[0].setCoordinate((self.head[0].x + CELL_SIZE) % INGAME_WIDTH, self.head[0].y)
        elif self.currentDirection == 'LL':
            self.head[0].setCoordinate((self.head[0].x - CELL_SIZE) % INGAME_WIDTH, self.head[0].y)
        
        #######  Update new image for head, body and tail  ##################################################
        newSnakeBlockIndexFrame = self.head[0].indexFrame
        self.head[0].indexFrame = (self.head[0].indexFrame -1) % 7
        self.head[0].update('HEAD')
        newSnakeBlock = SnakeBlock(SNAKE['BODY'][newSnakeBlockDirection][newSnakeBlockIndexFrame], x=newSnakeBlockCoordinate[0],
                                   y=newSnakeBlockCoordinate[1], direction=newSnakeBlockDirection, 
                                   indexFrame=self.head[0].indexFrame)
        self.body.insert(0, newSnakeBlock)
        
        
    ###########   Update snake displacement  ################################################################
    def updateDisplacement(self, foodList):
        if self.eatingFood(foodList):
            self.moveAndGrowUp()
        else:
            self.onlyMove()
        
        self.surface.fill((0, 0, 0, 0))
        self.tail[0].draw(self.surface)
        for index in range(len(self.body) - 1, -1, -1):
            self.body[index].draw(self.surface)
        self.head[0].draw(self.surface)
        
    
    def updateFrame(self):
        self.head[0].indexFrame = (self.head[0].indexFrame - 1) % 7
        self.head[0].update('HEAD')
        for snakeBlock in self.body :
            snakeBlock.indexFrame = (snakeBlock.indexFrame - 1) % 7
            snakeBlock.update('BODY')
        self.tail[0].indexFrame = (self.tail[0].indexFrame - 1) % 7
        self.tail[0].update('TAIL')
        
        self.surface.fill((0, 0, 0, 0))
        self.tail[0].draw(self.surface)
        for index in range(len(self.body) - 1, -1, -1):
            self.body[index].draw(self.surface)
        self.head[0].draw(self.surface)
    
    ###########   Draw snake on another surface   ###########################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)


###########  CLASS FOOD  ####################################################################################
class Food:
    ########### Constructor  ################################################################################
    def __init__(self, x, y):
        ###########  Create surface   #######################################################################
        self.surface = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (x, y)
        self.x = x
        self.y = y
        
        ###########  Default image food  ####################################################################
        self.surface.blit(FOOD[0], (0, 0))
        self.indexFrame = 0
    
    ###########  Get coordinate of food  ####################################################################
    def coordinate(self):
        return [self.x, self.y]
    
    ###########  Update image of food  ######################################################################
    def update(self):
        # self.indexFrame = (self.indexFrame + 1) % 4
        ###########  Remove old image food  #################################################################
        self.surface.fill((0, 0, 0, 0))
        ###########  Draw new image food  ###################################################################
        self.surface.blit(FOOD[self.indexFrame], (0, 0))
    
    ###########  Draw Food on another surface  ##############################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)


###########  CLASS FOOD MANAGER  ############################################################################
class FoodManager:
    ###########  Constructor  ###############################################################################
    def __init__(self):
        ###########  Surface and coordinate #################################################################
        self.surface = pygame.Surface((INGAME_WIDTH, INGAME_HEIGHT), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (0, 0)
        ###########  List food anf  number of foods  ########################################################
        self.listFood = []
        self.maxFood = DEFAULT_MAX_FOOD
    
    ###########  Get coordinate of all foods ################################################################
    def coordinateFoods(self):
        return [food.coordinate() for food in self.listFood]
    
    ###########  Create a random Food  ######################################################################
    def createRandomValidFood(self, coordinateSnakeBlockss=[]):
        if len(self.listFood) + len(coordinateSnakeBlockss) >= NUMBER_ROWS * NUMBER_COLUMNS:
            return None
        randomX = random.randint(0, NUMBER_COLUMNS-1) * CELL_SIZE
        randomY = random.randint(0, NUMBER_ROWS-1) * CELL_SIZE
        while ([randomX, randomY] in (self.coordinateFoods() + coordinateSnakeBlockss)):
            randomX = random.randint(0, NUMBER_COLUMNS-1) * CELL_SIZE
            randomY = random.randint(0, NUMBER_ROWS-1) * CELL_SIZE
        return Food(randomX, randomY)
    
    ###########  Update status food man #####################################################################
    def update(self, coordinateSnakeBlockss):
        ###########  Supplement the Food Manager  ###########################################################
        while len(self.listFood) < self.maxFood:
            randomValidFood = self.createRandomValidFood(coordinateSnakeBlockss)
            if randomValidFood == None:
                break
            else:
                self.listFood.append(randomValidFood)
        ###########  Remove old image foods  ################################################################
        self.surface.fill((0, 0, 0, 0))
        ###########  Draw all new image foods  ##############################################################
        for food in self.listFood:
            food.update()
            food.draw(self.surface)
        
    ###########  Draw all foods on another surface  #########################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)   


###########  CLASS INGAME  ##################################################################################
class InGame:
    ###########   Constructor   #############################################################################
    def __init__(self, snake=Snake(), foodManager = FoodManager()):
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
        self.scoreText = Button(f"Score: {self.snake.score}", menu.SMALL_FONT, 3*CELL_SIZE, CELL_SIZE)
        self.scoreText.isChosen = True
        
    ###########   Update screen    ##########################################################################
    def update(self):
        ###########   Remove old screen   ###################################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new screen with current status   #################################################
        if self.showingScreenStart:
            self.grid.draw(self.surface)
            self.snake.draw(self.surface)
            self.descriptionText.draw(self.surface)
            self.descriptionText.update("Press SPACE to start", menu.TITLE_FONT2, 'R')
        elif self.running:
            self.snake.updateDisplacement(self.foodManager.listFood)
            self.foodManager.update(self.snake.coordinateSnakeBlocks())
            self.scoreText.update(f"Score: {self.snake.score}", menu.SMALL_FONT, 'R')
            self.grid.draw(self.surface)
            self.foodManager.draw(self.surface)
            self.scoreText.draw(self.surface)
            self.snake.draw(self.surface)
        elif self.waiting:
            pass
        elif self.showingScreenEnd:
            self.grid.draw(self.surface)
            self.foodManager.draw(self.surface)
            self.snake.draw(self.surface)
            
    def updateOnlySnakeFrame(self):
        ###########   Remove old screen   ###################################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new screen with current status   #################################################
        if self.showingScreenStart:
            pass
        elif self.running:
            self.snake.updateFrame()
            self.grid.draw(self.surface)
            self.foodManager.draw(self.surface)
            self.scoreText.draw(self.surface)
            self.snake.draw(self.surface)
        elif self.waiting:
            pass
        elif self.showingScreenEnd:
            pass

    ###########   Draw current screen on anthor surface  ####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
        
        