from os import path

WIDTH=1280
HEIGHT=720

PLAYERS_WIDTH=80
PLAYERS_HEIGHT=80
PLAYER_JUMP = 50

BLOCK_WIDTH=480
BLOCK_HEIGHT=80

BULLET_WIDTH = 10
BULLET_HEIGHT = 10
VEL = 20

PLAYERS_VELOCITY=15

GRAVITY = 3

MAX_HP = 15

DANO_ARMA_1 = 1
DANO_ARMA_2 = 5

BARRA_WIDTH=150
BARRA_HEIGHT=30

IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


INIT = 0
GAME = 1
OVER =2
QUIT = 3
MAPS = 4

MIN_MAP_W=320
MIN_MAP_H=180


FPS = 60

OBLIQUEANGLE = 45
MAX_SPRAY = 85

TEMPO_SEM_DANO = 30 #tempo em frames

PLAYER_DEACCELERATION = 5
