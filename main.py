import pygame

#initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#Game loop
running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False


