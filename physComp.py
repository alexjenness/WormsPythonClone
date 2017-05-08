
import pygame
import os
import math

from vec2d import Vec2d

class PhysComp:
    
    def __init__(self, owner, width, height, position_vec2d):
        self.owner = owner
        self.pos = position_vec2d
        self.vel = Vec2d(0,0)
        self.force = Vec2d(0,0)
        self.width = width
        self.height = height
        
    def addForce(self, force):
        self.force += force
        
    def update(self, deltaTime):
        self.vel += self.force * deltaTime
        self.pos += self.vel * deltaTime
        self.force = 0
    
    def setPos(self, pos):
        self.pos = pos
        
    def getPos(self):
        return self.pos
    
    def setVel(self, vel):
        self.vel = vel
        
    def getVel(self):
        return self.vel

        