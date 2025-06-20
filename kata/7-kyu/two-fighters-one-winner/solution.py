def declare_winner(fighter1, fighter2, first_attacker):
    attacker, defender = (fighter1, fighter2) if first_attacker == fighter1.name else (fighter2, fighter1)
    while True:
        defender.health -= attacker.damage_per_attack
        if defender.health <= 0:
            return attacker.name
        else:
            attacker, defender = defender, attacker