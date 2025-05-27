import pygame
from constants import *
from circleshape import *
from bullet import *


class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.timer = 0
		self.immunity_time = 0

	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def update(self, dt):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_z]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_q]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_SPACE]:
			self.shoot()

		self.timer -= dt

		self.wrap_position()


	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt



	def shoot(self):
		if self.timer <= 0:
			bullet = Bullet(self.position, self.position, SHOT_RADIUS)
			direction = pygame.Vector2(0, 1).rotate(self.rotation)
			bullet.velocity = direction * PLAYER_SHOOT_SPEED
			self.timer = PLAYER_SHOOT_COOLDOWN


