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
    def __init__(self,img,x,y):
        pygame.sprite.Sprite.__init__(self)

        self.image= img # Imagem do personagem
        self.image = pygame.transform.scale(self.image,(TILESIZE,TILESIZE))
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.update(self.rect.x,self.rect.y,TILESIZE,TILESIZE)
        self.mask = pygame.mask.from_surface(self.image)
        self.speedx=0

    def update(self,x,y):
        self.rect.centerx= x # Posição plano x
        self.rect.centery= y # Posição plano y

def printTable(table):
    for ln in table:
        print(ln)

cursor = Block(assets[BLOCK1_MAP2],0,0)
all_sprites.add(cursor)


gameMap = [0]*31
gameMap = [gameMap]*31
blockselection = BLOCK1_MAP1

# Inicializa o mapa
for ln in range(len(gameMap)):
    for col in range(len(gameMap[ln])):
        if gameMap[ln][col] != 0:
            gameMap[ln][col] = Block(assets[blockselection],ln,col)
            all_sprites.add(gameMap[ln][col])

while game:
    
    mouseX, mouseY = pygame.mouse.get_pos()
    mouseX = mouseX//TILESIZE
    mouseY = mouseY//TILESIZE
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.MOUSEBUTTONUP:
            if gameMap[mouseY][mouseX]==0:
                gameMap[mouseY][mouseX] = Block(assets[blockselection],mouseX*TILESIZE,mouseY*TILESIZE)
                all_sprites.add(gameMap[mouseY][mouseX])
            else:
                gameMap[mouseY][mouseX].kill()
                gameMap[mouseY][mouseX] = 0
        
        if event.type == pygame.KEYDOWN:
            if cursor != 0:
                cursor.kill()
            if event.key == pygame.K_0 and cursor != 0:
                blockselection = 0
            if event.key == pygame.K_1:
                blockselection = BLOCK1_MAP2
                block = Block(assets[blockselection],mouseX*TILESIZE,mouseY*TILESIZE)
                all_sprites.add(block)
            if event.key == pygame.K_2:
                blockselection = BLOCK2_MAP2
                block = Block(assets[blockselection],mouseX*TILESIZE,mouseY*TILESIZE)
                all_sprites.add(block)
            if event.key == pygame.K_3:
                blockselection = BLOCK3_MAP2
                block = Block(assets[blockselection],mouseX*TILESIZE,mouseY*TILESIZE)
                all_sprites.add(block)
        if event.type == pygame.QUIT:
            game = False

    
    # GERAR GRID
    window.fill((0,0,0))  # Preenche com a cor branca
    for wI in range(0,w,TILESIZE):
        pygame.draw.line(window,(255,255,255),(wI,0),(wI,h))
    for hI in range(0,h,TILESIZE):
        pygame.draw.line(window,(255,255,255),(0,hI),(w,hI))


    
    # ----- Atualiza estado do jogo
    if cursor != 0:
        cursor.update(mouseX*TILESIZE+TILESIZE/2,mouseY*TILESIZE+TILESIZE/2)

    all_sprites.draw(window)
    pygame.display.update()  # Mostra o novo frame para o jogador
    
# ===== Finalização =====
pygame.quit()