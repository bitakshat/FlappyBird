# Flappy bird
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
	game_out = 10
	score = 0

	# message to inform
	message = [
		"You Crashed", "Score", "Game Over",
		"Play", "Play Again"
	]

	def flyBird(self):
		self.fps = 50
		# initial variables for pipe
		self.lives = 5
		self.touch = False
		self.bird_size = 15
		self.backgroundImage = pygame.image.load("./images/cityBackground.jpg").convert_alpha()
		self.backgroundImage = pygame.transform.scale(self.backgroundImage, (self.width, self.height))
		self.birdImage = pygame.image.load("./images/bird_wing_down.png").convert_alpha()
		self.groundImage = pygame.image.load("./images/ground.png").convert_alpha()
		self.pipe_width = 30		# pipe width
		self.pipe_x = self.width	# pipe x coordinate
		self.pipe_y = 0				# pipe y coordinate
		self.invisible_pipe_x = self.width
		self.invisible_pipe_y = random.randint(50, 250)		# invisible pipe random y coordinate
		self.invisible_pipe_len = random.randint(100, 250)	# random pipe length

		while not self.run:
			for event in pygame.event.get():
				# print(event)
				if event.type == pygame.QUIT:
					self.run = True
				# adding movements
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						self.velocity -= self.gravity*15

			self.window.fill((130,255,255))
			# adding gravity for bird
			self.velocity += self.gravity
			self.y_pos += self.velocity

			# changing pipe x-coordinate on render
			self.pipe_x -= 2
			self.invisible_pipe_x -= 2

			# Adding pipes
			self.window.fill((255,255,255))
			self.window.blit(self.backgroundImage, [0, 0])
			self.window.blit(self.groundImage, [0, 350])
			pygame.draw.rect(self.window, (0,0,180), [self.pipe_x, self.pipe_y, self.pipe_width, self.height])
			# for invisible pipe
			pygame.draw.rect(self.window, (255, 255, 255), [self.invisible_pipe_x, self.invisible_pipe_y, 30, self.invisible_pipe_len])
			pygame.display.update()

			# pipe spawn point
			if self.pipe_x <= 0:
				self.pipe_x = self.width
			if self.invisible_pipe_x <= 0:
				self.invisible_pipe_x = self.width
				self.invisible_pipe_len = random.randint(100, 250)
				self.invisible_pipe_y = random.randint(50, 170)

			# keeping the bird on screen
			if self.y_pos > self.height:
				self.y_pos = self.height
				self.velocity = 0
			if self.y_pos < 0:
				self.y_pos = 0
				self.velocity = 0
			# Bird
			self.window.blit(self.birdImage, [self.x_pos, self.y_pos])
			pygame.display.update()
			self.clock.tick(self.fps)

			# Game crash condition
			# True if player hits the boundry
			if self.y_pos >= self.height or self.y_pos <= 0:
				self.run = True
				print("You crashed: boundry")
			# True if player hits the pipe objects
			elif((self.x_pos == self.invisible_pipe_x) and (self.y_pos >= self.invisible_pipe_y+self.invisible_pipe_len or self.y_pos <= self.invisible_pipe_y)):
				self.run = True
				print("You crashed: Pipe")
				print("bird y coordinate: ", self.y_pos)
				print("pipe y coordinate: ", self.y_pos)
			else:
				self.score += 1
			# don't forget to add score

			# for pipe A (the Upper one)
			# if self.pipe_x == self.x_pos:
			# 	self.score += 1
			# 	print("Your score: ", self.score)
			# 	if self.y_pos <= self.pipeA_length:
			# 		self.run = True
			# 		print("You crashed: pipe")
			# 		print("Pipe ax coordinate:", self.pipe_x)
			# 		print("Pipe A Length: ", self.pipeA_length)
			# 		print("Bird y-coordinate: ", self.y_pos)

start = FlappyBird()
start.flyBird()
pygame.quit()