import pygame
from math import pi


pygame.init()
WIDTH = 400
HEIGHT = 600
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,225,0)
WHITE = (255,255,255)
BACKGROUND_COLOUR = (0,100,0)
transparent = pygame.Color(0,0,0,25)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,  HEIGHT))
screen.fill(BLUE)
pygame.display.set_caption('A basketball court')

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        
        pygame.draw.line(screen, WHITE, [0, HEIGHT / 2], [WIDTH, HEIGHT / 2], 2 )
        pygame.draw.circle(screen, WHITE, [WIDTH / 2, HEIGHT / 2], 60, 1)
        pygame.draw.circle(screen, WHITE, [WIDTH / 2, HEIGHT / 2], 30, 1)

        # draw 1st goal post
        pygame.draw.line(screen, WHITE, [50, 0], [50, 100], 2)
        pygame.draw.line(screen, WHITE, [350, 0], [350, 100], 2)
        rect1 = pygame.Rect(50, 20, 300, 150)
        pygame.draw.arc(screen, WHITE, rect1, pi, 2 * pi, 1)
        # pygame.draw.arc(screen, WHITE, [100, 50], [300, 50], 2)

        #-------
        #outmost post
        pygame.draw.line(screen, WHITE, [150, 0], [150, 100], 2)
        pygame.draw.line(screen, WHITE, [250, 0], [250, 100], 2)
        pygame.draw.line(screen, WHITE, [150, 100], [260, 100], 2)

        #second post
        pygame.draw.line(screen, WHITE, [160, 0], [160, 100], 2)
        pygame.draw.line(screen, WHITE, [260, 0], [260, 100], 2)
        rect2 = pygame.Rect(160, 65, 90, 70)
        pygame.draw.arc(screen, WHITE, rect2, pi, 2 * pi, 1)

        # draw 2nd goal post
        #first post
        pygame.draw.line(screen, WHITE, [50, 600], [50, 500], 2)
        pygame.draw.line(screen, WHITE, [350, 600], [350, 500], 2)
        rect3 = pygame.Rect(50, 430, 300, 150)
        pygame.draw.arc(screen, WHITE, rect3, 0, pi, 1)

        #second post
        pygame.draw.line(screen, WHITE, [150, 600], [150, 500], 2)
        pygame.draw.line(screen, WHITE, [250, 600], [250, 500], 2)
        pygame.draw.line(screen, WHITE, [150, 500], [260, 500], 2)

        #third post
        pygame.draw.line(screen, WHITE, [160, 600], [160, 500], 2)
        pygame.draw.line(screen, WHITE, [260, 600], [260, 500], 2)
        rect4 = pygame.Rect(160, 470, 90, 70)
        pygame.draw.arc(screen, WHITE, rect4, 0, pi, 1)



        


    pygame.display.update()
    clock.tick(60)