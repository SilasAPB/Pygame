import random
import pygame
from math import sin,cos,floor,radians
from random import randint

from config import *
from lista_assests import *
from guns import *
from jogo1 import *

class Player(pygame.sprite.Sprite):
    def __init__(self,nickname,img,posX,posY,groups,assets,controls,choose):
        pygame.sprite.Sprite.__init__(self)
        # Informações básicas
        self.logo=img
        self.name = nickname
        self.frame=1
        self.anim=assets[f'player_{choose}_img']

        self.image=self.anim[self.frame] #imagem do personagem
        self.playerControls = controls

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()


        # Grupos de colisão
        self.all_sprites = groups['all_sprites']
        self.all_bullets = groups['all_bullets']
        self.all_obstaculos = groups['all_obstaculos']

        # Movimentação
        self.rect=self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = posX #posição plano x
        self.rect.bottom = posY #posição plano y
        self.speedx=0
        self.speedy=0
        self.jump=True
        self.playerDirection = 1
        self.image_flip=pygame.transform.flip(self.image,True,False)
        self.image_noflip=pygame.transform.flip(self.image_flip,True,False)
        if self.rect.x > WIDTH/2:
            self.playerDirection = -1
        self.recoilforce = 0
        
        # Assets
        self.assets = assets
        # self.bullet_img = assets[BULLET_IMG]

        # Atributos de jogo
        self.max_health = MAX_HP
        self.health_now = MAX_HP
        self.comp_hp = 50
        self.immortal=0

        self.item = self.changeItem()
        self.all_sprites.add(self.item)
        self.firing = False

        self.frame_ticks=60
        


    # ----- Função para atualizar a posição do personagem
    def update(self):        

        if self.immortal > 0:
            self.immortal -= 1
            print(self.immortal)

        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update
        
        if self.speedx!=0:
            if elapsed_ticks>self.frame_ticks:
                self.last_update = now

            # Avança um quadro.
          
                if self.frame<4:
                    self.frame += 1
                else:
                    self.frame=1
        else: self.frame=1

        if self.speedy<0:
            self.frame=6
        elif self.speedy>0:
            self.frame=5

        if self.playerDirection<0:
            self.image=pygame.transform.flip(self.anim[self.frame],True,False)
        else:
            self.image=self.anim[self.frame]

        # self.image = self.anim[self.frame]


        # ----- Gravidade
        self.speedy+=GRAVITY


        # ----- Forca de recuo
        if self.recoilforce>0: self.recoilforce -= PLAYER_DEACCELERATION
        elif self.recoilforce<0: self.recoilforce = 0
        self.speedx-= self.recoilforce * self.playerDirection


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
            if dists[2] == min(dists): # Bottom Edge
                self.speedy = 0
                self.rect.bottom=obstaculos[0].rect.top
                self.jump = True

            elif dists[3] == min(dists): # Top Edge
                self.speedy = 0
                self.rect.top=obstaculos[0].rect.bottom
            elif dists[0] == min(dists): # Left edge
                self.rect.left = obstaculos[0].rect.right
                self.speedx = 0

            elif dists[1] == min(dists): # Right edge
                self.speedx = 0
                self.rect.right = obstaculos[0].rect.left



        # ----- Mantem o personagem dentro da tela
        if self.rect.bottom > HEIGHT: # Para Baixo
            self.rect.bottom = HEIGHT
            self.speedy=0
            self.jump = True
        if self.rect.top < 0: # Para Cima
            self.rect.top = 0
            self.speedy=0
        if self.rect.right > WIDTH: # Para Esquerda
            self.rect.right = WIDTH 
        if self.rect.left < 0: # Para Direita
            self.rect.left = 0
        

        # Funções para o item
        self.item.moveItem(self.rect.centerx,self.rect.centery,self.playerDirection)
        if self.firing:
            self.useItem()


    #Mudança/definição de arma a escolher
    def changeItem(self): # Você referencia o antigo item e ele te da um novo
       values = list(ITEMS.values())
       atributos =  random.choice(values)
       return Item((self.rect.centerx, self.rect.centery), self.playerDirection, self.assets, self.all_obstaculos, self.all_sprites, self.all_bullets, atributos)

    # Função para disparar um projétil
    def useItem(self):
        self.item.use()
        
    #define a intangibilidade
    def setImmortal(self,tempo):
        self.immortal = tempo 
    
    #IDENTIFICA O QUANTO DE VIDA DO PERSONAGEM FOI TIRADO POR CONTA DO DANO DA ARMA(DEPENDE DA ARMA, POR ISSO É UM PARÂMETRO, POR SER VARIÁVEL)
    def nivel_vida(self, dano_arma):
        if self.immortal == 0:
            if self.health_now > 0:
                self.health_now -= dano_arma
                return self.health_now
            else:
                return 0
        else:
            return self.health_now
        


# define classe da barra de vida, que considera a vida do peronagem a ela associado
class HealthBar():
    def __init__(self, x, y, w, h, player):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = player.max_health
        self.max_hp = player.max_health

    def draw(self, surface): #desenha a barra
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))  
    
    def update(self,vida): #atualiza o estado da barra
        self.hp=vida



#define a classe de plataformas
class Block(pygame.sprite.Sprite):
    def __init__(self,img,posx,posy):
        pygame.sprite.Sprite.__init__(self)

        self.image= img # Imagem do personagem
        self.rect=self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx= posx # Posição plano x
        self.rect.centery= posy # Posição plano y
        self.speedx=0



class Item(pygame.sprite.Sprite):
    def __init__(self, playerOrigin, direction, assets, collgroup, all_sprites, all_bullets, projectile):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[projectile['asset']]
        self.rect=self.image.get_rect()
        self.rect.centerx = playerOrigin[0] + (direction * PLAYERS_WIDTH/2)
        self.rect.centery = playerOrigin[1]
        self.direction = direction
        if self.direction < 0:
            self.image=pygame.transform.flip(self.image,True,False)
        self.assets = assets
        self.all_sprites = all_sprites
        self.all_bullets = all_bullets
        self.collideGroups = collgroup
        self.projectile = projectile
        self.avaliable = projectile['size']
        self.cooldown = 0
        pygame.mixer.music.load(os.path.join(SND_DIR, projectile['soundEffect']))
        self.mixer = pygame.mixer.Sound(os.path.join(SND_DIR, projectile['soundEffect']))
        self.mixer.set_volume(0.5)
    
    
    def use(self):
        if self.avaliable and (not self.cooldown):
            new_bullet = Bullet(self.assets, self.rect.centerx, self.rect.centery, self.projectile["velocity"]*self.direction, self.collideGroups, self.projectile["itemType"],self.projectile["spray"],self.projectile['damage'])
            self.all_sprites.add(new_bullet)
            self.all_bullets.add(new_bullet)
            self.avaliable-=1
            self.cooldown = self.projectile['cadence']
            self.mixer.play()
        elif not (self.avaliable and self.cooldown):
            self.avaliable = self.projectile['size']
            self.cooldown = self.projectile['reload']
            

    def moveItem(self,x,y,direction):
        if self.cooldown : self.cooldown -= 1
        self.rect.centerx = x + (direction * PLAYERS_WIDTH/2) + (5*direction)
        self.rect.centery = y
        if direction!=self.direction:
            self.image=pygame.transform.flip(self.image,True,False)
        self.direction = direction
        


class Bullet(pygame.sprite.Sprite):
    def __init__(self, assets,posx, posy, vel, collgroup, type, spray,damage):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        if self.type == "STRAIGHT":
            self.image = assets[BULLET_STRAIGHT]
        elif self.type == "OBLIQUE":
            self.image = assets[BULLET_OBLIQUE]
        else:
            self.image = assets[BULLET_BOUNCE]
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy
        self.angle = radians(randint(-floor((MAX_SPRAY*spray)),(floor(MAX_SPRAY*spray))))
        self.damage = damage
        self.bounces = 0
        if self.type == "OBLIQUE":
            self.speedx = abs(cos(OBLIQUEANGLE + self.angle))*vel # Velocidade fixa para a direita
            self.speedy = -sin(OBLIQUEANGLE)*abs(vel) # Velocidade fixa para a direita
        else:
            self.speedx = cos(self.angle)*vel # Velocidade fixa para a direita
            self.speedy = -sin(self.angle)*abs(vel) # Velocidade fixa para a direita
        self.collideGroup = collgroup
    
    def update(self):
        # ----- Gravidade
        if self.type == "OBLIQUE":
            self.speedy+=GRAVITY
        
        # ----- Atualiza posições
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # ----- Checa colisões entre bala e obstáculos
        hits = pygame.sprite.groupcollide([self],self.collideGroup,False,False,pygame.sprite.collide_mask)
        
        for bullet,block in hits.items():
            if self.type != 'BOUNCE':
                self.kill()
                if self.rect.left > WIDTH:
                    self.kill() # Se a bala que está indo da esquerda para a direita passar do comprimento da tela(width) a bala "morre"
                if self.rect.right < 0:
                    self.kill()
            elif self.bounces < MAX_BOUNCES:
                dists = [abs(self.rect.left - block[0].rect.right),
                    abs(self.rect.right - block[0].rect.left),
                    abs(self.rect.bottom - block[0].rect.top),
                    abs(self.rect.top - block[0].rect.bottom)]
                if dists[2] == min(dists) or dists[3] == min(dists): # Top Bottom
                    self.speedy*=-1
                elif dists[0] == min(dists) or dists[1] == min(dists): # Left Right
                    self.speedx*=-1
                self.bounces+=1
            else: self.kill()

class UI(pygame.sprite.Sprite):
    def __init__(self,cronometro,vidas,players):
        self.cronometro = cronometro
        self.vidas = vidas
        self.players = players