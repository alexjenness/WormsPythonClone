import pygame

from vec2d import Vec2d
from player import Player
from LevelManager import LevelManager
from GameStates import GS_PlayerMove
from GameStates import GS_PlayerAttack
import Globals

gameStates = []
gameState = None

def setGamestate(newGS):
    global gameState
    gameState = gameStates[newGS]
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((400,400), pygame.RESIZABLE)
    pygame.display.set_caption("Spell Slingers")
    clock = pygame.time.Clock()
    
    global gameState
    
    done = False
    
    levelManager = LevelManager(screen)
    levelManager.loadLevel(1)
    levelManager.addPlayer(Vec2d(700,100))
    levelManager.addPlayer(Vec2d(660,100))
    levelManager.setChangeGamestateFunction(setGamestate)
    #need to set first players game state and attach camera too them
    levelManager.players[levelManager.turnPlayer].state = Globals.PLAYER_STATE_MOVE
    levelManager.camera.setFollowObject(levelManager.players[levelManager.turnPlayer])
    levelManager.players[levelManager.turnPlayer + 1].canMove = False
    gameStates.append(GS_PlayerMove(levelManager))
    gameStates.append(GS_PlayerAttack(levelManager))
    
    gameState = gameStates[Globals.GS_PLAYER_MOVE]
    
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
        gameState.checkInputs()
        levelManager.update(dT)
        
        levelManager.draw(screen, dT)        
    pygame.quit()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pygame.quit()
        raise e