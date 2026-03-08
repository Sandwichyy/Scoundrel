from dataclasses import dataclass, field
from functools import cached_property
import sys
import pygame

from pygame_cards.hands import (
    HorizontalPileGraphic
)
from pygame_cards.manager import CardSetRights, CardsManager
from pygame_cards.deck import CardBackOwner, Deck

from pygame_cards.set import CardsSet
from pygame_cards.classics import CardSets, NumberCard, Level, Colors
from pygame_cards.abstract import AbstractCard, AbstractCardGraphics
import pygame_cards.events

import Game

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 800))
clock = pygame.time.Clock()

# testing purposes:
#current_menu = 1
current_menu = 0 # 0 = in-game, 1 = game over, 2 = game win
dt = 0

#boardBg = pygame.image.load(r"C:\Users\primu\OneDrive\Desktop\Mcdonald trump\Scoundrel\Scoundrel\game_board.png")
boardBg = pygame.image.load("game_board.png")
boardBg = pygame.transform.scale(boardBg, (1280, 800))

# pygame_cards setup
size = width, height = screen.get_size()
manager = CardsManager()
card_size = (160, 225)
pile_size = (250, 500)
full_deck = CardSets.n52
red_colors = [Colors.HEART, Colors.DIAMOND]
face_levels = [Level.JACK, Level.QUEEN, Level.KING, Level.AS]

# removes red face cards
card_set = CardsSet([
    card for card in full_deck
    if not (card.color in red_colors and card.number in face_levels)
])
card_set.shuffle()

# player stats
max_health = 20
player_health = 20
weapon_level = -1
ran_away = False

# deck
deck = Deck(
    CardsSet(card_set),
    card_size=card_size,
    size=(card_size[0], card_size[1] + 52),
)
#deck.load_graphics(face_path=r'customCards/', back_file=r'customCards/back.png')

#set up deck sprites
backImg = pygame.image.load('customCards/back.png').convert_alpha()
backImg = pygame.transform.smoothscale(backImg, (150, 225))

class BalatroGraphics(AbstractCardGraphics):
    def __init__(self, card, filepath, size=(150, 225)):
        super().__init__(card, size)
        self.filepath = filepath

    @cached_property
    def surface(self) -> pygame.Surface:
        img = pygame.image.load(self.filepath).convert_alpha()
        return pygame.transform.smoothscale(img, self.size)
    
    @cached_property
    def back_surface(self) -> pygame.Surface:
        return backImg
    
for card in deck.cardset:
    rankStr = card.name.split(' of ')[0].lower()
    rankStr = rankStr.replace('level.', '')
    if rankStr == 'as':
        rankStr = 'ace'

    suitStr = str(card.color).lower().replace('colors.', '') + 's'

    imgPath = f'customCards/{rankStr}_of_{suitStr}.png'

    card.graphics = BalatroGraphics(card, filepath=imgPath)
    card.back_image = backImg
    if hasattr(card, '_graphics'):
        card._graphics.back_surface = backImg

manager.add_set(
    deck,
    #(screen.get_size()[0] - deck.size[1] - deck.card_border_radius, 50),
    (50, 120),
    CardSetRights(
        clickable=True,
        draggable_in=False,
        draggable_out=False,
    ),
)

# main hand
card_hand = HorizontalPileGraphic(
    CardsSet(),
    card_size=card_size,
    size=(5.9 * card_size[0], card_size[1] + 52),
    rel_offset= 15,
)
card_hand_storage: list[CardsSet] = []

manager.add_set(
    card_hand,
    (270, 138),
    CardSetRights(
        clickable=True,
        draggable_in=False,
        # Only the last card can be used
        #draggable_out=lambda card: (
        #   card == card_hand.cardset[-1] if card_hand.cardset else True
        #),
        draggable_out=True,
    ),
)

# hp display
heart = pygame.image.load("heart.png").convert_alpha()
heart = pygame.transform.scale(heart, (60, 60))

bar_x = 110
bar_y = 500
bar_width = 30
bar_height = 200

heart_x = 45
heart_y = bar_y + bar_height + 0
hp_ratio = player_health / max_health
current_height = int(bar_height * hp_ratio)

# Since bar is vertical, make it fill from bottom upward
current_y = bar_y + (bar_height - current_height)

# weapon
weapon_slot = Deck(
    CardsSet(),  # starts empty
    card_size=card_size,
    size=(0.75 * card_size[0] + 52, card_size[1]),
    visible=True
)

manager.add_set(
    weapon_slot,
    (267, 490),
    CardSetRights(
        draggable_in=lambda card: card.color == Colors.DIAMOND,
        draggable_out=True,
    ),
)

# slain monsters
def card_value(card):
    if isinstance(card.number, int):
        return card.number
    else:
        level_order = {Level.JACK: 11, Level.QUEEN: 12, Level.KING: 13, Level.AS: 14}
        return level_order[card.number]

slain_monsters = Deck(
    CardsSet(),  # starts empty
    card_size=card_size,
    size=(2.95 * card_size[0] + 100, card_size[1]),
    visible=True
)

manager.add_set(
    slain_monsters,
    (445, 488),
    CardSetRights(
        draggable_in=lambda card: (card.color == Colors.CLUB or card.color == Colors.SPADE) and (not slain_monsters.cardset or card_value(slain_monsters.cardset[-1]) > card_value(card)) and weapon_level != -1,
        draggable_out=False,
    ),
)

# discard
discard = Deck(
    CardsSet(),  # starts empty
    card_size=card_size,
    size=(card_size[0], card_size[1]),
    visible=True
)

manager.add_set(
    discard,
    (1070, 165),
    CardSetRights(
        #draggable_in=lambda card: card.color != Colors.DIAMOND,
        draggable_in=True,
        draggable_out=False,
    ),
)

pygame.display.set_caption("Scoundrel: The Dungeon Crawler Card Game")

def Game_Session():
    # drawing health bar
    font = pygame.font.SysFont("Book Antiqua", 40)
    screen.blit(boardBg, (0, 0))

    # Draw current HP amount
    global player_health

    pygame.draw.rect(screen, (70, 70, 70), (bar_x, bar_y, bar_width, bar_height))
    hp_ratio = player_health / max_health
    current_height = int(bar_height * hp_ratio)

    # Since bar is vertical, make it fill from bottom upward
    current_y = bar_y + (bar_height - current_height)

    if player_health >= 10:
        pygame.draw.rect(
            screen,
            (20, 110, 20),  # pale pinkish-brown-ish color
            (bar_x, current_y, bar_width, current_height)
        )
    elif player_health > 5:
        pygame.draw.rect(
            screen,
            (180, 160, 50),  # pale pinkish-brown-ish color
            (bar_x, current_y, bar_width, current_height)
        )
    else:
        pygame.draw.rect(
            screen,
            (200, 50, 15),  # pale pinkish-brown-ish color
            (bar_x, current_y, bar_width, current_height)
        )

    screen.blit(heart, (heart_x, heart_y))

    hp_text = font.render(f"{player_health}/{max_health}", True, (135, 100, 50))
    text_rect = hp_text.get_rect(midleft=(heart_x + 60 , heart_y + 30))
    screen.blit(hp_text, text_rect)

    # handling events
    global weapon_level
    global ran_away
    
    for event in pygame.event.get():
        manager.process_events(event)
        match event.type:
            case pygame.QUIT:
                sys.exit()
            case pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            case pygame_cards.events.CARD_MOVED:
                card = event.card
                
                if event.from_set == card_hand:
                    if len(card_hand.cardset) == 0:
                        cards = deck.draw_cards(min(4, len(deck.cardset)))
                        if card_hand.cardset:
                            card_hand_storage.append(card_hand.cardset.draw(-1))
                        for card in cards:
                           card_hand.append_card(card)

                    elif len(card_hand.cardset) == 1:
                        cards = deck.draw_cards(min(3, len(deck.cardset)))
                        
                        card_hand.extend_cards(cards)
                        ran_away = False

                    if event.to_set == weapon_slot:
                        weapon_level = card_value(card)
                        if len(weapon_slot.cardset) == 2:
                            old_weapon = weapon_slot.cardset[0]
                            weapon_slot.remove_card(old_weapon)
                            discard.append_card(old_weapon)
                            cards = slain_monsters.draw_cards(len(slain_monsters.cardset))
                            for card in cards:
                                discard.append_card(card)

                    if event.to_set == discard:
                        if card.color == Colors.CLUB or card.color == Colors.SPADE:
                            player_health = player_health - card_value(card) if player_health - card_value(card) >= 0 else 0
                        elif card.color == Colors.HEART:
                            player_health = player_health + card_value(card) if player_health + card_value(card) <= 20 else 20

                    if event.to_set == slain_monsters:
                        damage_received = card_value(card) - weapon_level if card_value(card) - weapon_level >= 0 else 0
                        player_health = player_health - damage_received if player_health - damage_received >= 0 else 0

            case pygame_cards.events.CARDSSET_CLICKED:
                print("clicked", event.set, event.card)
                card = event.card
                set = event.set
                if set == deck:
                    if len(card_hand.cardset) == 0:
                        if card_hand.cardset:
                            # Put away the cards
                            card_hand_storage.append(card_hand.cardset.draw(-1))
                        cards = deck.draw_cards(min(4, len(deck.cardset)))
                        card_hand.extend_cards(cards)
                    
                    elif len(card_hand.cardset) == 4 and len(deck.cardset) != 0 and ran_away == False:
                        ran_away = True
                        for fled_cards in card_hand.cardset:
                            deck.append_card(fled_cards)
                            
                        card_hand.remove_all_cards()
                        cards = deck.draw_cards(4)
                        
                        card_hand.extend_cards(cards)        
    
    manager.update(dt)
    manager.draw(screen)
    pygame.display.flip()

def Death_Menu():
     screen.fill((105,90,60))

def Win_Menu():
    screen.fill((105, 90, 60))

# removes cards
def end_game():
    manager.start_crazy(screen)

running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    # ts messes up the other pygame event loops. 
    # Im not sure if that applies to main menu as well we may need to test
    """for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False"""

    # flip() the display to put your work on screen
    if current_menu == 0:
        Game_Session()
    elif current_menu == 1:
        Death_Menu()
    else:
        Win_Menu()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(60) / 1000

    pygame.display.flip()

pygame.quit()