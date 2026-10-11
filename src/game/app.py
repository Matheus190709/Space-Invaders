"""Loop principal, regras e desenho da partida."""
import random
import pygame
from .config import (LARGURA, ALTURA, FPS, TITULO, FUNDO, BRANCO, VERDE,
                     AMARELO, VERMELHO, CIANO, CINZA)
from .entities import Alien, Barreira, Nave, Tiro
from pathlib import Path

ALIEN_COLUNAS = 10
ALIEN_FILEIRAS = 6
ALIEN_LARGURA = 30
ALIEN_ALTURA = 24


def carregar_imagem(caminho, tamanho, cor=None):
    imagem = pygame.image.load(caminho).convert_alpha()
    imagem = pygame.transform.scale(imagem, tamanho)
    if cor:
        imagem.fill((*cor, 255), special_flags=pygame.BLEND_RGBA_MULT)
    return imagem


class Jogo:
    def __init__(self, tela, pasta_raiz):
        self.tela = tela
        self.raiz = pasta_raiz
        self.som_tiro_nave = pygame.mixer.Sound(
    str(self.raiz / "assets" / "audio" / "tiro-nave.wav")
)
        self.som_tiro_alien = pygame.mixer.Sound(
    str(self.raiz / "assets" / "audio" / "tiro-aliens.wav")
)

        self.som_tiro_nave.set_volume(0.45)
        self.som_tiro_alien.set_volume(0.35)
        self.fonte = pygame.font.SysFont("consolas", 18, bold=True)
        self.fonte_grande = pygame.font.SysFont("consolas", 36, bold=True)
        self.fonte_pequena = pygame.font.SysFont("consolas", 14, bold=True)
        self.estrela = [(random.randrange(LARGURA), random.randrange(ALTURA), random.choice((1, 1, 2))) for _ in range(75)]
        self.carregar_sprites()
        self.novo_jogo()

    def carregar_sprites(self):
        pasta = self.raiz / "assets" / "images"
        self.sprites = {
            "verde": carregar_imagem(pasta / "Green.png", (ALIEN_LARGURA, ALIEN_ALTURA)),
            "amarelo": carregar_imagem(pasta / "Yellow.png", (ALIEN_LARGURA, ALIEN_ALTURA)),
            "vermelho": carregar_imagem(pasta / "Red.png", (ALIEN_LARGURA, ALIEN_ALTURA)),
        }
        self.nave_imagem = carregar_imagem(pasta / "Space-Invaders-Ship-PNG-Images.png", (48, 48))

    def novo_jogo(self):
        self.nave = Nave(self.nave_imagem)
        self.aliens = []
        # Duas fileiras de cada cor: verde (10), amarelo (20), vermelho (30).
        ordem = ["verde", "verde", "amarelo", "amarelo", "vermelho", "vermelho"]
        inicio_x, inicio_y, passo_x, passo_y = 105, 82, 58, 42
        for linha, tipo in enumerate(ordem):
            for coluna in range(ALIEN_COLUNAS):
                self.aliens.append(Alien(inicio_x + coluna * passo_x, inicio_y + linha * passo_y,
                                         tipo, self.sprites[tipo], ALIEN_LARGURA, ALIEN_ALTURA))
        self.direcao = 1
        self.velocidade_alien = 34
        self.velocidade_descida = 18
        self.tiros = []
        self.barreiras = [Barreira(x, 430) for x in (100, 285, 470, 655)]
        self.pontuacao = 0
        self.estado = "jogando"
        self.ultimo_tiro_inimigo = 0
        self.intervalo_tiro_inimigo = random.uniform(0.65, 1.3)

    def atualizar_aliens(self, dt):
        if not self.aliens:
            self.estado = "vitoria"
            return
        esquerda = min(a.x for a in self.aliens)
        direita = max(a.x + a.largura for a in self.aliens)
        vai_bater = (direita + self.velocidade_alien * dt >= LARGURA - 12 if self.direcao > 0
                     else esquerda - self.velocidade_alien * dt <= 12)
        if vai_bater:
            self.direcao *= -1
            for alien in self.aliens:
                alien.y += self.velocidade_descida
            # Cada fileira perdida deixa o grupo um pouco mais rápido, sem descidas contínuas.
            self.velocidade_alien = min(105, self.velocidade_alien + 2.2)
        else:
            for alien in self.aliens:
                alien.x += self.direcao * self.velocidade_alien * dt
        for alien in self.aliens:
            for barreira in self.barreiras:
                barreira.receber_invasor(alien.rect)
            if alien.rect.bottom >= self.nave.y + 2 or alien.rect.colliderect(self.nave.rect):
                self.estado = "game_over"
                break

    def atualizar(self, dt, agora):
        if self.estado != "jogando":
            return
        teclas = pygame.key.get_pressed()
        self.nave.atualizar(dt, teclas)
        if teclas[pygame.K_SPACE]:
            self.nave.tentar_atirar(agora, self.tiros, self.som_tiro_nave)
        self.atualizar_aliens(dt)

        if agora - self.ultimo_tiro_inimigo >= self.intervalo_tiro_inimigo and self.aliens:
            # Dispara um alien aleatório, favorecendo os que estão na parte inferior das colunas.
            atiradores = []
            for alien in self.aliens:
                if not any(outro.x < alien.x + 8 and outro.x + outro.largura > alien.x - 8 and outro.y > alien.y for outro in self.aliens):
                    atiradores.append(alien)
            atirador = random.choice(atiradores or self.aliens)
            self.tiros.append(Tiro(atirador.x + atirador.largura / 2, atirador.y + atirador.altura, 210, False))
            self.som_tiro_alien.play()
            self.ultimo_tiro_inimigo = agora
            self.intervalo_tiro_inimigo = random.uniform(0.65, 1.35)

        for tiro in self.tiros[:]:
            tiro.atualizar(dt)
            if tiro.y < -20 or tiro.y > ALTURA + 20:
                self.tiros.remove(tiro)
                continue
            atingiu = False
            if tiro.aliado:
                for alien in self.aliens[:]:
                    if tiro.rect.colliderect(alien.rect):
                        self.pontuacao += alien.pontos
                        self.aliens.remove(alien)
                        self.tiros.remove(tiro)
                        atingiu = True
                        # O grupo acelera gradualmente à medida que diminui.
                        self.velocidade_alien = min(115, self.velocidade_alien + 1.2)
                        break
            else:
                if tiro.rect.colliderect(self.nave.rect):
                    self.tiros.remove(tiro)
                    self.estado = "game_over"
                    continue
            if atingiu:
                continue
            for barreira in self.barreiras:
                if barreira.receber_tiro(tiro.rect):
                    if tiro in self.tiros:
                        self.tiros.remove(tiro)
                    break

    def desenhar_fundo(self):
        self.tela.fill(FUNDO)
        for x, y, raio in self.estrela:
            pygame.draw.rect(self.tela, (95, 115, 150), (x, y, raio, raio))
        pygame.draw.line(self.tela, (30, 45, 70), (0, 48), (LARGURA, 48), 2)

    def texto(self, texto, fonte, cor, centro):
        superficie = fonte.render(texto, False, cor)
        self.tela.blit(superficie, superficie.get_rect(center=centro))

    def desenhar(self):
        self.desenhar_fundo()
        self.texto(f"SCORE {self.pontuacao:05d}", self.fonte, BRANCO, (115, 25))
        self.texto("SPACE INVADERS", self.fonte, CIANO, (LARGURA // 2, 25))
        self.texto("1UP", self.fonte, VERDE, (LARGURA - 85, 25))
        for alien in self.aliens:
            alien.desenhar(self.tela)
        for barreira in self.barreiras:
            barreira.desenhar(self.tela)
        for tiro in self.tiros:
            tiro.desenhar(self.tela)
        if self.estado == "jogando":
            self.nave.desenhar(self.tela)
        elif self.estado == "game_over":
            self.texto("GAME OVER", self.fonte_grande, VERMELHO, (LARGURA // 2, ALTURA // 2 - 35))
            self.texto(f"SCORE: {self.pontuacao:05d}", self.fonte, BRANCO, (LARGURA // 2, ALTURA // 2 + 12))
            self.texto("APERTE ENTER PARA REINICIAR", self.fonte_pequena, AMARELO, (LARGURA // 2, ALTURA // 2 + 55))
            self.texto("ESC PARA SAIR", self.fonte_pequena, CINZA, (LARGURA // 2, ALTURA // 2 + 82))
        elif self.estado == "vitoria":
            self.texto("YOU WIN!", self.fonte_grande, VERDE, (LARGURA // 2, ALTURA // 2 - 35))
            self.texto(f"SCORE: {self.pontuacao:05d}", self.fonte, BRANCO, (LARGURA // 2, ALTURA // 2 + 12))
            self.texto("APERTE ENTER PARA JOGAR DE NOVO", self.fonte_pequena, AMARELO, (LARGURA // 2, ALTURA // 2 + 55))
        pygame.display.flip()



def executar():
    pygame.init()
    pygame.mixer.init()

    pygame.display.set_caption(TITULO)
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    relogio = pygame.time.Clock()

    raiz = Path(__file__).resolve().parents[2]

    # Música de fundo
    musica = raiz / "assets" / "audio" / "Soundtrack.mp3"
    pygame.mixer.music.load(str(musica))
    pygame.mixer.music.set_volume(0.35)
    pygame.mixer.music.play(-1)

    # Sons dos disparos
    som_tiro_nave = pygame.mixer.Sound(
        str(raiz / "assets" / "audio" / "tiro-nave.wav")
    )

    som_tiro_alien = pygame.mixer.Sound(
        str(raiz / "assets" / "audio" / "tiro-aliens.wav")
    )

    som_tiro_nave.set_volume(0.45)
    som_tiro_alien.set_volume(0.35)

    # Cria o jogo
    jogo = Jogo(tela, raiz)

    # Disponibiliza os sons para a classe Jogo
    jogo.som_tiro_nave = som_tiro_nave
    jogo.som_tiro_alien = som_tiro_alien

    executando = True

    while executando:
        dt = min(relogio.tick(FPS) / 1000, 0.04)
        agora = pygame.time.get_ticks() / 1000

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    executando = False

                elif evento.key == pygame.K_RETURN and jogo.estado in (
                    "game_over", "vitoria"
                ):
                    jogo.novo_jogo()

        jogo.atualizar(dt, agora)
        jogo.desenhar()

    pygame.quit()

