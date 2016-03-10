import os

class GameConstants:
    BRICK_SIZE = [100, 30]
    BALL_SIZE = [16, 16]
    PAD_SIZE = [139, 13]
    SCREEN_SIZE = [800, 600]

    SPRITE_BALL = os.path.join("Assets", "ball.png")
    SPRITE_BRICK = os.path.join("Assets", "standard.png")
    SPRITE_SPEEDBRICK = os.path.join("Assets", "speed.png")
    SPRITE_LIFEBRICK = os.path.join("Assets", "life.png")

