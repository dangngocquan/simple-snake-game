import pygame
from account import ACCOUNT_MANAGER
from snake import Snake
from setting import *
import setting
from wall import Wall, WallManager
import wall
from grid import Grid
from grid import *
from button import Button

###########   VARIABLE   ####################################################################################
ANIMATION_SPEED = SETTING1['MENU']['ANIMATION_SPEED']
BIG_FONT = SETTING2['MENU']['BIG_FONT']
MEDIUM_FONT = SETTING2['MENU']['MEDIUM_FONT']
MEDIUM_FONT_HORVED = SETTING2['MENU']['MEDIUM_FONT_HORVED']
MEDIUM_FONT_2 = SETTING2['MENU']['MEDIUM_FONT_2']
SMALL_FONT = SETTING2['MENU']['SMALL_FONT']
DESCRIPTION_FONT = SETTING2['MENU']['DESCRIPTION_FONT']
WHITE = SETTING2['COLOR']['WHITE']


###########  CLASS GAME OVER MENU  ##########################################################################
class GameOverMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height, snake=Snake(), wallManager=WallManager()):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        self.snake = snake
        self.wallManager = wallManager
        self.dropType = '0'
        self.positionMouse = (-100, -100)
        self.positionLeftMouse = (-100, -100)
        
        ########### Buttons in Gameover Menu  ###############################################################
        self.titleDescription = Button("Press 0/1/2/3/4/5/6 to change the way snake drop", 
                                       DESCRIPTION_FONT_2, width//2, height*1//24)
        if self.snake.score >= SETTING1['GAMEMODE']['TARGET_SCORE']:
            self.titleGameOver = Button("<< YOU WON >>", BIG_FONT, width//2, height*3//12)
        else:
            self.titleGameOver = Button("GAME OVER", BIG_FONT, width//2, height*3//12)
        self.titleGameOver.isChosen = True
        self.titleTargetScore = Button(f"Target score: {SETTING1['GAMEMODE']['TARGET_SCORE']}", 
                                       MEDIUM_FONT_2, width//2, height*5//12)
        self.titleScore = Button(f"Your score: {self.snake.score}", MEDIUM_FONT_2, width//2, height*6//12)
       
        self.titlePlayAgain = Button("PLAY AGAIN", MEDIUM_FONT, width//2, height*8//12)
        self.titleBackMainMenu = Button("MAIN MENU", MEDIUM_FONT, width//2, height*10//12)
        
    
    ##################    Update current position of mouse    ###############################################
    def updatePositionMouse(self, position):
        self.positionMouse = position
    
    
    #############   Check if the mouse is poited at a surfaceRect   #########################################
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
    
    #############   Update text, button is horved by mouse   ################################################
    def updateMousePoitedAt(self):
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titlePlayAgain.textRect):
            self.titlePlayAgain.isChosen = True
            self.titlePlayAgain.update('PLAY AGAIN', MEDIUM_FONT_HORVED)
        else:
            self.titlePlayAgain.isChosen = False
            self.titlePlayAgain.update('PLAY AGAIN', MEDIUM_FONT)
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleBackMainMenu.textRect):
            self.titleBackMainMenu.isChosen = True
            self.titleBackMainMenu.update("MAIN MENU", MEDIUM_FONT_HORVED)
        else:
            self.titleBackMainMenu.isChosen = False
            self.titleBackMainMenu.update("MAIN MENU", MEDIUM_FONT)
    
    ###############     Update when player left-click    ####################################################
    def updatePositionLeftMouse(self):
        self.positionLeftMouse = self.positionMouse
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titlePlayAgain.textRect):
            self.cursor = 0
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleBackMainMenu.textRect):
            self.cursor = 1
        else:
            self.cursor = 2
        self.positionLeftMouse = (-100, -100)

        
    def updateDropType(self, dropType):
        self.dropType = dropType
    
    ###########   Update cursor and buttons status in Game Over Menu   ######################################
    def update(self, type='UpdateTextAnimation'):
        
        ###########   Update animation of text   ############################################################
        if type == 'UpdateTextAnimation':
            ###########   Update cursor and buttons   #######################################################
            self.updateMousePoitedAt()
            if self.snake.score >= SETTING1['GAMEMODE']['TARGET_SCORE']:
                self.titleGameOver.update("<< YOU WON >>", BIG_FONT, 'ALL')
            else:
                self.titleGameOver.update("GAME OVER", BIG_FONT, 'ALL')
            ###########   Remove old button display   #######################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ################################################################
            self.wallManager.draw(self.surface)
            self.snake.draw(self.surface)
            self.titleDescription.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleTargetScore.draw(self.surface)
            self.titleScore.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        ###########   Update location of snake when snake drop   ############################################
        elif type == 'UpdateSnakeDrop':
            ###########   Remove old button display   #######################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ################################################################
            if self.snake.score < SETTING1['GAMEMODE']['TARGET_SCORE']:
                self.snake.drop(wallCoordinateBlocks=self.wallManager.coordinateWalls(), 
                                dropType=self.dropType, positionMouse=self.positionMouse)
            self.wallManager.draw(self.surface)
            self.snake.draw(self.surface)
            self.titleDescription.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleTargetScore.draw(self.surface)
            self.titleScore.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        ###########   Update animation of snake   ###########################################################
        elif type == 'UpdateSnakeAnimation':
            ###########   Remove old button display   #######################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ################################################################
            self.snake.updateAnimation()
            self.wallManager.draw(self.surface)
            self.snake.draw(self.surface)
            self.titleDescription.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleTargetScore.draw(self.surface)
            self.titleScore.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        
    ###########  Draw Gameover Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
        

###########  CLASS GAME OVER MENU 02 ########################################################################
class GameOverMenu02:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height, snake01=Snake(), 
                 snake02=Snake(), winner=-1, wallManager=WallManager()):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        self.snake01 = snake01
        self.snake02 = snake02
        self.wallManager = wallManager
        self.dropType = '0'
        self.positionMouse = (-100,-100)
        self.positionLeftMouse = (-100, -100)
        self.winner = winner
        ########### Buttons in Gameover Menu  ###############################################################
        self.titleDescription = Button("Press 0/1/2/3/4/5/6 to change the way snake drop", 
                                       DESCRIPTION_FONT_2, width//2, height*1//24)
        self.titleGameOver = Button("END MATCH", BIG_FONT, width//2, height*2//12)
        self.titleGameOver.isChosen = True
        self.titleStatusPlayer01 = Button("LOSER", MEDIUM_FONT_2, width//4, height*4//12)
        self.titleStatusPlayer02 = Button("LOSER", MEDIUM_FONT_2, width//4*3, height*4//12)
        if self.winner == 0:
            self.titleStatusPlayer01 = Button("LOSER", MEDIUM_FONT_2, width//4, height*4//12)
            self.titleStatusPlayer02 = Button("LOSER", MEDIUM_FONT_2, width//4*3, height*4//12)
        elif self.winner == 1:
            self.titleStatusPlayer01 = Button("WINNER", MEDIUM_FONT_2, width//4, height*4//12)
            self.titleStatusPlayer02 = Button("LOSER", MEDIUM_FONT_2, width//4*3, height*4//12)
        elif self.winner == 2:
            self.titleStatusPlayer01 = Button("LOSER", MEDIUM_FONT_2, width//4, height*4//12)
            self.titleStatusPlayer02 = Button("WINNER", MEDIUM_FONT_2, width//4*3, height*4//12)
        elif self.winner == 3:
            self.titleStatusPlayer01 = Button("WINNER", MEDIUM_FONT_2, width//4, height*4//12)
            self.titleStatusPlayer02 = Button("WINNER", MEDIUM_FONT_2, width//4*3, height*4//12)
        self.titlePlayer01 = Button(f"{ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name}", 
                                    MEDIUM_FONT_2, width//4, height*21//48)
        self.titlePlayer02 = Button("OTHER PLAYER", MEDIUM_FONT_2, width//4*3, height*21//48)
        self.titleScore01 = Button(f"Score: {self.snake01.score}", DESCRIPTION_FONT, width//4, height*13//24)
        self.titleTargetScore = Button(f"Target Score: {SETTING1['GAMEMODE']['TARGET_SCORE']}", 
                                       DESCRIPTION_FONT, width//4*2, height*13//24)
        self.titleScore02 = Button(f"Score: {self.snake02.score}", DESCRIPTION_FONT, width//4*3, height*13//24)
        self.titlePlayAgain = Button("PLAY AGAIN", MEDIUM_FONT, width//2, height*16//24)
        self.titleBackMainMenu = Button("MAIN MENU", MEDIUM_FONT, width//2, height*19//24)
        
        self.titleStatusPlayer01.isChosen = True
        self.titleStatusPlayer02.isChosen = True
        self.titlePlayer01.isChosen = True
        self.titlePlayer02.isChosen = True 
        self.titleScore01.isChosen = True
        self.titleScore02.isChosen = True
        
    
    
    ##################    Update current position of mouse    ###############################################
    def updatePositionMouse(self, position):
        self.positionMouse = position
    
    
    #############   Check if the mouse is poited at a surfaceRect   #########################################
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
    
    #############   Update text, button is horved by mouse   ################################################
    def updateMousePoitedAt(self):
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titlePlayAgain.textRect):
            self.titlePlayAgain.isChosen = True
            self.titlePlayAgain.update('PLAY AGAIN', MEDIUM_FONT_HORVED)
        else:
            self.titlePlayAgain.isChosen = False
            self.titlePlayAgain.update('PLAY AGAIN', MEDIUM_FONT)
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleBackMainMenu.textRect):
            self.titleBackMainMenu.isChosen = True
            self.titleBackMainMenu.update("MAIN MENU", MEDIUM_FONT_HORVED)
        else:
            self.titleBackMainMenu.isChosen = False
            self.titleBackMainMenu.update("MAIN MENU", MEDIUM_FONT)
    
    ###############     Update when player left-click    ####################################################
    def updatePositionLeftMouse(self):
        self.positionLeftMouse = self.positionMouse
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titlePlayAgain.textRect):
            self.cursor = 0
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleBackMainMenu.textRect):
            self.cursor = 1
        else:
            self.cursor = 2
        self.positionLeftMouse = (-100, -100)
    
        
    def updateDropType(self, dropType):
        self.dropType = dropType
        
    ###########   Update cursor and buttons status in Game Over Menu   ######################################
    def update(self, type='UpdateTextAnimation'):
        ###########   Update animation of text   ############################################################
        if type == 'UpdateTextAnimation':
            ###########   Update cursor and buttons   #######################################################
            self.updateMousePoitedAt()
            self.titleGameOver.update("END MATCH", BIG_FONT, color='ALL')
            if self.winner == 1:
                self.titleStatusPlayer01.update("WINNER", MEDIUM_FONT_2, 'R')
                self.titlePlayer01.update(
                    f"{ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name}", 
                    MEDIUM_FONT_2, 'R')
                self.titleScore01.update(f"Score: {self.snake01.score}", DESCRIPTION_FONT, 'R')
            elif self.winner == 2:
                self.titleStatusPlayer02.update("WINNER", MEDIUM_FONT_2, 'R')
                self.titlePlayer02.update("OTHER PLAYER", MEDIUM_FONT_2, 'R')
                self.titleScore02.update(f"Score: {self.snake02.score}", DESCRIPTION_FONT, 'R')
            elif self.winner == 3:
                self.titleStatusPlayer01.update("WINNER", MEDIUM_FONT_2, 'R')
                self.titlePlayer01.update(
                    f"{ACCOUNT_MANAGER.listAccount[SETTING1['ACCOUNT']['INDEX_ACCOUNT']].name}", 
                    MEDIUM_FONT_2, 'R')
                self.titleScore01.update(f"Score: {self.snake01.score}", DESCRIPTION_FONT, 'R')
                self.titleStatusPlayer02.update("WINNER", MEDIUM_FONT_2, 'R')
                self.titlePlayer02.update("OTHER PLAYER", MEDIUM_FONT_2, 'R')
                self.titleScore02.update(f"Score: {self.snake02.score}", DESCRIPTION_FONT, 'R')
            ###########   Remove old button display   #######################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ################################################################
            self.wallManager.draw(self.surface)
            self.snake01.draw(self.surface)
            self.snake02.draw(self.surface)
            self.titleDescription.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleStatusPlayer01.draw(self.surface)
            self.titleStatusPlayer02.draw(self.surface)
            self.titlePlayer01.draw(self.surface)
            self.titlePlayer02.draw(self.surface)
            self.titleScore01.draw(self.surface)
            self.titleTargetScore.draw(self.surface)
            self.titleScore02.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        ###########   Update location of snake when snake drop   ############################################
        elif type == 'UpdateSnakeDrop':
            ###########   Remove old button display   #######################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ################################################################
            if self.winner == 0 or self.winner == 2:
                self.snake01.drop(otherSnakeCoordinateBlocks=self.snake02.coordinateSnakeBlocks(),
                                  wallCoordinateBlocks=self.wallManager.coordinateWalls(),
                                  dropType=self.dropType, positionMouse=self.positionMouse)
            if self.winner == 0 or self.winner == 1:
                self.snake02.drop(otherSnakeCoordinateBlocks=self.snake01.coordinateSnakeBlocks(),
                                  wallCoordinateBlocks=self.wallManager.coordinateWalls(),
                                  dropType=self.dropType, positionMouse=self.positionMouse)
            self.wallManager.draw(self.surface)
            self.snake01.draw(self.surface)
            self.snake02.draw(self.surface)
            self.titleDescription.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleStatusPlayer01.draw(self.surface)
            self.titleStatusPlayer02.draw(self.surface)
            self.titlePlayer01.draw(self.surface)
            self.titlePlayer02.draw(self.surface)
            self.titleScore01.draw(self.surface)
            self.titleTargetScore.draw(self.surface)
            self.titleScore02.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        ###########   Update animation of snake   ###########################################################
        elif type == 'UpdateSnakeAnimation':
            ###########   Remove old button display   #######################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ################################################################
            self.wallManager.draw(self.surface)
            self.snake01.updateAnimation()
            self.snake02.updateAnimation()
            if self.winner == 2:
                self.snake01.draw(self.surface)
                self.snake02.draw(self.surface)
            else:
                self.snake02.draw(self.surface)
                self.snake01.draw(self.surface)
            self.titleDescription.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleStatusPlayer01.draw(self.surface)
            self.titleStatusPlayer02.draw(self.surface)
            self.titlePlayer01.draw(self.surface)
            self.titlePlayer02.draw(self.surface)
            self.titleScore01.draw(self.surface)
            self.titleTargetScore.draw(self.surface)
            self.titleScore02.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        
    ###########  Draw Gameover Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)