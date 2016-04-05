import pygame
from pathFinding import aStar
import tileSet
import tile

class Creep:
    # Image Array
    creepImage = [
        pygame.image.load('textures/ufo.jpg')
    ]

    def __init__(self, health, speed, dimensions, creepType, tileSet):
        # Status Info
        self.health     = health
        self.speed      = speed
        self.alive      = True

        # Position & Info
        self.position   = (tileSet.start[0] * 64, tileSet.start[1] * 64)
        self.dimensions = dimensions
        self.image      = self.creepImage[creepType]

        # Pathing Info
        self.stepsTaken = 0
        self.path       = tileSet.route

    def draw(self, screen):
        screen.blit(self.image, self.position)

    def move(self, seconds, tileSet):
        if self.stepsTaken == len(self.path):
            self.alive = False
        else:
            # Extract destination and direction to move in from the path
            dest      = self.path[self.stepsTaken][0]
            direction = self.path[self.stepsTaken][1]

            # Pull the X and Y coordinates from the destination indices
            destX     = tileSet.grid[dest[0]][dest[1]].position[0]
            destY     = tileSet.grid[dest[0]][dest[1]].position[1]

            # Self's X and Y coordinates
            x         = self.position[0]
            y         = self.position[1]

            # Move in the specified direction.
            # If we go past our destination, set ourselves to our destination
            # and change direction
            if   direction == 0: # Left
                x -= self.speed * seconds
                if x < destX:
                    x = destX
                    self.stepsTaken += 1
            elif direction == 1: # Right
                x += self.speed * seconds
                if x > destX:
                    x = destX
                    self.stepsTaken += 1
            elif direction == 2: # Up
                y -= self.speed * seconds
                if y < destY:
                    y = destY
                    self.stepsTaken += 1
            elif direction == 3: # Down
                y += self.speed * seconds
                if y > destY:
                    y = destY
                    self.stepsTaken += 1

            self.position = (x, y)
