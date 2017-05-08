
import pygame
import os
import math
import Globals
from projectile import Projectile

from vec2d import Vec2d
from physComp import PhysComp
from drawComp import DrawComp

ANIM_LEFT = 0
ANIM_RIGHT = 1
class Player:
    
    
    def __init__(self, lvlMgr, playerId,position_vec2d):
        self.lvlMgr = lvlMgr
        self.width = 34
        self.height = 55
        self.walkSpeed = 48
        self.amountMoved = 0
        self.moveLimit = 100
        self.canMove = True
        self.falling = False
        self.attacked = False
        self.playerId = playerId
        self.direction = Globals.LEFT
        self.originPoint = Vec2d(self.width/2, self.height)
        self.physComp = PhysComp(self, self.width, self.height, position_vec2d)
        self.drawComp = DrawComp(self, "Char1.png", self.width, self.height)
        self.state = Globals.PLAYER_STATE_TURN_END
        
        
    def stop(self):
        if not self.falling:
            self.physComp.setVel(Vec2d(0,0))
            self.drawComp.frameSpeed = 0
            self.drawComp.subImageIndex = 0
            
    def moveRight(self):
        if self.canMove:
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
        if self.canMove:
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
        if self.canMove:
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
        if self.canMove:
            if not self.falling:
                self.falling = True
                self.physComp.setVel(Vec2d(0,0))
                if self.direction == Globals.LEFT:
                    self.physComp.addForce(Vec2d(-2000,-12000))
                    self.amountMoved += 1
                else:
                    self.physComp.addForce(Vec2d(2000,-12000))
                    self.amountMoved += 1
                
    def shoot(self):
        if self.state == Globals.PLAYER_STATE_ATTACK:
            mousePos = pygame.mouse.get_pos()
            self.lvlMgr.projectiles.append(Projectile(self.lvlMgr,Vec2d(mousePos[0],mousePos[1]),self))
            self.lvlMgr.projectiles[len(self.lvlMgr.projectiles)-1].physComp.addForce(self.lvlMgr.projectiles[len(self.lvlMgr.projectiles)-1].initVelocity)
            self.attacked = True
            
            
    def update(self, deltaTime):
        self.physComp.update(deltaTime)
        
        if abs(self.physComp.vel.y) > 60:
           self.drawComp.subImageIndex = 0
           self.drawComp.frameSpeed = 0
           
        if (self.lvlMgr.loadedMap.checkCollisionLine(self.physComp.pos - Vec2d(self.width/2, 1), self.physComp.pos + Vec2d(self.width/2, -1))):
                self.physComp.setPos(self.physComp.pos + Vec2d(0,-1)) 
                
        if self.state == Globals.PLAYER_STATE_MOVE:
            if self.amountMoved >= self.moveLimit:
                self.canMove = False
                self.lvlMgr.changeGamestate(Globals.GS_PLAYER_ATTACK)
                self.lvlMgr.processEvent(Globals.PLAYER_STOP)
                self.state = Globals.PLAYER_STATE_ATTACK
            if not self.falling:
                if not (self.lvlMgr.loadedMap.checkCollisionLine(self.physComp.pos - Vec2d(self.width/2,0), self.physComp.pos + Vec2d(self.width/2,0))):
                    self.falling = True           
            else:
                if (self.lvlMgr.loadedMap.checkCollisionLine(self.physComp.pos - Vec2d(self.width/2, 0), self.physComp.pos + Vec2d(self.width/2, 0))):
                    #print("landed")
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
        elif self.state == Globals.PLAYER_STATE_ATTACK:
            if self.attacked == True:
                self.lvlMgr.camera.setFollowObject(self.lvlMgr.projectiles[len(self.lvlMgr.projectiles) - 1])
                self.lvlMgr.processEvent(Globals.PLAYER_STATE_TURN_END)
            
    def draw(self, renderTarget, deltaTime):
        self.drawComp.draw(renderTarget, deltaTime)