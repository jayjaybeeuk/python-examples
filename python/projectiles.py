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
        self.standing = True

    def draw(self, screen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                screen.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                screen.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                screen.blit(walkRight[0], (self.x, self.y))
            else:
                screen.blit(walkLeft[0], (self.x, self.y))

class projectile():
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.vel = 8 * direction

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

def DrawInGameLoop():
    screen.blit(bg_image, (0, 0))
    clock.tick(25)
    soldier.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)
    pygame.display.flip()

soldier = player(50, 435, 64, 64, 5)
bullets = []
shoot = 0
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    if shoot > 0:
        shoot += 1
    if shoot > 3:
        shoot = 0
    
    for bullet in bullets:
        if bullet.x < w_width and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys =pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shoot == 0:
        if soldier.right:
            direction = 1
        else:
            direction = -1
        if len(bullets) < 5:
            bullets.append(projectile(round(soldier.x + soldier.width // 2), round(soldier.y + soldier.height // 2), 6, (0, 0, 0), direction))
        shoot = 1
    if keys[pygame.K_LEFT] and soldier.x > 0:
        soldier.x -= soldier.vel
        soldier.left = True
        soldier.right = False
        soldier.standing = False

    elif keys[pygame.K_RIGHT] and soldier.x < w_width - soldier.width:
        soldier.x += soldier.vel
        soldier.right = True
        soldier.left = False
        soldier.standing = False

    else:
        soldier.standing = True
        soldier.walkCount = 0


    if not(soldier.isJump):  
        if keys[pygame.K_UP]:
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
