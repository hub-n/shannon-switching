import pygame
from tools.classes import Player, Game
from tools.check_path import check_path_red, check_path_blue
from tools.config import config

red = Player()
blue = Player()
game = Game()
FPS, screen, clock = config([None], game)
screen = pygame.display.set_mode((750, 750))


def test_check_path_red_false():
    graph = {
        (135, 75): [(135, 195)],
        (135, 195): [(135, 75), (255, 195)],
        (255, 195): [(135, 195), (255, 315)],
        (255, 315): [(255, 195)]
    }
    assert not check_path_red(graph)


def test_check_path_red_true():
    graph = {
        (135, 75): [(135, 195)],
        (135, 195): [(135, 75), (135, 315)],
        (135, 315): [(135, 195), (255, 315)],
        (255, 315): [(135, 315), (255, 435)],
        (255, 435): [(255, 315), (375, 435)],
        (375, 435): [(255, 435), (375, 555)],
        (375, 555): [(375, 435), (495, 555)],
        (495, 555): [(375, 555), (495, 435)],
        (615, 555): [(615, 675), (615, 435)],
        (615, 675): [(615, 555)],
        (495, 435): [(615, 435), (495, 555)],
        (615, 435): [(495, 435), (615, 555)]
    }
    assert check_path_red(graph)


def test_check_path_blue_false():
    graph = {
        (75, 615): [(195, 615)],
        (195, 615): [(75, 615), (315, 615)],
        (315, 615): [(195, 615), (435, 615)],
        (435, 615): [(315, 615)]
    }
    assert not check_path_blue(graph)


def test_check_path_blue_true():
    graph = {
        (75, 615): [(195, 615)],
        (195, 615): [(75, 615), (315, 615)],
        (315, 615): [(195, 615), (435, 615)],
        (435, 615): [(315, 615), (555, 615)],
        (555, 615): [(435, 615), (675, 615)],
        (675, 615): [(555, 615)]
    }
    assert check_path_blue(graph)
