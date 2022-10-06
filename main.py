import pygame as pg, sys
from arena import Arena
from player import Player

#Sets FPS constant
FPS = 60

#Creates the game loop
class gameLoop:

    def __init__(self):
        
        pg.init()
        self.screen = pg.display.set_mode((1680, 1080))
        pg.display.set_caption('ShootnRun')
        self.clock = pg.time.Clock()
        self.arena = Arena()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if pg.key.get_pressed()[pg.K_ESCAPE]:
                    pg.quit()
                    sys.exit()

            self.screen.fill('darkgrey')
            self.arena.run()
            pg.display.update()
            print(Player.rect.y)
            self.clock.tick(FPS)

#Starts game loop
if __name__ == '__main__':
    loop = gameLoop()
    loop.run()