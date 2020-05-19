import pygame

# initialize pygame
pygame.init()

# creates a window with a pixel width of 800x600
window = pygame.display.set_mode((800, 600))

# set the title of the screen and the icon
title = pygame.display.set_caption("Car Game?")
# Icons made by https://www.flaticon.com/authors/eucalyp
icon = pygame.image.load('car-2.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('transport.png')
playerX = 370
playerY = 480
playerX_change = 0


def player(x, y):
    window.blit(player_img, (x, y))


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

    # update player x
    playerX += playerX_change
    # calls the player data
    player(playerX, playerY)
    # updates the game so changes are seen
    pygame.display.update()
