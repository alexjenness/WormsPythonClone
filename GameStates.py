
import pygame

import Globals


class GS_Base:
    def __init__(self, lvlMgr):
        self.lvlMgr = lvlMgr;
        
class GS_PlayerMove(GS_Base):
    
    def __init__(self, lvlMgr):
        GS_Base.__init__(self,lvlMgr)
        
        
    def checkInputs(self):
        pressed = pygame.key.get_pressed()
        clicked = pygame.mouse.get_pressed()
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
        
                
class GS_PlayerAttack(GS_Base):
    
    def __init__(self, lvlMgr):
        GS_Base.__init__(self,lvlMgr)
        
    def checkInputs(self):
        pressed = pygame.key.get_pressed()
        clicked = pygame.mouse.get_pressed()

        if clicked == (1,0,0):
            self.lvlMgr.processEvent(Globals.SHOOT)
            
                