import sys
import time
import pygame
import random

pygame.init()

# Constantes gerais
width, height = 400, 500
size = width, height
time = pygame.time.Clock()
clock = pygame.time.Clock()
fps = 60
imagem_fundo = pygame.image.load("background01.png")
tela = pygame.display.set_mode((width, height))
pygame.display.set_caption("Doodle jump")

# Constantes referentes as plataformas
plataforma = pygame.image.load("platform.png")
altura_plataforma = plataforma.get_height()
larguraplataforma = plataforma.get_width()
plataformas = []
continua = True
velocity_x = 0.1
plataformarect = plataforma.get_rect()
plataformarect.x = 200
plataformarect.y = 400

# Constantes referentes ao jogador
player = pygame.transform.scale(pygame.image.load("character_right.png"), (90, 70))
playerrect = player.get_rect()
playerrect.x = 200
playerrect.y = 400
is_jumping = False
jump_height = 0
jump_speed = -15
fall_speed = 20

# Cria e adicionar plataformas
def criar_plataforma():
    x = random.randint(0, width - larguraplataforma)
    return {'objeto': plataforma, 'posicao': (x, 0), 'velocidade': (3)}

# Função move plataformas
def move_plataformas(objeto):
    pos = list(objeto['posicao']) 
    pos[1] += objeto['velocidade'] 
    objeto['posicao'] = tuple(pos) 

# Função para verificar colisão
def verificar_colisao(playerrect, plataformas):
    for p in plataformas:
        plataforma_rect = pygame.Rect(p['posicao'][0], p['posicao'][1], larguraplataforma, altura_plataforma)
        if playerrect.colliderect(plataforma_rect):
            if playerrect.bottom <= plataforma_rect.top + jump_speed:  # Verifica se o jogador está caindo
                playerrect.bottom = plataforma_rect.top   # Ajusta a posição do jogador
                return True

    return False

while True:
    time.tick(fps)
    dt = clock.tick(30)
    tela.blit(imagem_fundo, (0, 0))
    tela.blit(player, (playerrect))

    # Criando novas plataformas no topo da tela quando a ultima estiver na metade da tela
    if len(plataformas) < 1:  
        plataformas.append(criar_plataforma())
    elif plataformas[-1]['posicao'][1] >= height / 3:
        plataformas.append(criar_plataforma())

    for p in plataformas:
        move_plataformas(p)
        tela.blit(p['objeto'], p['posicao']) 

    plataformas = [p for p in plataformas if p['posicao'][1] < height]

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

        # Verifica colisão com plataformas
        if verificar_colisao(playerrect, plataformas):
            is_jumping = False
            jump_speed = -15  # Reseta a velocidade de pulo

        if playerrect.bottom >= 480:  
            playerrect.bottom = 480
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

        if playerrect.right > 400:
            playerrect.right = 400

    pygame.display.flip()