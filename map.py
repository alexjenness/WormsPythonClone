import pygame
import os
import math

from vec2d import Vec2d

class Map:
    def __init__(self, lvlMgr, mapFileName, width, height):
        self.lvlMgr = lvlMgr
        self.width = width
        self.height = height
        self.pixelData = [[0 for x in range(self.height)] for y in range (self.width)]
        self.mapName = mapFileName
        self.mapSurface = None
        self.gravity = Vec2d(0,300)
        
        folder = "Data"
        try:
            self.mapSurface = pygame.image.load(os.path.join(folder, mapFileName))
        except:
            s = "Unable to load " 
            s += mapFileName
            raise(UserWarning, s)
        self.mapSurface.convert()
        
        self.generatePixelData()
        
    def checkCollisionLine(self, point1, point2):
        if (point1.y == point2.y):
            for i in range(min(math.floor(point1.x), math.floor(point2.x)), max(math.floor(point1.x), math.floor(point2.x))):
                if self.pixelData[i][math.floor(point1.y)] == 1:
                    return True
        elif (point1.x == point2.x):
            for i in range(min(math.floor(point2.y), math.floor(point1.y)), max(math.floor(point2.y), math.floor(point1.y))):
                if self.pixelData[math.floor(point1.x)][i] == 1:
                    return True
        return False
        
    def checkCollision(self, point):
        if self.pixelData[point.x][point.y] == 1:
            return True
        return False
    
    def generatePixelData(self):
        for i in range(0,self.width):
            for j in range(0,self.height):
                if (self.mapSurface.get_at((i,j)).a == 0):
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
