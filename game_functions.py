import  sys
import pygame

def check_events():
    """Respond to keypress and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    # redraw the screen during each pass.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # make screen visible.
    pygame.display.flip()