import pygame
import sys
import math
import random

# --- Inicialização e Configurações ---
pygame.init()

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (200, 50, 50)
AZUL_TORRE = (50, 50, 200)
VERDE_VIDA = (50, 200, 50)
CINZA_CAMINHO = (150, 150, 150)
AMARELO_UI = (255, 200, 0)

# Configurações da Tela
LARGURA_TELA = 1200
ALTURA_TELA = 700
TELA = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("PyTower Defense Simples")
FONTE_UI = pygame.font.Font(None, 36)

# Configurações do Jogo
FPS = 60
clock = pygame.time.Clock()

# Posições para o Caminho do Inimigo (uma lista de tuplas (x, y))
# O inimigo percorrerá estes pontos em sequência.
CAMINHO = [
    (100, 100),
    (100, 600),
    (700, 600),
    (700, 300),
    (1100, 300),
    (1100, 750) # Ponto final fora da tela
]

# --- Classes do Jogo ---

class Inimigo(pygame.sprite.Sprite):
    """Representa um inimigo que segue o CAMINHO."""
    def __init__(self, caminho, vida_base=50, velocidade=2):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(VERMELHO)
        self.rect = self.image.get_rect()
        self.caminho = caminho
        self.ponto_caminho_atual = 0
        self.rect.center = self.caminho[0]
        self.velocidade = velocidade
        self.vida = vida_base
        self.vida_maxima = vida_base
        self.recompensa = 10 # Dinheiro ganho ao derrotar

    def mover(self):
        """Calcula o movimento em direção ao próximo ponto do caminho."""
        if self.ponto_caminho_atual < len(self.caminho) - 1:
            alvo_x, alvo_y = self.caminho[self.ponto_caminho_atual + 1]
            
            dx = alvo_x - self.rect.centerx
            dy = alvo_y - self.rect.centery
            distancia = math.hypot(dx, dy)
            
            if distancia < self.velocidade:
                # Se perto o suficiente, mude para o próximo ponto
                self.ponto_caminho_atual += 1
                self.rect.centerx = alvo_x
                self.rect.centery = alvo_y
            else:
                # Mova-se na direção do alvo
                vetor_x = dx / distancia
                vetor_y = dy / distancia
                self.rect.x += vetor_x * self.velocidade
                self.rect.y += vetor_y * self.velocidade
        else:
            # Chegou ao fim do caminho
            self.kill()
            return True # Sinaliza que o inimigo escapou
        return False

    def levar_dano(self, dano):
        """Reduz a vida do inimigo."""
        self.vida -= dano
        if self.vida <= 0:
            self.morrer()
            return True # Sinaliza que o inimigo morreu
        return False

    def morrer(self):
        """Remove o inimigo do jogo."""
        self.kill()

    def atualizar(self):
        """Atualiza o estado do inimigo (apenas movimento)."""
        return self.mover()
        
    def desenhar_barra_vida(self, tela):
        """Desenha a barra de vida acima do inimigo."""
        barra_largura = 25
        barra_altura = 4
        porcentagem_vida = self.vida / self.vida_maxima
        vida_atual_largura = int(porcentagem_vida * barra_largura)

        # Fundo da barra (Preto)
        pygame.draw.rect(tela, PRETO, (self.rect.x - 2, self.rect.y - 10, barra_largura + 2, barra_altura + 2), 0, 3)
        # Vida atual (Verde)
        pygame.draw.rect(tela, VERDE_VIDA, (self.rect.x - 1, self.rect.y - 9, vida_atual_largura, barra_altura), 0, 3)
        
        # Opcional: Desenhar contorno de alcance (para depuração)
        # pygame.draw.circle(tela, VERMELHO, self.rect.center, 50, 1)

class Torre(pygame.sprite.Sprite):
    """Representa uma torre que ataca inimigos automaticamente."""
    def __init__(self, x, y, custo=100, dano=10, alcance=120, taxa_tiro=30):
        super().__init__()
        self.image = pygame.Surface([40, 40])
        self.image.fill(AZUL_TORRE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x - 20, y - 20) # Centraliza a torre no clique
        self.custo = custo
        self.dano = dano
        self.alcance = alcance
        self.taxa_tiro = taxa_tiro  # Intervalo de frames entre tiros
        self.contador_tiro = 0
        self.alvo = None

    def encontrar_alvo(self, inimigos):
        """Encontra o inimigo mais próximo dentro do alcance."""
        if self.alvo and self.alvo.alive() and self.esta_no_alcance(self.alvo):
            return self.alvo # Mantém o alvo atual
        
        self.alvo = None
        
        for inimigo in inimigos:
            if self.esta_no_alcance(inimigo):
                # Implementação simples: escolhe o primeiro que encontrar
                self.alvo = inimigo
                return inimigo
        return None

    def esta_no_alcance(self, inimigo):
        """Verifica se o inimigo está dentro do alcance da torre."""
        distancia = math.hypot(inimigo.rect.centerx - self.rect.centerx, inimigo.rect.centery - self.rect.centery)
        return distancia <= self.alcance

    def atirar(self, inimigo):
        """Aplica dano ao alvo e reseta o contador de tiro."""
        inimigo_morreu = inimigo.levar_dano(self.dano)
        self.contador_tiro = 0
        return inimigo_morreu

    def atualizar(self, inimigos):
        """Lógica de tiro e atualização da torre."""
        self.contador_tiro += 1
        alvo = self.encontrar_alvo(inimigos)
        
        if alvo and self.contador_tiro >= self.taxa_tiro:
            # Atira no alvo
            return self.atirar(alvo)
        
        return False
        
    def desenhar_alcance(self, tela):
        """Desenha um círculo para visualizar o alcance da torre."""
        s = pygame.Surface((self.alcance * 2, self.alcance * 2), pygame.SRCALPHA)
        pygame.draw.circle(s, (100, 100, 255, 50), (self.alcance, self.alcance), self.alcance)
        tela.blit(s, (self.rect.centerx - self.alcance, self.rect.centery - self.alcance))
        # Desenha a borda do alcance para feedback visual
        pygame.draw.circle(tela, AZUL_TORRE, self.rect.center, self.alcance, 1)

# --- Funções Auxiliares ---

def desenhar_caminho(tela, caminho):
    """Desenha a representação visual do caminho."""
    pygame.draw.lines(tela, CINZA_CAMINHO, False, caminho, 40)
    # Desenhar os pontos de início e fim
    pygame.draw.circle(tela, VERDE_VIDA, caminho[0], 20)
    pygame.draw.circle(tela, VERMELHO, caminho[-2], 20)


def desenhar_ui(tela, dinheiro, vida, onda):
    """Desenha a interface do usuário (Dinheiro, Vida, Onda)."""
    # Fundo da UI
    pygame.draw.rect(tela, PRETO, (0, 0, LARGURA_TELA, 50))
    pygame.draw.line(tela, AMARELO_UI, (0, 50), (LARGURA_TELA, 50), 2)
    
    # Dinheiro
    texto_dinheiro = FONTE_UI.render(f"Dinheiro: ${dinheiro}", True, AMARELO_UI)
    tela.blit(texto_dinheiro, (10, 10))
    
    # Vida
    texto_vida = FONTE_UI.render(f"Vida: {vida}", True, VERDE_VIDA)
    tela.blit(texto_vida, (LARGURA_TELA // 2 - texto_vida.get_width() // 2, 10))
    
    # Onda
    texto_onda = FONTE_UI.render(f"Onda: {onda}", True, BRANCO)
    tela.blit(texto_onda, (LARGURA_TELA - texto_onda.get_width() - 10, 10))


# --- Lógica do Jogo Principal ---

def main():
    # Variáveis do Jogo
    dinheiro = 500
    vida = 20
    custo_torre = 100
    onda = 1
    
    # Grupos de Sprites
    todas_sprites = pygame.sprite.Group()
    inimigos = pygame.sprite.Group()
    torres = pygame.sprite.Group()
    
    # Estado da Construção
    modo_construcao = False
    torre_sendo_colocada = None

    # Lógica da Onda (Spawn de Inimigos)
    tempo_ultima_onda = pygame.time.get_ticks()
    intervalo_onda = 10000 # 10 segundos entre ondas
    
    def iniciar_onda(numero_onda):
        """Gera inimigos com base no número da onda."""
        num_inimigos = 5 + numero_onda * 2
        vida_inimigo = 50 + numero_onda * 15
        velocidade = 1.5 + numero_onda * 0.1
        
        # Gera os inimigos com um pequeno atraso entre eles
        for i in range(num_inimigos):
            # Cria um closure para atrasar a adição do inimigo
            pygame.time.set_timer(pygame.USEREVENT + i, 500 * i, 1)
            
            # Adiciona o novo inimigo ao grupo quando o evento customizado disparar
            # (Simplificado para este exemplo; em um jogo real, usaria uma fila)
            # Para este exemplo simples, vamos apenas adicionar todos imediatamente
            # para não complicar com eventos customizados de tempo.
            novo_inimigo = Inimigo(CAMINHO, vida_base=vida_inimigo, velocidade=velocidade)
            inimigos.add(novo_inimigo)
            todas_sprites.add(novo_inimigo)


    # Inicia a primeira onda
    iniciar_onda(onda)

    # --- Loop Principal do Jogo ---
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = event.pos
                
                # Clique esquerdo para iniciar/colocar torre
                if event.button == 1: 
                    # Se estiver em modo de construção e tiver dinheiro
                    if modo_construcao and dinheiro >= custo_torre:
                        # Verifica se está fora da área da UI (y > 50)
                        if pos_y > 50:
                            # Coloca a torre
                            nova_torre = Torre(pos_x, pos_y, custo=custo_torre)
                            torres.add(nova_torre)
                            todas_sprites.add(nova_torre)
                            dinheiro -= custo_torre
                            modo_construcao = False # Sai do modo de construção
                            torre_sendo_colocada = None
                        else:
                            print("Não é possível construir na área da UI.")
                    
                    # Se não estiver em modo de construção e o clique for no botão "Construir" (exemplo de botão na UI)
                    elif pos_y < 50 and pos_x < 150: # Simplesmente assume um botão na parte superior esquerda
                        if dinheiro >= custo_torre:
                            modo_construcao = True
                            print("Modo de Construção Ativado. Clique no mapa para posicionar.")
                        else:
                            print("Dinheiro insuficiente para construir uma torre.")
                    
                    # Se não estiver em modo de construção, clique em uma torre para ver o alcance (opcional)
                    else:
                        for torre in torres:
                            if torre.rect.collidepoint(event.pos):
                                torre_sendo_colocada = torre # Usa essa variável para desenhar o alcance

                # Clique direito para cancelar o modo de construção
                elif event.button == 3: 
                    modo_construcao = False
                    torre_sendo_colocada = None
                    print("Modo de Construção Cancelado.")


        # --- Atualizações do Jogo ---

        # 1. Movimento e Dano dos Inimigos
        for inimigo in inimigos:
            # O inimigo tenta se mover. Se retornar True, significa que escapou.
            escapou = inimigo.atualizar()
            if escapou:
                vida -= 1
                if vida <= 0:
                    running = False # Fim do jogo
                    print("GAME OVER! Sua base foi destruída.")
                    
        # 2. Ataque das Torres
        for torre in torres:
            # A torre ataca. Se retornar True, significa que um inimigo morreu.
            inimigo_morreu = torre.atualizar(inimigos)
            if inimigo_morreu and torre.alvo.vida <= 0:
                dinheiro += torre.alvo.recompensa # Adiciona a recompensa

        # 3. Lógica da Onda
        if not inimigos and (pygame.time.get_ticks() - tempo_ultima_onda > intervalo_onda):
            onda += 1
            tempo_ultima_onda = pygame.time.get_ticks()
            print(f"Iniciando Onda {onda}!")
            iniciar_onda(onda)

        # 4. Modo de Construção (visualização de alcance)
        if modo_construcao:
            # Cria uma torre temporária para visualização do alcance
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_y > 50: # Não desenha na UI
                temp_torre = Torre(mouse_x, mouse_y)
                torre_sendo_colocada = temp_torre
        
        # --- Desenho (Renderização) ---
        TELA.fill(BRANCO)
        
        # 1. Desenha o Caminho
        desenhar_caminho(TELA, CAMINHO)
        
        # 2. Desenha o Alcance de Pré-visualização ou Seleção
        if torre_sendo_colocada:
            torre_sendo_colocada.desenhar_alcance(TELA)
            
        # 3. Desenha Torres e Inimigos
        todas_sprites.draw(TELA)
        
        # 4. Desenha Barras de Vida dos Inimigos
        for inimigo in inimigos:
            inimigo.desenhar_barra_vida(TELA)
            
        # 5. Desenha a UI (sempre por último)
        desenhar_ui(TELA, dinheiro, vida, onda)

        # Atualiza a tela
        pygame.display.flip()
        
        # Limita o FPS
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()