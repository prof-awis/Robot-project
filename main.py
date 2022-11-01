import pygame

#Initializing the surface of the rectangle and circle
surface = pygame.display.set_mode((500,500))

circleX = 250
circleY = 160
radius = 25
radius1 = 5

#initiliazing color
color = (255, 0, 0)
color1 = (255, 255, 255)

#Drawing the rectangle
# .Rect(x-axis left, y-axis top, base, width)
pygame.draw.rect(surface, color, pygame.Rect(240, 180, 20, 20)) #neck
pygame.draw.rect(surface, color, pygame.Rect(200, 200, 100, 120)) #torso
pygame.draw.rect(surface, color, pygame.Rect(140, 200, 60, 20)) #left arm
pygame.draw.rect(surface, color, pygame.Rect(140, 160, 20, 40))
pygame.draw.rect(surface, color, pygame.Rect(300, 200, 60, 20)) #right arm
pygame.draw.rect(surface, color, pygame.Rect(340, 160, 20, 40))
pygame.draw.rect(surface, color, pygame.Rect(200, 320, 30, 80)) #left foot
pygame.draw.rect(surface, color, pygame.Rect(180, 400, 50, 20))
pygame.draw.rect(surface, color, pygame.Rect(270, 320, 30, 80)) #right foot
pygame.draw.rect(surface, color, pygame.Rect(270, 400, 50, 20))



active = True

while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False

   pygame.draw.circle(surface, color,(250, 160), radius) # DRAW CIRCLE
   pygame.draw.circle(surface, color1, (240, 155), radius1) #eyes
   pygame.draw.circle(surface, color1, (260, 155), radius1)

   pygame.draw.rect(surface, color1, pygame.Rect(240, 168, 20, 6))  # mouth

   pygame.display.update()

pygame.quit()