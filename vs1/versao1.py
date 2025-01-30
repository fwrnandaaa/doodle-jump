import sys
import time

import pygame

pygame.init()
width, height = 640, 580
size = width, height
tela = pygame.display.set_mode((540, 630))
pygame.display.set_caption("Doodle jump")
time = pygame.time.Clock()

imagem_fundo = pygame.image.load("background01.png")

character = pygame.image.load("character_right.png")
character_rect = character.get_rect()
character_rect.y = 420
character_rect.x = 320

platform = pygame.image.load("platform.png")
platform_rect = platform.get_rect()
platform_rect.center = (width // 2, 578)

character_x = 50
character_y = 480

while True:
    tela.blit(platform, platform_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()
           sys.exit()

  
    tela.blit(imagem_fundo, (0, 0))
    tela.blit(character, (character_x, character_y))
    tela.blit(platform, platform_rect)
    pygame.display.flip()


