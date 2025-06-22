import pygame, random

pygame.init()

screen = pygame.display.set_mode((500, 400))

pygame.display.set_caption("Sprite Bounce")

clock = pygame.time.Clock()

SPRITE_COLOR_EVENT = pygame.USEREVENT + 1

BG_COLOR_EVENT = pygame.USEREVENT + 2

SPRITE_COLORS = [pygame.Color(c) for c in ['yellow', 'magenta', 'orange', 'white']]

BG_COLORS = [pygame.Color(c) for c in ['blue', 'lightblue', 'darkblue','pink']]

# Sprite Class

class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, w, h):

        super().__init__()

        self.image = pygame.Surface([w, h])

        self.image.fill(color)

        self.rect = self.image.get_rect(topleft=(random.randint(0, 480), random.randint(0, 380)))

        self.vel = [random.choice([-4, 4]), random.choice([-4, 4])]

    def update(self):

        self.rect.move_ip(*self.vel)

        if self.rect.left < 0 or self.rect.right > 500: self.vel[0] *= -1

        if self.rect.top < 0 or self.rect.bottom > 400: self.vel[1] *= -1

        if random.random() < 0.005:

           pygame.event.post(pygame.event.Event(random.choice([SPRITE_COLOR_EVENT, BG_COLOR_EVENT])))

    def change_color(self):

        self.image.fill(random.choice(SPRITE_COLORS))

# Setup

sprite = Sprite(random.choice(SPRITE_COLORS), 30, 30)

sprites = pygame.sprite.Group(sprite)

bg_color = random.choice(BG_COLORS)

# Game loop

running = True

while running:

    for event in pygame.event.get():

       if event.type == pygame.QUIT: running = False

       elif event.type == SPRITE_COLOR_EVENT: sprite.change_color()

       elif event.type == BG_COLOR_EVENT: bg_color = random.choice(BG_COLORS)

    sprites.update()

    screen.fill(bg_color)

    sprites.draw(screen)

    pygame.display.flip()

    clock.tick(240)

pygame.quit()