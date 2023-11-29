import pygame
from pygame import mixer

pygame.init()

screen=pygame.display.set_mode((800,600))

pygame.display.set_caption("space war")
background = pygame.image.load("background.png")
mixer.music.load("background.wav")
mixer.music.play(-1)

#player

playerIng = pygame.image.load("player.png")
playerX=350
playerY=450

playerX_change=0

def player(x,y):
    screen.blit(playerIng,(x,y))

running=True
while running:
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running=False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.type==pygame.K_LEFT:
                playerX_change= -5

            if event.type==pygame.K_RIGHT:
                playerX_change= 5


        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change = 0

    playerX+=playerX_change
    player(playerX,playerY)
    pygame.display.update()        