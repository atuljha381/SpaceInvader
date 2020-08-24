import pygame
import random
import math
from pygame import mixer
from sys import exit

# Initializing pygame
pygame.init()
# To create size of window
screen = pygame.display.set_mode((800, 600))
# Background Image
background = pygame.image.load("background.png")
# Background Sound
mixer.music.load('background.wav')
mixer.music.set_volume(0.1)
mixer.music.play(-1)

# To add window name and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# Player
playerIMG = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyIMG = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyIMG.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(0, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)

# Bullet
bulletIMG = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 8
bullet_state = 'ready'

# Score
score_value = 0
font = pygame.font.Font('Coaster Ghost Personal Use Only.ttf', 32)
textX = 10
textY = 10

# Pause
pauseIMG = pygame.image.load("stop.png")
pauseX = 770
pauseY = 10

# Game Over
over_font = pygame.font.Font('Coaster Ghost Personal Use Only.ttf', 64)

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
bright_blue = (0, 0, 200)
green = (0, 255, 0)
red = (255, 0, 0)
bright_green = (0, 200, 0)
bright_red = (200, 0, 0)


def control():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        mouse1 = pygame.mouse.get_pos()

        shoot_text = font.render("Shoot : Spacebar", True, (255, 255, 255))
        screen.blit(shoot_text, (350, 200))

        left_move = font.render("Move Left : Left Arrow", True, (255, 255, 255))
        screen.blit(left_move, (350, 250))

        right_move = font.render("Move Right : Right Arrow", True, (255, 255, 255))
        screen.blit(right_move, (350, 300))

        smallText = pygame.font.Font('Coaster Ghost Personal Use Only.ttf', 20)

        back_butSurf, back_butRect = text_objects("Back?", smallText)
        back_butRect.center = ((350 + (75 / 2)), (250 + (25 / 2)))

        back_button = pygame.Rect(350, 500, 75, 25)

        pygame.draw.rect(screen, blue, back_button)
        screen.blit(back_butSurf, back_butRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()

        if back_button.collidepoint((mouse1[0], mouse1[1])):
            pygame.draw.rect(screen, bright_blue, back_button)
            screen.blit(back_butSurf, back_butRect)
            if click:
                running = False
                main_menu()



        pygame.display.update()


def pause_button(x, y):
    screen.blit(pauseIMG, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerIMG, (x, y))


def enemy(x, y, i):
    screen.blit(enemyIMG[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletIMG, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


click = False


def main_menu():
    global click

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        menu = font.render("Main Menu", True, (255, 255, 255))
        screen.blit(menu, (350, 200))
        mouse = pygame.mouse.get_pos()
        # Text
        smallText = pygame.font.Font('Coaster Ghost Personal Use Only.ttf', 20)

        textSurf, textRect = text_objects("Play", smallText)
        text11Surf, textRect = text_objects("Let's Go", smallText)

        text2Surf, text2Rect = text_objects("Option", smallText)
        text22Surf, text2Rect = text_objects("Controls", smallText)

        text3Surf, text3Rect = text_objects("Quit", smallText)
        text33Surf, text3Rect = text_objects("Sure?", smallText)

        textRect.center = ((350 + (100 / 2)), (250 + (30 / 2)))
        text2Rect.center = ((350 + (100 / 2)), (300 + (30 / 2)))
        text3Rect.center = ((350 + (100 / 2)), (350 + (30 / 2)))

        button1 = pygame.Rect(350, 250, 100, 30)
        button2 = pygame.Rect(350, 300, 100, 30)
        button3 = pygame.Rect(350, 350, 100, 30)

        pygame.draw.rect(screen, green, button1)
        screen.blit(textSurf, textRect)

        pygame.draw.rect(screen, green, button2)
        screen.blit(text2Surf, text2Rect)

        pygame.draw.rect(screen, red, button3)
        screen.blit(text3Surf, text3Rect)

        if button1.collidepoint((mouse[0], mouse[1])):
            pygame.draw.rect(screen, bright_green, button1)
            screen.blit(text11Surf, textRect)
            if click:
                game()

        elif button2.collidepoint((mouse[0], mouse[1])):
            pygame.draw.rect(screen, bright_green, button2)
            screen.blit(text22Surf, text2Rect)
            if click:
                control()

        elif button3.collidepoint((mouse[0], mouse[1])):
            pygame.draw.rect(screen, bright_red, button3)
            screen.blit(text33Surf, text3Rect)
            if click:
                pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


# Game Loop
def game():
    global playerX, playerY, playerX_change
    global bullet_state, bulletY, bulletX, bulletY_change
    global score_value
    global pauseX, pauseY

    running = True
    while running:
        # To add color
        screen.fill((0, 0, 0))
        # Add Background
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            # To move spaceship by keystroke
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state is 'ready':
                        bullet_sound = mixer.Sound('laser.wav')
                        bullet_sound.set_volume(0.2)
                        bullet_sound.play()
                        bulletX = playerX
                        fire_bullet(playerX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        # Setting boundaries
        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        if playerX >= 736:
            playerX = 736

        # Enemy Movement
        for i in range(num_of_enemies):
            # Game over execution
            if enemyY[i] > 440:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 3
                enemyY[i] += enemyY_change[i]
            if enemyX[i] >= 736:
                enemyX_change[i] = -3
                enemyY[i] += enemyY_change[i]

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosion_Sound = mixer.Sound('explosion.wav')
                explosion_Sound.set_volume(0.2)
                explosion_Sound.play()
                bulletY = 480
                bullet_state = 'ready'
                score_value += 1
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(0, 150)

            enemy(enemyX[i], enemyY[i], i)

        # Bullet Movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = 'ready'
        if bullet_state is 'fire':
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        button_pause = pygame.Rect(770, 10, 24, 24)
        pygame.draw.rect(screen, white, button_pause)
        pause_button(pauseX, pauseY)

        player(playerX, playerY)
        show_score(textX, textY)

        # To continuously update any changes in the game display
        pygame.display.update()


main_menu()
