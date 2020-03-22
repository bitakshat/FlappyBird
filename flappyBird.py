#Flappy bird
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

	#message to inform
	message = [
		"You Crashed", "Score", "Game Over",
		"Play", "Play Again"
	]

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
		self.lives = 5
		self.touch = False
		self.bird_size = 15
		self.backgroundImage = pygame.image.load("cityBackground.jpg").convert_alpha()
		self.backgroundImage = pygame.transform.scale(self.backgroundImage, (self.width, self.height))
		self.birdImage = pygame.image.load("bird_wing_down.png").convert_alpha()
		self.groundImage = pygame.image.load("ground.png").convert_alpha()

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

			# print("Pipe ax-coordinate: ", self.pipe_ax)
			# print("Pipe ay-coordinate: ", self.pipe_ay)
			# print("Pipe bx-coordinate: ", self.pipe_bx)
			# print("pipe by-coordinate: ", self.pipe_by)
			# Adding pipes
			self.window.fill((255,255,255))
			self.window.blit(self.backgroundImage, [0, 0])
			self.window.blit(self.groundImage, [0, 350])
			pygame.draw.rect(self.window, (0,0,180), [self.pipe_ax, self.pipe_ay, self.pipe_width, self.pipeA_length])
			pygame.draw.rect(self.window, (0,0,180), [self.pipe_bx, self.pipe_by, self.pipe_width, self.pipeB_length])
			pygame.display.update()

			#pipe spawn poin
			if self.pipe_ax <= 0:
				self.pipe_ax = self.width
				self.pipeA_length = random.randint(70,150)

			if self.pipe_bx <= 0:
				self.pipe_bx = self.width
				self.pipeB_length = -random.randint(70,150)
                                                                                    
			#keeping the bird on screen
			if self.y_pos > self.height:
				self.y_pos = self.height
				self.velocity = 0
			if self.y_pos < 0:
				self.y_pos = 0
				self.velocity = 0
			#Bird
			self.window.blit(self.birdImage, [self.x_pos, self.y_pos])
			pygame.display.update()
			self.clock.tick(self.fps)

			#Game crash condition
			#True if player hits the boundry
			if self.y_pos >= self.height or self.y_pos <= 0:
				self.run = True
				print("You crashed on boundry")
			#True if player hits the pipe objects
			#for pipe A (the Upper one)
			if self.pipe_ax == self.x_pos:
				self.score += 1
				print("Your score: ", self.score)
				if self.y_pos <= self.pipeA_length:
					self.run = True
					print("You crashed on pipe")
					print("Pipe ax coordinate:", self.pipe_ax)
					print("Pipe A Length: ", self.pipeA_length)
					print("Bird y-coordinate: ", self.y_pos)
			#Unable to add game exit condition for Pipe B (the lower one)

start_game = FlappyBird()
start_game.flyBird()
pygame.quit()