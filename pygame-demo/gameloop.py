import pygame
pygame.init()

screen  = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))
pygame.display.set_caption("Game Loop *******")

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    pygame.display.flip()


