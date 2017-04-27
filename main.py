import pygame
import os

from player import Player




def main():
    pygame.init()
    screen = pygame.display.set_mode((400,400))
    bg_screen = pygame.Surface((400, 400))
    clock = pygame.time.Clock()
    testTime = 0
    done = False
    player = Player(1)
    while not done:
        elapsedTime = clock.tick(60) / 1000
        testTime += elapsedTime
        if player.drawComp.isAnimationFinished():
            player.moveRight()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE)
                windowWidth = event.dict['size'][0]
                windowHeight = event.dict['size'][1]
                #levelManager.setWindowSize(windowWidth, windowHeight)
        screen.blit(bg_screen, (0,0))
        player.update(elapsedTime)
        print(elapsedTime)
        player.draw(screen, elapsedTime)
        pygame.display.flip()            
    pygame.quit()





if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pygame.quit()
        raise e