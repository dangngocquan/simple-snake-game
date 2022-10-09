import datetime
import random
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
        
    ###########   Update cursor and buttons status in Options Menu   ########################################
    def update(self):
        ###########   Update cursor and buttons   ###########################################################
        if self.cursor == 0:
            self.titleMusic.isChosen = True
            self.descriptionText.update('Press ENTER to choose the music for game', DESCRIPTION_FONT, 'ALL')
        else:
            self.titleMusic.isChosen = False
        if self.cursor == 1:
            self.titleMusicOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titleMusicOptions.isChosen = False
        if self.cursor == 2:
            self.titleMusicVolume.isChosen = True
            self.descriptionText.update('Press ENTER to set volume of music', DESCRIPTION_FONT, 'ALL')
        else:
            self.titleMusicVolume.isChosen = False
        if self.cursor == 3:
            self.titleMusicVolumeOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titleMusicVolumeOptions.isChosen = False
        if self.cursor == 4:
            self.titleSoundVolume.isChosen = True
            self.descriptionText.update('Press ENTER to set volume of sound', DESCRIPTION_FONT, 'ALL')
        else:
            self.titleSoundVolume.isChosen = False
        if self.cursor == 5:
            self.titleSoundVolumeOptions.isChosen = True
            self.descriptionText.update('Press A D W S to change your choice, Press ENTER to save your setting', 
                                        DESCRIPTION_FONT_2, 'ALL')
        else:
            self.titleSoundVolumeOptions.isChosen = False
        if self.cursor == 6:
            self.titleBack.isChosen = True
            self.titleBack.update("BACK", MEDIUM_FONT_HORVED)
            self.descriptionText.update("", DESCRIPTION_FONT, 'ALL')
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
        
    ###########  Draw Sound setting Menu in another surface  ################################################
    def draw(self, parentSurface):
        parentSurface.blit(self.surface, self.surfaceRect)