def zombie_shootout(zombies, distance, ammo):
    count = 0
    while zombies > 0:
        if ammo == 0:
            return f'You shot {count} zombies before being eaten: ran out of ammo.'
        zombies -= 1
        ammo -= 1
        count += 1
        if zombies == 0:
            return f'You shot all {count} zombies.'
        
        distance -= 0.5
        if distance <= 0:
            return f'You shot {count} zombies before being eaten: overwhelmed.'        
    return f'You shot all {count} zombies.'