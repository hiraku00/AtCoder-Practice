import pygame
import sys
import random

# 画面サイズ
WIDTH = 800
HEIGHT = 600

# 色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# プレイヤーのサイズと初期位置
PLAYER_SIZE = 50
PLAYER_X = WIDTH // 2 - PLAYER_SIZE // 2
PLAYER_Y = HEIGHT - PLAYER_SIZE - 10
PLAYER_SPEED = 5
JUMP_POWER = 15
GRAVITY = 1

# 障害物のサイズと位置、移動速度
OBSTACLE_SIZE = 50
OBSTACLE_X = WIDTH // 2 - OBSTACLE_SIZE // 2
OBSTACLE_Y = HEIGHT // 2 - OBSTACLE_SIZE
OBSTACLE_BASE_SPEED = 3  # 基本速度
obstacle_speed_x = OBSTACLE_BASE_SPEED
obstacle_speed_y = OBSTACLE_BASE_SPEED
obstacle_direction_x = random.choice([-1, 1])
obstacle_direction_y = random.choice([-1, 1])
CHANGE_DIRECTION_INTERVAL = 60 # 〇フレームごとに方向を変える

# スコア
score = 0
frame_count = 0

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("シンプルなゲーム")

player_rect = pygame.Rect(PLAYER_X, PLAYER_Y, PLAYER_SIZE, PLAYER_SIZE)
obstacle_rect = pygame.Rect(OBSTACLE_X, OBSTACLE_Y, OBSTACLE_SIZE, OBSTACLE_SIZE)

clock = pygame.time.Clock()
is_jumping = False
jump_count = 0
game_over = False
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and not is_jumping:
                    is_jumping = True
                    jump_count = JUMP_POWER

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player_rect.x += PLAYER_SPEED

        # ジャンプ処理
        if is_jumping:
            player_rect.y -= jump_count
            jump_count -= GRAVITY
            if jump_count < -JUMP_POWER:
                is_jumping = False

        # 画面外に出た時の処理 (プレイヤー)
        if player_rect.left < 0:
            player_rect.right = WIDTH
        if player_rect.right > WIDTH:
            player_rect.left = 0
        if player_rect.top < 0:
            player_rect.bottom = HEIGHT
        if player_rect.bottom > HEIGHT:
            player_rect.top = 0

        # 障害物の移動 (予測不可能に)
        obstacle_rect.x += obstacle_speed_x * obstacle_direction_x
        obstacle_rect.y += obstacle_speed_y * obstacle_direction_y

        # 画面端で反射
        if obstacle_rect.right > WIDTH:
            obstacle_direction_x = -1
        elif obstacle_rect.left < 0:
            obstacle_direction_x = 1
        if obstacle_rect.bottom > HEIGHT:
            obstacle_direction_y = -1
        elif obstacle_rect.top < 0:
            obstacle_direction_y = 1

        # 一定間隔で速度と方向をランダムに変更
        if frame_count % CHANGE_DIRECTION_INTERVAL == 0:
            obstacle_speed_x = random.uniform(OBSTACLE_BASE_SPEED, OBSTACLE_BASE_SPEED * 2) # 速度を少しランダムに
            obstacle_speed_y = random.uniform(OBSTACLE_BASE_SPEED, OBSTACLE_BASE_SPEED * 2) # 速度を少しランダムに
            obstacle_direction_x = random.choice([-1, 1])
            obstacle_direction_y = random.choice([-1, 1])

        # 衝突判定
        if player_rect.colliderect(obstacle_rect):
            game_over = True

        # スコア加算
        score += 1
        frame_count += 1

    # 描画
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, player_rect)
    pygame.draw.rect(screen, RED, obstacle_rect)

    if game_over:
        text = font.render("Game Over! Score: " + str(score // 60), True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
    else:
        score_text = font.render("Score: " + str(score // 60), True, BLACK)
        screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
