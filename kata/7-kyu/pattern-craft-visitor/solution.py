class StarShip:
    def __init__(self, health):
        self._health = health
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value):
        self._health = value

class Marine(StarShip):
    def __init__(self):
        super().__init__(health = 100)
        
    def accept(self, visitor):
        return visitor.visit_light(self)

class Marauder(StarShip):
    def __init__(self):
        super().__init__(health = 125)
        
    def accept(self, visitor):
        return visitor.visit_armored(self)

class TankBullet:
    def visit_light(self, unit):
        unit.health -= 21
        
    def visit_armored(self, unit):
        unit.health -= 32