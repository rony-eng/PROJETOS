import pygame
import sys

# --- Configurações Iniciais ---
pygame.init()

# Configurações da Janela
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Clássico")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Taxa de Quadros (FPS)
FPS = 60
clock = pygame.time.Clock()

# --- Configurações do Jogo ---

# Dimensões e Velocidade das Pás (Paletas)
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
PADDLE_SPEED = 6

# Posição e Objeto da Pá Esquerda
left_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
left_score = 0

# Posição e Objeto da Pá Direita
right_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_score = 0

# Configurações da Bola
BALL_SIZE = 15
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
# Velocidade inicial e direção da bola
ball_dx = 5  # Velocidade horizontal
ball_dy = 5  # Velocidade vertical

# Fonte para a Pontuação
score_font = pygame.font.Font(None, 74)

# --- Funções do Jogo ---

def draw_elements():
    """Desenha todos os elementos do jogo no ecrã."""
    SCREEN.fill(BLACK)

    # Desenhar Pás
    pygame.draw.rect(SCREEN, WHITE, left_paddle)
    pygame.draw.rect(SCREEN, WHITE, right_paddle)

    # Desenhar Bola
    pygame.draw.ellipse(SCREEN, WHITE, ball)

    # Linha central (opcional, para estética)
    pygame.draw.aaline(SCREEN, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Desenhar Pontuação
    left_text = score_font.render(f"{left_score}", True, WHITE)
    SCREEN.blit(left_text, (WIDTH // 4, 20))
    right_text = score_font.render(f"{right_score}", True, WHITE)
    SCREEN.blit(right_text, (WIDTH * 3 // 4 - right_text.get_width(), 20))

    pygame.display.flip()

def move_paddles():
    """Move as pás com base na entrada do teclado e mantém dentro dos limites."""
    keys = pygame.key.get_pressed()

    # Movimento da Pá Esquerda (W e S)
    if keys[pygame.K_w]:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s]:
        left_paddle.y += PADDLE_SPEED

    # Movimento da Pá Direita (Seta Para Cima e Seta Para Baixo)
    if keys[pygame.K_UP]:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN]:
        right_paddle.y += PADDLE_SPEED

    # Garantir que as pás não saiam do ecrã
    if left_paddle.top < 0:
        left_paddle.top = 0
    if left_paddle.bottom > HEIGHT:
        left_paddle.bottom = HEIGHT

    if right_paddle.top < 0:
        right_paddle.top = 0
    if right_paddle.bottom > HEIGHT:
        right_paddle.bottom = HEIGHT

def move_ball():
    """Atualiza a posição da bola e lida com as colisões na parede."""
    global ball_dx, ball_dy, left_score, right_score

    # Mover a bola
    ball.x += ball_dx
    ball.y += ball_dy

    # Colisão Superior e Inferior (inverte o eixo Y)
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    # Pontuação (Se a bola sair das laterais)
    if ball.left <= 0:
        # Ponto para o jogador da direita
        right_score += 1
        reset_ball()
    elif ball.right >= WIDTH:
        # Ponto para o jogador da esquerda
        left_score += 1
        reset_ball()

def reset_ball():
    """Redefine a bola para o centro e inverte a direção horizontal para o lado que perdeu."""
    global ball_dx, ball_dy
    ball.center = (WIDTH // 2, HEIGHT // 2)
    
    # Inverter a direção horizontal para reiniciar o serviço no lado oposto
    ball_dx *= -1
    # Reiniciar a velocidade vertical para evitar colisões imediatas
    ball_dy = 5 if ball_dy > 0 else -5

def check_collision():
    """Verifica a colisão da bola com as pás e inverte a direção horizontal."""
    global ball_dx, ball_dy

    # Colisão com a Pá Direita
    if ball.colliderect(right_paddle) and ball_dx > 0:
        # Aumentar ligeiramente a velocidade para um jogo mais dinâmico
        ball_dx *= -1.05
        
        # Ajuste vertical dependendo de onde a bola bateu na pá
        center_y = right_paddle.centery
        diff = ball.centery - center_y
        ball_dy = diff * 0.1 # Ajuste a sensibilidade

    # Colisão com a Pá Esquerda
    if ball.colliderect(left_paddle) and ball_dx < 0:
        # Aumentar ligeiramente a velocidade
        ball_dx *= -1.05
        
        # Ajuste vertical
        center_y = left_paddle.centery
        diff = ball.centery - center_y
        ball_dy = diff * 0.1 # Ajuste a sensibilidade

# --- Loop Principal do Jogo ---
def game_loop():
    running = True
    while running:
        # 1. Entrada de Eventos (Fechar o Jogo)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Saída ao pressionar ESC
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # 2. Atualização do Jogo
        move_paddles()
        move_ball()
        check_collision()

        # 3. Desenho
        draw_elements()

        # Limitar a taxa de quadros (FPS)
        clock.tick(FPS)

    # 4. Sair do Jogo
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    game_loop()