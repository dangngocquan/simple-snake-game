import pygame
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
        self.snakeDropDependOnMouse = False
        ########### Buttons in Play Game Menu  ##############################################################
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
        
    ###########   Update cursor and buttons status in Game Over Menu   ######################################
    def update(self, type='UpdateTextAnimation', pos=(0,0)):
        ###########   Update animation of text   ############################################################
        if type == 'UpdateTextAnimation':
            ###########   Update cursor and buttons   #######################################################
            if self.cursor == 0:
                self.titlePlayAgain.isChosen = True
                self.titleBackMainMenu.isChosen = False
                self.titlePlayAgain.update("PLAY AGAIN", MEDIUM_FONT_HORVED)
                self.titleBackMainMenu.update("MAIN MENU", MEDIUM_FONT)
            elif self.cursor == 1:
                self.titlePlayAgain.isChosen = False
                self.titleBackMainMenu.isChosen = True
                self.titlePlayAgain.update("PLAY AGAIN", MEDIUM_FONT)
                self.titleBackMainMenu.update('MAIN MENU', MEDIUM_FONT_HORVED)
            if self.snake.score >= SETTING1['GAMEMODE']['TARGET_SCORE']:
                self.titleGameOver.update("<< YOU WON >>", BIG_FONT, color = 'ALL')
            else:
                self.titleGameOver.update("GAME OVER", BIG_FONT, color = 'ALL')
            self.titleScore.update(f"Your score: {self.snake.score}", MEDIUM_FONT_2)
            ###########   Remove old button display   #######################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ################################################################
            self.wallManager.draw(self.surface)
            self.snake.draw(self.surface)
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
                self.snake.drop(wallCoordinateBlocks=self.wallManager.coordinateWalls(), pos=pos)
            self.wallManager.draw(self.surface)
            self.snake.draw(self.surface)
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
            self.titleGameOver.draw(self.surface)
            self.titleTargetScore.draw(self.surface)
            self.titleScore.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        
    ###########  Draw PlayGame Menu in another surface  #####################################################
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
        self.winner = winner
        snake01Died = self.snake01.died(otherCoordinateSnakeBlocks=self.snake02.coordinateSnakeBlocks(),
                                        wallCoordinates=self.wallManager.coordinateWalls())
        snake02Died = self.snake02.died(otherCoordinateSnakeBlocks=self.snake01.coordinateSnakeBlocks(),
                                        wallCoordinates=self.wallManager.coordinateWalls())
        targetScoreReach01 = self.snake01.score >= SETTING1['GAMEMODE']['TARGET_SCORE']
        targetScoreReach02 = self.snake02.score >= SETTING1['GAMEMODE']['TARGET_SCORE']
        if self.winner == -1:
            if targetScoreReach01 and targetScoreReach02:
                self.winner = 3
            elif targetScoreReach01:
                self.winner = 1
            elif targetScoreReach02:
                self.winner = 2
            elif snake01Died and snake02Died:
                if self.snake01.score == self.snake02.score:
                    self.winner = 0
                elif self.snake01.score > self.snake02.score:
                    self.winner = 1
                elif self.snake01.score < self.snake02.score:
                    self.winner = 2
            elif snake01Died:
                self.winner = 2
            elif snake02Died:
                self.winner = 1
        ########### Buttons in Play Game Menu  ##############################################################
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
        self.titlePlayer01 = Button("PLAYER 01", MEDIUM_FONT_2, width//4, height*21//48)
        self.titlePlayer02 = Button("PLAYER 02", MEDIUM_FONT_2, width//4*3, height*21//48)
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
    ###########   Update cursor and buttons status in Game Over Menu   ######################################
    def update(self, type='UpdateTextAnimation'):
        ###########   Update animation of text   ############################################################
        if type == 'UpdateTextAnimation':
            ###########   Update cursor and buttons   #######################################################
            if self.cursor == 0:
                self.titlePlayAgain.isChosen = True
                self.titleBackMainMenu.isChosen = False
                self.titlePlayAgain.update("PLAY AGAIN", MEDIUM_FONT_HORVED)
                self.titleBackMainMenu.update("MAIN MENU", MEDIUM_FONT)
            elif self.cursor == 1:
                self.titlePlayAgain.isChosen = False
                self.titleBackMainMenu.isChosen = True
                self.titlePlayAgain.update("PLAY AGAIN", MEDIUM_FONT)
                self.titleBackMainMenu.update('MAIN MENU', MEDIUM_FONT_HORVED)
            self.titleGameOver.update("END MATCH", BIG_FONT, color='ALL')
            if self.winner == 1:
                self.titleStatusPlayer01.update("WINNER", MEDIUM_FONT_2, 'R')
                self.titlePlayer01.update("PLAYER 01", MEDIUM_FONT_2, 'R')
                self.titleScore01.update(f"Score: {self.snake01.score}", DESCRIPTION_FONT, 'R')
            elif self.winner == 2:
                self.titleStatusPlayer02.update("WINNER", MEDIUM_FONT_2, 'R')
                self.titlePlayer02.update("PLAYER 02", MEDIUM_FONT_2, 'R')
                self.titleScore02.update(f"Score: {self.snake02.score}", DESCRIPTION_FONT, 'R')
            elif self.winner == 3:
                self.titleStatusPlayer01.update("WINNER", MEDIUM_FONT_2, 'R')
                self.titlePlayer01.update("PLAYER 01", MEDIUM_FONT_2, 'R')
                self.titleScore01.update(f"Score: {self.snake01.score}", DESCRIPTION_FONT, 'R')
                self.titleStatusPlayer02.update("WINNER", MEDIUM_FONT_2, 'R')
                self.titlePlayer02.update("PLAYER 02", MEDIUM_FONT_2, 'R')
                self.titleScore02.update(f"Score: {self.snake02.score}", DESCRIPTION_FONT, 'R')
            ###########   Remove old button display   #######################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ################################################################
            self.wallManager.draw(self.surface)
            self.snake01.draw(self.surface)
            self.snake02.draw(self.surface)
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
                                  wallCoordinateBlocks=self.wallManager.coordinateWalls())
            if self.winner == 0 or self.winner == 1:
                self.snake02.drop(otherSnakeCoordinateBlocks=self.snake01.coordinateSnakeBlocks(),
                                  wallCoordinateBlocks=self.wallManager.coordinateWalls())
            self.wallManager.draw(self.surface)
            self.snake01.draw(self.surface)
            self.snake02.draw(self.surface)
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
            self.snake01.draw(self.surface)
            self.snake02.updateAnimation()
            self.snake02.draw(self.surface)
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
        
    ###########  Draw PlayGame Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)