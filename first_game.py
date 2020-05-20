import pygame
from pygame_functions import *

# initialize pygame and fonts
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)

# creates a window with a pixel width of 800x600
window = pygame.display.set_mode((800, 600))

# set the title of the screen and the icon
title = pygame.display.set_caption("Vroom Zoom")
# Icons made by https://www.flaticon.com/authors/eucalyp
icon = pygame.image.load('car-2.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('transport.png')

# temporary objects image
# TODO: update image add other objects
object_image = player_img

# Icons made by www.flaticon.com/authors/dinosoftlabs
background_img = pygame.image.load('road2.png')
background_img = pygame.transform.scale(background_img, (400, 800))


def player(x, y):
    window.blit(player_img, (x, y))


def objects(x, y):
    window.blit(object_image, (x, y))


# displays an intro screen for the game
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            text_out = font.render('Press Space Bar to Start...', False, (96, 250, 255))
            window.blit(text_out, (200, 300))
            pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run_game()
                    intro = False
            if event.type == pygame.QUIT:
                pygame.quit()


def run_game():
    # variables for player
    playerX = 370
    playerY = 480
    playerX_change = 0

    # variables for objects, TODO: make them spawn random, make them do damage
    objectX = 225
    objectY = 0
    # run the window until it's told to exit
    running = True
    while running:
        # sets the background of the game to black for now using R, G , B
        window.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # keystroke event handler for left/right
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
        window.blit(background_img, [200, 0])

        # this will spawn cars to avoid
        objectY += 5
        # update player x
        playerX += playerX_change
        # boundaries
        if playerX <= 200:
            playerX = 200
        if playerX >= 536:
            playerX = 536

        # calls the player data
        player(playerX, playerY)
        # calls the objects
        objects(objectX, objectY)
        # updates the game so changes are seen
        pygame.display.update()


# call needed methods
game_intro()
