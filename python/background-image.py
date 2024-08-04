import pygame
pygame.init()


w_width = 800
w_height = 600
screen  = pygame.display.set_mode((w_width, w_height))
screen.fill((255, 255, 255))
pygame.display.set_caption("Adding Background Image")

# creating object
x = 0
y = 0
width = 50
height = 50
vel = 5

clock = pygame.time.Clock()

# Jump variables
isJump = False
jumpCount = 10

# Images
bg_image = pygame.image.load("images/background.png")
bg_image = pygame.transform.scale(bg_image, (w_width, w_height))

def draw():
    screen.blit(bg_image, (0, 0))
    pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height))
    clock.tick(60)
    pygame.display.flip()



done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    keys =pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < w_width - width:
        x += vel
    if keys[pygame.K_SPACE]:
        isJump = True

    if not(isJump):
        if keys[pygame.K_UP] and y > 0:
            y -= vel
        if keys[pygame.K_DOWN] and y < w_height - height:
            y += vel
    else:
        if isJump:
            if jumpCount >= -10:
                # Neg is the direction of the jump
                neg = 1
                # Prevent a double jump
                if jumpCount < 0:
                    neg = -1
                # 0.5 is the gravity
                y -= (jumpCount ** 2) * 0.5 * neg
                jumpCount -= 1
            else:
                isJump = False
                jumpCount = 10
    draw()



