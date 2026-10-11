"""Entidades do jogo: nave, invasores, projéteis e barreiras."""
from dataclasses import dataclass
import random
import pygame
from .config import LARGURA, ALTURA, ALIEN_CORES, ALIEN_PONTOS, VERDE, CIANO, VERMELHO


@dataclass
class Alien:
    x: float
    y: float
    tipo: str
    imagem: pygame.Surface
    largura: int = 30
    altura: int = 24

    @property
    def rect(self):
        return pygame.Rect(round(self.x), round(self.y), self.largura, self.altura)

    @property
    def pontos(self):
        return ALIEN_PONTOS[self.tipo]

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)


@dataclass
class Tiro:
    x: float
    y: float
    velocidade: float
    aliado: bool
    largura: int = 4
    altura: int = 12

    @property
    def rect(self):
        return pygame.Rect(round(self.x), round(self.y), self.largura, self.altura)

    def atualizar(self, dt):
        self.y += self.velocidade * dt

    def desenhar(self, tela):
        cor = CIANO if self.aliado else VERMELHO
        pygame.draw.rect(tela, cor, self.rect)
        pygame.draw.rect(tela, (255, 255, 255), self.rect.inflate(-2, -4))


class Nave:
    def __init__(self, imagem):
        self.imagem = imagem
        self.largura = 48
        self.altura = 48
        self.x = (LARGURA - self.largura) / 2
        self.y = ALTURA - 76
        self.velocidade = 300
        self.ultimo_tiro = 0
        self.intervalo_tiro = 0.28

    @property
    def rect(self):
        return pygame.Rect(round(self.x), round(self.y), self.largura, self.altura)

    def atualizar(self, dt, teclas):
        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidade * dt
        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidade * dt
        self.x = max(8, min(LARGURA - self.largura - 8, self.x))

    
    def tentar_atirar(self, agora, tiros, som_tiro=None):
        if agora - self.ultimo_tiro >= self.intervalo_tiro:
            tiros.append(
                Tiro(self.x + self.largura / 2 - 2, self.y - 5, -440, True)
            )
            self.ultimo_tiro = agora

            if som_tiro:
                som_tiro.play()
    def desenhar(self, tela):
            tela.blit(self.imagem, self.rect)         


class Barreira:
    """Barreira feita de blocos; o desenho deixa o centro inferior aberto (U invertido)."""
    TAMANHO = 6

    def __init__(self, x, y):
        # 12 colunas x 8 linhas. Os cantos inferiores são removidos para formar o arco.
        self.blocos = set()
        for linha in range(8):
            for coluna in range(12):
                if linha >= 5 and (coluna < 2 or coluna > 9):
                    continue
                self.blocos.add((coluna, linha))
        self.x, self.y = x, y

    def retangulos(self):
        s = self.TAMANHO
        return [((c, r), pygame.Rect(self.x + c * s, self.y + r * s, s, s))
                for c, r in self.blocos]

    def desenhar(self, tela):
        for _, rect in self.retangulos():
            pygame.draw.rect(tela, VERDE, rect)

    def receber_tiro(self, tiro_rect):
        for bloco, rect in self.retangulos():
            if rect.colliderect(tiro_rect):
                self.blocos.discard(bloco)
                # Um impacto remove também um pequeno vizinho, dando efeito de dano.
                c, r = bloco
                for vizinho in ((c - 1, r), (c + 1, r), (c, r - 1)):
                    if random.random() < 0.28:
                        self.blocos.discard(vizinho)
                return True
        return False

    def receber_invasor(self, alien_rect):
        # Invasores que descem até a barreira corroem os blocos que tocam.
        atingidos = [bloco for bloco, rect in self.retangulos() if rect.colliderect(alien_rect)]
        for c, r in atingidos:
            self.blocos.discard((c, r))
            self.blocos.discard((c - 1, r))
            self.blocos.discard((c + 1, r))
        return bool(atingidos)
