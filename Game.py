import random

cards = [] #fill w cards
discarded = []
health = 20


#if weapon DNE -1 else dmg value
weaponVal = -1
lastAttacked = None
weapon = None
health = 20
skip = False

room = []
for i in range(4):
     room[i] = -1

def fillRoom():
     for i in range(4):
          index = random.randInt(0, 51)
          while (cards[index].suit == "Diamonds" or cards[index].suit == "Hearts") and (cards[index].rank > 10):
               cards.remove(index)
               index = random.randInt(0, 51)

          room[i] = cards[index]
          cards.remove(index)

def discard(slot):
     discarded.append(room[slot])
     room[slot] = -1

def heal(slot):
     heal += room[slot].rank
     discard[slot]


#Attack fxns
def equipWeapon(slot: int) -> int:
     card = room[slot]
     if card.suit != 'Diamonds':
          return -1

     weapon = card
     weaponVal = card.rank

def attackWithWeapon(slot: int) -> int:
     currCard = room[slot]
     if lastAttacked.rank > currCard.rank:
          health -= max(lastAttacked.rank - weaponVal, 0)
          lastAttacked = currCard
          discard(slot)
     else:
          return -1
    

def attackUnarmed(slot: int) -> int:
     card = room[slot]
     health -= card.rank
     discard(slot)


#main loop
while health > 0 or cards.len == 0:
     fillRoom()
     #implement primary attack/heal/weapon loop
     