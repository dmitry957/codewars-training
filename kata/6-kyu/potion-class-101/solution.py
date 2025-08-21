from math import ceil

class Potion:
    def __init__(self, color, volume):
        self.color = color
        self.volume = volume
    
    def mix(self, other):
        #ceiling((C1 * V1 + C2 * V2) / (V1 + V2))
        self_r, self_g, self_b = self.color
        other_r, other_g, other_b = other.color
        new_volume = self.volume + other.volume
        new_r = ceil((self_r*self.volume + other_r*other.volume) / (new_volume))
        new_g = ceil((self_g*self.volume + other_g*other.volume) / (new_volume))
        new_b = ceil((self_b*self.volume + other_b*other.volume) / (new_volume))
        new_potion = Potion((new_r, new_g, new_b), new_volume)
        return new_potion