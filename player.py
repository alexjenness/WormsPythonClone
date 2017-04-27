
import pygame
import os
import math

from vec2d import Vec2d
from physComp import PhysComp
from drawComp import DrawComp

ANIM_LEFT = 1
ANIM_RIGHT = 2
class Player:
    
    
    def __init__(self, playerId):
        self.width = 48
        self.height = 48
        self.walkSpeed = 48
        self.falling = False
        self.playerId = playerId
        self.physComp = PhysComp(self, self.width, self.height)
        self.drawComp = DrawComp(self, "Base_M.png", self.width, self.height)
        
        self.physComp.setPos(Vec2d(100,100))
        
        
    def moveRight(self):
        self.drawComp.setAnimation(ANIM_RIGHT)
        self.physComp.setVel(Vec2d(50,0))
        
    def moveLeft(self):
        self.drawComp.setAnimation(ANIM_LEFT)
        self.physComp.setVel(Vec2d(-50,0))
        
    def update(self, deltaTime):
        self.physComp.update(deltaTime)
    
    def draw(self, renderTarget, deltaTime):
        self.drawComp.draw(renderTarget, deltaTime)