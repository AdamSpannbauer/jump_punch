class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.speed = 1
        self.gravity = 1
        self.jump_speed = 1
        self.hitboxes = []
        self.hurtboxes = []
        self.health = 1
        self.network_client = None

    def draw(self):
        pass

    def update(self):
        pass

    def jump(self):
        pass

    def punch(self):
        pass

    def move(self):
        pass

    def send(self):
        pass
