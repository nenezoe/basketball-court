import pygame


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
pygame.display.set_caption('A bit Racey')

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        
        pygame.draw.line(screen, WHITE, [0, HEIGHT / 2], [WIDTH, HEIGHT / 2], 2 )
        pygame.draw.circle(screen, WHITE, [WIDTH / 2, HEIGHT / 2], 60, 1)

        # draw 1st goal post
        pygame.draw.line(screen, WHITE, [100, 0], [100, 50], 2)
        pygame.draw.line(screen, WHITE, [300, 0], [300, 50], 2)
        pygame.draw.line(screen, WHITE, [100, 50], [300, 50], 2)

        # draw 2nd goal post
        pygame.draw.line(screen, WHITE, [100, 600], [100, 550], 2)
        pygame.draw.line(screen, WHITE, [300, 600], [300, 550], 2)
        pygame.draw.line(screen, WHITE, [100, 550], [300, 550], 2)
        


    pygame.display.update()
    clock.tick(60)