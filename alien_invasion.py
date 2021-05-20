import pygame
import game_functions as gf
from settings import Settings
from ship import Ship


def run_game():
    # initialize game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #put ship in screen.
    ship = Ship(screen)


    # main loop for the game.
    while True:
        # listen keyboard and mouse events.
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)
