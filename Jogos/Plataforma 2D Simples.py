import pygame
import sys
import os

# Configurações iniciais do Pygame
pygame.init()

# --- Configurações da Janela ---
# Definição do tamanho da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Criação da tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Plataforma Simples 2D")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

# --- Configurações do Jogo ---
CLOCK = pygame.time.Clock()
FPS = 60
GRAVITY = 1
JUMP_STRENGTH = -15
PLAYER_SPEED = 5

# --- Classes do Jogo ---

class Player(pygame.sprite.Sprite):
    """Representa o personagem controlável do jogador."""
    def __init__(self, x, y):
        super().__init__()
        # Criação do retângulo do jogador (o visual)
        self.image = pygame.Surface((32, 32))
        self.image.fill(BLUE) # Cor do jogador: Azul
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Variáveis de movimento
        self.change_x = 0
        self.change_y = 0
        self.on_ground = False # Indica se o jogador está sobre uma plataforma

    def apply_gravity(self):
        """Aplica a gravidade ao movimento vertical."""
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += GRAVITY

        # Limite máximo de queda para evitar aceleração infinita
        if self.change_y > 15:
            self.change_y = 15

    def jump(self):
        """Permite que o jogador salte se estiver no chão."""
        if self.on_ground:
            self.change_y = JUMP_STRENGTH
            self.on_ground = False # O jogador não está mais no chão

    def go_left(self):
        """Define o movimento para a esquerda."""
        self.change_x = -PLAYER_SPEED

    def go_right(self):
        """Define o movimento para a direita."""
        self.change_x = PLAYER_SPEED

    def stop(self):
        """Para o movimento horizontal."""
        self.change_x = 0

    def update(self, platform_list):
        """Atualiza a posição do jogador e verifica colisões."""
        # 1. Aplica a gravidade antes de mover na vertical
        self.apply_gravity()

        # 2. Movimento horizontal
        self.rect.x += self.change_x

        # 3. Colisão horizontal
        block_hit_list = pygame.sprite.spritecollide(self, platform_list, False)
        for block in block_hit_list:
            # Se estamos nos movendo para a direita, definimos o lado direito no lado esquerdo do bloco
            if self.change_x > 0:
                self.rect.right = block.rect.left
            # Se estamos nos movendo para a esquerda, definimos o lado esquerdo no lado direito do bloco
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        # 4. Movimento vertical
        self.rect.y += self.change_y

        # 5. Colisão vertical
        self.on_ground = False # Assumimos que não estamos no chão, até que a colisão prove o contrário
        block_hit_list = pygame.sprite.spritecollide(self, platform_list, False)

        for block in block_hit_list:
            # Colisão vinda de cima (pouso)
            if self.change_y > 0:
                self.rect.bottom = block.rect.top # Coloca o jogador exatamente no topo
                self.on_ground = True
            # Colisão vinda de baixo (bate a cabeça)
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom # Coloca o jogador exatamente abaixo

            # Para qualquer colisão vertical, a velocidade vertical é zerada
            self.change_y = 0

        # 6. Colisão com os limites da tela (chão inferior)
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.change_y = 0
            self.on_ground = True


class Platform(pygame.sprite.Sprite):
    """Representa uma plataforma estática no jogo."""
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN) # Cor da plataforma: Verde
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# --- Criação de Objetos e Grupos ---

# Lista para todas as sprites (Desenho)
all_sprites = pygame.sprite.Group()
# Lista para todas as plataformas (Colisão)
platform_list = pygame.sprite.Group()

# Cria o jogador
player = Player(50, SCREEN_HEIGHT - 32)
all_sprites.add(player)

# Coordenadas: (x, y, largura, altura) das plataformas
level_platforms = [
    # Chão principal
    (0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, 20),
    # Plataformas flutuantes
    (150, 450, 150, 20),
    (350, 350, 150, 20),
    (550, 250, 150, 20),
    (10, 500, 100, 20),
    (650, 400, 100, 20),
]

# Cria as plataformas a partir da lista
for p_info in level_platforms:
    x, y, w, h = p_info
    platform = Platform(x, y, w, h)
    all_sprites.add(platform)
    platform_list.add(platform)

# --- Loop Principal do Jogo ---
running = True
while running:
    # --- 1. Processamento de Eventos (Entrada do Usuário) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Eventos de teclado para pressionar
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.go_left()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player.go_right()
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP or event.key == pygame.K_w:
                player.jump() # Tenta saltar

        # Eventos de teclado para soltar
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and player.change_x < 0:
                player.stop()
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and player.change_x > 0:
                player.stop()

    # --- 2. Lógica do Jogo (Atualização) ---
    # Passamos a lista de plataformas para o método update do jogador
    all_sprites.update(platform_list)

    # --- 3. Desenho ---
    # Preenche o fundo com branco (ou outra cor)
    screen.fill(WHITE)

    # Desenha todas as sprites (jogador e plataformas)
    all_sprites.draw(screen)

    # --- 4. Atualiza a Tela e Sincroniza o Tempo ---
    pygame.display.flip()
    CLOCK.tick(FPS) # Limita o jogo a 60 frames por segundo

# Sai do Pygame e do sistema
pygame.quit()
sys.exit()