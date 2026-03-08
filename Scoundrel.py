from dataclasses import dataclass, field
from functools import cached_property
import sys
import webbrowser
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

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 800))
clock = pygame.time.Clock()
current_menu = 3  # 0 = in-game, 1 = game over, 2 = game win, 3 = main menu, 4 = credits
dt = 0

boardBg = pygame.image.load("imageAssets/game_board.png")
boardBg = pygame.transform.scale(boardBg, (1280, 800))

game_over_bg = pygame.image.load("imageAssets/game_over.png")
game_over_bg = pygame.transform.scale(game_over_bg, (1280, 800))

you_win_bg = pygame.image.load("imageAssets/you_win.png")
you_win_bg = pygame.transform.scale(you_win_bg, (1280, 800))

main_menu_bg = pygame.image.load("imageAssets/main_menu.png")
main_menu_bg = pygame.transform.scale(main_menu_bg, (1280, 800))

credits_bg = pygame.image.load("imageAssets/credits.png")
credits_bg = pygame.transform.scale(credits_bg, (1280, 800))

# image assets
backImg = pygame.image.load('customCards/back.png').convert_alpha()
backImg = pygame.transform.smoothscale(backImg, (150, 225))

heart = pygame.image.load("imageAssets/heart.png").convert_alpha()
heart = pygame.transform.scale(heart, (60, 60))

pygame.display.set_caption("Scoundrel: The Dungeon Crawler Card Game")

# constants
size = width, height = screen.get_size()
card_size = (160, 225)
pile_size = (250, 500)

max_health = 20

bar_x = 110
bar_y = 500
bar_width = 30
bar_height = 200

heart_x = 45
heart_y = bar_y + bar_height + 0


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


def card_value(card):
    if isinstance(card.number, int):
        return card.number
    else:
        level_order = {Level.JACK: 11, Level.QUEEN: 12, Level.KING: 13, Level.AS: 14}
        return level_order[card.number]


# game-state globals, initialized in new_game()
manager = None
deck = None
card_hand = None
weapon_slot = None
slain_monsters = None
discard = None
card_hand_storage = []

player_health = 20
weapon_level = -1
ran_away = False

def new_game():
    global manager
    global deck
    global card_hand
    global weapon_slot
    global slain_monsters
    global discard
    global card_hand_storage
    global player_health
    global weapon_level
    global ran_away
    global current_menu

    player_health = 20
    weapon_level = -1
    ran_away = False
    current_menu = 0
    card_hand_storage = []

    manager = CardsManager()

    full_deck = CardSets.n52
    red_colors = [Colors.HEART, Colors.DIAMOND]
    face_levels = [Level.JACK, Level.QUEEN, Level.KING, Level.AS]

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
        size=(card_size[0], card_size[1] + 52),
    )

    # set up deck sprites
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
        rel_offset=15,
    )

    manager.add_set(
        card_hand,
        (270, 138),
        CardSetRights(
            clickable=True,
            draggable_in=False,
            draggable_out=True,
        ),
    )

    # weapon
    weapon_slot = Deck(
        CardsSet(),
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
    slain_monsters = Deck(
        CardsSet(),
        card_size=card_size,
        size=(2.95 * card_size[0] + 100, card_size[1]),
        visible=True
    )

    manager.add_set(
        slain_monsters,
        (445, 488),
        CardSetRights(
            draggable_in=lambda card: (
                (card.color == Colors.CLUB or card.color == Colors.SPADE)
                and (not slain_monsters.cardset or card_value(slain_monsters.cardset[-1]) > card_value(card))
                and weapon_level != -1
            ),
            draggable_out=False,
        ),
    )

    # discard
    discard = Deck(
        CardsSet(),
        card_size=card_size,
        size=(card_size[0], card_size[1]),
        visible=True
    )

    manager.add_set(
        discard,
        (1070, 165),
        CardSetRights(
            draggable_in=True,
            draggable_out=False,
        ),
    )


def Game_Session():
    global player_health
    global current_menu
    global weapon_level
    global ran_away

    if player_health == 0:
        current_menu = 1

    # drawing health bar
    font = pygame.font.SysFont("Book Antiqua", 40)
    screen.blit(boardBg, (0, 0))

    # Draw current HP amount
    pygame.draw.rect(screen, (70, 70, 70), (bar_x, bar_y, bar_width, bar_height))
    hp_ratio = player_health / max_health
    current_height = int(bar_height * hp_ratio)

    # Since bar is vertical, make it fill from bottom upward
    current_y = bar_y + (bar_height - current_height)

    if player_health >= 10:
        pygame.draw.rect(
            screen,
            (20, 110, 20),
            (bar_x, current_y, bar_width, current_height)
        )
    elif player_health > 5:
        pygame.draw.rect(
            screen,
            (180, 160, 50),
            (bar_x, current_y, bar_width, current_height)
        )
    else:
        pygame.draw.rect(
            screen,
            (200, 50, 15),
            (bar_x, current_y, bar_width, current_height)
        )

    screen.blit(heart, (heart_x, heart_y))

    hp_text = font.render(f"{player_health}/{max_health}", True, (135, 100, 50))
    text_rect = hp_text.get_rect(midleft=(heart_x + 60, heart_y + 30))
    screen.blit(hp_text, text_rect)

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
                    if event.to_set == weapon_slot:
                        weapon_level = card_value(card)
                        if len(weapon_slot.cardset) == 2:
                            old_weapon = weapon_slot.cardset[0]
                            weapon_slot.remove_card(old_weapon)
                            discard.append_card(old_weapon)
                            cards = slain_monsters.draw_cards(len(slain_monsters.cardset))
                            for card in cards:
                                discard.append_card(card)

                    elif event.to_set == discard:
                        if card.color == Colors.CLUB or card.color == Colors.SPADE:
                            player_health = player_health - card_value(card) if player_health - card_value(card) >= 0 else 0
                        elif card.color == Colors.HEART:
                            player_health = player_health + card_value(card) if player_health + card_value(card) <= 20 else 20

                    elif event.to_set == slain_monsters:
                        damage_received = card_value(card) - weapon_level if card_value(card) - weapon_level >= 0 else 0
                        player_health = player_health - damage_received if player_health - damage_received >= 0 else 0

                    if len(card_hand.cardset) == 0:
                        if (len(deck.cardset) == 0):
                            current_menu = 2
                        cards = deck.draw_cards(min(4, len(deck.cardset)))
                        if card_hand.cardset:
                            card_hand_storage.append(card_hand.cardset.draw(-1))
                        for card in cards:
                            card_hand.append_card(card)

                    elif len(card_hand.cardset) == 1:
                        cards = deck.draw_cards(min(3, len(deck.cardset)))
                        card_hand.extend_cards(cards)
                        ran_away = False

            case pygame_cards.events.CARDSSET_CLICKED:
                print("clicked", event.set, event.card)
                card = event.card
                clicked_set = event.set

                if clicked_set == deck:
                    if len(card_hand.cardset) == 0:
                        if card_hand.cardset:
                            card_hand_storage.append(card_hand.cardset.draw(-1))
                        cards = deck.draw_cards(min(4, len(deck.cardset)))
                        card_hand.extend_cards(cards)

                    elif len(card_hand.cardset) == 4 and len(deck.cardset) != 0 and ran_away is False:
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
    screen.blit(game_over_bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if x >= 315 and x < 620 and y >= 425 and y < 510:
                new_game()
                return
            elif x >= 660 and x < 965 and y >= 425 and y < 510:
                sys.exit()

        if event.type == pygame.QUIT:
            sys.exit()


def Win_Menu():
    screen.blit(you_win_bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if x >= 315 and x < 620 and y >= 425 and y < 510:
                new_game()
                return
            elif x >= 660 and x < 965 and y >= 425 and y < 510:
                sys.exit()

        if event.type == pygame.QUIT:
            sys.exit()

def Main_Menu():
    screen.blit(main_menu_bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            x,y = event.pos

            if x >= 375 and x < 895:
                if y >= 190 and y < 265:
                    new_game()
                    return
                elif y >= 300 and y < 375:
                    url = "http://www.stfj.net/art/2011/Scoundrel.pdf"
                    webbrowser.open(url)
                elif y >= 410 and y < 485:
                    global current_menu
                    current_menu = 4
                    return
                elif y >= 520 and y < 595:
                    sys.exit()

def Credits():
    screen.blit(credits_bg, (0,0))

    font_text = pygame.font.SysFont("book antiqua", 36)

    lines = [
        "Original Game Creators:",
        "Zach Gage and Kurt Bieg",
        "",
        "Project Team:",
        "Obadiah Smolenski - Game Logic",
        "Abdulmateen Shaikh - Sprites and Visuals",
        "Samuel Xu - Control Scheme and Testing",
        "Mohammed Sadaf - UI/UX and Debugging",
        "",
        "Special Thanks:",
        "HackBU for helping make this project possible"
    ]

    y = 180
    for line in lines:
        text = font_text.render(line, True, (240, 220, 170))
        screen.blit(text, (screen.get_width()//2 - text.get_width()//2, y))
        y += 50

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

running = True
while running:
    if current_menu == 0:
        Game_Session()
    elif current_menu == 1:
        Death_Menu()
    elif current_menu == 2:
        Win_Menu()
    elif current_menu == 3:
        Main_Menu()
    else:
        Credits()

    dt = clock.tick(60) / 1000
    pygame.display.flip()

pygame.quit()