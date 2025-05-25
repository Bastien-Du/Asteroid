import pygame
from constants import * 
from player import *
from asteroidfield import *
from asteroid import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print ("Starting Asteroids!")
	print (f"Screen width: {SCREEN_WIDTH}")
	print (f"Screen height: {SCREEN_HEIGHT}")

	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	CircleShape.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable,)

	player = Player(x, y)

	field = AsteroidField()

	clock = pygame.time.Clock()
	dt = clock.tick(60)


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return
		screen.fill((0, 0, 0))
		updatable.update(dt)
		for x in drawable:
			x.draw(screen)
		clock.tick(60)
		pygame.display.flip()


if __name__ == "__main__":
    main()
