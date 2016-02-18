from Game.Bricks import Brick
from Game.Shared import *

class SpeedBrick(Brick):

    def __init__(self, position, sprite, game):
        super(SpeedBrick, self).__init__(position, sprite, game)

    def hit(self):
        game = self.getGame()

        for ball in game.getBalls():
            ball.setSpeed(ball.getSpeed() + 1)

        super(SpeedBrick, self).hit()

    def getHitSound(self):
        return GameConstants.SOUND_HIT_BRICK_SPEED