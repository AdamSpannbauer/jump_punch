import pygame

from network_client import NetworkClient
from network_utils import get_host_name, PORT, FORMAT

from player import Player

BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

FPS = 60
DISPLAY_SIZE = (600, 600)

SERVER = get_host_name()


class Client:
    def __init__(self):
        self.player1 = Player(50, 50)
        self.player2 = Player(50, 50)

        self.players = [self.player1, self.player2]
        self.network_client = NetworkClient(SERVER, PORT)

        self.HUD = None

        self.clock = None
        self.screen = None
        self.game_over = False
        self.winner = None

    def _quit_pygame(self):
        pygame.display.quit()
        pygame.quit()
        print(f"GAME OVER\nWinner: {self.winner}")
        quit()

    def _init_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode(DISPLAY_SIZE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("FIGHT!")

    def update_player_1(self):
        self.player1.update()

        data = self.player1.encode_network_data()
        self.network_client.send(data)

    def update_player_2(self):
        data = self.network_client.recv()
        self.player2.decode_network_data(data)

    def update(self):
        self.clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_pygame()

        self.update_player_1()
        self.update_player_2()

    def draw_hud(self):
        pass

    def draw(self):
        self.screen.fill(GRAY)
        for player in self.players:
            player.draw(self.screen)

    def play(self):
        self._init_pygame()

        while not game.game_over:
            self.update()
            self.draw()
            self.draw_hud()

            pygame.display.update()


if __name__ == "__main__":
    game = Client()
    game.play()
