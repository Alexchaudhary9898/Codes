import pygame
import random
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("space invader with sprites")
clock = pygame.tick.Clock()
player_img = pygame.image.load("OIP.webp")
enemy_img = pygame.image.load("download 2.webp")
bullet_img = pygame.image.load("download.webp")
player_img = pygame.transform.scale(player_img, (50, 40))
enemy_img = pygame.transform.scale(enemy_img, (40, 40))
bullet_img = pygame.transform.scale(bullet_img, (5, 20))
player_rect = player_img.get_rect(midbottom=(300, 300))
enemy_rect = enemy_img.get_rect(topleft=(random.randint(0, 500), 50))
bullet_rect = bullet_img.get_rect(center=(-100, -100))
running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False