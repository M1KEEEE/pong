import pygame

pygame.mixer.init()
pygame.mixer.music.set_volume(1)

sound = {
    "ball_hit": pygame.mixer.Sound('assets/ball_hit.wav'),
    "score_player": pygame.mixer.Sound('assets/score_player.wav'),
    "score_opponent": pygame.mixer.Sound('assets/score_opponent.wav')
}