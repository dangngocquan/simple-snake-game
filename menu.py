import random
import pygame
from snake import Snake
from setting import *
import setting

###########   VARIABLE   ####################################################################################
ANIMATION_SPEED = SETTING1['MENU']['ANIMATION_SPEED']
BIG_FONT = SETTING2['MENU']['BIG_FONT']
MEDIUM_FONT = SETTING2['MENU']['MEDIUM_FONT']
MEDIUM_FONT_HORVED = SETTING2['MENU']['MEDIUM_FONT_HORVED']
MEDIUM_FONT_2 = SETTING2['MENU']['MEDIUM_FONT_2']
SMALL_FONT = SETTING2['MENU']['SMALL_FONT']
DESCRIPTION_FONT = SETTING2['MENU']['DESCRIPTION_FONT']
WHITE = SETTING2['COLOR']['WHITE']

###########  CLASS BUTTON  ##################################################################################
class Button:
    ###########  Constructor  ###############################################################################
    def __init__(self, text, font, x, y, typeLocation='center'):
        self.text = font.render(text, True, WHITE, None)
        self.textRect = self.text.get_rect()
        self.typeLocation = typeLocation
        if self.typeLocation == 'center':
            self.textRect.center = (x, y)
        elif self.typeLocation == 'topLeft':
            self.textRect.topleft = (x, y)
        self.x = x
        self.y = y
        self.isChosen = False
        self.valueR = 255
        self.valueG = 255
        self.valueB = 255
        self.valueRStatus = 1
        self.valueGStatus = 1
        self.valueBStatus = 1
    
    ###########  Update text, font, coordinate and color of Button  #########################################
    def update(self, text, font, color='G'):
        ###########  Update text, font, coordinate   ########################################################
        self.text = font.render(text, True, WHITE, None)
        self.textRect = self.text.get_rect()
        if self.typeLocation == 'center':
            self.textRect.center = (self.x, self.y)
        elif self.typeLocation == 'topLeft':
            self.textRect.topleft = (self.x, self.y)
        ###########  Update color   #########################################################################
        if self.isChosen:
            if color == 'R':
                self.valueG += 51 * self.valueGStatus
                self.valueB += 51 * self.valueBStatus
            elif color == 'G':
                self.valueR += 51 * self.valueRStatus
                self.valueB += 51 * self.valueBStatus
            elif color == 'B':
                self.valueR += 51 * self.valueRStatus
                self.valueG += 51 * self.valueGStatus
            elif color == 'ALL':
                self.valueR += random.randint(-25, 25)
                self.valueG += random.randint(-25, 25)
                self.valueB += random.randint(-25, 25)
            if self.valueR < 0:
                self.valueR = - self.valueR
                self.valueRStatus = 1
            elif self.valueR > 255:
                self.valueR = 510 - self.valueR
                self.valueRStatus = -1
            if self.valueG < 0:
                self.valueG = - self.valueG
                self.valueGStatus = 1
            elif self.valueG > 255:
                self.valueG = 510 - self.valueG
                self.valueGStatus = -1
            if self.valueB < 0:
                self.valueB = - self.valueB
                self.valueBStatus = 1
            elif self.valueB > 255:
                self.valueB = 510 - self.valueB
                self.valueBStatus = -1
                
            self.text = font.render(text, True, (self.valueR, self.valueG, self.valueB), None)
        else:
            self.valueR = 255
            self.valueG = 255
            self.valueB = 255
            self.text = font.render(text, True, (self.valueR, self.valueG, self.valueB), None)
            
    ###########  Draw button in another surface  ############################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.text, self.textRect)
  
        
###########  CLASS MAIN MENU  ###############################################################################
class MainMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor   ######################################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        ########### Buttons   ###############################################################################
        self.titleSimpleSnake = Button("SIMPLE SNAKE", BIG_FONT, width//2, height//6)
        self.titleSimpleSnake.isChosen = True
        self.titlePlayGame = Button("PLAY GAME", MEDIUM_FONT, width//2, height*5//12)
        self.titleOptions = Button("OPTIONS", MEDIUM_FONT, width//2, height*7//12)
        self.titleQuitGame = Button("QUIT GAME", MEDIUM_FONT, width//2, height*9//12)
        
    ###########  Update cursor and button status in Main Menu ###############################################
    def update(self):
        ###########  Update cursor and button of main menu  #################################################
        if self.cursor == 0:
            self.titlePlayGame.isChosen = True
            self.titleOptions.isChosen = False
            self.titleQuitGame.isChosen = False
            self.titleSimpleSnake.update('SIMPLE SNAKE', BIG_FONT, 'ALL')
            self.titlePlayGame.update('PLAY GAME', MEDIUM_FONT_HORVED)
            self.titleOptions.update('OPTIONS', MEDIUM_FONT)
            self.titleQuitGame.update('QUIT GAME', MEDIUM_FONT)
        elif self.cursor == 1:
            self.titlePlayGame.isChosen = False
            self.titleOptions.isChosen = True
            self.titleQuitGame.isChosen = False
            self.titleSimpleSnake.update('SIMPLE SNAKE', BIG_FONT, 'ALL')
            self.titlePlayGame.update('PLAY GAME', MEDIUM_FONT)
            self.titleOptions.update('OPTIONS', MEDIUM_FONT_HORVED)
            self.titleQuitGame.update('QUIT GAME', MEDIUM_FONT)
        elif self.cursor == 2:
            self.titlePlayGame.isChosen = False
            self.titleOptions.isChosen = False
            self.titleQuitGame.isChosen = True
            self.titleSimpleSnake.update('SIMPLE SNAKE', BIG_FONT, 'ALL')
            self.titlePlayGame.update('PLAY GAME', MEDIUM_FONT)
            self.titleOptions.update('OPTIONS', MEDIUM_FONT)
            self.titleQuitGame.update('QUIT GAME', MEDIUM_FONT_HORVED)
        ###########  Remove old button display  #############################################################
        self.surface.fill((0, 0, 0, 0))
        ###########  Draw new button   ######################################################################
        self.titleSimpleSnake.draw(self.surface)
        self.titlePlayGame.draw(self.surface)
        self.titleOptions.draw(self.surface)
        self.titleQuitGame.draw(self.surface)
    
    ###########  Draw Main Menu in another surface  #########################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        

###########  CLASS PLAY GAME MENU  ##########################################################################
class PlayGameMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        ########### Buttons in Play Game Menu  ##############################################################
        self.titleNewGame = Button("NEW GAME", MEDIUM_FONT, width//2, height*4//12)
        self.titleContinueGame = Button("CONTINUE GAME", MEDIUM_FONT, width//2, height*6//12)
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*8//12)
        
    ###########   Update cursor and buttons status in Play Game Menu   ######################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleNewGame.isChosen = True
            self.titleContinueGame.isChosen = False
            self.titleBack.isChosen = False
            self.titleNewGame.update('NEW GAME', MEDIUM_FONT_HORVED)
            self.titleContinueGame.update('CONTINUE GAME', MEDIUM_FONT)
            self.titleBack.update('BACK', MEDIUM_FONT)
        elif self.cursor == 1:
            self.titleNewGame.isChosen = False
            self.titleContinueGame.isChosen = True
            self.titleBack.isChosen = False
            self.titleNewGame.update('NEW GAME', MEDIUM_FONT)
            self.titleContinueGame.update('CONTINUE GAME', MEDIUM_FONT_HORVED)
            self.titleBack.update('BACK', MEDIUM_FONT)
        elif self.cursor == 2:
            self.titleNewGame.isChosen = False
            self.titleContinueGame.isChosen = False
            self.titleBack.isChosen = True
            self.titleNewGame.update('NEW GAME', MEDIUM_FONT)
            self.titleContinueGame.update('CONTINUE GAME', MEDIUM_FONT)
            self.titleBack.update('BACK', MEDIUM_FONT_HORVED)
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
        self.titleNewGame.draw(self.surface)
        self.titleContinueGame.draw(self.surface)
        self.titleBack.draw(self.surface)
    
    ###########  Draw PlayGame Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
       
        
###########  CLASS OPTIONS MENU  ##########################################################################
class OptionsMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        ########### Buttons in Options Menu  ##############################################################
        self.titleGameSetting = Button("GAME SETTING", MEDIUM_FONT, width//2, height*1//4)
        self.titleSoundSetting = Button("SOUND SETTING", MEDIUM_FONT, width//2, height*2//4)
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*3//4)
        
    ###########   Update cursor and buttons status in Options Menu   ########################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleGameSetting.isChosen = True
            self.titleGameSetting.update('GAME SETTING', MEDIUM_FONT_HORVED, 'G')
            self.titleSoundSetting.update('SOUND SETTING', MEDIUM_FONT, 'G')
            self.titleBack.update('BACK', MEDIUM_FONT, 'G')
        else:
            self.titleGameSetting.isChosen = False
        if self.cursor == 1:
            self.titleSoundSetting.isChosen = True
            self.titleGameSetting.update('GAME SETTING', MEDIUM_FONT, 'G')
            self.titleSoundSetting.update('SOUND SETTING', MEDIUM_FONT_HORVED, 'G')
            self.titleBack.update('BACK', MEDIUM_FONT, 'G')
        else:
            self.titleSoundSetting.isChosen = False
        if self.cursor == 2:
            self.titleBack.isChosen = True
            self.titleGameSetting.update('GAME SETTING', MEDIUM_FONT, 'G')
            self.titleSoundSetting.update('SOUND SETTING', MEDIUM_FONT, 'G')
            self.titleBack.update('BACK', MEDIUM_FONT_HORVED, 'G')
        else:
            self.titleBack.isChosen = False
        
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
        self.titleGameSetting.draw(self.surface)
        self.titleSoundSetting.draw(self.surface)
        self.titleBack.draw(self.surface)
        
    ###########  Draw Options Menu in another surface  ######################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
   

###########  CLASS GAME SETTING MENU  #######################################################################
class GameSettingMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 12
        ########### Buttons in Game Setting Menu  ###########################################################
        self.descriptionText = Button("", SMALL_FONT, width//2, height*1//17)
        self.descriptionText.isChosen = True
        self.titleGridSetting= Button("GRID SETTING", SMALL_FONT, width//2, height*3//17)
        self.titleGrid= Button("Show grid", SMALL_FONT, width//6, height*4//17, 'topLeft')
        self.titleGridOptions= Button(f"{SETTING1['GRID']}", SMALL_FONT, 
                                      width//6*5, height*4//17, 'topLeft')
        self.titleSnakeSetting= Button("SNAKE SETTING", SMALL_FONT, width//2, height*6//17)
        self.titleSnakeMoveSpeed = Button("Move Speed", SMALL_FONT, width//6, height*7//17, 'topLeft')
        self.titleSnakeMoveSpeedOptions = Button(f"{SETTING1['SNAKE']['MOVE_SPEED']}", SMALL_FONT, 
                                                 width//6*5, height*7//17, 'topLeft')
        self.titleSnakeDropSpeed = Button("Drop Speed (when snake died)", SMALL_FONT, 
                                          width//6, height*8//17, 'topLeft')
        self.titleSnakeDropSpeedOptions = Button(f"{SETTING1['SNAKE']['DROP_SPEED']}", SMALL_FONT, 
                                                 width//6*5, height*8//17, 'topLeft')
        self.titleSnakeAnimationSpeed = Button("Animation Speed", SMALL_FONT, 
                                               width//6, height*9//17, 'topLeft')
        self.titleSnakeAnimationSpeedOptions = Button(f"{SETTING1['SNAKE']['ANIMATION_SPEED']}", SMALL_FONT, 
                                                      width//6*5, height*9//17, 'topLeft')
        self.titleFoodSetting = Button("FOOD SETTING", SMALL_FONT, width//2, height*11//17)
        self.titleFoodMax = Button("Max Food", SMALL_FONT, width//6, height*12//17, 'topLeft')
        self.titleFoodMaxOptions = Button(f"{SETTING1['FOOD']['MAX_FOOD']}", SMALL_FONT, 
                                          width//6*5, height*12//17, 'topLeft')
        self.titleFoodAnimationSpeed = Button("Animation Speed", SMALL_FONT, 
                                              width//6, height*13//17, 'topLeft')
        self.titleFoodAnimationSpeedOptions = Button(f"{SETTING1['FOOD']['ANIMATION_SPEED']}", SMALL_FONT, 
                                                     width//6*5, height*13//17, 'topLeft')
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*15//17)
        
    ###########   Update cursor and buttons status in Game Setting Menu   ###################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleGrid.isChosen = True
            self.descriptionText.update('Press ENTER to setup the grid', SMALL_FONT, 'ALL')
        else:
            self.titleGrid.isChosen = False
        if self.cursor == 1:
            self.titleGridOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        SMALL_FONT, 'ALL')
        else:
            self.titleGridOptions.isChosen = False
        if self.cursor == 2:
            self.titleSnakeMoveSpeed.isChosen = True
            self.descriptionText.update('Press ENTER to setup the move speed of snake', SMALL_FONT, 'ALL')
        else:
            self.titleSnakeMoveSpeed.isChosen = False
        if self.cursor == 3:
            self.titleSnakeMoveSpeedOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        SMALL_FONT, 'ALL')
        else:
            self.titleSnakeMoveSpeedOptions.isChosen = False
        if self.cursor == 4:
            self.titleSnakeDropSpeed.isChosen = True
            self.descriptionText.update('Press ENTER to setup the drop speed of snake', SMALL_FONT, 'ALL')
        else:
            self.titleSnakeDropSpeed.isChosen = False
        if self.cursor == 5:
            self.titleSnakeDropSpeedOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        SMALL_FONT, 'ALL')
        else:
            self.titleSnakeDropSpeedOptions.isChosen = False
        if self.cursor == 6:
            self.titleSnakeAnimationSpeed.isChosen = True
            self.descriptionText.update('Press ENTER to setup the animation speed of snake', SMALL_FONT, 'ALL')
        else:
            self.titleSnakeAnimationSpeed.isChosen = False
        if self.cursor == 7:
            self.titleSnakeAnimationSpeedOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        SMALL_FONT, 'ALL')
        else:
            self.titleSnakeAnimationSpeedOptions.isChosen = False
        if self.cursor == 8:
            self.titleFoodMax.isChosen = True
            self.descriptionText.update('Press ENTER to setup the max number of food', SMALL_FONT, 'ALL')
        else:
            self.titleFoodMax.isChosen = False
        if self.cursor == 9:
            self.titleFoodMaxOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        SMALL_FONT, 'ALL')
        else:
            self.titleFoodMaxOptions.isChosen = False
        if self.cursor == 10:
            self.titleFoodAnimationSpeed.isChosen = True
            self.descriptionText.update('Press ENTER to setup the animation speed of food', SMALL_FONT, 'ALL')
        else:
            self.titleFoodAnimationSpeed.isChosen = False
        if self.cursor == 11:
            self.titleFoodAnimationSpeedOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        SMALL_FONT, 'ALL')
        else:
            self.titleFoodAnimationSpeedOptions.isChosen = False
        if self.cursor == 12:
            self.titleBack.isChosen = True
            self.titleBack.update('BACK', MEDIUM_FONT_HORVED)
            self.descriptionText.update('', SMALL_FONT, 'ALL')
        else:
            self.titleBack.isChosen = False
            self.titleBack.update('BACK', MEDIUM_FONT)
            
        self.titleGrid.update('Show grid', SMALL_FONT, 'B')
        self.titleGridOptions.update(f"{SETTING1['GRID']}", SMALL_FONT, 'B')
        self.titleSnakeMoveSpeed.update("Move speed", SMALL_FONT, 'B')
        self.titleSnakeMoveSpeedOptions.update(f"{SETTING1['SNAKE']['MOVE_SPEED']}", 
                                               SMALL_FONT, 'B')
        self.titleSnakeDropSpeed.update("Drop speed", SMALL_FONT, 'B')
        self.titleSnakeDropSpeedOptions.update(f"{SETTING1['SNAKE']['DROP_SPEED']}", 
                                               SMALL_FONT, 'B')
        self.titleSnakeAnimationSpeed.update('Animation speed', SMALL_FONT, 'B')
        self.titleSnakeAnimationSpeedOptions.update(f"{SETTING1['SNAKE']['ANIMATION_SPEED']}", 
                                                    SMALL_FONT, 'B')
        self.titleFoodMax.update('Max food', SMALL_FONT, 'B')
        self.titleFoodMaxOptions.update(f"{SETTING1['FOOD']['MAX_FOOD']}", SMALL_FONT, 'B')
        self.titleFoodAnimationSpeed.update('Animation speed', SMALL_FONT, 'B')
        self.titleFoodAnimationSpeedOptions.update(f"{SETTING1['FOOD']['ANIMATION_SPEED']}", 
                                                   SMALL_FONT, 'B')
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
        self.descriptionText.draw(self.surface)
        self.titleGridSetting.draw(self.surface)
        self.titleGrid.draw(self.surface)
        self.titleGridOptions.draw(self.surface)
        self.titleSnakeSetting.draw(self.surface)
        self.titleSnakeMoveSpeed.draw(self.surface)
        self.titleSnakeMoveSpeedOptions.draw(self.surface)
        self.titleSnakeDropSpeed.draw(self.surface)
        self.titleSnakeDropSpeedOptions.draw(self.surface)
        self.titleSnakeAnimationSpeed.draw(self.surface)
        self.titleSnakeAnimationSpeedOptions.draw(self.surface)
        self.titleFoodSetting.draw(self.surface)
        self.titleFoodMax.draw(self.surface)
        self.titleFoodMaxOptions.draw(self.surface)
        self.titleFoodAnimationSpeed.draw(self.surface)
        self.titleFoodAnimationSpeedOptions.draw(self.surface)
        self.titleBack.draw(self.surface)
    
    ###########  Draw Game Setting Menu in another surface  #################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
   
   
###########  CLASS SOUND SETTING MENU  ######################################################################
class SoundSettingMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        ########### Buttons in Options Menu  ##############################################################
        self.descriptionText = Button("", SMALL_FONT, width//2, height*1//12)
        self.descriptionText.isChosen = True
        self.titleMusicSetting = Button("MUSIC SETTING", SMALL_FONT, width//2, height*3//12)
        self.titleMusic = Button("Music", SMALL_FONT, width//6, height*4//12, 'topLeft')
        self.titleMusicOptions = Button(f"Music {SETTING1['SOUND']['MUSIC_INDEX']}", SMALL_FONT,
                                        width//6*5, height*4//12, 'topLeft')
        self.titleMusicVolume = Button("Music volume", SMALL_FONT, width//6, height*5//12, 'topLeft')
        self.titleMusicVolumeOptions = Button(f"{SETTING1['SOUND']['MUSIC_VOLUME']}", SMALL_FONT,
                                              width//6*5, height*5//12, 'topLeft')
        self.titleSoundSetting = Button("SOUND SETTING", SMALL_FONT, width//2, height*7//12)
        self.titleSoundVolume =  Button("Sound volume", SMALL_FONT, width//6, height*8//12, 'topLeft')
        self.titleSoundVolumeOptions = Button(f"{SETTING1['SOUND']['SOUND_VOLUME']}", SMALL_FONT,
                                              width//6*5, height*8//12, 'topLeft')
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*10//12)
        
    ###########   Update cursor and buttons status in Options Menu   ########################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleMusic.isChosen = True
            self.descriptionText.update('Press ENTER to choose the music for game', SMALL_FONT, 'ALL')
        else:
            self.titleMusic.isChosen = False
        if self.cursor == 1:
            self.titleMusicOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        SMALL_FONT, 'ALL')
        else:
            self.titleMusicOptions.isChosen = False
        if self.cursor == 2:
            self.titleMusicVolume.isChosen = True
            self.descriptionText.update('Press ENTER to set volume of music', SMALL_FONT, 'ALL')
        else:
            self.titleMusicVolume.isChosen = False
        if self.cursor == 3:
            self.titleMusicVolumeOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        SMALL_FONT, 'ALL')
        else:
            self.titleMusicVolumeOptions.isChosen = False
        if self.cursor == 4:
            self.titleSoundVolume.isChosen = True
            self.descriptionText.update('Press ENTER to set volume of sound', SMALL_FONT, 'ALL')
        else:
            self.titleSoundVolume.isChosen = False
        if self.cursor == 5:
            self.titleSoundVolumeOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        SMALL_FONT, 'ALL')
        else:
            self.titleSoundVolumeOptions.isChosen = False
        if self.cursor == 6:
            self.titleBack.isChosen = True
            self.titleBack.update("BACK", MEDIUM_FONT_HORVED)
            self.descriptionText.update("", SMALL_FONT, 'ALL')
        else:
            self.titleBack.isChosen = False
            self.titleBack.update("BACK", MEDIUM_FONT)
        
        self.titleMusic.update("Music", SMALL_FONT, 'B')
        self.titleMusicOptions.update(f"Music {SETTING1['SOUND']['MUSIC_INDEX']}", SMALL_FONT, 'B')
        self.titleMusicVolume.update("Music volume", SMALL_FONT, 'B')
        self.titleMusicVolumeOptions.update(f"{SETTING1['SOUND']['MUSIC_VOLUME']}", SMALL_FONT, 'B')
        self.titleSoundVolume.update("Sound volume", SMALL_FONT, 'B')
        self.titleSoundVolumeOptions.update(f"{SETTING1['SOUND']['SOUND_VOLUME']}", SMALL_FONT, 'B')
        
        ###########   Remove old button display   ###########################################################
        self.surface.fill((0, 0, 0, 0))
        ###########   Draw new buttons   ####################################################################
        self.descriptionText.draw(self.surface)
        self.titleMusicSetting.draw(self.surface)
        self.titleMusic.draw(self.surface)
        self.titleMusicOptions.draw(self.surface)
        self.titleMusicVolume.draw(self.surface)
        self.titleMusicVolumeOptions.draw(self.surface)
        self.titleSoundSetting.draw(self.surface)
        self.titleSoundVolume.draw(self.surface)
        self.titleSoundVolumeOptions.draw(self.surface)
        self.titleBack.draw(self.surface)
        
    ###########  Draw Options Menu in another surface  ######################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
  
        
###########  CLASS GAME OVER MENU  ##########################################################################
class GameOverMenu:
    ###########  Constructor  ###############################################################################
    def __init__(self, x, y, width, height, snake=Snake()):
        ###########  Surface, cursor and coordinate center  #################################################
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.surfaceRect = self.surface.get_rect()
        self.surfaceRect.center = (x, y)
        self.FPS = ANIMATION_SPEED
        self.cursor = 0
        self.snake = snake
        ########### Buttons in Play Game Menu  ##############################################################
        self.titleGameOver = Button("GAME OVER", BIG_FONT, width//2, height*3//12)
        self.titleScore = Button(f"Your score: {self.snake.score}", MEDIUM_FONT_2, width//2, height*5//12)
        self.titlePlayAgain = Button("PLAY AGAIN", MEDIUM_FONT, width//2, height*7//12)
        self.titleBackMainMenu = Button("MAIN MENU", MEDIUM_FONT, width//2, height*9//12)
        
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
            ###########   Remove old button display   #######################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ################################################################
            self.titleScore.update(f"Your score: {self.snake.score}", MEDIUM_FONT_2)
            self.snake.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleScore.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        ###########   Update location of snake when snake drop   ############################################
        elif type == 'UpdateSnakeDrop':
            ###########   Remove old button display   #######################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ################################################################
            self.snake.drop()
            self.snake.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleScore.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        ###########   Update animation of snake   ###########################################################
        elif type == 'UpdateSnakeAnimation':
            ###########   Remove old button display   #######################################################
            self.surface.fill((0, 0, 0, 0))
            ###########   Draw new buttons   ################################################################
            self.snake.updateAnimation()
            self.snake.draw(self.surface)
            self.titleGameOver.draw(self.surface)
            self.titleScore.draw(self.surface)
            self.titlePlayAgain.draw(self.surface)
            self.titleBackMainMenu.draw(self.surface)
        
    ###########  Draw PlayGame Menu in another surface  #####################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)
        
        
    
        
        
        