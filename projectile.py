
from vec2d import Vec2d
from physComp import PhysComp
from drawComp import DrawComp

class Projectile:
    def __init__(self, lvlMgr, type = 0, pos = Vec2d(0,0)):
        self.lvlMgr = lvlMgr
        self.entType = 1 #This is a projectile
        self.type = type    #0, 1, 2 = Rocket, Grenade, Homing
        self.pos = pos
        self.width = 34     #TEMP values based off type of projectile
        self.height = 55    #TEMP
        self.originPoint = Vec2d(self.width/2, self.height)
        self.lifespan = 200 #Time until it just times out
        self.toRemove = False
        
        #Physics handler component
        self.physComp = PhysComp(self, self.width, self.height)
        #Rendering handler component
        self.drawComp = DrawComp(self, "Char1.png", self.width, self.height) #TODO fix this to be bullet images
        
        #Spawn the projectile
        self.physComp.setPos(self.pos)
	
    def update(self, deltaTime):
        #Update physics
        self.physComp.addForce(self.lvlMgr.loadedMap.gravity)
        self.physComp.update(deltaTime)
        
        #Check lifespan
        self.lifespan -= 1
        if self.lifespan <= 0:
            self.toRemove = True
    
    def draw(self, renderTarget, deltaTime):
        self.drawComp.draw(renderTarget, deltaTime)
        
    def check_collisions():
        #may not be needed/handled elsewhere
        pass
