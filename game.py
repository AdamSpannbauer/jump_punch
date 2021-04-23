import pygame

BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

FPS = 60
DISPLAY_SIZE = (600, 600)


class Game:
    def __init__(self, players):
        self.players = players

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

    def update(self):
        self.clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_pygame()

    def draw_hud(self):
        pass

    def draw(self):
        self.screen.fill(BLACK)

    def play(self):
        self._init_pygame()

        while not game.game_over:
            self.update()
            self.draw()
            self.draw_hud()

            pygame.display.update()


if __name__ == "__main__":
    players = None
    game = Game(players)
    game.play()
