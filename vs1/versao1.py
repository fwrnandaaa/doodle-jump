import sys
import time
import pygame
pygame.init()

width, height = 400, 500
size = width, height
time = pygame.time.Clock()
fps = 60

imagem_fundo = pygame.image.load("background01.png")
tela = pygame.display.set_mode((width, height))
pygame.display.set_caption("Doodle jump")
player = pygame.transform.scale(pygame.image.load("character_right.png"), (90, 70))
playerrect = player.get_rect()
playerrect.x = 170
playerrect.y = 400

plataforma = pygame.image.load("platform.png")

playerrect = pygame.Rect(100, 100, 50, 50)
is_jumping = False
jump_height = 0
jump_speed = -15
fall_speed = 20

while True:
    time.tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP] and not is_jumping:
        is_jumping = True
        jump_height = 0

    if is_jumping:
        playerrect.y += jump_speed
        jump_height += 1

        if jump_height >= 10: 
            jump_speed = fall_speed  
        if playerrect.bottom >= 500:  
            playerrect.bottom = 450
            is_jumping = False
            jump_speed = -15
    if keys[pygame.K_LEFT]:
        playerrect.x -= 5
        player = pygame.transform.scale(pygame.image.load("character_left.png"), (90, 70))
        if playerrect.left < 0:
            playerrect.left = 0
    if keys[pygame.K_RIGHT]:
        playerrect.x += 5
        player = pygame.transform.scale(pygame.image.load("character_right.png"), (90, 70))
        if playerrect.right > 500:
            playerrect.right = 500


    tela.blit(imagem_fundo, (0, 0))
    tela.blit(player, playerrect)
    tela.blit(plataforma, (width/2, height/2))
    pygame.display.flip()
