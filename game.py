import pygame


class Game:
    def __init__(self, players):
        self.players = players
        self.HUD = None

    def update(self):
        pass

    def draw_hud(self):
        pass

    def draw(self):
        pass


BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

fps = 60
game_over = False
winner = None
display_size = (600, 600)

pygame.init()


def _quit():
    pygame.display.quit()
    pygame.quit()
    print(f"GAME OVER\nWinner: {winner}")
    quit()


screen = pygame.display.set_mode(display_size)
pygame.display.set_caption("FIGHT!")

# YEP
clock = pygame.time.Clock()

while game_over is False:
    clock.tick(fps)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _quit()
