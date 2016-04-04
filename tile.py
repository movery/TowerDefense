import pygame
import sys
import time

class TileType:
    tileTypeEnum = [
        [pygame.image.load('textures/dirt.jpg'), True, False],
        [pygame.image.load('textures/grass.jpg'), False, True],
        [pygame.image.load('textures/water.jpg'), False, False]
    ]

    tileCheckpointImages = [
        pygame.image.load('textures/Start.jpg'),
        pygame.image.load('textures/One.jpg'),
        pygame.image.load('textures/Two.jpg'),
        pygame.image.load('textures/Three.jpg'),
        pygame.image.load('textures/Four.jpg'),
        pygame.image.load('textures/Five.jpg'),
        pygame.image.load('textures/Six.jpg'),
        pygame.image.load('textures/Finish.jpg')
    ]

    def __init__(self, tileType, checkNumber = None):
        if tileType < 3:
            self.image        = self.tileTypeEnum[tileType][0]
            self.pathable     = self.tileTypeEnum[tileType][1]
            self.buildable    = self.tileTypeEnum[tileType][2]
            self.isCheckpoint = False
        else:
            self.image           = self.tileTypeEnum[0][0]
            self.checkpointImage = self.tileCheckpointImages[checkNumber]
            self.isCheckpoint    = True
            self.pathable        = True
            self.buildable       = False

class Tile:
    def __init__(self, position, dimensions, tileType, checkNumber = None):
        self.position   = position
        self.dimensions = dimensions
        self.tileType   = TileType(tileType, checkNumber)
        self.rect       = self.tileType.image.get_rect()

    def getCenter(self):
        x = self.position[0] + self.rect.centerx
        y = self.position[1] + self.rect.centery
        return (x, y)

    def draw(self, screen):
        screen.blit(self.tileType.image, self.position)
        if self.tileType.isCheckpoint:
            screen.blit(self.tileType.checkpointImage, self.position)
