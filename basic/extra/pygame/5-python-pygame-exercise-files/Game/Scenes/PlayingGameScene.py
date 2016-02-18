import pygame
from Game.Scenes.Scene import Scene

class PlayingGameScene(Scene):

    def __init__(self, game):
         super(PlayingGameScene, self).__init__(game)

    def render(self):
        super(PlayingGameScene, self).render()

        game = self.getGame()

        for ball in game.getBalls():

            for brick in game.getLevel().getBricks():
                if ball.intersects(brick):
                    brick.hit()
                    ball.changeDirection(brick)
                    break

            ball.updatePosition()

            game.screen.blit(ball.getSprite(), ball.getPosition())

        for brick in game.getLevel().getBricks():
            if not brick.isDestroyed():
                game.screen.blit(brick.getSprite(), brick.getPosition())

    def handleEvents(self, events):
        super(PlayingGameScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()