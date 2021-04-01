from collision_box import CollisionBox


class Hitbox(CollisionBox):
    def __init__(self, x, y, radius, damage):
        super(Hitbox, self).__init__(x, y, radius)
        self.damage = damage
