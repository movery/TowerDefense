import pygame

class TileType:
    tileTypeEnum = [
        [pygame.image.load('textures/dirt.jpg'), True, False],
        [pygame.image.load('textures/grass.jpg'), False, True],
        [pygame.image.load('textures/water.jpg'), False, False]
    ]

    def __init__(self, tileType):
        self.image     = self.tileTypeEnum[tileType][0]
        self.pathable  = self.tileTypeEnum[tileType][1]
        self.buildable = self.tileTypeEnum[tileType][2]

class Tile:
    def __init__(self, position, dimensions, tileType):
        self.position   = position
        self.dimensions = dimensions
        self.tileType   = TileType(tileType)
        self.rect       = self.tileType.image.get_rect()

    def getCenter(self):
        x = self.position[0] + self.rect.centerx
        y = self.position[1] + self.rect.centery
        return (x, y)

    def draw(self, screen):
        screen.blit(self.tileType.image, self.position)
