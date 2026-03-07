room = []
weapon = None
weaponMaxDamage = None
health = 20

def equipWeapon(slot: int) -> int:
    card = room[slot]
    if card.suit != 'Diamonds':
        return -1

    global weapon, weaponMaxDamage
    weapon = card
    weaponMaxDamage = card.rank

def attackWithWeapon(slot: int) -> int:
    card = room[slot]
    if card.suit not in ['Clubs', 'Spades'] or card.rank >= weaponMaxDamage:
        return -1
    global health, weaponMaxDamage
    health -= max(card.rank - weapon.rank, 0)
    weaponMaxDamage = card.rank

def attackUnarmed(slot: int) -> int:
    card = room[slot]
    global health
    health -= card.rank
