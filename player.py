from uuid import uuid4
import pygame
from network_utils import encode_network_data, decode_network_data


class Player:
    def __init__(self, x, y, color=(200, 50, 200), player_id=None):
        self.x = x
        self.y = y

        self.id = player_id
        if not self.id:
            self.id = self._gen_player_id()

        self.color = color
        self.speed = 1
        self.gravity = 1
        self.jump_speed = 1
        self.hitboxes = []
        self.hurtboxes = []
        self.health = 1

    @staticmethod
    def _gen_player_id():
        return str(uuid4())

    def encode_network_data(self):
        return encode_network_data(self.id, self.x, self.y)

    def decode_network_data(self, data):
        _, x, y = decode_network_data(data)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, 50, 50))

    def update(self):
        self.move()

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
