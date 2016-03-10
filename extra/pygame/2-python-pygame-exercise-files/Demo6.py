import pygame, sys

pygame.init()
pygame.mixer.init()

windowSize = (800, 600)

screen = pygame.display.set_mode(windowSize)

helloWorld = pygame.image.load("PS circle.png")

helloWorldSize = helloWorld.get_size()

sound = pygame.mixer.Sound("Pluralsight.wav")

pygame.mouse.set_visible(0)

x,y = 0,0
directionX, directionY = 1, 1
clock = pygame.time.Clock()

while 1:

    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x += 5
            if event.key == pygame.K_LEFT:
                x -= 5

            if event.key == pygame.K_DOWN:
                y += 5
            if event.key == pygame.K_UP:
                y -= 5

    screen.fill((0,0,0))

    if x + helloWorldSize[0] > 800:
        x = 800 - helloWorldSize[0]
        sound.stop()
        sound.play()

    if y + helloWorldSize[1] > 600:
        y = 600 - helloWorldSize[1]
        sound.stop()
        sound.play()

    if x <= 0:
        x = 0
        sound.stop()
        sound.play()
    if y <= 0:
        y = 0
        sound.stop()
        sound.play()

    screen.blit(helloWorld, (x, y))

    pygame.display.update()

