"""
    screen,
    center_x,
    center_y,
    width,
    height,
    velocity_x,
    velocity_y,
    color
"""
    def __init__(
        screen,
        center_x=100,
        center_y=100,
        width=100,
        height=100,
        velocity_x=10,
        velocity_y=10,
        color=(255, 255, 255)
    ):

    def draw(self):
        self.screen.blit(self.image, self.rect)