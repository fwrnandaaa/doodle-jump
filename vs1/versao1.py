import sys
import time
import pygame
pygame.init()

width, height = 400, 500
size = width, height
time = pygame.time.Clock()
fps = 60
green = (35, 111, 51)
platforms = [[175, 480, 70, 10]]


imagem_fundo = pygame.image.load("background01.png")
tela = pygame.display.set_mode((width, height))
pygame.display.set_caption("Doodle jump")
player = pygame.transform.scale(pygame.image.load("character_right.png"), (90, 70))

player_x = 170
player_y = 400
blocks = []
jump = False
y_change = player_y
rect_list= []

#atualizando y do jogador
def player_position(y):
    global jump
    global y_change
    gravity = .4
    jump_h = 10
    if jump == True:
        y_change -= jump_h
        jump = False
    y = y_change
    y_change += gravity
    return y

#Verificando colisões
def check_collision(rect_list, j):
    global player_x
    global player_y
    global y_change
    for i in range(len(rect_list)):
  
        if rect_list[i].colliderect([player_x, player_y + 60, 90, 10]) and not jump and y_change > 0:
            j = True
    return j


while True:
    time.tick(fps)
    tela.blit(imagem_fundo, (0, 0))
    tela.blit(player, (player_x, player_y))
    for i in range (len(platforms)):
        block = pygame.draw.rect(tela, green, platforms[i])
        blocks.append(block)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()

    player_y = player_position(player_y)
    jump = check_collision(blocks, jump)

    pygame.display.flip()


