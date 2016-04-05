import pygame, sys
import tile
import tileSet
import creep

# GLOBALS
SCREEN_WIDTH  = 704
SCREEN_HEIGHT = 704

# PYGAME STUFF
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock  = pygame.time.Clock()

#INITIALIZE TILESET
map = tileSet.TileSet('map.csv')

# Creep Testing
creep = creep.Creep(100, 200, (64, 64), 0, map)

while (True):
    seconds = clock.tick(128) / 1000.0

    for e in pygame.event.get():
        if e.type == pygame.QUIT or e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()



    map.draw(screen)

    if creep.alive:
        creep.move(seconds, map)
        creep.draw(screen)

    pygame.display.flip()
