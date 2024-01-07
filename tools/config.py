import pygame
import argparse
from tools.classes import Game


def config(args: list, game: Game) -> (int, pygame.surface.Surface,
                                       pygame.time.Clock):
    """Configurable game settings are set by flags"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--fps')
    parser.add_argument('--color1p')
    parser.add_argument('--color1s')
    parser.add_argument('--color2p')
    parser.add_argument('--color2s')
    args = parser.parse_args(args[1:])

    # game frame rate
    FPS = args.fps if args.fps else 60

    game.set_colors(args.color1p, args.color2p, args.color1s, args.color2s)

    # screen size and clock are not configurable
    screen = pygame.display.set_mode((750, 750))
    clock = pygame.time.Clock()

    return (FPS, screen, clock)
