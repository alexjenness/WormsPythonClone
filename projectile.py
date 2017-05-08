
from vec2d import Vec2d
from physComp import PhysComp
from drawComp import DrawComp

class Projectile:
    def __init__(self, lvlMgr, finalVector, owner,type = 0):
        self.lvlMgr = lvlMgr
        self.entType = 1 #This is a projectile
        self.type = type    #0, 1, 2 = Rocket, Grenade, Homing
        self.owner = owner
        self.pos = self.owner.physComp.pos
        self.width = 16     #TEMP values based off type of projectile
        self.height = 19    #TEMP
        self.originPoint = Vec2d(self.width/2, self.height)
        self.lifespan = 200 #Time until it just times out
        self.toRemove = False
        self.finalVector = finalVector
        
        #Physics handler component
        self.physComp = PhysComp(self, self.width, self.height,self.owner.physComp.pos)
        self.xVel = self.finalVector.x - self.owner.physComp.pos.x
        self.yVel = self.finalVector.y - self.owner.physComp.pos.y
        self.initVelocity = Vec2d(self.xVel/10,self.yVel/10)
        #Rendering handler component
        if self.type == 0:
            self.drawComp = DrawComp(self, "projectile1.png", self.width, self.height)
        elif self.type == 1:
            self.drawComp = DrawComp(self, "projectile2.png", self.width, self.height)
        elif self.type == 2:
            self.drawComp = DrawComp(self, "projectile3.png", self.width, self.height)


         
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
