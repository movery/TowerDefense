import pygame, sys
import tile
import tileSet
import creep

# GLOBALS
SCREEN_HEIGHT = 512
SCREEN_WIDTH  = 512

# PYGAME STUFF
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock  = pygame.time.Clock()

#INITIALIZE TILESET
map = tileSet.TileSet('map.txt')

# Creep Testing
creep = creep.Creep((0, 0), (7,0), 100, 100, (64, 64), 0, map, map.findShortestPath())

while (True):
    seconds = clock.tick(128) / 1000.0

    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    creep.move(seconds, map)

    map.draw(screen)
    creep.draw(screen)

    pygame.display.flip()
