import pygame
import sys
import json
import os

sys.path.insert(0, 'jogo')
from lista_assests import *


mapName = input("Digite o nome do mapa: ")

modo = "NEW"

if os.path.exists(os.path.join('jogo','assets','maps',f'{mapName}.json')):
    modo = "EDITING"
    with open(os.path.join('jogo','assets','maps',f'{mapName}.json'),'r') as mapjson:
        gamePlainMap = json.load(mapjson)

pygame.init()

window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption(f'Map creator - {mapName}  [{modo}]')

w, h = pygame.display.get_surface().get_size()

game = True

TILESIZE = 80

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

if modo == "NEW":
    gamePlainMap = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]

gameMap = []
for ln in gamePlainMap:
    gameMap.append(list(ln))

blockselection = BLOCK1_MAP2
blockSymbol = 1

# Inicializa o mapa
for ln in range(len(gameMap)):
    for col in range(len(gameMap[ln])):
        if gameMap[ln][col] != 0:
            gameMap[ln][col] = Block(assets[blockselection],col*TILESIZE,ln*TILESIZE)
            all_sprites.add(gameMap[ln][col])

printTable(gamePlainMap)

while game:
    mouseX, mouseY = pygame.mouse.get_pos()
    mouseX = mouseX//TILESIZE
    mouseY = mouseY//TILESIZE
    
    # ----- Trata eventos
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            if gameMap[mouseY][mouseX] == 0 and cursor != 0:
                gameMap[mouseY][mouseX] = Block(assets[blockselection],mouseX*TILESIZE,mouseY*TILESIZE)
                all_sprites.add(gameMap[mouseY][mouseX])
                gamePlainMap[mouseY][mouseX] = blockSymbol

            elif cursor != 0:
                # print(gameMap[mouseY][mouseX])
                gameMap[mouseY][mouseX].kill()
                gameMap[mouseY][mouseX] = 0
                gamePlainMap[mouseY][mouseX] = 0
            printTable(gamePlainMap)
        
        if event.type == pygame.KEYDOWN:
            if cursor != 0:
                cursor.kill()
            if event.key == pygame.K_0 and cursor != 0:
                blockselection = 0
                cursor = 0
                blockSymbol = 0
                print(0)
            if event.key == pygame.K_1:
                blockselection = BLOCK1_MAP2
                cursor = Block(assets[blockselection],mouseX*TILESIZE,mouseY*TILESIZE)
                all_sprites.add(cursor)
                blockSymbol = 1
                print(1)
            if event.key == pygame.K_2:
                blockselection = BLOCK2_MAP2
                cursor = Block(assets[blockselection],mouseX*TILESIZE,mouseY*TILESIZE)
                all_sprites.add(cursor)
                blockSymbol = 2
                print(2)
            if event.key == pygame.K_3:
                blockselection = BLOCK3_MAP2
                cursor = Block(assets[blockselection],mouseX*TILESIZE,mouseY*TILESIZE)
                all_sprites.add(cursor)
                blockSymbol = 3
                print(3)
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

printTable(gamePlainMap)

jsonObject = json.dumps(gamePlainMap,indent=4)

with open(f"jogo/assets/maps/{mapName}.json", "w") as outfile:
    outfile.write(jsonObject)