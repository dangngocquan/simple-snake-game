import random
import pygame
from setting import *
import setting


###########   VARIABLE   ####################################################################################
WIDTH = SETTING2['SCREEN']['WIDTH']
HEIGHT = SETTING2['SCREEN']['HEIGHT']
NUMBER_ROWS = SETTING2['SCREEN']['NUMBER_ROWS']
NUMBER_COLUMNS = SETTING2['SCREEN']['NUMBER_COLUMNS']
SETTING2['SCREEN']['CELL_SIZE'] = SETTING2['SCREEN']['CELL_SIZE']
SNAKE = SETTING2['SNAKE']

###########   Load data of snake from json file   ###########################################################
def loadPreviousSnake(path='./data/player/onePlayer/snake/snake.json'):
    snakesDict = None
    with open(path, 'r') as file:
        snakesDict = json.load(file)
    file.close()
    
    snakeDict = snakesDict['SNAKE'][SETTING1['ACCOUNT']['INDEX_ACCOUNT']]
    head = []
    for snakeBlock in snakeDict['HEAD']:
        if snakeDict['typeColor'] == 'blue':
            head.append(SnakeBlock(SNAKE['HEAD'][snakeBlock['direction']][snakeBlock['indexFrame']], 
                                x=snakeBlock['x'], y=snakeBlock['y'], 
                                direction=snakeBlock['direction'], indexFrame=snakeBlock['indexFrame'],
                                typeColor=snakeDict['typeColor']))
        elif snakeDict['typeColor'] == 'green':
            head.append(SnakeBlock(SNAKE_02['HEAD'][snakeBlock['direction']][snakeBlock['indexFrame']], 
                                x=snakeBlock['x'], y=snakeBlock['y'], 
                                direction=snakeBlock['direction'], indexFrame=snakeBlock['indexFrame'],
                                typeColor=snakeDict['typeColor']))
    body = []
    
    for snakeBlock in snakeDict['BODY']:
        if snakeDict['typeColor'] == 'blue':
            body.append(SnakeBlock(SNAKE['BODY'][snakeBlock['direction']][snakeBlock['indexFrame']], 
                                x=snakeBlock['x'], y=snakeBlock['y'], 
                                direction=snakeBlock['direction'], indexFrame=snakeBlock['indexFrame'],
                                typeColor=snakeDict['typeColor']))
        elif snakeDict['typeColor'] == 'green':
            body.append(SnakeBlock(SNAKE_02['BODY'][snakeBlock['direction']][snakeBlock['indexFrame']], 
                                x=snakeBlock['x'], y=snakeBlock['y'], 
                                direction=snakeBlock['direction'], indexFrame=snakeBlock['indexFrame'],
                                typeColor=snakeDict['typeColor']))
    tail = []
    for snakeBlock in snakeDict['TAIL']:
        if snakeDict['typeColor'] == 'blue':
            tail.append(SnakeBlock(SNAKE['TAIL'][snakeBlock['direction']][snakeBlock['indexFrame']], 
                                x=snakeBlock['x'], y=snakeBlock['y'], 
                                direction=snakeBlock['direction'], indexFrame=snakeBlock['indexFrame'],
                                typeColor=snakeDict['typeColor']))
        elif snakeDict['typeColor'] == 'green':
            tail.append(SnakeBlock(SNAKE_02['TAIL'][snakeBlock['direction']][snakeBlock['indexFrame']], 
                                x=snakeBlock['x'], y=snakeBlock['y'], 
                                direction=snakeBlock['direction'], indexFrame=snakeBlock['indexFrame'],
                                typeColor=snakeDict['typeColor']))
    score = snakeDict["score"]
    currentDirection = snakeDict["previousDirection"]
    previousDirection = snakeDict["previousDirection"]
    typeColor = snakeDict["typeColor"]
    
    return Snake(head=head, typeColor=typeColor, body=body, tail=tail, score=score, 
                 currentDirection=currentDirection, previousDirection=previousDirection)

###########   Save data of current snake to json file   #####################################################
def saveSnake(snake, path='./data/player/onePlayer/snake/snake.json'):
    snakeDict = {
        "HEAD" : [],
        "BODY" : [],
        "TAIL" : [],
        "score" : snake.score,
        "currentDirection" : snake.currentDirection,
        "previousDirection" : snake.previousDirection,
        "typeColor" : snake.typeColor
    }
    for snakeBlock in snake.head:
        dictSnakeBlock = {
            "direction" : snakeBlock.direction,
            "indexFrame" : snakeBlock.indexFrame,
            "x" : snakeBlock.x,
            "y" : snakeBlock.y
        }
        snakeDict['HEAD'].append(dictSnakeBlock)
    for snakeBlock in snake.body:
        dictSnakeBlock = {
            "direction" : snakeBlock.direction,
            "indexFrame" : snakeBlock.indexFrame,
            "x" : snakeBlock.x,
            "y" : snakeBlock.y
        }
        snakeDict['BODY'].append(dictSnakeBlock)
    for snakeBlock in snake.tail:
        dictSnakeBlock = {
            "direction" : snakeBlock.direction,
            "indexFrame" : snakeBlock.indexFrame,
            "x" : snakeBlock.x,
            "y" : snakeBlock.y
        }
        snakeDict['TAIL'].append(dictSnakeBlock)
        
    
    snakesDict = None
    with open(path, 'r') as file:
        snakesDict = json.load(file)
    file.close()
    
    for indexAccount in range(len(snakesDict['SNAKE'])):
        if indexAccount == SETTING1['ACCOUNT']['INDEX_ACCOUNT']:
            snakesDict['SNAKE'][indexAccount] = snakeDict
    
    with open(path, 'w') as file:
        json.dump(snakesDict, file, indent=4)
    file.close()
    

def removeSnake(index=-1, path='./data/player/onePlayer/snake/snake.json', 
                path2='./data/player/twoPlayer/snake/snake01.json',
                path3='./data/player/twoPlayer/snake/snake02.json'):
    if index >= 0:
        snakesDict = None
        with open(path, 'r') as file:
            snakesDict = json.load(file)
        file.close()
        snakesDict['SNAKE'].pop(index)
        with open(path, 'w') as file:
            json.dump(snakesDict, file, indent=4)
        file.close()
        
        snakesDict = None
        with open(path2, 'r') as file:
            snakesDict = json.load(file)
        file.close()
        snakesDict['SNAKE'].pop(index)
        with open(path2, 'w') as file:
            json.dump(snakesDict, file, indent=4)
        file.close()
        
        snakesDict = None
        with open(path3, 'r') as file:
            snakesDict = json.load(file)
        file.close()
        snakesDict['SNAKE'].pop(index)
        with open(path3, 'w') as file:
            json.dump(snakesDict, file, indent=4)
        file.close()

def addNewSnake(path1='./data/player/onePlayer/snake/snake.json', 
                path2='./data/player/twoPlayer/snake/snake01.json',
                path3='./data/player/twoPlayer/snake/snake02.json'):
    for typeLocation in range(-1,2):
        path = ""
        typeColor = ""
        if typeLocation == -1:
            path = path2
            typeColor = 'blue'
        elif typeLocation == 0:
            path = path1
            typeColor = 'blue'
        elif typeLocation == 1:
            path = path3
            typeColor = 'green'
            
        snake = Snake(typeLocation=typeLocation, typeColor=typeColor)
        snakeDict = {
            "HEAD" : [],
            "BODY" : [],
            "TAIL" : [],
            "score" : snake.score,
            "currentDirection" : snake.currentDirection,
            "previousDirection" : snake.previousDirection,
            "typeColor" : snake.typeColor
        }
        for snakeBlock in snake.head:
            dictSnakeBlock = {
                "direction" : snakeBlock.direction,
                "indexFrame" : snakeBlock.indexFrame,
                "x" : snakeBlock.x,
                "y" : snakeBlock.y
            }
            snakeDict['HEAD'].append(dictSnakeBlock)
        for snakeBlock in snake.body:
            dictSnakeBlock = {
                "direction" : snakeBlock.direction,
                "indexFrame" : snakeBlock.indexFrame,
                "x" : snakeBlock.x,
                "y" : snakeBlock.y
            }
            snakeDict['BODY'].append(dictSnakeBlock)
        for snakeBlock in snake.tail:
            dictSnakeBlock = {
                "direction" : snakeBlock.direction,
                "indexFrame" : snakeBlock.indexFrame,
                "x" : snakeBlock.x,
                "y" : snakeBlock.y
            }
            snakeDict['TAIL'].append(dictSnakeBlock)
            
        snakesDict = None
        with open(path, 'r') as file:
            snakesDict = json.load(file)
        file.close()
        snakesDict['SNAKE'].append(snakeDict)
        with open(path, 'w') as file:
            json.dump(snakesDict, file, indent=4)
        file.close()


###########  CLASS SNAKE BLOCK  #############################################################################
class SnakeBlock:
    ###########   Constructor   #############################################################################
    def __init__(self, image, x=NUMBER_COLUMNS//2 * SETTING2['SCREEN']['CELL_SIZE'], y=NUMBER_ROWS//2 * SETTING2['SCREEN']['CELL_SIZE'], 
                 direction='UU', indexFrame=0, typeColor='blue'):
        self.surface = pygame.Surface((SETTING2['SCREEN']['CELL_SIZE'], SETTING2['SCREEN']['CELL_SIZE']), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (x, y)
        self.surface.blit(image, (0, 0))
        self.x = x
        self.y = y
        self.direction = direction
        self.indexFrame = indexFrame
        self.typeColor = typeColor
    
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
        if self.typeColor == 'blue':
            img = SNAKE[part][self.direction][self.indexFrame]
        elif self.typeColor == 'green':
            img = SNAKE_02[part][self.direction][self.indexFrame]
        self.surface.blit(img, (0, 0))

    ###########   Draw SnakeBlock in another surface   ######################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
      
      
        
###########  CLASS SNAKE  ###################################################################################
class Snake:
    ###########   Constructor   #############################################################################
    def __init__(self, typeLocation=0, typeColor = 'blue', head=None, body=None, tail=None,
                 currentDirection='UU', previousDirection='UU', score=0):
        ###########   Surface and coordinate   ##############################################################
        self.surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.topleft = (0, 0)
        self.typeColor = typeColor
        ###########   Create first head, body anf tail for Snake   ##########################################
        if head == None:
            if typeColor == 'blue':
                self.head = [SnakeBlock(SNAKE['HEAD']['UU'][0], 
                                        x=NUMBER_COLUMNS//4*(2+typeLocation)*SETTING2['SCREEN']['CELL_SIZE'], 
                                        y=NUMBER_ROWS//2*SETTING2['SCREEN']['CELL_SIZE'],
                                        indexFrame=0, typeColor=typeColor)]
            elif typeColor == 'green':
                self.head = [SnakeBlock(SNAKE_02['HEAD']['UU'][0], 
                                        x=NUMBER_COLUMNS//4*(2+typeLocation)*SETTING2['SCREEN']['CELL_SIZE'], 
                                        y=NUMBER_ROWS//2*SETTING2['SCREEN']['CELL_SIZE'],
                                        indexFrame=0, typeColor=typeColor)]
        else:
            self.head = head
        if body == None:
            if typeColor == 'blue':
                self.body = [SnakeBlock(image=SNAKE['BODY']['UU'][1], 
                                        x=NUMBER_COLUMNS//4*(2+typeLocation)*SETTING2['SCREEN']['CELL_SIZE'], 
                                        y=NUMBER_ROWS//2*SETTING2['SCREEN']['CELL_SIZE'] + SETTING2['SCREEN']['CELL_SIZE'],
                                        indexFrame=1, typeColor=typeColor)]
            elif typeColor == 'green':
                self.body = [SnakeBlock(image=SNAKE_02['BODY']['UU'][1], 
                                        x=NUMBER_COLUMNS//4*(2+typeLocation)*SETTING2['SCREEN']['CELL_SIZE'], 
                                        y=NUMBER_ROWS//2*SETTING2['SCREEN']['CELL_SIZE'] + SETTING2['SCREEN']['CELL_SIZE'],
                                        indexFrame=1, typeColor=typeColor)]
        else:
            self.body = body
        if tail == None:
            if typeColor == 'blue':
                self.tail = [SnakeBlock(image=SNAKE['TAIL']['UU'][2], 
                                        x=NUMBER_COLUMNS//4*(2+typeLocation)*SETTING2['SCREEN']['CELL_SIZE'], 
                                        y=NUMBER_ROWS//2*SETTING2['SCREEN']['CELL_SIZE'] + 2*SETTING2['SCREEN']['CELL_SIZE'],
                                        indexFrame=2, typeColor=typeColor)]
            elif typeColor == 'green':
                self.tail = [SnakeBlock(image=SNAKE_02['TAIL']['UU'][2], 
                                        x=NUMBER_COLUMNS//4*(2+typeLocation)*SETTING2['SCREEN']['CELL_SIZE'], 
                                        y=NUMBER_ROWS//2*SETTING2['SCREEN']['CELL_SIZE'] + 2*SETTING2['SCREEN']['CELL_SIZE'],
                                        indexFrame=2, typeColor=typeColor)]
        else:
            self.tail = tail
        self.head[0].draw(self.surface)
        self.body[0].draw(self.surface)
        self.tail[0].draw(self.surface)
        ###########   Speed, Direction of Snake #############################################################
        self.moveSpeed = SETTING1['SNAKE']['MOVE_SPEED']
        self.dropSpeed = SETTING1['SNAKE']['DROP_SPEED']
        self.animationSpeed = SETTING1['SNAKE']['ANIMATION_SPEED']
        self.currentDirection = currentDirection
        self.previousDirection = previousDirection
        self.score = score

    ###########  Get all coordinate of Snake Blocks #########################################################
    def coordinateSnakeBlocks(self, avoidCoordinates=[]):
        ans = []
        for snakeBlock in (self.head + self.body + self.tail):
            if snakeBlock.coordinate() not in avoidCoordinates:
                ans.append(snakeBlock.coordinate())
        return ans
    
    ###########   Check if snake can move or not with next direction   ######################################
    def checkSnakeCanMove(self, aDirection):
        if aDirection == 'UU' and (self.head[0].y - SETTING2['SCREEN']['CELL_SIZE']) == self.body[0].y:
            return False
        elif aDirection == 'DD' and (self.head[0].y + SETTING2['SCREEN']['CELL_SIZE']) == self.body[0].y:
            return False
        elif aDirection == 'RR' and (self.head[0].x + SETTING2['SCREEN']['CELL_SIZE']) == self.body[0].x:
            return False
        elif aDirection == 'LL' and (self.head[0].x - SETTING2['SCREEN']['CELL_SIZE']) == self.body[0].x:
            return False
        return True
    
    ###########   Check if snake is eating food   ###########################################################
    def eatingFood(self, foodList):
        for food in foodList:
            if self.head[0].coordinate() == food.coordinate():
                foodList.remove(food)
                self.score += self.moveSpeed
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
            self.head[0].setCoordinate(self.head[0].x, 
                                       (self.head[0].y - SETTING2['SCREEN']['CELL_SIZE']) % HEIGHT)
        elif self.currentDirection == 'DD':
            self.head[0].setCoordinate(self.head[0].x, 
                                       (self.head[0].y + SETTING2['SCREEN']['CELL_SIZE']) % HEIGHT)
        elif self.currentDirection == 'RR':
            self.head[0].setCoordinate((self.head[0].x + SETTING2['SCREEN']['CELL_SIZE']) % WIDTH, 
                                       self.head[0].y)
        elif self.currentDirection == 'LL':
            self.head[0].setCoordinate((self.head[0].x - SETTING2['SCREEN']['CELL_SIZE']) % WIDTH, 
                                       self.head[0].y)
    
    ###########   Snake eat food, grow up and move   ########################################################
    def moveAndGrowUp(self):
        if self.currentDirection == None:
            return
        SETTING2['SOUND']['SNAKE_EAT_FOOD'].play()
        ########  Correct direction for head, body and tail  ################################################
        self.head[0].direction = self.head[0].direction[1] + self.currentDirection[0]
        newSnakeBlockDirection = self.head[0].direction
        ########  New Coordinate of snakeBlocks  ############################################################
        newSnakeBlockCoordinate = [self.head[0].x, self.head[0].y]
        if self.currentDirection == 'UU':
            self.head[0].setCoordinate(self.head[0].x, 
                                       (self.head[0].y - SETTING2['SCREEN']['CELL_SIZE']) % HEIGHT)
        elif self.currentDirection == 'DD':
            self.head[0].setCoordinate(self.head[0].x, 
                                       (self.head[0].y + SETTING2['SCREEN']['CELL_SIZE']) % HEIGHT)
        elif self.currentDirection == 'RR':
            self.head[0].setCoordinate((self.head[0].x + SETTING2['SCREEN']['CELL_SIZE']) % WIDTH, 
                                       self.head[0].y)
        elif self.currentDirection == 'LL':
            self.head[0].setCoordinate((self.head[0].x - SETTING2['SCREEN']['CELL_SIZE']) % WIDTH, 
                                       self.head[0].y)
        #######  Update new image for head, body and tail  ##################################################
        newSnakeBlockIndexFrame = self.head[0].indexFrame
        self.head[0].indexFrame = (self.head[0].indexFrame -1) % 7
        self.head[0].update('HEAD')
        newSnakeBlock = SnakeBlock(SNAKE['BODY'][newSnakeBlockDirection][newSnakeBlockIndexFrame], 
                                   x=newSnakeBlockCoordinate[0],
                                   y=newSnakeBlockCoordinate[1], direction=newSnakeBlockDirection, 
                                   indexFrame=self.head[0].indexFrame,
                                   typeColor=self.typeColor)
        self.body.insert(0, newSnakeBlock)
    
    ###########   Check if snake died, game over   ##########################################################
    def died(self, otherCoordinateSnakeBlocks=[], wallCoordinates=[]):
        if self.head[0].coordinate() in [snakeBlock.coordinate() for snakeBlock in (self.body + self.tail)]:
            return True
        if self.head[0].coordinate() in (otherCoordinateSnakeBlocks + wallCoordinates):
            return True
                
         
    ###########   Update snake displacement  ################################################################
    def updateLocation(self, foodList):
        if self.eatingFood(foodList):
            self.moveAndGrowUp()
        else:
            self.onlyMove()
        ###########   Remove old images   ###################################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new images   #####################################################################
        self.tail[0].draw(self.surface)
        for index in range(len(self.body) - 1, -1, -1):
            self.body[index].draw(self.surface)
        self.head[0].draw(self.surface)
        
    ###########   Update animation of snake   ###############################################################
    def updateAnimation(self):
        ###########   Update indexFrame of snakeBlocks   ####################################################
        self.head[0].indexFrame = (self.head[0].indexFrame - 1) % 7
        self.head[0].update('HEAD')
        for snakeBlock in self.body :
            snakeBlock.indexFrame = (snakeBlock.indexFrame - 1) % 7
            snakeBlock.update('BODY')
        self.tail[0].indexFrame = (self.tail[0].indexFrame - 1) % 7
        self.tail[0].update('TAIL')
        ###########   Remove old images   ###################################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new images   #####################################################################
        self.tail[0].draw(self.surface)
        for index in range(len(self.body) - 1, -1, -1):
            self.body[index].draw(self.surface)
        self.head[0].draw(self.surface)
    
    def correctCoordinate(self, by='x'):
        if by == 'x':
            for snakeBlock in (self.head + self.body + self.tail):
                tempCoordinate = snakeBlock.coordinate()
                if tempCoordinate[0] % CELL_SIZE != 0:
                    snakeBlock.setCoordinate(tempCoordinate[0]//CELL_SIZE*CELL_SIZE, tempCoordinate[1])
        elif by == 'y':
            for snakeBlock in (self.head + self.body + self.tail):
                tempCoordinate = snakeBlock.coordinate()
                if tempCoordinate[1] % CELL_SIZE != 0:
                    snakeBlock.setCoordinate(tempCoordinate[0], tempCoordinate[1]//CELL_SIZE*CELL_SIZE)
        elif by == 'xy':
            for snakeBlock in (self.head + self.body + self.tail):
                tempCoordinate = snakeBlock.coordinate()
                if tempCoordinate[0] % CELL_SIZE != 0 or tempCoordinate[1] % CELL_SIZE != 0:
                    snakeBlock.setCoordinate(tempCoordinate[0]//CELL_SIZE*CELL_SIZE, 
                                             tempCoordinate[1]//CELL_SIZE*CELL_SIZE)
    
    def isOverlap(self, x, y, coordinates=[]):
        if x > CELL_SIZE*(NUMBER_COLUMNS-1) or y > CELL_SIZE*(NUMBER_ROWS-1):
            return True
        for coordinate in coordinates:
            x0 = coordinate[0]
            y0 = coordinate[1]
            if ((x0-CELL_SIZE < x and x < x0+CELL_SIZE and y0-CELL_SIZE < y and y < y0+CELL_SIZE)):
                return True
        return False
    
    ###########   Snake drop   ##############################################################################
    def drop(self, otherSnakeCoordinateBlocks=[], wallCoordinateBlocks=[], dropType='0', positionMouse=(0,0)):
        if dropType == '0':
            self.correctCoordinate('xy')
            for snakeBlock in (self.head + self.body + self.tail):
                if [snakeBlock.x, snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE']] not in self.coordinateSnakeBlocks():
                    if [snakeBlock.x, snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE']] not in (
                        otherSnakeCoordinateBlocks + wallCoordinateBlocks):
                        if snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE'] < HEIGHT:
                            snakeBlock.setCoordinate(snakeBlock.x, snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE'])
                else:
                    if snakeBlock.x < WIDTH//2:
                        if [snakeBlock.x + SETTING2['SCREEN']['CELL_SIZE'], 
                            snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE']] not in self.coordinateSnakeBlocks():
                            if [snakeBlock.x + SETTING2['SCREEN']['CELL_SIZE'], 
                                snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE']] not in (
                                    otherSnakeCoordinateBlocks + wallCoordinateBlocks):
                                if snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE'] < HEIGHT:
                                    snakeBlock.setCoordinate(snakeBlock.x + SETTING2['SCREEN']['CELL_SIZE'], 
                                                            snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE'])
                        elif [snakeBlock.x - SETTING2['SCREEN']['CELL_SIZE'], 
                            snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE']] not in self.coordinateSnakeBlocks():
                            if [snakeBlock.x - SETTING2['SCREEN']['CELL_SIZE'], 
                            snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE']] not in (
                                otherSnakeCoordinateBlocks + wallCoordinateBlocks):
                                if (snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE'] < HEIGHT 
                                    and snakeBlock.x - SETTING2['SCREEN']['CELL_SIZE'] >= 0):
                                    snakeBlock.setCoordinate(snakeBlock.x - SETTING2['SCREEN']['CELL_SIZE'], 
                                                            snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE'])
                    else:
                        if [snakeBlock.x - SETTING2['SCREEN']['CELL_SIZE'], 
                            snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE']] not in self.coordinateSnakeBlocks():
                            if [snakeBlock.x - SETTING2['SCREEN']['CELL_SIZE'], 
                            snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE']] not in (
                                otherSnakeCoordinateBlocks + wallCoordinateBlocks):
                                if (snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE'] < HEIGHT 
                                    and snakeBlock.x - SETTING2['SCREEN']['CELL_SIZE'] >= 0):
                                    snakeBlock.setCoordinate(snakeBlock.x - SETTING2['SCREEN']['CELL_SIZE'], 
                                                            snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE'])
                        elif [snakeBlock.x + SETTING2['SCREEN']['CELL_SIZE'], 
                            snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE']] not in self.coordinateSnakeBlocks():
                            if [snakeBlock.x + SETTING2['SCREEN']['CELL_SIZE'], 
                            snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE']] not in (
                                otherSnakeCoordinateBlocks + wallCoordinateBlocks):
                                if snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE'] < HEIGHT:
                                    snakeBlock.setCoordinate(snakeBlock.x + SETTING2['SCREEN']['CELL_SIZE'], 
                                                            snakeBlock.y + SETTING2['SCREEN']['CELL_SIZE'])
        elif dropType == '1':
            x = positionMouse[0]//CELL_SIZE*CELL_SIZE
            y = positionMouse[1]//CELL_SIZE*CELL_SIZE
            self.correctCoordinate('xy')
            for snakeBlock in (self.head + self.body + self.tail):
                tempCoordinate = snakeBlock.coordinate()
                if tempCoordinate[0] == x:
                    continue
                x1 = tempCoordinate[0] + (x - tempCoordinate[0])//abs(tempCoordinate[0] - x)*CELL_SIZE
                y1 = tempCoordinate[1]
                if [x1, y1] not in (self.coordinateSnakeBlocks() 
                                    + otherSnakeCoordinateBlocks + wallCoordinateBlocks):
                    snakeBlock.setCoordinate(x1, y1)
        elif dropType == '2':
            x = positionMouse[0]
            y = positionMouse[1]
            for snakeBlock in (self.head + self.body + self.tail):
                tempCoordinate = snakeBlock.coordinate()
                if tempCoordinate[0] == x:
                    continue
                x1 = tempCoordinate[0] + (x-tempCoordinate[0])//abs(x-tempCoordinate[0])
                y1 = tempCoordinate[1]
                if not self.isOverlap(x1, y1, (self.coordinateSnakeBlocks(avoidCoordinates=[tempCoordinate]) 
                                    + otherSnakeCoordinateBlocks + wallCoordinateBlocks)):
                    snakeBlock.setCoordinate(x1, y1)
                
        elif dropType == '3':
            x = positionMouse[0]//CELL_SIZE*CELL_SIZE
            y = positionMouse[1]//CELL_SIZE*CELL_SIZE
            self.correctCoordinate('xy')
            for snakeBlock in (self.head + self.body + self.tail):
                tempCoordinate = snakeBlock.coordinate()
                if tempCoordinate[1] == y:
                    continue
                x1 = tempCoordinate[0] 
                y1 = tempCoordinate[1] + (y - tempCoordinate[1])//abs(tempCoordinate[1] - y)*CELL_SIZE
                if [x1, y1] not in (self.coordinateSnakeBlocks() + otherSnakeCoordinateBlocks + wallCoordinateBlocks):
                    snakeBlock.setCoordinate(x1, y1)    
        elif dropType == '4':
            x = positionMouse[0]
            y = positionMouse[1]
            for snakeBlock in (self.head + self.body + self.tail):
                tempCoordinate = snakeBlock.coordinate()
                if tempCoordinate[1] == y:
                    continue
                x1 = tempCoordinate[0]
                y1 = tempCoordinate[1] + (y-tempCoordinate[1])//abs(y-tempCoordinate[1])
                if not self.isOverlap(x1, y1, (self.coordinateSnakeBlocks(avoidCoordinates=[tempCoordinate]) 
                                    + otherSnakeCoordinateBlocks + wallCoordinateBlocks)):
                    snakeBlock.setCoordinate(x1, y1)
        elif dropType == '5':
            x = positionMouse[0]
            y = positionMouse[1]
            for snakeBlock in (self.head + self.body + self.tail):
                tempCoordinate = snakeBlock.coordinate()
                
                k = max(abs(x-tempCoordinate[0]), abs(y-tempCoordinate[1]))
                if k == 0:
                    continue
                x1 = tempCoordinate[0] + (x - tempCoordinate[0])//k
                y1 = tempCoordinate[1] + (y - tempCoordinate[1])//k
                if not self.isOverlap(x1, y1, (self.coordinateSnakeBlocks(avoidCoordinates=[tempCoordinate]) 
                                    + otherSnakeCoordinateBlocks + wallCoordinateBlocks)):
                    snakeBlock.setCoordinate(x1, y1)
        elif dropType == '6':
            x = positionMouse[0]
            y = positionMouse[1]
            for snakeBlock in (self.head + self.body + self.tail):
                tempCoordinate = snakeBlock.coordinate()
                
                k = min(abs(x-tempCoordinate[0]), abs(y-tempCoordinate[1]))
                if k == 0:
                    continue
                x1 = tempCoordinate[0] + (x - tempCoordinate[0])//k
                y1 = tempCoordinate[1] + (y - tempCoordinate[1])//k
                if [x1, y1] not in self.coordinateSnakeBlocks():
                    snakeBlock.setCoordinate(x1, y1)
        ###########   Remove old images   ###################################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new images   #####################################################################
        self.tail[0].draw(self.surface)
        for index in range(len(self.body) - 1, -1, -1):
            self.body[index].draw(self.surface)
        self.head[0].draw(self.surface)
    
    ###########   Draw snake on another surface   ###########################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)