import pygame, sys

pygame.init()

windowSize = (800, 600)

screen = pygame.display.set_mode(windowSize)

myriadProFont = pygame.font.SysFont("Myriad Pro", 48)

helloWorld = myriadProFont.render("Hello World", 1, (255, 0, 255), (255, 255, 255))

helloWorldSize = helloWorld.get_size()

x,y = 0,0
directionX, directionY = 1, 1
clock = pygame.time.Clock()

while 1:

    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill((0,0,0))

    x += 5 * directionX
    y += 5 * directionY

    if x + helloWorldSize[0] > 800 or x <= 0:
        directionX *= -1

    if y + helloWorldSize[1] > 600 or y <= 0:
        directionY *= -1

    screen.blit(helloWorld, (x, y))

    pygame.display.update()

