import random
import pygame
from math import sin,cos,floor,radians
from random import randint

from config import *
from lista_assests import *

class Player(pygame.sprite.Sprite):
    def __init__(self,nickname,img,posX,posY,groups,assets,controls):
        pygame.sprite.Sprite.__init__(self)
        # Informações básicas
        self.name = nickname
        self.image=img #imagem do personagem
        self.playerControls = controls
        
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
        self.image_noflip=img
        self.image_flip=pygame.transform.flip(self.image,True,False)
        if self.rect.x > WIDTH/2:
            self.playerDirection = -1
        self.recoilforce = 0
        
        # Assets
        self.assets = assets
        self.bullet_img = assets[BULLET_IMG]

        # Atributos de jogo
        self.max_health = MAX_HP
        self.health_now = MAX_HP
        self.comp_hp = 50
        self.immortal=0
        self.item = self.changeItem()
        self.firing = False
        


    # ----- Função para atualizar a posição do personagem
    def update(self):

        if self.immortal > 0:
            self.immortal -= 1
            print(self.immortal)


        if self.playerDirection<0:
            self.image=self.image_flip
        else:
            self.image=self.image_noflip


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
            self.speedy=0
        if self.rect.right > WIDTH: # Para Esquerda
            self.rect.right = WIDTH 
        if self.rect.left < 0: # Para Direita
            self.rect.left = 0
        
        self.item.update(self.rect.centerx,self.rect.centery,self.playerDirection)

        if self.firing:
            self.useItem()


    #Mudança/definição de arma a escolher
    def changeItem(self):
        PISTOL={
                "asset" : "../assets/img/pistola.png",  # Imagem do sprite da arma
                "itemType" : "STRAIGHT",  # Tipo do projétil
                "velocity" : 30,  # Velocidade do projétil
                "spray" : .2,  # % da variação de ângulo de tiro
                "size" : 8,  # Quantidade de projéteis antes de cooldown
                "cadence" : 5,  # Quantidade de Frames entre os usos do item
                "recoil" : 4,  # Velocidade do recuo da arma
                'reload': 3,  # Cooldown entre a velocidade de recarga da arma
                "soundEffect" : "Som1.wav"
                #"useParticle" : "" 
                #"hitParticle" : ""
        }
        return Item((self.rect.centerx, self.rect.centery), self.playerDirection, self.assets, self.all_obstaculos, self.all_sprites, self.all_bullets, PISTOL)

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


# self.item = Item((self.rect.centerx, self.rect.centery), self.playerDirection, self.assets, self.all_obstaculos, PISTOL)
class Item(pygame.sprite.Sprite):
    def __init__(self, playerOrigin, direction, assets, collgroup, all_sprites, all_bullets, projectile):
        self.originX = playerOrigin[0] + (direction * PLAYERS_WIDTH/2 + 5)
        self.originY = playerOrigin[1]
        self.direction = direction
        self.assets = assets
        self.all_sprites = all_sprites
        self.all_bullets = all_bullets
        self.collideGroups = collgroup
        self.projectile = projectile
        self.avaliable = projectile['size']
        self.cooldown = 0
        pygame.mixer.music.load(os.path.join(SND_DIR, projectile['soundEffect']))
        self.mixer = pygame.mixer.Sound(os.path.join(SND_DIR, projectile['soundEffect']))
        self.mixer.set_volume(0.4)
    
    
    def use(self):
        if self.avaliable and (not self.cooldown):
            new_bullet = Bullet(self.assets, self.originX, self.originY, self.projectile["velocity"]*self.direction, self.collideGroups, self.projectile["itemType"],self.projectile["spray"])
            self.all_sprites.add(new_bullet)
            self.all_bullets.add(new_bullet)
            self.avaliable-=1
            self.cooldown = self.projectile['cadence']
            self.mixer.play()
        elif not (self.avaliable and self.cooldown):
            self.avaliable = self.projectile['size']
            self.cooldown = self.projectile['reload']
            

    def update(self,x,y,direction):
        if self.cooldown : self.cooldown -= 1
        self.originX = x + (direction * PLAYERS_WIDTH/2) + (5*direction)
        self.originY = y
        self.direction = direction


class Bullet(pygame.sprite.Sprite):
    def __init__(self, assets,posx, posy, vel, collgroup, type, spray):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.image = assets[BULLET_IMG]
        self.rect = self.image.get_rect()
        self.rect.centerx = posx
        self.rect.centery = posy
        self.angle = radians(randint(-floor((MAX_SPRAY*spray)),(floor(MAX_SPRAY*spray))))
        print('angle',self.angle)
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
        
        for b in hits.keys():
            if self.type != 'BOUNCE':
                b.kill()
                if self.rect.left > WIDTH:
                    self.kill() # Se a bala que está indo da esquerda para a direita passar do comprimento da tela(width) a bala "morre"
                if self.rect.right < 0:
                    self.kill()
            else:
                self.speedx*=-1
