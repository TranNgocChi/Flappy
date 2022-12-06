import pygame
import random
import time
import sys 

pygame.init()

width = 400
height = 600
screen = pygame.display.set_mode((width,height))
caption = pygame.display.set_caption("Flappy Bird")

fps = 60
clock = pygame.time.Clock()

bg = pygame.image.load("assets/background-night.png").convert()
bg = pygame.transform.scale(bg,(700,700))


class Bird:
	def __init__(self):
		self.img = pygame.image.load('assets/yellowbird-downflap.png').convert()
		self.img =  pygame.transform.scale2x(self.img)
		self.img1 = pygame.image.load('assets/yellowbird-midflap.png').convert()
		self.img1 = pygame.transform.scale2x(self.img1)
		self.img2 = pygame.image.load('assets/yellowbird-upflap.png').convert()
		self.img2 = pygame.transform.scale2x(self.img2)
		self.width = self.img.get_width()
		self.height = self.img.get_height()
		self.x = (width-self.width)/2
		self.y = (height-self.height)/2
		self.speed = 0
		self.tocdo = -8
		self.giatoc = 0.5
	def draw(self):
		screen.blit(self.img,(int(self.x),int(self.y)))

	def move(self, space):
		self.y += self.speed + 0.5*self.giatoc
		self.speed += self.giatoc
		if space == True:
			self.speed = self.tocdo
class Column:
	def __init__(self):
		self.x1 = 600
		self.x2 = 800
		self.x3 = 1000
		self.h1 = random.randrange(100,400,50)
		self.h2 = random.randrange(100,400,50)
		self.h3 = random.randrange(100,400,50)
		self.gap = 170
		self.width = 50
		self.speed = 2  
		self.tube = pygame.image.load("assets/pipe-green.png").convert()
		self.tube1 = self.tube2 = self.tube3 = self.tube4 = self.tube5 = self.tube6 = self.tube

		self.tube1 = pygame.transform.scale(self.tube, (self.width,self.h1))
		self.tube1 = pygame.transform.flip(self.tube1, False, True)
		self.tube2 = pygame.transform.scale(self.tube, (self.width, self.h2))
		self.tube2 = pygame.transform.flip(self.tube2, False, True)
		self.tube3 = pygame.transform.scale(self.tube, (self.width, self.h3))
		self.tube3 = pygame.transform.flip(self.tube3, False, True)
		self.tube4 = pygame.transform.scale(self.tube, (self.width,height-self.gap-self.h1))
		self.tube5 = pygame.transform.scale(self.tube, (self.width, height-self.gap-self.h2))
		self.tube6 = pygame.transform.scale(self.tube, (self.width, height-self.gap-self.h3))
	def draw(self):
		# draw ong o tren
		screen.blit(self.tube1, (self.x1, 0))
		screen.blit(self.tube2, (self.x2, 0))
		screen.blit(self.tube3, (self.x3, 0))
		# draw ong o duoi
		screen.blit(self.tube4, (self.x1, self.h1 + self.gap))
		screen.blit(self.tube5, (self.x2, self.h2 + self.gap))
		screen.blit(self.tube6, (self.x3, self.h3 + self.gap))
	def move(self):
		self.x1 -= self.speed
		self.x2 -= self.speed
		self.x3 -= self.speed
	def update(self):
		if self.x1 < -self.width:
			self.x1 = 550
		if self.x2 < -self.width:
			self.x2 = 550 
		if self.x3 < -self.width:
			self.x3 = 550
def rectCollision(rect1,rect2):
	if rect1[0] <= rect2[0] + rect2[2] and rect2[0] <= rect1[0] + rect1[2] and rect1[1] <= rect2[1] + rect2[3] and rect2[1] <= rect1[1] + rect1[3]:
		return True
	return False
def isgameover(bird, column):
	rect_bird =  [bird.x,bird.y,bird.width,bird.height]
	rect_tube1 = [column.x1, 0, column.width, column.h1]
	rect_tube2 = [column.x2, 0, column.width, column.h2]
	rect_tube3 = [column.x3, 0, column.width, column.h3]
	rect_tube4 = [column.x1, column.h1 + column.gap, column.width, column.h1]
	rect_tube5 = [column.x2,column.h2 + column.gap, column.width, column.h2]
	rect_tube6 = [column.x3,column.h3 + column.gap, column.width, column.h3]
	if rectCollision(rect_bird, rect_tube1) == True or rectCollision(rect_bird, rect_tube2) == True or rectCollision(rect_bird, rect_tube3) == True or rectCollision(rect_bird, rect_tube4) == True or rectCollision(rect_bird, rect_tube5) == True	or rectCollision(rect_bird, rect_tube6) == True or bird.y > height:		
		return True
	return False
class Score():
	def __init__(self):
		self.score = 0
	def draw(self):
		font = pygame.font.SysFont('consolas', 40)
		score = font.render(str(int(self.score)), True, (0,0,0))
		screen.blit(score, (200,100))
	def update(self):
		self.score += 0.01
		if self.score <= 10:
			Column().speed = 5

def gamestart(bird):
	bird.__init__()
	font = pygame.font.SysFont('consolas', 60)
	headingSurface = font.render("Flappy Bird", True, (255,231,2))

	font = pygame.font.SysFont('consolas', 60)
	commentSurface = font.render('CLICK SPACE', True, (255,231,2))

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					return
			screen.blit(bg, (0,0))
			bird.draw()
			screen.blit(headingSurface, (int(width/2 - 190), 100))
			screen.blit(commentSurface, (20, 500))

			pygame.display.update()
			clock.tick(fps) 
			
def gameplay(bird, column, score):
	bird.__init__()
	column.__init__()
	score.__init__()
	while True:
		space = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					space = True
		screen.blit(bg, (0,0))
		score.draw()
		score.update()

		bird.draw()
		bird.move(space)

		column.draw()
		column.move()
		column.update()

		if isgameover(bird, column) == True:
			return

		clock.tick(fps)
		pygame.display.flip()
		pygame.display.update()
	pygame.quit()


def gameover(bird, column, score):

	font = pygame.font.SysFont('consolas', 60)
	headingSurface = font.render('YOU LOSED', True, (255,0,0))

	font = pygame.font.SysFont('consolas', 50)
	commentSurface = font.render("PRESS SPACE", True, (255,0,0))

	font = pygame.font.SysFont('consolas', 30)
	scoreSurface = font.render('Score: ' + str(int(score.score)), True, (0,0,0))

	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					return
		screen.blit(bg, (0,0))
		column.draw()
		bird.draw()
		screen.blit(headingSurface, (int(width/2 - 145), 100))
		screen.blit(commentSurface,(70,500))
		screen.blit(scoreSurface, (int(width/2 - 50), 160))
		pygame.display.update()
		clock.tick()
		
def main():
	score = Score()
	column = Column()
	bird = Bird()

	run = True
	while run:
		gamestart(bird)
		gameplay(bird, column, score)
		gameover(bird, column, score)	 
	
if __name__ == "__main__":
	main()