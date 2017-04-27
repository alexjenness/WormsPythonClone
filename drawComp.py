
import pygame
import os
import math

from vec2d import Vec2d

class DrawComp:
    def __init__(self, owner,fileName, width, height):
        self.fileName = fileName
        self.owner = owner
        self.width = width
        self.height = height
        self.animations = [] #array of an array
        self.animationIndex = 0
        self.subImageIndex = 0
        self.frameLength = .5
        self.frameTime = 0
        self.animationFinished = False
        self.originPoint = Vec2d(width/2, height)
        
        folder = "Data"
        try:
            self.spriteSheet = pygame.image.load(os.path.join(folder, fileName))
        except:
            s = "Unable to load " 
            s += fileName
            raise(UserWarning, s)
        self.spriteSheet.convert()
        hImageAmount = math.floor(self.spriteSheet.get_size()[0]/ width)
        vImageAmount = math.floor(self.spriteSheet.get_size()[1] / height)
        
        print("hImageAmount= ", hImageAmount)
        print("vImageAmount= ", vImageAmount)
        for j in range(1, vImageAmount + 1):
            animation = []
            for i in range(1,hImageAmount + 1):
                animation.append(self.spriteSheet.subsurface(width * (i - 1), height * (j - 1), width, height))
            self.animations.append(animation)
            print(len(animation))
            
        print("Animation Amount = ", len(self.animations))
        
    def setAnimation(self, animationIndex):
        if (self.animationIndex == animationIndex):
            return
        self.animationIndex = animationIndex
        self.frameTime = 0
        self.subImageIndex = 0
        
    def getAnimationAmount(self):
        return len(self.animations)
    
    def isAnimationFinished(self):
        return self.animationFinished
        
    def nextAnimation(self):
        self.animationIndex += 1
        if self.animationIndex == len(self.animations):
            self.animationIndex = 0
            
    def draw(self, surface, deltaTime):
        self.frameTime += deltaTime
        self.animationFinished = False
        if self.frameTime > self.frameLength:
            self.frameTime = 0
            self.subImageIndex += 1
            if self.subImageIndex == len(self.animations[self.animationIndex]):
                self.subImageIndex = 0
                self.animationFinished = True
        surface.blit(self.animations[self.animationIndex][self.subImageIndex], (self.owner.physComp.pos.x, self.owner.physComp.pos.y))
        