import sys
import time

import pygame

#Personagem mexe da esquerda pra direita
pygame.init()
width, height = 640, 580
size = width, height
tela = pygame.display.set_mode((540, 630))
pygame.display.set_caption("Doodle jump")
time = pygame.time.Clock()

imagem_fundo = pygame.image.load("background01.png")
character = pygame.image.load("character_right.png")
platform = pygame.image.load("platform.png")
character_rect = character.get_rect()
character_rect.y = 420
character_rect.x = 320
black = (0,0,0)

character_x = 50
character_y = 480
platforms = [(175, 480, 70, 10)]
blocks = []

for i in range (len(platforms)):
    block = pygame.draw.rect(tela, black,  platforms[i])
    blocks.append(block)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

  
    tela.blit(imagem_fundo, (0, 0))
    tela.blit(character, (character_x, character_y))
    tela.blit(platform, (220, 300))
    pygame.display.flip()


