import pygame
import sys
from math import ceil

sys.path.insert(0, 'jogo')
from lista_assests import *


pygame.init()

window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Map creator')

w, h = pygame.display.get_surface().get_size()

game = True

TILESIZE = 32

all_sprites=pygame.sprite.Group()


assets = load_assets()

class Block(pygame.sprite.Sprite):
    def __init__(self,img,sizex,sizey):
        pygame.sprite.Sprite.__init__(self)

        self.image= img # Imagem do personagem
        self.image = pygame.transform.scale(self.image,(TILESIZE,TILESIZE))
        self.rect=self.image.get_rect()
        self.rect.update(self.rect.x,self.rect.y,TILESIZE,TILESIZE)
        self.mask = pygame.mask.from_surface(self.image)
        self.speedx=0

    def update(self,x,y):
        self.rect.centerx= x # Posição plano x
        self.rect.centery= y # Posição plano y


cursor = Block(assets[BLOCK1_IMG],TILESIZE,TILESIZE)
all_sprites.add(cursor)

while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    
    # GERAR GRID
    window.fill((0,0,0))  # Preenche com a cor branca
    for wI in range(ceil(w/TILESIZE)):
        pygame.draw.line(window,(255,255,255),(wI*TILESIZE,0),(wI*TILESIZE,h))
    for hI in range(ceil(w/TILESIZE)):
        pygame.draw.line(window,(255,255,255),(0,hI*TILESIZE),(w,hI*TILESIZE))

    mouseX, mouseY = pygame.mouse.get_pos()
    print(mouseX//TILESIZE,mouseY//TILESIZE)
    # ----- Atualiza estado do jogo
    
    cursor.update(mouseX//TILESIZE*TILESIZE+TILESIZE/2,mouseY//TILESIZE*TILESIZE+TILESIZE/2)

    all_sprites.draw(window)
    pygame.display.update()  # Mostra o novo frame para o jogador
    
# ===== Finalização =====
pygame.quit()