import pygame
from pygame import mixer 

import random
import math

#initializing pygame
pygame.init() #mandatory to open the game

screen = pygame.display.set_mode((800,600)) #width & height

#Background
background = pygame.image.load('background_down.png')

#Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1) #-1 will enable the music to play on loop

#Title
pygame.display.set_caption("Space Invaders")

#Icon
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370 # x-axis(width)
playerY = 500 # y-axis(height)
playerX_change = 0

#Enemy

#A list for multiple enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 15

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(40)

#Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 500
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready" 
#Ready = can't see bullet on scree
#Fire = Bullet is currently moving

#Font: Score & Game Over
#Score Text
score_value = 0
font = pygame.font.Font('PixelifySans.ttf', 32) #fontstyle, font size

textX = 10
textY = 10

#Game Over Text
over_font = pygame.font.Font('PixelifySans.ttf', 64)

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text(x, y):
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (230, 250))

def player(x, y):
    screen.blit(playerImg, (x, y)) #blit = to draw img playerimg on the window

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

# Distance between two coordinates D = sqrt( ((x2 -x1)**2) + ((y2 - y1)**2) )
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

#Game Loop
running = True
while running:

    #screen color: RGB - grey
    screen.fill((38, 47, 74))
    #background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # if keystroke is press, check if it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_Sound = mixer.Sound('laser.wav')
                    bullet_Sound.play()
                    #Current x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        
        #when arrow is not pressed, spaceship will stop moving
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    #Player boundary
    playerX += playerX_change

    if playerX <=0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    #Enemy boundary
    for i in range(num_of_enemies):

        #Game Over
        if enemyY[i] > 450:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text(230, 250)
            break
            
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]
        
        #Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)    

        enemy(enemyX[i], enemyY[i], i)

    #Bullet movement
    if bulletY <= 0:
        bulletY = 500
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY) #calling the player function
    show_score(textX, textY)
    pygame.display.update() #always to include this line after adding stuff into display


#== https://www.youtube.com/watch?v=FfWpgLFMI7w# ==#