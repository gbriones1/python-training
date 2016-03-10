import pygame

from Game import *
from Game.Scenes import *
from Game.Shared import GameConstants

class Breakout:

    def __init__(self):
        self.__lives = 1
        self.__score = 0

        self.__level = Level(self)
        self.__level.load(0)

        self.__pad = Pad((GameConstants.SCREEN_SIZE[0]/2,
                         GameConstants.SCREEN_SIZE[1] - GameConstants.PAD_SIZE[1]),
                         pygame.image.load(GameConstants.SPRITE_PAD)
                         )
        self.__balls = [
            Ball((400, 400), pygame.image.load(GameConstants.SPRITE_BALL), self)
        ]

        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption("Game Programming with Python & PyGame")

        self.__clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE,
                                              pygame.DOUBLEBUF, 32)

        pygame.mouse.set_visible(0)

        self.__scenes = (
            PlayingGameScene(self),
            GameOverScene(self),
            HighscoreScene(self),
            MenuScene(self)
        )

        self.__currentScene = 0

        self.__sounds = ()

    def start(self):
        while 1:
            self.__clock.tick(100)

            self.screen.fill((0, 0, 0))

            currentScene = self.__scenes[self.__currentScene]
            currentScene.handleEvents(pygame.event.get())
            currentScene.render()

            pygame.display.update()

    def changeScene(self, scene):
        self.__currentScene = scene

    def getLevel(self):
        return self.__level

    def getScore(self):
        return self.__score

    def increaseScore(self, score):
        self.__score += score

    def getLives(self):
        return self.__lives

    def getBalls(self):
        return self.__balls

    def getPad(self):
        return self.__pad

    def playSound(self, soundClip):
        sound = self.__sounds[soundClip]

        sound.stop()
        sound.play()

    def reduceLives(self):
        self.__lives -= 1

    def increaseLives(self):
        self.__lives += 1

    def reset(self):
        self.__lives = 5
        self.__score = 0
        self.__level.load(0)

Breakout().start()
