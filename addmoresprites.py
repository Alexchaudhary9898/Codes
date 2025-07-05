import pygame
import random
pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("simplest game")

player = pygame.rect(300, 220, 40, 40)
enemies = [pygame.rect(random.randint(0, 600), random.randint(0, 440), 30, 30) for _ in range(7)]
score = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player.x -= 5
    if keys[pygame.K_RIGHT]: player.x += 5
    if keys[pygame.K_UP]: player.y -= 5
    if keys[pygame.K_DOWN]:player.y += 5
    for enemy in enemies[:]
        if player.colliderect(enemy):
            enemies.remove(enemy)
            score += 1
    score.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), player)
    for enemy in enemies:
        pygame.draw.rect(screen, (0, 0, 255), player)
    screen.blit(text, (160, 250))
    pygame.display.flip()
    