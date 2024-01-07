import pygame
from sys import exit, argv
from tools.board import create_board, draw_board
from tools.computer_player import computer_move
from tools.user_interface import start_screen, end_screen, instructions
from tools.user_interface import draw_start_screen_background
from tools.classes import Player, Game
from tools.config import config


def main(args: list) -> None:
    # game setup
    pygame.init()
    pygame.display.set_caption('Shannon switching - GALE')

    buttonsUI = []
    red = Player()
    blue = Player()
    game = Game()

    FPS, screen, clock = config(args, game)

    create_board(screen, red, blue, buttonsUI, game)
    draw_start_screen_background(screen)

    # main loop of the game
    while True:
        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if game.info:
            instructions(screen, buttonsUI, game)
            continue
        if not game.run[0]:
            start_screen(screen, game, buttonsUI)
            continue
        if game.end[0]:
            end_screen(screen, game)
            continue

        draw_board(screen, red, blue, game)

        if not game.turn and game.run[1] and game.run[2]:
            # best computer move
            computer_move(screen, red, blue, game)
        elif not game.turn and game.run[1]:
            # random computer move
            computer_move(screen, red, blue, game)


if __name__ == "__main__":
    main(argv)
