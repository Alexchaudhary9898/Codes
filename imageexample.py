import pygame
pygame.init()
screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("image example")
image = pygame.image.load("download.jpg")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255)) # Optional background color
    screen.blit(image, (100, 100)) # Display the image on screen
    pygame.display.update()
pygame.quit()