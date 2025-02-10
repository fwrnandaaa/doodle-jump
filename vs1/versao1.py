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
platform_1_width = 160
platform_1_height = 440
platform_position = (350, 500)
platform_fall_speed = 0
plataformas_na_tela = []

def platforma_desce(plataforma, plataforma_position):
    while True:
        plataforma_position += 1
        tela.blit(plataforma, (plataforma_position) )
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
        plataforma_nova = platforma_desce(plataforma, platform_position)
        plataformas_na_tela.append(plataforma_nova)
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
    tela.blit(plataforma, (200, 100))
    pygame.display.flip()
  