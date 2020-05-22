import random
import sched
import time
from pygame_functions import *
import simpleaudio as sa


def main():
    # call needed methods
    game_intro()


# initialize pygame and fonts
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)

# Sound from https://freesound.org/people/squareal/
filename = 'crash.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)

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
# image made by https://pixabay.com/users/publicdomainpictures-14/
background_img2 = pygame.image.load('grass.jpg')

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


# spawns obstacles, called from run_game()
def obstacle():
    # Loop 3 times and add a snow flake in a random x,y position
    for i in range(0, 3):
        # variables for obstacles
        spawn_cords = [253, 323, 408, 483]
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


# ------------Main program loop------------
def run_game():
    # variables for player
    playerX = 370
    playerY = 480
    playerX_change = 0

    # initialize counter
    counter = 0

    # variable im using to set speed the cars fall at
    x = 20000

    # the speed that the cars move at
    speed = 1

    # the frequency the cars spawn at
    spawn_rate = 125

    # run the window until it's told to exit
    running = True
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
        window.blit(background_img2, [0, 0])
        window.blit(background_img, [238, 0])

        # this is my way of setting a spawn speed
        counter += 1
        if counter % spawn_rate == 0 or counter == 1:
            obstacle()

        """   
         # set the speed to increase per 10 seconds (1px increase)
         # Also, each time this is true, we will spawn cars at a higher
         # Frequency
         """
        speed_increase = pygame.time.get_ticks()
        if speed_increase >= x and counter != 1:
            x += 20000
            # so that its still playable if you make it this far max speed and spawn rate
            if spawn_rate > 50:
                spawn_rate -= 25
            if speed < 10:
                speed += 1
            # reset speed and frequency of spawns if program resets, because of stacks, easiest way
            reset = len(obstacle_list)
            print(reset)
            if reset <= 3:
                speed = 2
                spawn_rate = 125

        # calls the function to spawn cars and moves the y value of the cars
        for k in range(len(obstacle_list)):
            window.blit(obstacle_image, (obstacle_list[k][0], obstacle_list[k][1]))
            # move the Y position of the car down n pixels
            obstacle_list[k][1] += speed

        # update players x coordinate
        playerX += playerX_change

        # this is going to be the score just using the length of the list
        score = str(len(obstacle_list) * 10)
        score_out = font.render("Score: " + score, False, (255, 255, 255))
        window.blit(score_out, (0, 0))

        # boundaries for player
        if playerX <= 245:
            playerX = 245
        if playerX >= 600:  # 490
            playerX = 600

        # calls the player data
        player(playerX, playerY)

        # checks if there is a collision and if there is, restart from intro
        for k in range(len(obstacle_list)):
            collision = is_collision(obstacle_list[k][1], playerY, obstacle_list[k][0], playerX)
            if collision:
                play_obj = wave_obj.play()
                running = False
                obstacle_list.clear()
                game_intro()

        # updates the game so changes are seen
        pygame.display.flip()

        # limit fps to 60
        clock.tick(60)
    # closes everything
    pygame.quit()


if __name__ == '__main__':
    main()
