import pygame
import os
from jogo1 import*
from config import *

BACKGROUD = 'backgroud'
PLAYER1_IMG = 'player_1_img'
PLAYER2_IMG = 'player_2_img'
BLOCK1_IMG = 'block_1_img'
BLOCK2_IMG = 'block_2_img'
BULLET_IMG= 'img_bala'
BARRA_IMG= 'img_bar'
MINIMAP1_IMG= 'minimap_1_bar'
MINIMAP2_IMG= 'minimap_2_bar'
MINIMAP3_IMG= 'minimap_3_bar'
MINIMAP4_IMG= 'minimap_4_bar'



def load_assets():
    assets ={}
    assets[BACKGROUD]=pygame.image.load(os.path.join(IMG_DIR, 'background.gif')).convert()
    assets[BACKGROUD]=pygame.transform.scale(assets[BACKGROUD], (WIDTH, HEIGHT))

    assets[PLAYER1_IMG]=pygame.image.load(os.path.join(IMG_DIR,'player1.png'))
    assets[PLAYER1_IMG]=pygame.transform.scale(assets[PLAYER1_IMG], (PLAYERS_WIDTH, PLAYERS_HEIGHT))

    assets[PLAYER2_IMG]=pygame.image.load(os.path.join(IMG_DIR,'player2.png'))
    assets[PLAYER2_IMG]=pygame.transform.scale(assets[PLAYER2_IMG], (PLAYERS_WIDTH, PLAYERS_HEIGHT))

    assets[BLOCK1_IMG]=pygame.image.load(os.path.join(IMG_DIR,'block.png'))
    assets[BLOCK1_IMG]=pygame.transform.scale(assets[BLOCK1_IMG], (BLOCK_WIDTH, BLOCK_HEIGHT))

    assets[BLOCK2_IMG]=pygame.image.load(os.path.join(IMG_DIR,'block2.png'))
    assets[BLOCK2_IMG]=pygame.transform.scale(assets[BLOCK2_IMG], (BLOCK_WIDTH, BLOCK_HEIGHT))

    assets[BULLET_IMG]=pygame.image.load(os.path.join(IMG_DIR,'bullet.png'))
    assets[BULLET_IMG]=pygame.transform.scale(assets[BULLET_IMG], (BULLET_WIDTH,BULLET_HEIGHT))

    assets[BARRA_IMG]=pygame.image.load(os.path.join(IMG_DIR,'health_bar (2).png'))
    assets[BARRA_IMG]=pygame.transform.scale(assets[BARRA_IMG],(BARRA_WIDTH, BARRA_HEIGHT))

    assets[MINIMAP1_IMG]=pygame.image.load(os.path.join(IMG_DIR,'background.gif'))
    assets[MINIMAP1_IMG]=pygame.transform.scale(assets[MINIMAP1_IMG],(MIN_MAP_W, MIN_MAP_H))

    assets[MINIMAP2_IMG]=pygame.image.load(os.path.join(IMG_DIR,'mapa2.png'))
    assets[MINIMAP2_IMG]=pygame.transform.scale(assets[MINIMAP2_IMG],(MIN_MAP_W, MIN_MAP_H))

    assets[MINIMAP3_IMG]=pygame.image.load(os.path.join(IMG_DIR,'mapa3.png'))
    assets[MINIMAP3_IMG]=pygame.transform.scale(assets[MINIMAP3_IMG],(MIN_MAP_W, MIN_MAP_H))

    assets[MINIMAP4_IMG]=pygame.image.load(os.path.join(IMG_DIR,'mapa4.png'))
    assets[MINIMAP4_IMG]=pygame.transform.scale(assets[MINIMAP4_IMG],(MIN_MAP_W, MIN_MAP_H))

    return assets