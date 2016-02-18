import pygame, sys

pygame.init()

windowSize = (800, 600)

screen = pygame.display.set_mode(windowSize)

myriadProFont = pygame.font.SysFont("Myriad Pro", 48)

helloWorld = myriadProFont.render("Hello world!", 1, (255, 0, 255), (255, 255, 255))

x, y = 0, 0

clock = pygame.time.Clock()

while 1:

    clock.tick(40)

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.blit(helloWorld, (x, y))

    x += 5

    pygame.display.update()