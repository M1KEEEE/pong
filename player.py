import pygame

class Player(pygame.sprite.Sprite):
	def __init__(
		self, 
		screen, 
		width=10, 
		height=100, 
		color=(255, 255, 255),
		centerx=100,
		centery=100,
		velocity=10
	):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.image = pygame.Surface((width, height))
		self.image.fill((color))
		self.rect = self.image.get_rect()
		self.rect.centerx = centerx
		self.rect.centery = centery
	
	def draw(self):
		self.screen.blit(self.image, self.rect)
