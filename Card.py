import pygame
from pygame.math import Vector2

def loadCardSprites(filepath, columns, rows):
     filepath = "C:\Users\primu\OneDrive\Desktop\Mcdonald trump\Scoundrel\Sprites\sprite.png"
     sheet = pygame.image.load(filepath)
     cardHeight = 71
     cardWidth = 95

     cards = []

     for x in range(13):
          for y in range(4):
               cardRect = pygame.rect(x, y, cardWidth, cardHeight)
               cardImg = sheet.subsurface(cardRect)
               cards.append(cardImg)
     
     
     return cards

class VisualCard:
     def __init__(self, suit, value, image, startX, startY):
          self.suit = suit
          self.rank = self.rank

          suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
          ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]