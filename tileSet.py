import tile
import pathFinding

class TileSet:
    def __init__(self, file):

        # Initialize everything from file
        with open(file) as f:
            self.dim   = tuple([int(x) for x in f.readline().split(",")])
            self.start = tuple([int(x) for x in f.readline().split(",")])

            # Mark checkpoints until -1 is read
            self.checkpoints = []
            while True:
                line = f.readline().split(",")
                if '-1' in line: break
                self.checkpoints.append(tuple([int(x) for x in line]))

            # Initialize all grid slots to 0
            self.grid  = [[0 for x in xrange(self.dim[0])] for x in xrange(self.dim[1])]

            # Read the grid data from file
            tiles = f.read().split('\n')
            for i in xrange(self.dim[0]):
                for j in xrange(self.dim[1]):
                    self.grid[i][j] = tile.Tile((i*64, j*64), (64, 64), int(tiles[j][i]))

            # Find initial shortest path
            self.route = self.findShortestPath()

    # Draw every tile in the grid
    def draw(self, screen):
        for i in xrange(self.dim[0]):
            for j in xrange(self.dim[1]):
                self.grid[i][j].draw(screen)

    # Checks to see if a position is in the bounds of our grid
    def inBounds(self, pos):
        (x, y) = pos
        return 0 <= x < self.dim[0] and 0 <= y < self.dim[1]

    # Checks to see if a position is pathable
    def pathable(self, pos):
        return self.grid[pos[0]][pos[1]].tileType.pathable

    # Finds the pathable neighbors of a position
    def neighbors(self, pos):
        (x, y) = pos
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0: results.reverse() # aesthetics
        results = filter(self.inBounds, results)
        results = filter(self.pathable, results)
        return results

    # Used aStar to find shortest path from start, through all checkpoints, to finish
    def findShortestPath(self):
        path = [x for x in self.checkpoints]
        path.insert(0, self.start)

        ret = []
        for i in xrange(len(path) - 1):
            print i
            ret.extend(pathFinding.aStar(self, path[i], path[i+1]))

        return ret
