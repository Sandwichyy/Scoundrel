from dataclasses import dataclass, field
from functools import cached_property
import sys
import pygame

from pygame_cards.hands import (
    HorizontalPileGraphic,
    VerticalPileGraphic,
)
from pygame_cards.manager import CardSetRights, CardsManager
from pygame_cards.deck import CardBackOwner, Deck

from pygame_cards.set import CardsSet
from pygame_cards.classics import CardSets, NumberCard, Level, Colors
from pygame_cards.abstract import AbstractCard, AbstractCardGraphics
import pygame_cards.events


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
current_menu = 0   # 0 = main, 1 = game over, 2 = in-game
# testing purposes:
#current_menu = 1
current_menu = 2
dt = 0

#boardBg = pygame.image.load(r"C:\Users\primu\OneDrive\Desktop\Mcdonald trump\Scoundrel\Scoundrel\game_board.png")
boardBg = pygame.image.load("game_board.png")
boardBg = pygame.transform.scale(boardBg, (1280, 720))

# pygame_cards setup
size = width, height = screen.get_size()
manager = CardsManager()
card_size = (150, 225)
pile_size = (250, 500)
full_deck = CardSets.n52
red_colors = [Colors.HEART, Colors.DIAMOND]
face_levels = [Level.JACK, Level.QUEEN, Level.KING]

# removes red face cards
card_set = CardsSet([
    card for card in full_deck
    if not (card.color in red_colors and card.number in face_levels)
])
card_set.shuffle()

# deck
deck = Deck(
    CardsSet(card_set),
    card_size=card_size,
    size=(card_size[0] + 52, card_size[1] + 52),
)
#deck.load_graphics(face_path=r'customCards/', back_file=r'customCards/back.png')

#set up deck sprites
"""backImg = pygame.image.load('customCards/back.png').convert_alpha()
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
"""
manager.add_set(
    deck,
    #(screen.get_size()[0] - deck.size[1] - deck.card_border_radius, 50),
    (50, 200),
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
    size=(5 * card_size[0], card_size[1] + 52),
    rel_offset=6,
)
card_hand_storage: list[CardsSet] = []

manager.add_set(
    card_hand,
    (200, 200),
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

# weapon
weapon_slot = Deck(
    CardsSet(),  # starts empty
    card_size=card_size,
    size=(card_size[0] + 52, card_size[1] + 52),
    visible=True
)

manager.add_set(
    weapon_slot,
    (150, 500),
    CardSetRights(
        draggable_in=lambda card: card.color == Colors.DIAMOND and len(weapon_slot.cardset) < 1,
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
    size=(card_size[0] + 300, card_size[1]),
    visible=True
)

manager.add_set(
    slain_monsters,
    (500, 500),
    CardSetRights(
        draggable_in=lambda card: card.color == Colors.CLUB or card.color == Colors.SPADE and card_value(slain_monsters.cardset[-1]) > card_value(card),
        draggable_out=True,
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
    (900, 200),
    CardSetRights(
        #draggable_in=lambda card: card.color != Colors.DIAMOND,
        draggable_in=True,
        draggable_out=True,
    ),
)

pygame.display.set_caption("Scoundrel: The Dungeon Crawler Card Game")

def Main_Menu():
    screen.fill((105,90,60))
    # title appearance
    title_font = pygame.font.SysFont("Book Antiqua", 150)
    title_text = title_font.render("Scoundrel", True, (255,255,255))

    splash_font = pygame.font.SysFont("Book Antiqua", 40)
    splash_text = splash_font.render("The Dungeon Crawler Card Game", True, (255, 255, 255))

    screen.blit(title_text, (screen.get_width() / 4, 75))
    screen.blit(splash_text, (screen.get_width() / 4 + 40, 250))

    # button rectangles
    start_rect = pygame.Rect(1 * screen.get_width() / 10, 7 * screen.get_height() / 10, 210, 100)
    pygame.draw.rect(screen, (200,200,200), start_rect)

    tutorial_rect = pygame.Rect(4 * screen.get_width() / 10, 7 * screen.get_height() / 10, 210, 100)
    pygame.draw.rect(screen, (200,200,200), tutorial_rect)

    quit_rect = pygame.Rect(7 * screen.get_width() / 10, 7 * screen.get_height() / 10, 210, 100)
    pygame.draw.rect(screen, (200,200,200), quit_rect)
    
    # button text
    button_font = pygame.font.SysFont("Book Antiqua", 50)
    start_text = button_font.render("Start", True, (0,0,0))
    tutorial_text = button_font.render("How to Play", True, (0,0,0))
    quit_text = button_font.render("Quit", True, (0,0,0))

    screen.blit(start_text, (1 * screen.get_width() / 10, 7 * screen.get_height() / 10))
    screen.blit(tutorial_text, (4 * screen.get_width() / 10, 7 * screen.get_height() / 10))
    screen.blit(quit_text, (7 * screen.get_width() / 10, 7 * screen.get_height() / 10))

    # button press stuff
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                current_menu = 2
            elif tutorial_rect.collidepoint(event.pos):
                current_menu = 1
            elif quit_rect.collidepoint(event.pos):
                running = False
        
def Death_Menu():
     screen.fill((105,90,60))

def Game_Session():
    screen.blit(boardBg, (0, 0))

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

                    """elif len(card_hand.cardset) == 1:
                        cards = deck.draw_cards(min(3, len(deck.cardset)))
                        card_hand.extend_cards(cards)"""
        
    
    manager.update(dt)
    manager.draw(screen)
    pygame.display.flip()


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

    if current_menu == 0:
        Main_Menu()
    # flip() the display to put your work on screen
    elif current_menu == 1:
        Death_Menu()
    else:
        Game_Session()


    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(60) / 1000

    pygame.display.flip()

pygame.quit()