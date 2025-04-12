import pygame

# base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):

        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    
    def draw(self, screen):
        # child classes must override
        pass

    def update(self, dt):
        # child classes must override
        pass


    def collides(self, shape) -> bool:
        distance = self.position.distance_to(shape.position)
        r1, r2 = self.radius, shape.radius
        if distance <= r1 + r2:
            return True

        return False
