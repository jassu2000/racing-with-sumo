import random                    # for generating random no
import sys                      # used so use the exit func when someone clicks on the cross sign   sys.exit()
import pygame
from pygame.locals import *         #basic pygame imports
# global variables
FPS = 32                          # frames per sec
SCREENWIDTH = 1000
SCREENHEIGHT = 600
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))         # initialises a screen for window display
GROUNDY = SCREENHEIGHT *0.99
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/sprite/.....'
BACKGROUND = 'gallery/sprite/background1.png'
OBSTACLE = 'gallery/sprite/....'


def welcomeScreen():
    backgroundx = 0
    readyX = (SCREENWIDTH/2)-(900/2)
    readyY = (SCREENHEIGHT/2)-(600/2)
    while True:
        for event in pygame.event.get():    # ie if user entres any key or clicks the mouse
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE): #keydown == if any key is pressed and K_ESCAPE is for when esc key is pressed by the user
                pygame.quit()
                sys.exit()

# if user presses space or up key ,start the game
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'],(0,50))   #func that displays images       image[] = coordiantw
                SCREEN.blit(GAME_SPRITES['background'],(500,50)) 
                SCREEN.blit(GAME_SPRITES['getready'],(readyX,readyY))
                pygame.display.update()  #else screen will not change
                FPSCLOCK.tick(FPS)


if __name__ == "__main__":
                                         #GAME START HERE  main func
    pygame.init()           #initialise pygames modules
    FPSCLOCK = pygame.time.Clock()      #here we give fps so that a limit of no of frames will set


    pygame.display.set_caption('Racing with sumo by team 8')   # sets caption
    GAME_SPRITES['background']= pygame.image.load(BACKGROUND).convert()   #convert alpha is used for faster blitting
    # CONVERT will change the pixels only
    GAME_SPRITES['getready']= pygame.image.load('gallery/sprite/trans1.png').convert() 

   #game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    

    while True:
        welcomeScreen()       
        mainGame()                      #main game function
