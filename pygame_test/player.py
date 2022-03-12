import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self, width, height):
		super().__init__()
		self.image = pygame.Surface((25, 150))
		self.image.fill((255, 255, 255))
		self.rect = self.image.get_rect()
		self.rect.center = (screen_width // 2, screen_height // 2)
