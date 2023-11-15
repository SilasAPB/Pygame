# ===== Inicialização =====
# ----- Importa e inicia pacotes
#from typing import Any
import pygame
# from pygame.sprite import _Group

from config import *
from math import sin,cos

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SandmannVille: Terra de Faroeste')

# ----- Inicia assets
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


# ----- Inicia estruturas de dados
class Player(pygame.sprite.Sprite):
    def __init__(self,nickname,img,posX,posY,all_bullets, all_sprites,img_bala,controls):
        pygame.sprite.Sprite.__init__(self)
        self.name = nickname
        self.image=img #imagem do personagem
        self.rect=self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = posX #posição plano x
        self.rect.bottom = posY #posição plano y
        self.speedx=0
        self.speedy=0
        self.jump=True
        self.bullet_img = img_bala
        self.all_sprites = all_sprites
        self.all_bullets = all_bullets
        self.playerControls = controls
        self.playerDirection = 1
        self.max_health = MAX_HP
        self.health_now = self.max_health
        self.comp_hp = 50
        if self.rect.x > WIDTH/2:
            self.playerDirection = -1


    # ----- Função para atualizar a posição do personagem
    def update(self):
        # ----- Gravidade
        self.speedy+=GRAVITY


        # ----- Atualiza a posição do player com base na velocidade dele
        self.rect.x += self.speedx
        self.rect.y += self.speedy


        # ----- Colisão entre player e blocos
        hits = pygame.sprite.groupcollide([self],all_obstaculos,False,False,pygame.sprite.collide_mask)
        for player,obstaculos in hits.items():
            # ----- Detectar qual aresta foi colidida baseado na distância entre as arestas do objeto e do player
            # A menor distância define a aresta colidida
            dists = [abs(self.rect.left-obstaculos[0].rect.right),
                    abs(self.rect.right-obstaculos[0].rect.left),
                    abs(self.rect.bottom-obstaculos[0].rect.top),
                    abs(self.rect.top-obstaculos[0].rect.bottom)]
            if dists[0] == min(dists): # Left edge
                self.rect.left = obstaculos[0].rect.right
                self.speedx = 0

            if dists[1] == min(dists): # Right edge
                self.speedx = 0
                self.rect.right = obstaculos[0].rect.left

            if dists[2] == min(dists): # Bottom Edge
                self.speedy = 0
                self.rect.bottom=obstaculos[0].rect.top
                self.jump = True

            if dists[3] == min(dists): # Top Edge
                self.speedy = 0
                self.rect.top=obstaculos[0].rect.bottom


        # ----- Mantem o personagem dentro da tela
        if self.rect.bottom > HEIGHT: # Para Baixo
            self.rect.bottom = HEIGHT
            self.speedy=0
            self.jump = True
        if self.rect.top < 0: # Para Cima
            self.rect.top = 0  
            self.speedy=F*30    
        if self.rect.right > WIDTH: # Para Esquerda
            self.rect.right = WIDTH 
        if self.rect.left < 0: # Para Direita
            self.rect.left = 0 


    # Função para disparar um projétil
    def shoot(self):
        gunPos = self.rect.centerx+(PLAYERS_WIDTH/2+10)*self.playerDirection
        new_bullet = Bullet(self.bullet_img, self.rect.centery,gunPos,VEL*self.playerDirection)
        all_sprites.add(new_bullet)
        all_bullets.add(new_bullet)


    def nivel_vida(self, dano_arma):
        if self.health_now > 0:
            self.health_now -= dano_arma
            print(self.health_now)
            return self.health_now
        else:
            return 0
    
class HealthBar():
    def __init__(self, x, y, w, h, player):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = player.health_now
        self.max_hp = player.max_health

    def draw(self, surface):
        #calculate health ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))  
    
    def update(self,dano):
        self.hp-=dano




class Block(pygame.sprite.Sprite):
    def __init__(self,img,posx,posy):
        pygame.sprite.Sprite.__init__(self)

        self.image=img # Imagem do personagem
        self.rect=self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx= posx # Posição plano x
        self.rect.centery= posy # Posição plano y
        self.speedx=0
    
class Bullet(pygame.sprite.Sprite):
    def __init__(self,img,centery,left,vx):
        pygame.sprite.Sprite.__init__(self)
        # self.type
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.centery = centery
        self.speedx = cos(OBLIQUEANGLE)*vx # Velocidade fixa para a direita
        self.speedy = -sin(OBLIQUEANGLE)*abs(vx) # Velocidade fixa para a direita
    
    def update(self):
        # ----- Gravidade
        self.speedy+=GRAVITY
        
        # ----- Atualiza posições
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # ----- Checa colisões entre bala e obstáculos
        # hits = pygame.sprite.groupcollide([self],all_obstaculos,True,False,pygame.sprite.collide_mask)
        if self.rect.left > WIDTH:
            self.kill() # Se a bala que está indo da esquerda para a direita passar do comprimento da tela(width) a bala "morre"
        if self.rect.right < 0:
            self.kill()

game = True
# ----- Variável para o ajuste de velocidade do jogo
clock=pygame.time.Clock()

G=30
T=clock.get_time()/ 1000

playerControls={
    'p1' : [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN,pygame.K_RSHIFT],
    'p2' : [pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s,pygame.K_r]
}

# ----- Criando um grupo de sprites(que vai agir/atualizar conforme o tempo)
all_sprites=pygame.sprite.Group()
all_players=pygame.sprite.Group()
all_obstaculos=pygame.sprite.Group()
all_bullets=pygame.sprite.Group()


player1=Player('P1',player_1_img,WIDTH*3/4,HEIGHT-PLAYERS_HEIGHT/2,all_bullets,all_sprites,img_bala,playerControls['p1']) #adicionando jogador ao jogo
player2=Player('P2',player_2_img,WIDTH/4,HEIGHT-PLAYERS_HEIGHT/2,all_bullets,all_sprites,img_bala,playerControls['p2'])
plataforma1=Block(block_1_img,300,380)
plataforma2=Block(block_2_img,BLOCK_WIDTH/2,210)

health_bar1 = HealthBar(10, 10, 150, 30, player1)

health_bar2 = HealthBar(WIDTH-160, 10, 150, 30, player2)


all_sprites.add(player1)
all_sprites.add(player2) # Adicionando jogador ao grupo de sprites
all_sprites.add(plataforma1)
all_sprites.add(plataforma2)

all_players.add(player1)
all_players.add(player2)
all_obstaculos.add(plataforma1)
all_obstaculos.add(plataforma2)


T=clock.get_time()/ 1000
F = G * T

# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # ----- Dependendo da tecla, altera a velocidade.
            for plr in all_players:
                if event.key == plr.playerControls[0]:  # Left
                    plr.speedx -= PLAYERS_VELOCITY
                    plr.playerDirection = -1
                if event.key == plr.playerControls[1]:  # Right
                    plr.speedx += PLAYERS_VELOCITY
                    plr.playerDirection = +1
                if event.key == plr.playerControls[2] and plr.jump==True:  # Up
                    plr.jump = False
                    plr.speedy -= PLAYER_JUMP
                if event.key == plr.playerControls[4]:  # Shift
                    plr.shoot()


        # ----- Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            for plr in all_players:
                if event.key == plr.playerControls[0]:
                    plr.speedx = 0
                if event.key == plr.playerControls[1]:
                    plr.speedx = 0
                if event.key == plr.playerControls[2]:
                    plr.speedy += F*10


        # ----- Verifica se usuário fechou o jogo
        if event.type == pygame.QUIT:
            game = False

    # ----- Colisão entre players e projetis
    hit = pygame.sprite.groupcollide(all_players,all_bullets,False,True,pygame.sprite.collide_mask)
    if hit:
        vidap1=1
        vidap2=1
        for player in hit.keys():
            if player == player1:
                vidap1 = player1.nivel_vida(DANO_ARMA_1)
                health_bar1.update(DANO_ARMA_1)
            elif player == player2:
                vidap2 = player2.nivel_vida(DANO_ARMA_1)
                health_bar2.update(DANO_ARMA_1)
        
        # se um morrer, o outro não morre
        if vidap1 == 0 :
            player1.kill()
            all_players.remove(player2)
        elif vidap2 == 0:
            player2.kill()
            all_players.remove(player1)



    all_sprites.update() # Atualiza a posição dos sprites(objetos)

    # ----- Gera saídas
    window.fill((0, 0, 255))  # Preenche com a cor branca
    window.blit(backgroud, (0,0)) # Nosso Fundo
    health_bar1.draw(window)
    health_bar2.draw(window)


    all_sprites.draw(window) # ----- Desenha os sprites(objetos) na tela

    # ----- Atualiza estado do jogo
    pygame.display.update()
    clock.tick(FPS)  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados