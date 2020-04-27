import pygame

pygame.init()
window = pygame.display.set_mode((1368, 772))

pygame.display.set_caption("Perfect Game")

left = [pygame.image.load('1.png'), pygame.image.load('2.png'),
pygame.image.load('3.png'),
pygame.image.load('4.png'), pygame.image.load('5.png'),
pygame.image.load('6.png'),]

right = [pygame.image.load('7.png'), pygame.image.load('8.png'),
pygame.image.load('9.png'),
pygame.image.load('10.png'), pygame.image.load('11.png'),
pygame.image.load('12.png'),]

stand = pygame.image.load('idle.png')

fon = pygame.image.load('fon.png')


x = 100
y = 620
width = 60
height = 71
speed = 5
isJump = False
JumpCount = 10
isLeft = False
isRight = False
animCount = 0

clock = pygame.time.Clock()

def animation():
    global animCount
    window.blit(fon, (0, 0))

    if animCount == 29:
        animCount = 0

    if isLeft:
        window.blit(left[animCount // 5], (x, y))
        animCount += 1
    elif isRight:
        window.blit(right[animCount // 5], (x, y))
        animCount += 1
    else:
        window.blit(stand, (x, y))

    pygame.display.update()

flag = True
while flag:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        isLeft = True
        isRight = False
    elif keys[pygame.K_RIGHT] and x < 1368 - 5 - width:
        x += speed
        isRight = True
        isLeft = False
    else:
        isRight = False
        isLeft = False
        animCount = 0

    if not(isJump):
        if keys[pygame.K_UP] and y > 600:
            y -= speed
        if keys[pygame.K_DOWN] and y < 772 - height - 15 and y > 600:
            y += speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if JumpCount >= -10:
            if JumpCount < 0:
                y += (JumpCount ** 2) / 2
            else:
                y -= (JumpCount ** 2) / 2
            JumpCount -= 1
        else:
            isJump = False
            JumpCount = 10
    animation()

pygame.quit()
