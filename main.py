import pygame

#initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Animated Robot")
icon = pygame.image.load("robot.png")
pygame.display.set_icon(icon)

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #RGB
    screen.fill((255, 255, 0))
    pygame.display.update()
