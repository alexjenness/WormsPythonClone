
import pygame

import Globals

class GS_Playing:
    
    def __init__(self, lvlMgr):
        self.lvlMgr = lvlMgr
        
        
    def checkInputs(self):
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_a]:
            self.lvlMgr.processEvent(Globals.PLAYER_LEFT)
        if pressed[pygame.K_d]:
            self.lvlMgr.processEvent(Globals.PLAYER_RIGHT)
        if pressed[pygame.K_SPACE]:
            self.lvlMgr.processEvent(Globals.TALL_JUMP)
        if pressed[pygame.K_LSHIFT]:
            self.lvlMgr.processEvent(Globals.LONG_JUMP)
            
        if not pressed[pygame.K_a] and not pressed[pygame.K_d]:
            self.lvlMgr.processEvent(Globals.PLAYER_STOP)
