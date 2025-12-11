import pygame
import random
import time

# --- Constantes do Jogo (Ajustáveis) ---
TELA_LARGURA = 600
TELA_ALTURA = 800
GRAVIDADE = 1.2
VELOCIDADE_CANO = 5
ESPACO_CANO = 200  # Altura da abertura entre o cano superior e inferior
TEMPO_ENTRE_CANOS = 1500 # Milissegundos

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AMARELO_PASSARO = (255, 220, 0)
VERDE_CANO = (50, 200, 50)

# Inicializa o Pygame
pygame.init()
TELA = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption("Flappy Bird Clone (por Gemini)")
RELOGIO = pygame.time.Clock()
FONTE = pygame.font.Font(None, 48)
FONTE_GRANDE = pygame.font.Font(None, 72)

# --- Classe do Pássaro (Bird) ---
class Passaro:
    def __init__(self):
        self.largura = 40
        self.altura = 40
        self.x = TELA_LARGURA // 4
        self.y = TELA_ALTURA // 2
        self.velocidade_y = 0
        self.impulso = -18 # Força do pulo

    def pular(self):
        # Aumenta a velocidade vertical para cima (valor negativo)
        self.velocidade_y = self.impulso

    def atualizar(self):
        # Aplica gravidade
        self.velocidade_y += GRAVIDADE
        self.y += self.velocidade_y
        
        # Limita a velocidade de queda máxima para evitar bugs
        if self.velocidade_y > 20:
             self.velocidade_y = 20

    def desenhar(self, tela):
        # Desenha o pássaro como um círculo amarelo para simplificar
        pygame.draw.circle(tela, AMARELO_PASSARO, (int(self.x), int(self.y)), self.largura // 2)

    def get_rect(self):
        # Retorna o retângulo de colisão do pássaro
        return pygame.Rect(self.x - self.largura // 2, self.y - self.altura // 2, self.largura, self.altura)

# --- Classe do Cano (Pipe) ---
class Cano:
    def __init__(self, x, espaco_y):
        self.x = x
        self.largura = 60
        self.espaco = ESPACO_CANO
        self.espaco_y = espaco_y # Centro do espaço livre
        self.velocidade = VELOCIDADE_CANO
        self.passado = False # Flag para pontuação

        # Cano Superior
        self.topo_altura = self.espaco_y - self.espaco // 2
        # Cano Inferior
        self.base_y = self.espaco_y + self.espaco // 2
        self.base_altura = TELA_ALTURA - self.base_y

    def atualizar(self):
        # Move o cano para a esquerda
        self.x -= self.velocidade

    def desenhar(self, tela):
        # Desenha o cano superior
        pygame.draw.rect(tela, VERDE_CANO, (self.x, 0, self.largura, self.topo_altura))
        # Desenha o cano inferior
        pygame.draw.rect(tela, VERDE_CANO, (self.x, self.base_y, self.largura, self.base_altura))

        # Adiciona bordas pretas para melhor definição
        pygame.draw.rect(tela, PRETO, (self.x, 0, self.largura, self.topo_altura), 2)
        pygame.draw.rect(tela, PRETO, (self.x, self.base_y, self.largura, self.base_altura), 2)

    def get_rects(self):
        # Retorna os retângulos de colisão para o cano superior e inferior
        topo_rect = pygame.Rect(self.x, 0, self.largura, self.topo_altura)
        base_rect = pygame.Rect(self.x, self.base_y, self.largura, self.base_altura)
        return topo_rect, base_rect
    
    def esta_na_tela(self):
        # Verifica se o cano ainda está visível na tela
        return self.x + self.largura > 0

# --- Função Principal do Jogo ---
def jogo_principal():
    passaro = Passaro()
    canos = []
    pontuacao = 0
    jogo_ativo = True
    ultima_geracao_cano = pygame.time.get_ticks()

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            
            # Ação de pulo (apenas se o jogo estiver ativo)
            if evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
                if jogo_ativo:
                    passaro.pular()
                elif not jogo_ativo and evento.type == pygame.MOUSEBUTTONDOWN:
                    # Reinicia o jogo no 'Fim de Jogo'
                    return  # Chama a função principal novamente para reiniciar

        TELA.fill(PRETO) # Limpa a tela (fundo preto)

        if jogo_ativo:
            # --- 1. Atualização da Lógica ---
            
            # Geração de Canos
            agora = pygame.time.get_ticks()
            if agora - ultima_geracao_cano > TEMPO_ENTRE_CANOS:
                # Gera uma altura aleatória para o centro do espaço do cano
                # (Min 100 até Max TELA_ALTURA - 100)
                espaco_y_aleatorio = random.randint(100 + ESPACO_CANO // 2, TELA_ALTURA - 100 - ESPACO_CANO // 2)
                canos.append(Cano(TELA_LARGURA, espaco_y_aleatorio))
                ultima_geracao_cano = agora
            
            # Atualiza Pássaro
            passaro.atualizar()

            # Atualiza e Remove Canos
            novos_canos = []
            for cano in canos:
                cano.atualizar()
                
                # Checagem de Pontuação
                if not cano.passado and passaro.x > cano.x + cano.largura:
                    pontuacao += 1
                    cano.passado = True

                if cano.esta_na_tela():
                    novos_canos.append(cano)
            canos = novos_canos

            # --- 2. Checagem de Colisão ---
            
            passaro_rect = passaro.get_rect()

            # Colisão com o chão ou teto
            if passaro.y + passaro.altura // 2 > TELA_ALTURA or passaro.y - passaro.altura // 2 < 0:
                jogo_ativo = False
            
            # Colisão com os Canos
            for cano in canos:
                topo_rect, base_rect = cano.get_rects()
                if passaro_rect.colliderect(topo_rect) or passaro_rect.colliderect(base_rect):
                    jogo_ativo = False
        
        # --- 3. Desenho ---
        
        # Desenha Canos
        for cano in canos:
            cano.desenhar(TELA)
        
        # Desenha Pássaro
        passaro.desenhar(TELA)
        
        # Desenha Pontuação
        texto_pontuacao = FONTE.render(f"Pontuação: {pontuacao}", True, BRANCO)
        TELA.blit(texto_pontuacao, (10, 10))

        # --- 4. Estado de Fim de Jogo ---
        if not jogo_ativo:
            # Se o jogo não está ativo, exibe a tela de Fim de Jogo
            texto_fim = FONTE_GRANDE.render("FIM DE JOGO", True, (255, 50, 50))
            texto_clique = FONTE.render("Clique para Recomeçar", True, BRANCO)
            
            TELA.blit(texto_fim, (TELA_LARGURA // 2 - texto_fim.get_width() // 2, TELA_ALTURA // 3))
            TELA.blit(texto_clique, (TELA_LARGURA // 2 - texto_clique.get_width() // 2, TELA_ALTURA // 3 + 80))


        # Atualiza o display e controla o FPS
        pygame.display.flip()
        RELOGIO.tick(60) # 60 FPS


if __name__ == '__main__':
    # Loop para permitir reinício
    while True:
        try:
            jogo_principal()
        except pygame.error as e:
            # Captura erro de saída do Pygame (janela fechada)
            print(f"Erro do Pygame: {e}")
            break
        except Exception as e:
            print(f"Ocorreu um erro: {e}. Encerrando.")
            break
    
    pygame.quit()