import pygame
import random
import time

# --- Configurações do Jogo ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
FPS = 10  # Velocidade inicial do jogo

# --- Cores ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
DARK_GRAY = (40, 40, 40)

# --- Inicialização do Pygame ---
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo da Cobrinha (Snake)")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# --- Direções ---
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# --- Classe da Cobrinha ---
class Snake:
    def __init__(self):
        # A cabeça da cobra começa no centro da tela
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.length = 1
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN
        self.score = 0

    def get_head_position(self):
        """Retorna a posição da cabeça da cobra."""
        return self.positions[0]

    def turn(self, point):
        """Muda a direção da cobra, evitando inversão imediata."""
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        self.direction = point

    def move(self):
        """Calcula a nova posição e move a cobra."""
        cur = self.get_head_position()
        x, y = self.direction
        new = (cur[0] + x, cur[1] + y)

        # 1. Verifica colisão com as paredes
        if not (0 <= new[0] < GRID_WIDTH and 0 <= new[1] < GRID_HEIGHT):
            return "wall_collision"

        # 2. Verifica colisão com o próprio corpo
        if len(self.positions) > 2 and new in self.positions[2:]:
            return "self_collision"

        # Adiciona a nova cabeça
        self.positions.insert(0, new)

        # Remove a cauda se não cresceu
        if len(self.positions) > self.length:
            self.positions.pop()

        return "ok"

    def grow(self):
        """Aumenta o tamanho da cobra e a pontuação."""
        self.length += 1
        self.score += 1

    def draw(self, surface):
        """Desenha a cobra na tela."""
        for p in self.positions:
            r = pygame.Rect((p[0] * GRID_SIZE, p[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            # Adiciona uma borda escura para melhor definição
            pygame.draw.rect(surface, BLACK, r, 1)

    def reset(self):
        """Reinicia o estado da cobra para um novo jogo."""
        self.length = 1
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0


# --- Classe da Comida ---
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        """Gera uma nova posição aleatória para a comida."""
        self.position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    def draw(self, surface):
        """Desenha a comida na tela."""
        r = pygame.Rect((self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
        pygame.draw.ellipse(surface, self.color, r)


# --- Função para Desenhar a Pontuação e Mensagens ---
def draw_score(surface, score):
    """Exibe a pontuação atual do jogador."""
    score_text = font.render(f"Pontuação: {score}", True, WHITE)
    surface.blit(score_text, (5, 5))

def draw_message(surface, message):
    """Exibe uma mensagem no centro da tela."""
    text_surface = font.render(message, True, WHITE)
    rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    surface.blit(text_surface, rect)

# --- Função Principal do Jogo ---
def game_loop():
    """O loop principal que contém toda a lógica do jogo."""
    snake = Snake()
    food = Food()
    game_over = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    snake.turn(UP)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    snake.turn(DOWN)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    snake.turn(LEFT)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    snake.turn(RIGHT)
                
                # Permite reiniciar o jogo após Game Over
                if game_over and event.key == pygame.K_SPACE:
                    snake.reset()
                    food.randomize_position()
                    game_over = False

        if not game_over:
            # Lógica de Movimento e Colisão
            collision_status = snake.move()

            if collision_status != "ok":
                game_over = True
                
            # Verifica se a cobra comeu a comida
            if snake.get_head_position() == food.position:
                snake.grow()
                
                # Garante que a nova comida não nasça dentro da cobra
                while food.position in snake.positions:
                    food.randomize_position()

            # --- Desenho na Tela ---
            screen.fill(DARK_GRAY) # Fundo

            food.draw(screen)
            snake.draw(screen)
            draw_score(screen, snake.score)
        else:
            # Tela de Game Over
            draw_message(screen, f"Fim de Jogo! Pontuação Final: {snake.score} | Pressione ESPAÇO para Recomeçar")

        pygame.display.update()
        
        # Controla a velocidade do jogo. Aumenta a velocidade (FPS) baseada na pontuação
        # Para um jogo mais desafiador: FPS = 10 + (snake.score // 5)
        current_fps = FPS + (snake.score // 4) 
        clock.tick(current_fps)

    pygame.quit()

if __name__ == '__main__':
    game_loop()