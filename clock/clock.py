import pygame
import time
import math

pygame.init()

running = True
starting = False
mouse_left = 1
screen = pygame.display.set_mode((500, 600))

GREY = (150, 150, 147);
BLACK = (0, 0, 0);
WHITE = (255, 255, 255);
RED = (237, 5, 5);

font = pygame.font.SysFont('sans', 50)
start = font.render("START", True, BLACK)
reset = font.render("RESET", True, BLACK)
stop = font.render("STOP", True, RED)
total_secs = 0
total = 0
while running:
	screen.fill(GREY)
	mouse_x, mouse_y = pygame.mouse.get_pos()
	# hang 1
	pygame.draw.rect(screen, WHITE, (100, 50, 50, 50))
	pygame.draw.rect(screen, WHITE, (200, 50, 50, 50))
	pygame.draw.rect(screen, WHITE, (300, 50, 150, 50))
	#hang 2
	pygame.draw.rect(screen, WHITE, (100, 200, 50, 50))
	pygame.draw.rect(screen, WHITE, (200, 200, 50, 50))
	pygame.draw.rect(screen, WHITE, (300, 120, 150, 50))

	pygame.draw.rect(screen, WHITE, (300, 190, 150, 50))

	#hang 3
	pygame.draw.rect(screen, BLACK, (50, 520, 400, 50))
	pygame.draw.rect(screen, WHITE, (60, 530, 380, 30))
	#vong tron
	pygame.draw.circle(screen, BLACK, (250, 400), 100)
	pygame.draw.circle(screen, WHITE, (250, 400), 95)
	pygame.draw.circle(screen, BLACK, (250, 400), 5)
	# pygame.draw.line(screen, BLACK, (250, 400), (250, 310))
	#bind text vao cac o
	screen.blit(start, (310, 47))
	screen.blit(reset, (310, 117))
	screen.blit(stop, (310, 187))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if  event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == mouse_left:
				if 100 < mouse_x < 150 and 50 < mouse_y < 100: 
					total_secs += 60
					total = total_secs
				if 200 < mouse_x < 250 and 50 < mouse_y < 100: 
					total_secs += 1
					total = total_secs
				if 100 < mouse_x < 150 and 200 < mouse_y < 250: 
					total_secs -= 60
					total = total_secs
				if 200 < mouse_x < 250 and 200 < mouse_y < 250: 
					total_secs -= 1
					total = total_secs
				if 300 < mouse_x < 450 and 50 < mouse_y < 100: 
					starting = True
				if 300 < mouse_x < 450 and 120 < mouse_y < 170: 
					total_secs = 0
					starting = False
				if 300 < mouse_x < 450 and 190 < mouse_y < 240: 
					starting = False
	if total_secs == 0:
		starting = False
		total = 0

	if starting:
		total_secs -=1
		time.sleep(1)

	countdown_mins = int(total_secs/60)
	countdown_secs = total_secs - countdown_mins*60

	countdown_time = str(countdown_mins) + ' : ' + str(countdown_secs)
	text_time = font.render(countdown_time, True, BLACK)
	screen.blit(text_time, (120,120))

	x_sec = 250 + 90 * math.sin(6* countdown_secs * math.pi/180)
	y_sec = 400 - 90 * math.cos(6* countdown_secs * math.pi/180)
	pygame.draw.line(screen, BLACK, (250, 400), (int(x_sec), int(y_sec)))

	x_min = 250 + 40 * math.sin(6* countdown_mins * math.pi/180)
	y_min = 400 - 40 * math.cos(6* countdown_mins * math.pi/180)
	pygame.draw.line(screen, RED, (250, 400), (int(x_min), int(y_min)))

	if total_secs != 0:

		pygame.draw.rect(screen, RED, (60,530, 380 * (total_secs/total), 30))

	pygame.display.flip()
pygame.quit()