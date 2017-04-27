import pygame
import os
import math

from vec2d import Vec2d

class Map:
    def __init__(self, lvlMgr, mapFileName, width, height):
        self.lvlMgr = lvlMgr
        self.width = width
        self.height = height
        self.pixelData = [[0 for x in range(self.width)] for y in range (self.height)]
        self.mapName = mapFileName
        self.mapSurface = None
        self.gravity = Vec2d(0,100)
        
        folder = "Data"
        try:
            self.mapSurface = pygame.image.load(os.path.join(folder, mapFileName))
        except:
            s = "Unable to load " 
            s += mapFileName
            raise(UserWarning, s)
        self.mapSurface.convert()
        
        self.generatePixelData()
        
    def checkCollision(self, point):
        yVal = math.floor(point.y + 1)
        for i in range(math.floor(point.x - 10), math.floor(point.x + 10)):
            if self.pixelData[yVal][i] == 1:
                return True
            
        return False
    
    def generatePixelData(self):
        for i in range(0,600):
            for j in range(0,800):
                if (self.mapSurface.get_at((j,i)).a == 0):
                    self.pixelData[i][j] = 0
                else:
                    self.pixelData[i][j] = 1
                
    def draw(self, surface):
        surface.blit(self.mapSurface, (0,0))
        
class Map1(Map):
    def __init__(self, lvlMgr):
        Map.__init__(self, lvlMgr, "TestMap.png", 800, 600)

class Map2(Map):
    def __init__(self, lvlMgr):
        Map.__init__(self, lvlMgr, "TestMap2.png", 1600, 1200)
