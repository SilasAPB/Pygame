import pygame
from jogo1 import*
from config import *





backgroud=pygame.image.load('jogo/assets/img/fundo1.png').convert()

player_1_img=pygame.image.load('jogo/assets/img/player1.png')
player_1_img=pygame.transform.scale(player_1_img, (PLAYERS_WIDTH, PLAYERS_HEIGHT))

player_2_img=pygame.image.load('jogo/assets/img/player2.png')
player_2_img=pygame.transform.scale(player_2_img, (PLAYERS_WIDTH, PLAYERS_HEIGHT))

block_1_img=pygame.image.load('jogo/assets/img/block.png')
block_1_img=pygame.transform.scale(block_1_img, (BLOCK_WIDTH, BLOCK_HEIGHT))

block_2_img=pygame.image.load('jogo/assets/img/block.png')
block_2_img=pygame.transform.scale(block_2_img, (BLOCK_WIDTH, BLOCK_HEIGHT))

img_bala=pygame.image.load('jogo/assets/img/bullet_img.png')
img_bala=pygame.transform.scale(img_bala,(BULLET_WIDTH, BULLET_HEIGHT))

img_bar=pygame.image.load('jogo/assets/img/health_bar (2).png')
img_bar=pygame.transform.scale(img_bar,(BARRA_WIDTH, BARRA_HEIGHT))