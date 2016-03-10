import pygame, sys
from GameObject import GameObject

# Initialize PyGame
pygame.init()
pygame.mixer.init()
windowSize = (800, 600)
screen = pygame.display.set_mode(windowSize)
pygame.mouse.set_visible(0)

# Load resources
helloWorld = pygame.image.load("PS circle.png")
sound = pygame.mixer.Sound("Pluralsight.wav")
myriadProFont = pygame.font.SysFont("Myriad Pro", 48)
intersectText = myriadProFont.render("Intersecting!", 1, (255, 0, 255), (0, 0, 0))

# Prepare logo
helloWorldSize = helloWorld.get_size()
helloWorld.fill((0,0,0), None, pygame.BLEND_RGBA_MAX)

x, y = 0, 0
clock = pygame.time.Clock()
directionX, directionY = 1, 1

def playSound():
    sound.stop()
    sound.play()

rectangle = GameObject(100, 100, 400, 400)
logo = GameObject(0, 0, helloWorldSize[0], helloWorldSize[1])

while 1:
    clock.tick(30)

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    mousePosition  = pygame.mouse.get_pos()

    x = mousePosition[0]
    y = mousePosition[1]

    logo.setPosition(x, y)

    if logo.intersects(rectangle):
        screen.blit(intersectText, (10, 10))
        playSound()

    if x + helloWorldSize[0] > 800:
        x = 800 - helloWorldSize[0]

    if y + helloWorldSize[1] > 600:
        y = 600 - helloWorldSize[1]

    if y <= 0:
        y = 0
    if x <= 0:
        x = 0

    pygame.draw.rect(screen, (255,255,255), (100,100,400,400), 1)

    screen.blit(helloWorld, (x, y))

    pygame.display.update()




