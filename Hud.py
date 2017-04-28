# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 15:35:45 2017

@author: rlwar
"""
from drawComp import DrawComp
from physComp import PhysComp
from vec2d import Vec2d

class Hud:
    
    def __init__(self, lvlMgr):
        self.lvlMgr = lvlMgr
        self.physComp = PhysComp(self,508,152)
        self.physComp.pos.y = self.lvlMgr.windowHeight - self.physComp.height
        self.originPoint = Vec2d(0,0)
        #self.aimArrow = DrawComp(self,"arrow.png",42,260)
        self.itemSlots = DrawComp(self,"GUI.png",508,152)
        self.hidden = False
    def reveal(self):
        if(self.physComp.pos.y > (self.lvlMgr.windowHeight - self.physComp.height)):
            self.physComp.pos.y -= 5
    def hide(self):
        if(self.physComp.pos.y < self.lvlMgr.windowHeight):
            self.physComp.pos.y += 5
    def update(self, dT):
        if self.lvlMgr.players[self.lvlMgr.turnPlayer].physComp.vel.x > 0:
            self.hidden = True
        elif self.lvlMgr.players[self.lvlMgr.turnPlayer].physComp.vel.x:
            self.hidden = True
        else:
            self.hidden = False
        if self.hidden:
            self.hide()
        else:
            self.reveal()
        
    def draw(self, renderTarget, deltaTime):
        #self.aimArrow.draw(renderTarget, deltaTime)
        self.itemSlots.draw(renderTarget,deltaTime)

            