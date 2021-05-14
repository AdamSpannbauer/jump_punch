import pygame


class Player:
    def __init__(self, x, y, color=(200, 50, 200)):
        self.x = x
        self.y = y
        self.color = color
        self.speed = 1
        self.gravity = 1
        self.jump_speed = 1
        self.hitboxes = []
        self.hurtboxes = []
        self.health = 1
        self.network_client = None

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 50, 50))

    def update(self):
        pass

    def jump(self):
        pass

    def punch(self):
        pass

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if keys[pygame.K_UP]:
            self.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def send(self):
        pass
