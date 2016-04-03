import pygame
from pathFinding import aStar
import tileSet
import tile

class Creep:
    creepImage = [
        pygame.image.load('textures/ufo.jpg')
    ]

    def __init__(self, spawnPoint, destination, health, speed, dimensions, creepType, tileSet, path):
        self.x           = spawnPoint[0]
        self.y           = spawnPoint[1]
        self.destination = destination
        self.health      = health
        self.speed       = speed
        self.dim         = dimensions
        self.image       = self.creepImage[creepType]

        self.stepsTaken  = 0
        self.path        = path


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    # Moves in the direction specified by 'path'
    def move(self, seconds, tileSet):
        if self.stepsTaken == len(self.path):
            return

        dest      = self.path[self.stepsTaken][0]
        direction = self.path[self.stepsTaken][1]

        destX = tileSet.grid[dest[0]][dest[1]].position[0]
        destY = tileSet.grid[dest[0]][dest[1]].position[1]

        if abs(self.x - destX) < 3 and abs(self.y - destY) < 3:
            self.stepsTaken += 1

        if direction == 0:
            self.x -= self.speed * seconds
        elif direction == 1:
            self.x += self.speed * seconds
        elif direction == 2:
            self.y -= self.speed * seconds
        elif direction == 3:
            self.y += self.speed * seconds

    def getPositionIndex(self):
        i = int(self.x // 64)
        j = int(self.y // 64)

        return (i, j)
