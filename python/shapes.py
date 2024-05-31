import pygame
pygame.init()

screen  = pygame.display.set_mode((500, 500))
screen.fill((255, 255, 255))
pygame.display.set_caption("Drawing shapes on surface")

pygame.draw.line(screen, (0, 0, 0), (0, 0), (300, 300), 5)
# closed=False means the shape will be closed
pygame.draw.lines(screen, "blue", False, [(150, 150), (250, 150), (150, 250)], 4)
# closed=True means the shape will be closed
pygame.draw.lines(screen, "orange", True, [(100, 100), (200, 100), (100, 200)], 4)
pygame.draw.rect(screen, "red", (50, 50, 100, 100), 7)
pygame.draw.circle(screen, "green", (200, 150), 50, 1)
pygame.draw.ellipse(screen, "yellow", (300, 100, 100, 50), 4)
# polygon with a width=1, so is not fillled
pygame.draw.polygon(screen, "purple", [(250, 75), (300, 25), (350, 75)], 1)
# polygon with a width=0, so is fillled
pygame.draw.polygon(screen, "purple", [(300, 225), (350, 175), (400, 225)], 0)

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    pygame.display.flip()


