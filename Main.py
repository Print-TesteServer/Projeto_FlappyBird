import pygame
import os
import random

TELA_ALTURA = 500
TELA_LARGURA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('data', 'imgs', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('data', 'imgs', 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('data', 'imgs', 'bg.png')))
IMAGEM_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('data', 'imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('data', 'imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('data', 'imgs', 'bird3.png'))),
    ]

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont('arial', 50)

class Passaro:
    IMGS = IMAGEM_PASSARO
    # Animação da rotação
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = IMGS[0]