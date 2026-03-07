room = []
def useWeapon(slot: int) -> int:
    if room[slot].suit != 'Diamonds':
        return -1
