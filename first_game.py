import random
import sched
import time

from pygame_functions import *


def main():
    # call needed methods
    game_intro()


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
obstacle_image = player_img

# Icons made by www.flaticon.com/authors/dinosoftlabs
background_img = pygame.image.load('road2.png')
background_img = pygame.transform.scale(background_img, (400, 800))


def player(x, y):
    window.blit(player_img, (x, y))


def obstacle(x, y):
    window.blit(obstacle_image, (x, y))


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


# find out if there is a collision
def is_collision(obstacleY, playerY, obstacleX, playerX):
    distance = math.sqrt((math.pow(obstacleX - playerX, 2)) + (math.pow(playerY - obstacleY, 2)))
    if distance < 27:
        return True
    else:
        return False


def run_game():
    running = True
    # variables for player
    playerX = 370
    playerY = 480
    playerX_change = 0

    # initialize obstacle
    obstacleX = 225
    obstacleY = 0

    # run the window until it's told to exit
    counter = 0
    while running:
        # sets the background of the game to black for now using R, G , B
        window.fill((0, 0, 0))

        # picks which spawn location for the car (at random from list of cords)
        # current code can spawn cars on top of each other but never 4 cars
        counter += 1
        if counter % 100 == 0:
            # variables for obstacles
            spawn_cords = [225, 315, 415, 500]
            num = spawn_cords[random.randint(0, 3)]
            obstacleX = num
            obstacleY = 0

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
        # displays the background image
        window.blit(background_img, [200, 0])

        # calls the function to spawn cars and moves the y value of the cars
        for i in range(0, 3):
            obstacle(obstacleX, obstacleY)
        # move the position of the car
        obstacleY += 5

        # update players x coordinate
        playerX += playerX_change

        # boundaries for player
        if playerX <= 200:
            playerX = 200
        if playerX >= 536:
            playerX = 536

        # calls the player data
        player(playerX, playerY)

        # updates the game so changes are seen
        pygame.display.update()

        # checks if there is a collision and if there is, restart from intro
        collision = is_collision(obstacleY, playerY, obstacleX, playerX)
        if collision:
            game_intro()
            break


if __name__ == '__main__':
    main()
