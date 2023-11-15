from os import path

WIDTH=600
HEIGHT=420

PLAYERS_WIDTH=80
PLAYERS_HEIGHT=80

BLOCK_WIDTH=120
BLOCK_HEIGHT=80

BULLET_WIDTH = 10
BULLET_HEIGHT = 10
VEL = 10

PLAYERS_VELOCITY=15

GRAVITY = 3

MAX_HP = 15

DANO_ARMA_1 = 1
DANO_ARMA_2 = 5

BARRA_WIDTH=150
BARRA_HEIGHT=30

IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


INIT = 0
GAME = 1
QUIT = 2
FPS = 60
