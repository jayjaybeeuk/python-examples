import pygame
pygame.init()


w_width = 800
w_height = 600
screen  = pygame.display.set_mode((w_width, w_height))
screen.fill((255, 255, 255))
pygame.display.set_caption("Handling keyboard events")

# creating object
x = 0
y = 0
width = 50
height = 50
vel = 5

clock = pygame.time.Clock()
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    keys =pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel

    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height))
    clock.tick(60)
    pygame.display.flip()


