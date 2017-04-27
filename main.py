import pygame
import os

from vec2d import Vec2d
from player import Player
from LevelManager import LevelManager



def main():
    pygame.init()
    screen = pygame.display.set_mode((400,400), pygame.RESIZABLE)
    pygame.display.set_caption("Spell Slingers")
    clock = pygame.time.Clock()

    done = False
    
    levelManager = LevelManager(screen)
    levelManager.loadLevel(1)
    levelManager.addPlayer()
    dT = 0
    while not done:
        dT = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)
                windowWidth = event.dict['size'][0]
                windowHeight = event.dict['size'][1]
                levelManager.setWindowSize(windowWidth, windowHeight)
        levelManager.update(dT)
        
        levelManager.draw(screen, dT)        
    pygame.quit()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pygame.quit()
        raise e