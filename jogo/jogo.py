# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
# from pygame.sprite import _Group

from config import *

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
block_2_img=pygame.image.load('jogo/assets/img/block2.png')
block_2_img=pygame.transform.scale(block_2_img, (BLOCK_WIDTH, BLOCK_HEIGHT))
# ----- Inicia estruturas de dados
class Player(pygame.sprite.Sprite):
    def __init__(self, img,controls):
        pygame.sprite.Sprite.__init__(self)

        self.image=img #imagem do personagem
        self.rect=self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx= WIDTH/4 #posição plano x
        self.rect.bottom= HEIGHT-40 #posição plano y
        self.speedx=0
        self.speedy=0
        self.jump=True
        self.colisions = [False,False,False,False] # Esquerda, Direita, Cima, Baixo
        self.playerControls = controls

    def update(self):
        #atualiza a possição do personagem
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        self.colisions = [False,False,False,False]

        #mantem o personagem dentro da tela

        if self.rect.bottom > HEIGHT: #Para Baixo
            self.rect.bottom = HEIGHT
            self.speedy=0
            self.jump==True
        if self.rect.top < 0: #Para Cima
            self.rect.top = 0  
            self.speedy=F*30    

        if self.rect.right > WIDTH: #Para Esquerda
            self.rect.right = WIDTH 
        if self.rect.left < 0: #Para Direita
            self.rect.left = 0 
        


class Block(pygame.sprite.Sprite):
    def __init__(self,img,posx,posy):
        pygame.sprite.Sprite.__init__(self)

        self.image=img #imagem do personagem
        self.rect=self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx= posx #posição plano x
        self.rect.centery= posy #posição plano y
        self.speedx=0


# class Bullet(pygame.sprite.Sprite):
#     def __init__(self, img,)

a=True
game = True
#Variável para o ajuste de velocidade do jogo
clock=pygame.time.Clock()
FPS = 60
G=30

playerControls={
    'p1' : [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN],
    'p2' : [pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_s]
}

#Criando um grupo de sprites(que vai agir/atualizar conforme o tempo)
all_sprites=pygame.sprite.Group()
all_players=pygame.sprite.Group()
all_obstaculos=pygame.sprite.Group()


player1=Player(player_1_img,playerControls['p1']) #adicionando jogador ao jogo
player2=Player(player_2_img,playerControls['p2'])
plataforma1=Block(block_1_img,300,380)
plataforma2=Block(block_2_img,BLOCK_WIDTH/2,210)


all_sprites.add(player1)
all_sprites.add(player2) #adicionando jogador ao grupo de sprites
all_sprites.add(plataforma1)
all_sprites.add(plataforma2)
all_players.add(player1)
all_players.add(player2)
all_obstaculos.add(plataforma1)
all_obstaculos.add(plataforma2)



# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
         # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            for plr in all_players:
                if event.key == plr.playerControls[0] and not plr.colisions[0]:
                    plr.speedx -= PLAYERS_VELOCITY
                if event.key == plr.playerControls[1] and not plr.colisions[1]:
                    plr.speedx += PLAYERS_VELOCITY
                if event.key == plr.playerControls[2] and player1.jump==True:
                    plr.jump = False
                    plr.speedy -= 50

        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            for plr in all_players:
                if event.key == plr.playerControls[0]:
                    plr.speedx = 0
                if event.key == plr.playerControls[1]:
                    plr.speedx = 0
                if event.key == plr.playerControls[2]:
                    plr.speedy += F*10


    hits= pygame.sprite.groupcollide(all_players,all_obstaculos,False,False,pygame.sprite.collide_mask)
    for player,obstaculos in hits.items():
        # Detectar qual aresta foi colidida baseado na distância entre as arestas do objeto e do player
        # A menor distância define a aresta colidida
        dists = [abs(player.rect.left-obstaculos[0].rect.right),
                 abs(player.rect.right-obstaculos[0].rect.left),
                 abs(player.rect.bottom-obstaculos[0].rect.top),
                 abs(player.rect.top-obstaculos[0].rect.bottom)]
        if dists[0] == min(dists):
            player.rect.left = obstaculos[0].rect.right
            player.speedx = 0
            player.colisions[0] = True

        if dists[1] == min(dists):
            player.speedx = 0
            player.rect.right = obstaculos[0].rect.left
            player.colisions[1] = True

        if dists[2] == min(dists):
            player.speedy =0
            player.rect.bottom=obstaculos[0].rect.top
            player.jump=False
            # a=True
            player.colisions[3] = True

        if dists[3] == min(dists):
            player.speedy = 0
            player.rect.top=obstaculos[0].rect.bottom
            player.colisions[2] = True

    if player1.rect.left>plataforma1.rect.right:
        player1.jump=True
    if player1.rect.right<plataforma1.rect.left:
        if player1.rect.left>plataforma2.rect.right:
            player1.jump=True   
    if player2.rect.left>plataforma1.rect.right:
        player2.jump=True
    if player2.rect.right<plataforma1.rect.left:
        if player2.rect.left>plataforma2.rect.right:
            player2.jump=True
    
    T=clock.get_time()/ 1000

    F = G * T
    
    if player1.jump:
        player1.speedy+=F*10
    if player2.jump:
        player2.speedy+=F*10

    all_sprites.update() #Atualiza a posição dos sprites(objetos)

    # ----- Gera saídas
    window.fill((0, 0, 255))  # Preenche com a cor branca
    window.blit(backgroud, (0,0)) #Nosso Fundo

    all_sprites.draw(window) #Desenha os sprites(objetos) na tela

    


    # ----- Atualiza estado do jogo
    pygame.display.update()
    clock.tick(FPS)  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados