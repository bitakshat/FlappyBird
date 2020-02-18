#The flappybird game
#!/usr/bin/env python
import pygame
import random

pygame.init()
class FlappyBird:
	width = 500
	height = 400
	window = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Flappy Bird")

	#bird spawn position
	x_pos = width // 5
	y_pos = height // 2
	y_init = y_pos
	gravity = 1
	velocity = 0
	clock = pygame.time.Clock()
	run = False
	upForce = 5

	def flyBird(self):
		self.fps = 50
		#ariables for pipe(initial)
		self.pipe_ax = random.randint(0, self.width)
		self.pipe_ay = 0
		self.pipe_bx = self.pipe_ax
		self.pipe_by = self.height
		self.pipeA_length = random.randint(60, 200)
		self.pipeB_length = -random.randint(60, 200)
		self.pipe_width = 30

		while not self.run:
			for event in pygame.event.get():
				print(event)
				if event.type == pygame.QUIT:
					self.run = True
				#adding movements
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						self.velocity += -self.gravity*15

			self.window.fill((130,255,255))
			#adding gravity
			self.velocity += self.gravity
			self.y_pos += self.velocity

			#changing pipe x-coordinate
			self.pipe_ax -= 2
			self.pipe_bx -= 2

			print("Pipe a x-coordinate: ", self.pipe_ax)
			print("Pipe a y-coordinate: ", self.pipe_ay)
			print("Pipe b x-coordinate: ", self.pipe_bx)
			print("Pipe b y-coordinate: ", self.pipe_by)
			#Adding pipes
			self.window.fill((255,255,255))
			pygame.draw.rect(self.window, (0,0,0), [self.pipe_ax, self.pipe_ay, self.pipe_width, self.pipeA_length])
			pygame.draw.rect(self.window, (0,0,0), [self.pipe_bx, self.pipe_by, self.pipe_width, self.pipeB_length])
			pygame.display.update()

			#pipe spawn point
			if self.pipe_ax <= 0:
				self.pipe_ax = self.width
				self.pipeA_length = random.randint(70,200)
			if self.pipe_bx <= 0:
				self.pipe_bx = self.width
				self.pipeB_length = -random.randint(70,200)

			#keeping the bird on screen
			if self.y_pos > self.height:
				self.y_pos = self.height
				self.velocity = 0
			if self.y_pos <= 0:
				self.y_pos = self.height
				self.velocity = 0
			#Bird
			pygame.draw.circle(self.window, (0,0,0), [self.x_pos, self.y_pos], 15)
			pygame.display.update()
			self.clock.tick(self.fps)

#Main Class Method call
start_game = FlappyBird()
start_game.flyBird()
pygame.quit()