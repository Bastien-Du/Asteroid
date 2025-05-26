import sys
import pygame
from constants import *
from player import *
from asteroidfield import *
from asteroid import *
from bullet import *
from circleshape import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	print ("Starting Asteroids!")
	print (f"Screen width: {SCREEN_WIDTH}")
	print (f"Screen height: {SCREEN_HEIGHT}")

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	bullet = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	field = AsteroidField()
	Player.containers = (updatable, drawable)
	Bullet.containers = (bullet, updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	dt = 0


	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return


		updatable.update(dt)
		screen.fill((0, 0, 0))

		for asteroid in asteroids:
			for b in bullet:
				if asteroid.collision(b):
					asteroid.split()
					b.kill()

		for asteroid in asteroids:
			if asteroid.collision(player):
				print("Game Over")
				sys.exit()

		for x in drawable:
			x.draw(screen)
		pygame.display.flip()



		dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
