import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
current_menu = 0   # 0 = main, 1 = game over, 2 = in-game
dt = 0

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                current_menu = 2
            elif tutorial_rect.collidepoint(event.pos):
                current_menu = 1
            elif quit_rect.collidepoint(event.pos):
                running = False
        
def Death_Menu():
     screen.fill((105,90,60))

def Game_Session():
     screen.fill((105,90,60))

running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if current_menu == 0:
        Main_Menu()

    # flip() the display to put your work on screen
    elif current_menu == 1:
        Death_Menu()
    else :
        Game_Session()
        
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()