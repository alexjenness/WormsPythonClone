
from vec2d import Vec2d
from physComp import PhysComp
from drawComp import DrawComp

class Projectile:
    def __init__(self, lvlMgr, type = 0, pos = Vec2d(0,0)):
        self.lvlMgr = lvlMgr
        self.entType = 1 #This is a projectile
        self.type = type    #0, 1, 2 = Rocket, Grenade, Homing
        self.pos = pos
        self.width = 16     #TEMP values based off type of projectile
        self.height = 19    #TEMP
        self.originPoint = Vec2d(self.width/2, self.height)
        self.lifespan = 200 #Time until it just times out
        self.toRemove = False
        
        #Physics handler component
        self.physComp = PhysComp(self, self.width, self.height)
        #Rendering handler component
        if self.type == 0:
            self.drawComp = DrawComp(self, "projectile1.png", self.width, self.height)
        elif self.type == 1:
            self.drawComp = DrawComp(self, "projectile2.png", self.width, self.height)
        elif self.type == 2:
            self.drawComp = DrawComp(self, "projectile3.png", self.width, self.height)
        
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
