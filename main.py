"""
    ЗВУКИ!
"""

import pygame
from paddle import Paddle
from ball import Ball
from score import Score


pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH = pygame.display.Info().current_w
HEIGHT = pygame.display.Info().current_h
pygame.display.set_caption("Моя игра")

player = Paddle(screen, centerx=WIDTH * 0.05)
opponent = Paddle(screen, centerx=WIDTH * 0.95, is_auto=True)
ball = Ball(screen)
player_score = Score(screen, owner=player, centerx=WIDTH * 0.4)
opponent_score = Score(screen, owner=opponent, centerx=WIDTH * 0.6)
clock = pygame.time.Clock()

game = True
while game:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        game = False

    if keys[pygame.K_q]:
        ball.move_to_center()


    player.draw()
    opponent.draw()
    ball.draw()
    player_score.draw()
    opponent_score.draw()

    player.control(keys, ball)
    opponent.control(keys, ball)
    ball.movement(player, opponent)
    ball.goal(player_score, opponent_score, player, opponent)

    player_score.update()
    opponent_score.update()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
