import os

class GameConstants:
    BRICK_SIZE = [100, 30]
    BALL_SIZE = [16, 16]
    PAD_SIZE = [139, 13]
    SCREEN_SIZE = [800, 600]

    SPRITE_BALL = os.path.join("Game", "Assets", "ball.png")
    SPRITE_PAD = os.path.join("Game", "Assets", "pad.png")
    SPRITE_BRICK = os.path.join("Game", "Assets", "standard.png")
    SPRITE_SPEEDBRICK = os.path.join("Game", "Assets", "speed.png")
    SPRITE_LIFEBRICK = os.path.join("Game", "Assets", "life.png")
    SPRITE_HIGHSCORE = os.path.join("Game", "Assets", "highscore.png")
    SPRITE_MENU = os.path.join("Game", "Assets", "menu.png")

    SOUND_FILE_HIT_BRICK = os.path.join("Game", "Assets", "BrickHit.wav")
    SOUND_FILE_HIT_BRICK_LIFE = os.path.join("Game", "Assets", "ExtraLife.wav")
    SOUND_FILE_HIT_BRICK_SPEED = os.path.join("Game", "Assets", "SpeedUp.wav")
    SOUND_FILE_HIT_WALL = os.path.join("Game", "Assets", "WallBounce.wav")
    SOUND_FILE_HIT_PAD = os.path.join("Game", "Assets", "PadBounce.wav")
    SOUND_FILE_GAMEOVER = os.path.join("Game", "Assets", "GameOver.wav")

    SOUND_GAMEOVER = 0
    SOUND_HIT_BRICK = 1
    SOUND_HIT_BRICK_LIFE = 2
    SOUND_HIT_BRICK_SPEED = 3
    SOUND_HIT_WALL = 4
    SOUND_HIT_PAD = 5

    PLAYING_SCENE = 0
    GAMEOVER_SCENE = 1
    HIGHSCORE_SCENE = 2
    MENU_SCENE = 3

