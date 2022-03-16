import pygame
from player import Player


# настройки экрана
WIDTH = 800
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Моя игра")

# настройки игроков
player = Player(screen, centerx=100)
opponent = Player(screen, centerx=700, is_auto=True)
clock = pygame.time.Clock()

while True: 
	screen.fill((0, 0, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	keys = pygame.key.get_pressed()

# вызов функций
	player.draw()
	player.control(keys)
	opponent.draw()
	opponent.control(keys)
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
