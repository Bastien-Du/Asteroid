import sys
import pygame
from constants import *
from player import *
from asteroidfield import *
from asteroid import *
from bullet import *
from circleshape import *


def show_menu(screen):
	running = True
	font = pygame.font.SysFont(None, 72)
	screen.fill("black")
	text = font.render("Press SPACE to Start", True, "white")
	screen.blit(text, (400, 300))   # Adjust as you like
	pygame.display.flip()

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return False     # Player closed window
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				running = False # Player pressed SPACE to start
	return True

def game_runnning():
	pygame.init()
	pygame.font.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
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
	score = 0
	lives = 3

	score_police = pygame.font.SysFont('arial', 30)
	lives_police = pygame.font.SysFont('arial', 30)

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
					score += 10

		for asteroid in asteroids:
				if asteroid.collision(player) and player.immunity_time <= 0:
					lives -= 1
					player.kill()
					if lives > 0:
						player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
						player.immunity_time = PLAYER_IMMUNITY_TIME
					if lives == 0:
						lives = 3
						score = 0
						asteroids.empty()
						drawable.empty()
						updatable.empty()
						return



		player.immunity_time -= dt

		for x in drawable:
			x.draw(screen)

		pygame.draw.rect(screen, "black", pygame.Rect(0, 0, SCREEN_WIDTH, 50))
		lives_surface = lives_police.render('Live(s): ' + str(lives-1), False, "red")
		screen.blit(lives_surface,(SCREEN_WIDTH - 150,10))
		score_surface = score_police.render('Score: '+ str(score), False, (255,255,255))
		screen.blit(score_surface, (10,10))


		pygame.display.flip()



		dt = clock.tick(60) / 1000

def main():
	pygame.init()
	pygame.font.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	menu = show_menu(screen)
	if  menu == True:
		game_runnning()


if __name__ == "__main__":
    main()
