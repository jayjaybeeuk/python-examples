import pygame
pygame.init()


w_width = 800
w_height = 600
screen  = pygame.display.set_mode((w_width, w_height))
screen.fill((255, 255, 255))
pygame.display.set_caption("Moving Character")

clock = pygame.time.Clock()
bg_image = pygame.image.load("images/background.png")
bg_image = pygame.transform.scale(bg_image, (w_width, w_height))
walkRight = [pygame.image.load(f'soldier/{i}.png') for i in range(1, 10)]
walkLeft = [pygame.image.load(f'soldier/L{i}.png') for i in range(1, 10)]
char = pygame.image.load('soldier/standing.png')

class player():
    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            screen.blit(walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            screen.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            screen.blit(char, (self.x, self.y))

def DrawInGameLoop():
    screen.blit(bg_image, (0, 0))
    clock.tick(25)
    soldier.draw(screen)
    pygame.display.flip()

soldier = player(50, 435, 64, 64, 5)
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    keys =pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and soldier.x > 0:
        soldier.x -= soldier.vel
        soldier.left = True
        soldier.right = False
    elif keys[pygame.K_RIGHT] and soldier.x < w_width - soldier.width:
        soldier.x += soldier.vel
        soldier.right = True
        soldier.left = False

    else:
        soldier.left = False
        soldier.right = False
        soldier.walkCount = 0


    if not(soldier.isJump):  
        if keys[pygame.K_SPACE]:
            soldier.isJump = True
            soldier.right = False
            soldier.left = False
    else:
        if soldier.isJump:
            if soldier.jumpCount >= -10:
                # Neg is the direction of the jump
                soldier.neg = 1
                # Prevent a double jump
                if soldier.jumpCount < 0:
                    soldier.neg = -1
                # 0.5 is the gravity
                soldier.y -= (soldier.jumpCount ** 2) * 0.5 * soldier.neg
                soldier.jumpCount -= 1
            else:
                soldier.isJump = False
                soldier.jumpCount = 10
    DrawInGameLoop()
