import pygame
import sys
import time

class TileType:
    tileTypeEnum = {
        'D' : [pygame.image.load('textures/dirt.jpg'), True, False],
        'G' : [pygame.image.load('textures/grass.jpg'), False, True],
        'W' : [pygame.image.load('textures/water.jpg'), False, False]
    }

    tileCheckpointImages = {
        'S' : pygame.image.load('textures/Start.jpg'),
        '1' : pygame.image.load('textures/One.jpg'),
        '2' : pygame.image.load('textures/Two.jpg'),
        '3' : pygame.image.load('textures/Three.jpg'),
        '4' : pygame.image.load('textures/Four.jpg'),
        '5' : pygame.image.load('textures/Five.jpg'),
        '6' : pygame.image.load('textures/Six.jpg'),
        'F' : pygame.image.load('textures/Finish.jpg')
    }

    def __init__(self, tileType, checkNumber = None):
        if checkNumber == None:
            self.image        = self.tileTypeEnum[tileType][0]
            self.pathable     = self.tileTypeEnum[tileType][1]
            self.buildable    = self.tileTypeEnum[tileType][2]
            self.isCheckpoint = False
        else:
            self.image           = self.tileTypeEnum['D'][0]
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
