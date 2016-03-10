import pygame
from Game.Scenes.Scene import Scene
from Game.Shared import *
from Game import Highscore

class GameOverScene(Scene):

    def __init__(self, game):
        super(GameOverScene, self).__init__(game)

        self.__playerName = ""
        self.__highscoreSprite = pygame.image.load(GameConstants.SPRITE_HIGHSCORE)

    def render(self):

        self.getGame().screen.blit(self.__highscoreSprite, (50, 50))

        self.clearText()
        self.addText("Your name: ", 300, 200, size=30)
        self.addText(self.__playerName, 420, 200, size=30)
        super(GameOverScene, self).render()

    def handleEvents(self, events):
        super(GameOverScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game = self.getGame()
                    Highscore().add(self.__playerName, game.getScore())
                    game.reset()
                    game.changeScene(GameConstants.HIGHSCORE_SCENE)
                elif event.key >= 65 and event.key <= 122:
                    self.__playerName += chr(event.key)
                if event.key == pygame.K_F1:
                    self.getGame().reset()
                    self.getGame().changeScene(GameConstants.PLAYING_SCENE)