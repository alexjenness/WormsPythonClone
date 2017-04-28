

from vec2d import Vec2d

class Camera:
    
    def __init__(self, size):
        self.pos = Vec2d(0,0)
        self.size = size
        self.setCenter(Vec2d(0,0))
        
    def setCenter(self, pos):
        self.pos.x = pos.x - self.size.x/2
        self.pos.y = pos.y - self.size.y/2
        
    def setSize(self, size):
        self.size = size
    def getCenter(self):
        return Vec2d(self.pos.x + self.size.x/2, self.pos.y + self.size.y/2)
