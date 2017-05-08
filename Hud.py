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
        self.physComp = PhysComp(self,33,152,Vec2d(0,0))
        self.physComp.pos.y = self.lvlMgr.windowHeight - self.physComp.height
        self.originPoint = Vec2d(0,0)
        self.aimArrow = DrawComp(self,"arrow.png",42,260)
        self.itemSlots = DrawComp(self,"GUI.png",508,152)
        self.healthBar = DrawComp(self,"healthbar.png",331,19)
        self.movementBar = DrawComp(self,"healthbar.png",331,19)
        self.hidden = False
        self.movePhase = DrawComp(self,"movePhase.png",150,75)
        self.phase = DrawComp(self,"movePhase.png",150,75)
    def update(self, dT):          
        if self.lvlMgr.turnPlayer == 0:
            self.currentPlayer = DrawComp(self,"player1.png",150,75)
        elif self.lvlMgr.turnPlayer == 1:
            self.currentPlayer = DrawComp(self,"player2.png",150,75)
        elif self.lvlMgr.turnPlayer == 2:
            self.currentPlayer = DrawComp(self,"player3.png",150,75)
        elif self.lvlMgr.turnPlayer == 3:
            self.currentPlayer = DrawComp(self,"player4.png",150,75)
        if self.lvlMgr.players[self.lvlMgr.turnPlayer].state == Globals.PLAYER_STATE_MOVE:
            self.phase = DrawComp(self,"movePhase.png",150,75)
        elif self.lvlMgr.players[self.lvlMgr.turnPlayer].state == Globals.PLAYER_STATE_ATTACK:
            self.phase = DrawComp(self,"attackPhase.png",150,75)

        
    def draw(self, renderTarget, deltaTime):
        if self.lvlMgr.players[self.lvlMgr.turnPlayer].state == Globals.PLAYER_STATE_MOVE:
            self.healthBar.draw(renderTarget,deltaTime,Vec2d(0,0))
            self.movementBar.draw(renderTarget,deltaTime,Vec2d(0,19))            
        elif self.lvlMgr.players[self.lvlMgr.turnPlayer].state == Globals.PLAYER_STATE_ATTACK:
            self.aimArrow.draw(renderTarget,deltaTime,Vec2d(self.lvlMgr.windowWidth/2,self.lvlMgr.windowHeight/2))
            self.itemSlots.draw(renderTarget,deltaTime)
        self.currentPlayer.draw(renderTarget,deltaTime,Vec2d(0, 350))
        self.phase.draw(renderTarget,deltaTime,Vec2d(250,350))