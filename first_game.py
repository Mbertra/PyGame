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

# Icons made by www.flaticon.com/authors/dinosoftlabs
background_img = pygame.image.load('road2.png')
background_img = pygame.transform.scale(background_img, (325, 800))

# Player
player_img = pygame.image.load('transport.png')

# temporary objects image
# TODO: update image add other objects
obstacle_image = player_img

# Create an empty array
obstacle_list = []

# clock to keep track of some things
clock = pygame.time.Clock()


def player(x, y):
    window.blit(player_img, (x, y))


def obstacle():
    # Loop 3 times and add a snow flake in a random x,y position
    for i in range(0, 3):
        # variables for obstacles
        spawn_cords = [215, 285, 370, 445]
        num = random.randint(0, 3)
        obstacleX = spawn_cords[num]
        obstacleY = 0
        obstacle_list.append([obstacleX, obstacleY])


# displays an intro screen for the game
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            text_out = font.render('Press Space Bar to Start...', False, (96, 250, 255))
            window.blit(text_out, (200, 300))
            pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                    run_game()


# find out if there is a collision
def is_collision(obstacleY, playerY, obstacleX, playerX):
    distance = math.sqrt((math.pow(obstacleX - playerX, 2)) + (math.pow(playerY - obstacleY, 2)))
    if distance < 50:
        return True
    else:
        return False


def run_game():
    running = True
    # variables for player
    playerX = 370
    playerY = 480
    playerX_change = 0

    # run the window until it's told to exit
    counter = 0
    while running:
        # sets the background of the game to black for now using R, G , B
        window.fill((0, 0, 0))

        # these statements check for key presses, and for user quits
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

        # this is my way of setting a spawn speed
        counter += 1
        if counter % 75 == 0 or counter == 1:
            obstacle()

        # calls the function to spawn cars and moves the y value of the cars
        for k in range(len(obstacle_list)):
            window.blit(obstacle_image, (obstacle_list[k][0], obstacle_list[k][1]))
            # move the Y position of the car down n pixels
            obstacle_list[k][1] += 3

        # update players x coordinate
        playerX += playerX_change

        # boundaries for player
        if playerX <= 200:
            playerX = 200
        if playerX >= 536:
            playerX = 536

        # calls the player data
        player(playerX, playerY)

        # checks if there is a collision and if there is, restart from intro
        for k in range(len(obstacle_list)):
            collision = is_collision(obstacle_list[k][1], playerY, obstacle_list[k][0], playerX)
            if collision:
                # ToDo : clear_board()
                game_intro()
                break
        # updates the game so changes are seen
        pygame.display.flip()

        # limit fps to 60
        clock.tick(60)
    # closes everything
    pygame.quit()


if __name__ == '__main__':
    main()
