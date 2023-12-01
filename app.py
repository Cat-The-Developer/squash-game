import pygame
import random

# input player names
# player1_name = input("Enter player 1 name: ").title() + ": "
# player2_name = input("Enter player 2 name: ").title() + ": "
player1_name = "You" + ": "
player2_name = "Meow the destroyer (also you)" + ": "


# initialize
pygame.init()
screen = pygame.display.set_mode(size=(1280, 720), flags=pygame.RESIZABLE)
pygame.display.set_caption("phase 1")
clock = pygame.time.Clock()
dt = 0

# screen size
screen_width = screen.get_width()
screen_height = screen.get_height()

# player 1 pedal position
player1_rect_left = screen_width / 4
player1_rect_top = screen_height - 100

# player 2 pedal position
player2_rect_left = screen_width / 1.5
player2_rect_top = screen_height - 100

running = True

font = pygame.font.Font(None, 36)

# ball
ball_radius = 10
ball_speed = [300, 300]
ball_position = [screen_width // 2, screen_height // 2]
ball_color = "white"

# initialize scores
score_player1 = 0
score_player2 = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    # a line showing the playable area of the respective player
    dividing_line_horizontal = pygame.Rect((0, screen_height // 2 - 25), (screen_width, 4))
    dividing_line_vertical = pygame.Rect((screen_width // 2, screen_height // 2 - 25), (4, screen_height // 2 + 25))

    # keys binding
    keys = pygame.key.get_pressed()

    # key binding for player 1 pedal
    if keys[pygame.K_w] and player1_rect_top >= screen_height // 2 - 25:
        player1_rect_top -= 300 * dt
    if keys[pygame.K_s] and player1_rect_top + 10 <= screen_height:
        player1_rect_top += 300 * dt
    if keys[pygame.K_a] and player1_rect_left >= 0:
        player1_rect_left -= 300 * dt
    if keys[pygame.K_d] and player1_rect_left + screen_width / 10 <= screen_width // 2:
        player1_rect_left += 300 * dt

    # key binding for player 2 pedal
    if keys[pygame.K_UP] and player2_rect_top >= screen_height // 2 - 25:
        player2_rect_top -= 300 * dt
    if keys[pygame.K_DOWN] and player2_rect_top + 10 <= screen_height:
        player2_rect_top += 300 * dt
    if keys[pygame.K_LEFT] and player2_rect_left >= screen_width // 2:
        player2_rect_left -= 300 * dt
    if keys[pygame.K_RIGHT] and player2_rect_left + screen_width / 10 <= screen_width:
        player2_rect_left += 300 * dt

    # pedals
    player1_rect = pygame.Rect((player1_rect_left, player1_rect_top), (screen_width / 10, 10))
    player2_rect = pygame.Rect((player2_rect_left, player2_rect_top), (screen_width / 10, 10))

    # move the ball
    ball_position[0] += ball_speed[0] * dt
    ball_position[1] += ball_speed[1] * dt

    # check collision with top and bottom walls
    if ball_position[1] - ball_radius < 0 or ball_position[1] + ball_radius > screen_height:
        ball_speed[1] = -ball_speed[1]  # Reflect the ball vertically

    if ball_position[0] - ball_radius < 0 or ball_position[0] + ball_radius > screen_width:
        ball_speed[0] = -ball_speed[0]  # Reflect the ball vertically

    # check collision with player 1
    if player1_rect.colliderect(pygame.Rect((ball_position[0] - ball_radius, ball_position[1] - ball_radius),
                                        (2 * ball_radius, 2 * ball_radius))):
        if ball_speed[1] > 0:  # Ball is moving downward
            ball_speed[1] = -abs(ball_speed[1]) * 1.01  # Increase the ball speed and reflect vertically
        else:
            ball_speed[1] = abs(ball_speed[1]) * 1.01  # Increase the ball speed and reflect vertically

        ball_position[1] = player1_rect_top - ball_radius  # Adjust ball position to prevent overlap

        if ball_speed[0] > 0:
            ball_speed[0] = -abs(ball_speed[0]) * 1.01  # Increase the ball speed and reflect horizontally
        else:
            ball_speed[0] = abs(ball_speed[0]) * 1.01  # Increase the ball speed and reflect horizontally

        ball_color = "white"

    # check collision with player 2
    if player2_rect.colliderect(pygame.Rect((ball_position[0] - ball_radius, ball_position[1] - ball_radius),
                                        (2 * ball_radius, 2 * ball_radius))):
        if ball_speed[1] > 0:  # Ball is moving downward
            ball_speed[1] = -abs(ball_speed[1]) * 1.01  # Increase the ball speed and reflect vertically
        else:
            ball_speed[1] = abs(ball_speed[1]) * 1.01  # Increase the ball speed and reflect vertically

        ball_position[1] = player2_rect_top - ball_radius  # Adjust ball position to prevent overlap

        if ball_speed[0] > 0:
            ball_speed[0] = -abs(ball_speed[0]) * 1.01  # Increase the ball speed and reflect horizontally
        else:
            ball_speed[0] = abs(ball_speed[0]) * 1.01  # Increase the ball speed and reflect horizontally

        ball_color = "orange"

    # check scoring
    if ball_position[1] + ball_radius > screen_height and ball_position[0] + ball_radius < screen_width //2:
        score_player2 += 1
        print(score_player2)
    elif ball_position[1] + ball_radius > screen_height and ball_position[0] + ball_radius > screen_width //2:
        score_player1 += 1
        print(score_player1)

    # rendering player 1 name
    player1 = font.render(player1_name + str(score_player1), True, "white")
    player1_name_rect = player1.get_rect()
    player1_name_rect.left = 25
    player1_name_rect.top = 50

    # rendering player 2 name
    player2 = font.render(player2_name + str(score_player2) , True, "orange")
    player2_name_rect = player2.get_rect()
    player2_name_rect.left = 25
    player2_name_rect.top = 100

    # rendering this
    screen.fill("black")
    pygame.draw.rect(screen, "white", player1_rect)
    pygame.draw.rect(screen, "orange", player2_rect)
    pygame.draw.rect(screen, "gray", dividing_line_horizontal)
    pygame.draw.rect(screen, "gray", dividing_line_vertical)
    screen.blit(player1, player1_name_rect)
    screen.blit(player2, player2_name_rect)

    # render ball
    pygame.draw.circle(screen, ball_color, (int(ball_position[0]), int(ball_position[1])), ball_radius)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
