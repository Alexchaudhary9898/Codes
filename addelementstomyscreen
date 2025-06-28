import pygame
pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("simple game")
font = pygame.font.Font(None, 36)
text = font.render("hello, pygame!", True, (0, 0, 0))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 128, 255), (150, 100, 200, 100))
    screen.blit(text, (160, 250))
    pygame.display.flip()
    