import pygame
from Game.Scenes.Scene import Scene
from Game import Highscore
from Game.Shared import *
class HighscoreScene(Scene):

    def __init__(self, game):
        super(HighscoreScene, self).__init__(game)
        self.__highscoreSprite = pygame.image.load(GameConstants.SPRITE_HIGHSCORE)

    def render(self):
        self.getGame().screen.blit(self.__highscoreSprite, (50, 50))

        self.clearText()

        highscore  = Highscore()

        x = 350
        y = 100
        for score in highscore.getScores():
            self.addText(score[0], x, y, size = 30)
            self.addText(str(score[1]), x + 200, y, size = 30)

            y += 30

        self.addText("Press F1 to start a new game", x, y + 60, size = 30)

        super(HighscoreScene, self).render()

    def handleEvents(self, events):
        super(HighscoreScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.getGame().reset()
                    self.getGame().changeScene(GameConstants.PLAYING_SCENE)