import pygame
from setting import *
import setting
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
        self.positionMouse = (-100, -100)
        self.positionLeftMouse = (-100, -100)
        ########### Buttons in Sound Setting Menu  ##########################################################
        self.descriptionText = Button("", DESCRIPTION_FONT, width//2, height*1//12)
        self.descriptionText.isChosen = True
        self.titleMusicSetting = Button("MUSIC SETTING", MEDIUM_FONT_2, width//2, height*3//12)
        self.titleMusic = Button("Music", SMALL_FONT, width//8, height*4//12, 'topLeft')
        self.titleMusicOptions = Button(f"Music {SETTING1['SOUND']['MUSIC_INDEX']}", SMALL_FONT,
                                        width//16*13, height*4//12, 'topLeft')
        self.titleMusicVolume = Button("Music volume", SMALL_FONT, width//8, height*5//12, 'topLeft')
        self.titleMusicVolumeOptions = Button(f"{SETTING1['SOUND']['MUSIC_VOLUME']}", SMALL_FONT,
                                              width//16*13, height*5//12, 'topLeft')
        self.titleSoundSetting = Button("SOUND SETTING", MEDIUM_FONT_2, width//2, height*7//12)
        self.titleSoundVolume =  Button("Sound volume", SMALL_FONT, width//8, height*8//12, 'topLeft')
        self.titleSoundVolumeOptions = Button(f"{SETTING1['SOUND']['SOUND_VOLUME']}", SMALL_FONT,
                                              width//16*13, height*8//12, 'topLeft')
        self.titleBack = Button("BACK", MEDIUM_FONT, width//2, height*10//12)
    
    
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
        if self.cursor != 0:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleMusic.textRect):
                self.titleMusic.isChosen = True
            else:
                self.titleMusic.isChosen = False
            self.titleMusic.update("Music", DESCRIPTION_FONT)
        if self.cursor != 1:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleMusicOptions.textRect):
                self.titleMusicOptions.isChosen = True
            else:
                self.titleMusicOptions.isChosen = False
            self.titleMusicOptions.update(f"Music {SETTING1['SOUND']['MUSIC_INDEX']}", DESCRIPTION_FONT)
        if self.cursor != 2:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleMusicVolume.textRect):
                self.titleMusicVolume.isChosen = True
            else:
                self.titleMusicVolume.isChosen = False
            self.titleMusicVolume.update("Music volume", DESCRIPTION_FONT) 
        if self.cursor != 3:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleMusicVolumeOptions.textRect):
                self.titleMusicVolumeOptions.isChosen = True
            else:
                self.titleMusicVolumeOptions.isChosen = False
            self.titleMusicVolumeOptions.update(f"{SETTING1['SOUND']['MUSIC_VOLUME']}", DESCRIPTION_FONT)
        if self.cursor != 4:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleSoundVolume.textRect):
                self.titleSoundVolume.isChosen = True
            else:
                self.titleSoundVolume.isChosen = False
            self.titleSoundVolume.update("Sound volume", DESCRIPTION_FONT) 
        if self.cursor != 5:
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleSoundVolumeOptions.textRect):
                self.titleSoundVolumeOptions.isChosen = True
            else:
                self.titleSoundVolumeOptions.isChosen = False
            self.titleSoundVolumeOptions.update(f"{SETTING1['SOUND']['SOUND_VOLUME']}", DESCRIPTION_FONT) 
        if self.cursor != 6:   
            if self.isPointedAt(positionMouse=self.positionMouse,
                                surfaceCheckRect=self.titleBack.textRect):
                self.titleBack.isChosen = True
                self.titleBack.update('BACK', MEDIUM_FONT_HORVED, 'G')
            else:
                self.titleBack.isChosen = False
                self.titleBack.update('BACK', MEDIUM_FONT, 'G')
    
    ###############     Update when player left-click    ####################################################
    def updatePositionLeftMouse(self):
        self.positionLeftMouse = self.positionMouse
        if self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleMusic.textRect):
            self.cursor = 0
            self.titleMusic.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleMusicOptions.textRect):
            self.cursor = 1
            self.titleMusicOptions.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleMusicVolume.textRect):
            self.cursor = 2
            self.titleMusicVolume.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleMusicVolumeOptions.textRect):
            self.cursor = 3
            self.titleMusicVolumeOptions.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleSoundVolume.textRect):
            self.cursor = 4
            self.titleSoundVolume.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleSoundVolumeOptions.textRect):
            self.cursor = 5
            self.titleSoundVolumeOptions.isChosen = True
            SETTING2['SOUND']['PRESS_BUTTON'].play()
        elif self.isPointedAt(positionMouse=self.positionMouse,
                            surfaceCheckRect=self.titleBack.textRect):
            self.cursor = 6
            self.titleBack.isChosen = True
        else:
            self.cursor = 7
        self.positionLeftMouse = (-100, -100)
      
    ###########   Update cursor and buttons status in Sound Setting Menu   ##################################
    def update(self):
        self.updateMousePoitedAt()
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleMusic.update("Music", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Setup the music for game.", DESCRIPTION_FONT, 'R')
        else:
            self.titleMusic.update("Music", DESCRIPTION_FONT, 'G')    
        if self.cursor == 1:
            self.titleMusicOptions.update(f"Music {SETTING1['SOUND']['MUSIC_INDEX']}", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Wheel-up or wheel-down to change your choice", 
                                        DESCRIPTION_FONT_2, 'R')
        else:
            self.titleMusicOptions.update(f"Music {SETTING1['SOUND']['MUSIC_INDEX']}", DESCRIPTION_FONT, 'G')
        if self.cursor == 2:
            self.titleMusicVolume.update("Music volume", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Setup the volume of music in game.", DESCRIPTION_FONT, 'R')
        else:
            self.titleMusicVolume.update("Music volume", DESCRIPTION_FONT, 'G')
        if self.cursor == 3:
            self.titleMusicVolumeOptions.update(f"{SETTING1['SOUND']['MUSIC_VOLUME']}", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Wheel-up or wheel-down to change your choice", 
                                        DESCRIPTION_FONT_2, 'R')
        else:
            self.titleMusicVolumeOptions.update(f"{SETTING1['SOUND']['MUSIC_VOLUME']}", DESCRIPTION_FONT, 'G')
        if self.cursor == 4:
            self.titleSoundVolume.update("Sound volume", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Setup the volume of the sound in game.", DESCRIPTION_FONT_2, 'R')
        else:
            self.titleSoundVolume.update("Sound volume", DESCRIPTION_FONT, 'G')
        if self.cursor == 5:
            self.titleSoundVolumeOptions.update(f"{SETTING1['SOUND']['SOUND_VOLUME']}", DESCRIPTION_FONT, 'B')
            self.descriptionText.update("Wheel-up or wheel-down to change your choice", 
                                        DESCRIPTION_FONT_2, 'R')
        else:
            self.titleSoundVolumeOptions.update(f"{SETTING1['SOUND']['SOUND_VOLUME']}", DESCRIPTION_FONT, 'G')
        if self.cursor == 6:
            self.titleBack.update("BACK", MEDIUM_FONT_HORVED, 'B')
            self.descriptionText.update("", DESCRIPTION_FONT, 'R')
        if self.cursor == 7:
            self.descriptionText.update("", DESCRIPTION_FONT, 'R')
        
        
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
        
    ###########  Draw Sound Setting Menu in another surface  ################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)