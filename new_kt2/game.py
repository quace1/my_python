import pygame
import random

pygame.init()

display_width = 800
display_height = 600

window = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Trump's wars")

movement = [pygame.image.load('7.png'), pygame.image.load('8.png'),
pygame.image.load('9.png'),
pygame.image.load('10.png'), pygame.image.load('11.png'),
pygame.image.load('12.png'),]

enemies_arr = []
enemies_options = [80, 407, 80, 375, 80, 418]

fon = pygame.image.load('fon.jpg')
enemies_img = [pygame.image.load('hillary.png'),
pygame.image.load('mexican.png'), pygame.image.load('greta.png')]


x = 100
y = display_height - 170
user_width = 60
user_height = 71

isJump = False
JumpCount = 30
animCount = 0
score = 0
isAbove = False

clock = pygame.time.Clock()

def print_smth(message, x, y, font_colour = (0, 0, 0), font_type = 'font.ttf', font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_colour)
    window.blit(text, (x, y))

def pause():
    isPause = True
    while isPause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_smth('Pause. Press ENTER to continue', 160, 300)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            isPause = False
        pygame.display.update()
        clock.tick(15)

def count_score(barriers):
    global score, isAbove
    if not(isAbove):
        for barrier in barriers:
            if barrier.x <= x + user_width / 2 <= barrier.x + barrier.width:
                if y + user_height - 5 <= barrier.y:
                    isAbove = True
                    break
    else:
        if JumpCount == -30:
            score += 1
            isAbove = False

class Enemies:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed
    def move(self):
        if self.x >= -self.width:
            window.blit(self.image, (self.x, self.y))
            self.x -= 5
            return True
        else:
            self.x = display_width + 100 + random.randrange(-80, 60)
            return False
    def return_self(self, radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image
        window.blit(self.image, (self.x, self.y))

choice = random.randrange(0, 3)
img = enemies_img[choice]
width = enemies_options[choice * 2]
height = enemies_options[choice * 2 + 1]
enemies_arr.append(Enemies(display_width + 20, height, width, img, 4))

choice = random.randrange(0, 3)
img = enemies_img[choice]
width = enemies_options[choice * 2]
height = enemies_options[choice * 2 + 1]
enemies_arr.append(Enemies(display_width + 300, height, width, img, 4))

choice = random.randrange(0, 3)
img = enemies_img[choice]
width = enemies_options[choice * 2]
height = enemies_options[choice * 2 + 1]
enemies_arr.append(Enemies(display_width + 600, height, width, img, 4))

def isCollision(barriers):
    for barrier in barriers:
        if y + user_height >= barrier.y:
            if barrier.x + 10 <= x - 10 <= barrier.x + barrier.width - 20:
                return True
            elif barrier.x + 10 <= x + user_width - 20 <= barrier.x + barrier.width - 10:
                return True
    return False

def game_over():
    isPause = True
    while isPause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_smth('Game over! Press ESC to leave.', 100, 300)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return True
        pygame.display.update()
        clock.tick(15)

def draw_enemy(array):
    for enemy in array:
        check = enemy.move()
        if (not check):
            radius = find_radius(array)
            choice = random.randrange(0, 3)
            img = enemies_img[choice]
            width = enemies_options[choice * 2]
            height = enemies_options[choice * 2 + 1]
            enemy.return_self(radius, height, width, img)

def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x)
    if maximum < display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 150
    else:
        radius = maximum
    choice = random.randrange(0, 5)
    if choice == 0:
        radius += random.randrange(5, 10)
    else:
        radius += random.randrange(250, 400)
    return radius

def animation():
    global animCount
    window.blit(fon, (0, 0))
    draw_enemy(enemies_arr)
    print_smth('Score : ' + str(score), 600, 10)
    if animCount == 29:
        animCount = 0
    else:
        window.blit(movement[animCount // 5], (x, y))
        animCount += 1
    pygame.display.update()

flag = True
while flag:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pause()
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if JumpCount >= -30:
            y -= JumpCount / 2.5
            JumpCount -= 1
        else:
            isJump = False
            JumpCount = 30
    count_score(enemies_arr)
    if  isCollision(enemies_arr):
        if game_over():
            pygame.quit()
            quit()
    animation()
