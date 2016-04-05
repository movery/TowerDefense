import tile
import pathFinding
import csv
import time
import pygame

class TileSet:
    def __init__(self, file):
        # Initialize everything from file
        with open(file) as f:
            reader = csv.reader(f)
            self.dimensions   = tuple(map(int, reader.next()))

            # Initialize all grid slots to 0
            self.grid  = [[0 for x in xrange(self.dimensions[0])] for x in xrange(self.dimensions[1])]

            # Iterate through the tilemap.
            # j refers to X coord, i refers to Y coord
            self.checkpoints = []
            for j in xrange(self.dimensions[0]):
                line = reader.next()
                for i in xrange(self.dimensions[1]):
                    if 'C' not in line[i] :
                        self.grid[i][j] = tile.Tile((i*64, j*64), (64, 64), line[i])
                    else:
                        if   line[i][1] == 'S':
                            self.start  = (i, j)
                        elif line[i][1] == 'F':
                            self.finish = (i, j)
                        else:
                            self.checkpoints.insert(0, [(i, j), int(line[i][1])])

                        self.grid[i][j] = tile.Tile((i*64, j*64), (64, 64), 'D', line[i][1])

            self.checkpoints = [x[0] for x in sorted(self.checkpoints, key = lambda x: x[1])]
            self.checkpoints.insert(0, self.start)
            self.checkpoints.append(self.finish)

            # Find initial shortest path
            self.route = self.findShortestPath()

    # Draws the grid of tiles to the screen
    def draw(self, screen):
        for i in xrange(self.dimensions[0]):
            for j in xrange(self.dimensions[1]):
                self.grid[i][j].draw(screen)

    # Check if passed coordinates is in bounds of the grid
    def inBounds(self, coordinates):
        return 0 <= coordinates[0] < self.dimensions[0] and \
               0 <= coordinates[1] < self.dimensions[1]

    # Check if passed coordinates contains a pathable tile
    def pathable(self, coordinates):
        return self.grid[coordinates[0]][coordinates[1]].tileType.pathable

    # Finds the pathable neighbor tiles of a position
    # Return a list of tile coordinates
    def neighbors(self, coordinates):
        (i, j) = coordinates
        results = [(i+1, j), (i, j-1), (i-1, j), (i, j+1)]
        results = filter(self.inBounds, results)
        results = filter(self.pathable, results)
        return results

    # Use aStar to find shortest path through all checkpoints
    def findShortestPath(self):
        path = []
        for i in xrange(len(self.checkpoints) - 1):
            path.extend(pathFinding.aStar(self, self.checkpoints[i], self.checkpoints[i+1]))

        return path
