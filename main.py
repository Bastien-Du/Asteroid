import sys
import pygame
from constants import *
from player import *
from asteroidfield import *
from asteroid import *
from bullet import *
from circleshape import *

big_font = None
medium_font = None
small_font = None
score = 0

def show_menu(screen):
	running = True
	screen.fill("black")
	title = big_font.render("ASTEROID", True, "white")
	title_x = (SCREEN_WIDTH - title.get_width()) // 2
	screen.blit(title, (title_x, SCREEN_HEIGHT/4))
	play = small_font.render("PLAY", True, "white")
	play_x = (SCREEN_WIDTH // 3 - play.get_width() // 2)
	play_button = screen.blit(play, (play_x, (SCREEN_HEIGHT*2)/3))
	quit = small_font.render("QUIT", True, "white")
	quit_x = (((SCREEN_WIDTH*2)/3) - quit.get_width() // 2)
	quit_button = screen.blit(quit,(quit_x,(SCREEN_HEIGHT*2)/3))
	weapon = small_font.render("WEAPON", True, "white")
	weapon_x = ((SCREEN_WIDTH // 3) - quit.get_width() // 2)
	weapon_button = screen.blit(weapon,(weapon_x,(SCREEN_HEIGHT*2)/3 + 120 ))
	pygame.display.flip()

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return False     # Player closed window
			if event.type == pygame.MOUSEBUTTONDOWN:
				if play_button.collidepoint(event.pos):
					running = False
				if weapon_button.collidepoint(event.pos):
					result = weapon_menu()
					if result == "back":
						show_menu(screen)
				if quit_button.collidepoint(event.pos):
					return False
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
	lives = 3
	global score

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

def weapon_menu():
	running = True
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	screen.fill("black")
	basic = medium_font.render("BASIC", True, "white")
	basic_x = ((SCREEN_WIDTH/4) - basic.get_width() // 2 )
	basic_button = screen.blit(basic, (basic_x, (SCREEN_HEIGHT/4)))
	shotgun = medium_font.render("SHOTGUN", True, "white")
	shotgun_x = (((SCREEN_WIDTH*3)/4) - shotgun.get_width() // 2 )
	shotgun_button = screen.blit(shotgun, (shotgun_x, (SCREEN_HEIGHT/4)))
	orbital = medium_font.render("ORBITAL", True, "white")
	orbital_x = ((SCREEN_WIDTH/4) - orbital.get_width() // 2 )
	orbital_button = screen.blit(orbital, (orbital_x, ((SCREEN_HEIGHT*3)/4)))
	back = small_font.render("BACK", True, "white")
	back_x =((SCREEN_WIDTH) - back.get_width())
	back_button = screen.blit(back, (back_x - 50, SCREEN_HEIGHT - 100))
	pygame.display.flip()

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.collidepoint(event.pos):
					running = False

	return "back"


def game_ending():
	running = True
	global score
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	screen.fill("black")
	dead = big_font.render("GAME OVER !", True, "white")
	dead_x = (SCREEN_WIDTH - dead.get_width()) // 2
	screen.blit(dead, (dead_x, SCREEN_HEIGHT/4))
	final_score = medium_font.render(f"FINAL SCORE: {score}", True, "white")
	score_x = ((SCREEN_WIDTH - final_score.get_width()) // 2)
	screen.blit(final_score,(score_x, SCREEN_HEIGHT/2))
	try_again = small_font.render("TRY AGAIN", True, "white")
	try_again_x = (SCREEN_WIDTH // 3 - try_again.get_width() // 2)
	try_again_button = screen.blit(try_again, (try_again_x, (SCREEN_HEIGHT*2)/3))
	quit = small_font.render("QUIT", True, "white")
	quit_x = (((SCREEN_WIDTH*2)/3) - quit.get_width() // 2)
	quit_button = screen.blit(quit,(quit_x,(SCREEN_HEIGHT*2)/3))
	pygame.display.flip()

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				return False
			if event.type == pygame.MOUSEBUTTONDOWN:
					if try_again_button.collidepoint(event.pos):
						score = 0
						running = False
					if quit_button.collidepoint(event.pos):
						return False
	return True

def main():
	global big_font, medium_font, small_font, score
	pygame.init()
	pygame.font.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	big_font = pygame.font.SysFont(None, 200)
	small_font = pygame.font.SysFont(None, 80)
	medium_font = pygame.font.SysFont(None, 120)
	running = True
	while running:
		menu = show_menu(screen)
		if  menu == True:
			game_runnning()
		if menu == False:
			sys.exit()
		end_menu = game_ending()
		if end_menu == False:
			running = False
	return True

if __name__ == "__main__":
    main()


