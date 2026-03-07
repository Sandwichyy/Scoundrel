import random

cards = [] #fill w cards
health = 20

#if weapon DNE -1 else dmg value
weaponVal = -1
skip = False

room = []
for i in range(4):
     room[i] = -1

def fillRoom():
     for i in range(4):
          index = random.randInt(0, 51)
          while (cards[index].suit == "Hearts" or cards[index].suit == "Hearts") and (cards[index].rank > 10):
               index = random.randInt(0, 51)

          room[i] = cards[index]
          cards.remove(index)




while health > 0:
     fillRoom()

     #implement primary attack/heal/weapon loop

     


