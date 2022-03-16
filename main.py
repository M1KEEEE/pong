import pygame
from player import Player

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Моя игра")

all_sprites = pygame.sprite.Group()
player = Player(screen, centerx=300, centery=300)
opponent = Player(screen)
clock = pygame.time.Clock()

while True: 
	screen.fill((0, 0, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	keys = pygame.key.get_pressed()

	player.draw()
	opponent.draw()
	pygame.display.flip()
	clock.tick(60)

pygame.quit()
