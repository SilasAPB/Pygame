import random
import pygame
from math import sin,cos

from config import *
from lista_assests import *

class Player(pygame.sprite.Sprite):
    def __init__(self,nickname,img,posX,posY,groups,assets,controls):
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
        self.bullet_img = assets[BULLET_IMG]
        self.all_sprites = groups['all_sprites']
        self.all_bullets = groups['all_bullets']
        self.all_obstaculos= groups['all_obstaculos']
        self.playerControls = controls
        self.playerDirection = 1
        self.max_health = MAX_HP
        self.health_now = self.max_health
        self.comp_hp = 50
        self.assets= assets
        self.immortal = 0
        if self.rect.x > WIDTH/2:
            self.playerDirection = -1


    # ----- Função para atualizar a posição do personagem
    def update(self):

        if self.immortal > 0:
            self.immortal -= 1
            print(self.immortal)

        # ----- Gravidade
        self.speedy+=GRAVITY


        # ----- Atualiza a posição do player com base na velocidade dele
        self.rect.x += self.speedx
        self.rect.y += self.speedy


        # ----- Colisão entre player e blocos
        hits = pygame.sprite.groupcollide([self],self.all_obstaculos,False,False,pygame.sprite.collide_mask)
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
            self.speedy=GRAVITY*30    
        if self.rect.right > WIDTH: # Para Esquerda
            self.rect.right = WIDTH 
        if self.rect.left < 0: # Para Direita
            self.rect.left = 0 


    # Função para disparar um projétil
    def shoot(self):
        gunPos = self.rect.centerx+(PLAYERS_WIDTH/2+10)*self.playerDirection
        new_bullet = Bullet(self.assets, self.rect.centery,gunPos,VEL*self.playerDirection)
        self.all_sprites.add(new_bullet)
        self.all_bullets.add(new_bullet)

    def setImmortal(self,tempo):
        self.immortal = tempo 
        


    def nivel_vida(self, dano_arma):
        if self.immortal == 0:
            if self.health_now > 0:
                self.health_now -= dano_arma
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
    
    def update(self,vida):
        self.hp = vida




class Block(pygame.sprite.Sprite):
    def __init__(self,img,posx,posy):
        pygame.sprite.Sprite.__init__(self)

        self.image= img # Imagem do personagem
        self.rect=self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx= posx # Posição plano x
        self.rect.centery= posy # Posição plano y
        self.speedx=0
    
class Bullet(pygame.sprite.Sprite):
    def __init__(self,assets,centery,left,vx):
        pygame.sprite.Sprite.__init__(self)
        # self.type
        self.image = assets[BULLET_IMG]
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
