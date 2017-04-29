# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 15:35:45 2017

@author: rlwar
"""
from drawComp import DrawComp
from physComp import PhysComp
from vec2d import Vec2d
import Globals
class Hud:
    
    def __init__(self, lvlMgr):
        self.lvlMgr = lvlMgr
        self.physComp = PhysComp(self,33,152)
        self.physComp.pos.y = self.lvlMgr.windowHeight - self.physComp.height
        self.originPoint = Vec2d(0,0)
        self.aimArrow = DrawComp(self,"arrow.png",42,260)
        self.itemSlots = DrawComp(self,"GUI.png",508,152)
        self.healthBar = DrawComp(self,"healthbar.png",331,19)
        self.movementBar = DrawComp(self,"healthbar.png",331,19)
        self.hidden = False
        self.currentState = Globals.PLAYER_STATE_MOVE

    def update(self, dT):          
        if self.currentState == Globals.PLAYER_STATE_MOVE:
            if self.lvlMgr.players[self.lvlMgr.turnPlayer].canMove == False:
                self.currentState = Globals.PLAYER_STATE_AIM
        elif self.currentState == Globals.PLAYER_STATE_AIM:
            a = 5
        elif self.currentState == Globals.PLAYER_STATE_ATTACK:
            a = 5
        
    def draw(self, renderTarget, deltaTime):
        if self.currentState == Globals.PLAYER_STATE_MOVE:
            self.healthBar.draw(renderTarget,deltaTime,Vec2d(0,0))
            self.movementBar.draw(renderTarget,deltaTime,Vec2d(0,20))
        elif self.currentState == Globals.PLAYER_STATE_AIM:
            self.itemSlots.draw(renderTarget,deltaTime)
            self.aimArrow.draw(renderTarget,deltaTime,Vec2d(self.lvlMgr.windowWidth/2,self.lvlMgr.windowHeight/2))
        elif self.currentState == Globals.PLAYER_STATE_ATTACK:
                self.itemSlots.draw(renderTarget,deltaTime)