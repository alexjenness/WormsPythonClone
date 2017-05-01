
class Projectile:
    def __init__(self, lvlMgr, type = 0, pos = Vec2d(0,0), vel = Vec2d(0,0)):
        self.lvlMgr = lvlMgr
        self.type = type    #0, 1, 2 = Rocket, Grenade, Homing
		self.pos = pos
		self.vel = vel
        self.width = 10     #TEMP
        self.height = 10    #TEMP
        
        #Physics handler component
        self.physComp = PhysComp(self, self.width, self.height)
        #Rendering handler component
        self.drawComp = DrawComp(self, "Char1.png", self.width, self.height)
	
    def update_self(self, deltaTime):
        #Update physics
        self.physComp.update(deltaTime)
    
    def draw_self(self, renderTarget, deltaTime):
        self.drawComp.draw(renderTarget, deltaTime)
    
	def move_self(self, dt):
		pass
    
    def check_collisions(self):
        pass