# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

from config import WIDTH, HEIGHT, PLAYERS_HEIGHT, PLAYERS_WIDTH, PLAYERS_VELOCITY, BLOCK_WIDTH, BLOCK_HEIGHT

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
# ----- Inicia estruturas de dados
class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image=img #imagem do personagem
        self.rect=self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx= WIDTH/4 #posição plano x
        self.rect.bottom= HEIGHT-40 #posição plano y
        self.speedx=0
        self.speedy=0
        self.jump=False

    def update(self):
        #atualiza a possição do personagem
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        #mantem o personagem dentro da tela

        if self.rect.bottom > HEIGHT: #Para Baixo
            self.rect.bottom = HEIGHT
            self.speedy=0
            self.jump==False
        if self.rect.top < 0: #Para Cima
            self.rect.top = 0  
            self.speedy=0      

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


game = True
#Variável para o ajuste de velocidade do jogo
clock=pygame.time.Clock()
FPS = 60
G=10

#Criando um grupo de sprites(que vai agir/atualizar conforme o tempo)
all_sprites=pygame.sprite.Group()
all_players=pygame.sprite.Group()
all_obstaculos=pygame.sprite.Group()
player1=Player(player_1_img) #adicionando jogador ao jogo
player2=Player(player_2_img)
plataforma=Block(block_1_img,300,380)
all_sprites.add(player1)
all_sprites.add(player2) #adicionando jogador ao grupo de sprites
all_sprites.add(plataforma)
all_players.add(player1)
all_players.add(player2)
all_obstaculos.add(plataforma)

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
            if event.key == pygame.K_LEFT:
                player1.speedx -= PLAYERS_VELOCITY
            if event.key == pygame.K_RIGHT:
                player1.speedx += PLAYERS_VELOCITY
            if event.key==pygame.K_UP and player1.jump==False:
                player1.speedy -= 100
            if event.key == pygame.K_a:
                player2.speedx -= PLAYERS_VELOCITY
            if event.key == pygame.K_d:
                player2.speedx += PLAYERS_VELOCITY
            if event.key==pygame.K_w and player2.jump==False:
                player2.speedy -= 100

        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player1.speedx += PLAYERS_VELOCITY
            if event.key == pygame.K_RIGHT:
                player1.speedx -= PLAYERS_VELOCITY
            if event.key==pygame.K_UP :
                player1.speedy += 100
            if event.key == pygame.K_a:
                player2.speedx += PLAYERS_VELOCITY
            if event.key == pygame.K_d:
                player2.speedx -= PLAYERS_VELOCITY
            if event.key==pygame.K_w :
                player2.speedy += 100

    
    hits= pygame.sprite.groupcollide(all_players,all_obstaculos,False,False,pygame.sprite.collide_mask)
    for player,obstaculos in hits.items():
        if player.rect.bottom<=obstaculos[0].rect.top-BLOCK_HEIGHT/2:
            player.rect.bottom=obstaculos[0].rect.top-BLOCK_HEIGHT/2
            player.speedx=-10
        elif player.rect.left>obstaculos[0].rect.centerx-BLOCK_WIDTH/2 and player.rect.bottom>obstaculos[0].rect.top :
            player.rect.left=obstaculos[0].rect.right
        elif player.rect.right<obstaculos[0].rect.centerx+BLOCK_WIDTH/2 and player.rect.bottom>obstaculos[0].rect.top:
            player.rect.right=obstaculos[0].rect.left
          
    # for sprite in all_obstaculos.sprites:  
    #     if sprite.rect.colliderect(player1.rect):
    #         if player1.direction.x<0:      
    #             player1.rect.left=sprite.rect.right 
    #         if player1.direction.x>0:      
    #             player1.rect.right=sprite.rect.left     
 
    all_sprites.update() #Atualiza a posição dos sprites(objetos)

    # ----- Gera saídas
    window.fill((0, 0, 255))  # Preenche com a cor branca
    window.blit(backgroud, (0,0)) #Nosso Fundo

    all_sprites.draw(window) #Desenha os sprites(objetos) na tela

    T=clock.get_time()/ 1000

    F = G * T

    
    
    player1.speedy+=10
    player2.speedy+=10

    # ----- Atualiza estado do jogo
    pygame.display.update()
    clock.tick(FPS)  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados