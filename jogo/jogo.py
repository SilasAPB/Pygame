# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import WIDTH, HEIGHT, PLAYERS_HEIGHT, PLAYERS_WIDTH

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SandmannVille: Terra de Faroeste')

# ----- Inicia assets
backgroud=pygame.image.load('jogo/assets/img/fundo1.png').convert()
player_1_img=pygame.image.load('jogo/assets/img/player1.png')
player_1_img=pygame.transform.scale(player_1_img, (PLAYERS_WIDTH, PLAYERS_HEIGHT))
# ----- Inicia estruturas de dados
class Player(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)

        self.image=img #imagem do personagem
        self.rect=self.image.get_rect()
        self.rect.centerx= WIDTH/4 #posição plano x
        self.rect.bottom= HEIGHT-40 #posição plano y
        self.speedx=0

    def update(self):
        #atualiza a possição do personagem
        self.rect.x += self.speedx

        #mantem o personagem dentro da tela
        if self.rect.bottom > HEIGHT: #Para Baixo
            self.rect.bottom = HEIGHT
        if self.rect.top < 0: #Para Cima
            self.rect.top = 0        

        if self.rect.right > WIDTH: #Para Esquerda
            self.rect.right = WIDTH 
        if self.rect.left < 0: #Para Direita
            self.rect.left = 0        


game = True
#Variável para o ajuste de velocidade do jogo
clock=pygame.time.Clock()
FPS = 30

#Criando um grupo de sprites(que vai agir/atualizar conforme o tempo)
all_sprites=pygame.sprite.Group()
player1=Player(player_1_img) #adicionando jogador ao jogo
all_sprites.add(player1) #adicionando jogador ao grupo de sprites

# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False


    all_sprites.update() #Atualiza a posição dos sprites(objetos)

    # ----- Gera saídas
    window.fill((0, 0, 255))  # Preenche com a cor branca
    window.blit(backgroud, (0,0)) #Nosso Fundo

    all_sprites.draw(window) #Desenha os sprites(objetos) na tela

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados