
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
            
        if pygame.mouse.get_focused():
            mouseButton = pygame.mouse.get_pressed()
            if mouseButton == (1,0,0):
                self.lvlMgr.mouseX, self.lvlMgr.mouseY = pygame.mouse.get_pos()
                #Shoot projectile
                self.lvlMgr.processEvent(Globals.PLAYER_SHOOT)
            if mouseButton == (0,0,1):
                #Change projectile type
                self.lvlMgr.players[self.lvlMgr.turnPlayer].shotType += 1
                if self.lvlMgr.players[self.lvlMgr.turnPlayer].shotType > 2:
                    self.lvlMgr.players[self.lvlMgr.turnPlayer].shotType = 0
            
        if not pressed[pygame.K_a] and not pressed[pygame.K_d]:
            self.lvlMgr.processEvent(Globals.PLAYER_STOP)
