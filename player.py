
import pygame
import os
import math

from vec2d import Vec2d
from physComp import PhysComp
from drawComp import DrawComp

ANIM_LEFT = 0
ANIM_RIGHT = 1
class Player:
    
    
    def __init__(self, lvlMgr, playerId):
        self.lvlMgr = lvlMgr
        self.width = 34
        self.height = 55
        self.walkSpeed = 48
        self.falling = False
        self.playerId = playerId
        self.originPoint = Vec2d(self.width/2, self.height)
        self.physComp = PhysComp(self, self.width, self.height)
        self.drawComp = DrawComp(self, "Char1.png", self.width, self.height)
        
        self.physComp.setPos(Vec2d(700,100))
        
    def moveRight(self):
        if not self.falling:
            self.drawComp.setAnimation(ANIM_RIGHT)
            self.physComp.setVel(Vec2d(50,0))
        
    def moveLeft(self):
        if not self.falling:
            self.drawComp.setAnimation(ANIM_LEFT)
            self.physComp.setVel(Vec2d(-50,0))
        
    def longJumpLeft(self):
        if not self.falling:
            self.physComp.addForce(Vec2d(-200,100))
        
    def tallJumpLeft(self):
        if not self.falling:
            self.physComp.addForce(Vec2d(-300,-6000)) 
            self.falling = True
            
    def update(self, deltaTime):
        
        if not self.falling:
            if not (self.lvlMgr.loadedMap.checkCollision(self.physComp.pos)):
                self.falling = True
                self.drawComp.subImageIndex = 0
                self.drawComp.frameSpeed = 0
        else:
            if (self.lvlMgr.loadedMap.checkCollision(self.physComp.pos)):
                self.falling = False
        if self.falling:       
            self.physComp.addForce(self.lvlMgr.loadedMap.gravity)
        else:
            self.physComp.vel.y = 0
        self.physComp.update(deltaTime)
        self.moveLeft()
            
    
    def draw(self, renderTarget, deltaTime):
        self.drawComp.draw(renderTarget, deltaTime)