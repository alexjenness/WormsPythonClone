
import pygame
import os
import math
import Globals

from vec2d import Vec2d
from physComp import PhysComp
from drawComp import DrawComp

ANIM_LEFT = 0
ANIM_RIGHT = 1
class Player:
    
    
    def __init__(self, lvlMgr, playerId):
        self.lvlMgr = lvlMgr
        self.entType = 0 #This is a player
        self.width = 34
        self.height = 55
        self.walkSpeed = 48
        self.amountMoved = 0
        self.moveLimit = 100
        self.canMove = True
        self.falling = False
        self.canShoot = False
        self.hasShot = False
        self.shotPower = 1 #TODO This is the power of the shot, it amplifies the force applied to the projectile in LevelManager
        self.playerId = playerId
        self.direction = Globals.LEFT
        self.originPoint = Vec2d(self.width/2, self.height)
        self.physComp = PhysComp(self, self.width, self.height)
        self.drawComp = DrawComp(self, "Char1.png", self.width, self.height)
        
        self.physComp.setPos(Vec2d(700,100))
        
    def stop(self):
        if not self.falling:
            self.physComp.setVel(Vec2d(0,0))
            self.drawComp.frameSpeed = 0
            self.drawComp.subImageIndex = 0
            
    def moveRight(self):
        if self.amountMoved < self.moveLimit:
            if not self.falling:
                self.drawComp.setAnimation(ANIM_RIGHT)
                self.direction = Globals.RIGHT
                if not (self.lvlMgr.loadedMap.checkCollisionLine(self.physComp.pos - Vec2d(self.width/2, self.height), self.physComp.pos + Vec2d(self.width/2, -1))):
                    self.physComp.setVel(Vec2d(50,0))
                    self.drawComp.frameSpeed = 5
                    self.amountMoved += 1
                else:
                    self.physComp.setVel(Vec2d(0,0))
                    self.drawComp.frameSpeed = 0
        else:
            self.physComp.setVel(Vec2d(0,0))
            self.drawComp.frameSpeed = 0
            
    def moveLeft(self):
        if self.amountMoved < self.moveLimit:
            if not self.falling:
                self.drawComp.setAnimation(ANIM_LEFT)
                self.direction = Globals.LEFT
                if not (self.lvlMgr.loadedMap.checkCollisionLine(self.physComp.pos - Vec2d(self.width/2, self.height - 24), self.physComp.pos - Vec2d(self.width/2,2))):
                    self.physComp.setVel(Vec2d(-50,0))
                    self.drawComp.frameSpeed = 5
                    self.amountMoved += 1
                else:
                    self.physComp.setVel(Vec2d(0,0))
                    self.drawComp.frameSpeed = 0
        else:
            self.physComp.setVel(Vec2d(0,0))
            self.drawComp.frameSpeed = 0
            
    def longJump(self):
        if self.amountMoved < self.moveLimit:
            if not self.falling:
                self.falling = True
                self.physComp.setVel(Vec2d(0,0))
                if self.direction == Globals.LEFT:
                    self.physComp.addForce(Vec2d(-8000,-7000))
                    self.amountMoved += 5
                else:
                    self.physComp.addForce(Vec2d(8000,-7000))
                    self.amountMoved += 5
        
    def tallJump(self):
        if self.amountMoved < self.moveLimit:
            if not self.falling:
                self.falling = True
                self.physComp.setVel(Vec2d(0,0))
                if self.direction == Globals.LEFT:
                    self.physComp.addForce(Vec2d(-2000,-12000))
                    self.amountMoved += 1
                else:
                    self.physComp.addForce(Vec2d(2000,-12000))
                    self.amountMoved += 1
            
    def update(self, deltaTime):
        self.physComp.update(deltaTime)
        if self.amountMoved >= self.moveLimit:
            self.canMove = False
            self.canShoot = True
        if not self.falling:
            if not (self.lvlMgr.loadedMap.checkCollisionLine(self.physComp.pos - Vec2d(self.width/2,0), self.physComp.pos + Vec2d(self.width/2,0))):
                self.falling = True
                
        else:
            if (self.lvlMgr.loadedMap.checkCollisionLine(self.physComp.pos - Vec2d(self.width/2, 0), self.physComp.pos + Vec2d(self.width/2, 0))):
                self.falling = False
            else:
                if abs(self.physComp.vel.y) > 60:
                    self.drawComp.subImageIndex = 0
                    self.drawComp.frameSpeed = 0
        if self.falling:       
            self.physComp.addForce(self.lvlMgr.loadedMap.gravity)
        else:
            self.physComp.vel.y = 0
        if (self.lvlMgr.loadedMap.checkCollisionLine(self.physComp.pos - Vec2d(self.width/2, 1), self.physComp.pos + Vec2d(self.width/2, -1))):
            self.physComp.setPos(self.physComp.pos + Vec2d(0,-1))

        
    def draw(self, renderTarget, deltaTime):
        self.drawComp.draw(renderTarget, deltaTime)