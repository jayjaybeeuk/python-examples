import pygame
pygame.init()


w_width = 800
w_height = 600
screen  = pygame.display.set_mode((w_width, w_height))
screen.fill((255, 255, 255))
pygame.display.set_caption("Moving Character")

# creating object
x = 50
y = 435
width = 64
height = 64
vel = 5

clock = pygame.time.Clock()

# Jump variables
isJump = False
jumpCount = 10

# Images
bg_image = pygame.image.load("images/background.png")
bg_image = pygame.transform.scale(bg_image, (w_width, w_height))

# Character
left = False
right = False
walkCount = 0

walkRight = [pygame.image.load(f'soldier/{i}.png') for i in range(1, 10)]
walkLeft = [pygame.image.load(f'soldier/L{i}.png') for i in range(1, 10)]
char = pygame.image.load('soldier/standing.png')

def draw():
    screen.blit(bg_image, (0, 0))
    # pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height))
    clock.tick(25)
    global walkCount
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        screen.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        screen.blit(char, (x, y))
    pygame.display.flip()



done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    keys =pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < w_width - width:
        x += vel
        right = True
        left = False

    else:
        left = False
        right = False
        walkCount = 0


    if not(isJump):  
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
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
