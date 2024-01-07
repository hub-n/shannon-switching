import pygame
from tools.classes import Player, Game, Button
from tools.config import config

red = Player()
blue = Player()
game = Game()
FPS, screen, clock = config([None], game)
screen = pygame.display.set_mode((750, 750))


def test_button_init_red():
    button = Button(screen, game.COLORS[0], (255, 75), 15, game.COLORS)
    assert button.surface == screen
    assert button.radius == 15
    assert not button.isPressed
    assert button.player


def test_button_init_blue():
    button = Button(screen, game.COLORS[1], (75, 135), 15, game.COLORS)
    assert button.surface == screen
    assert button.radius == 15
    assert not button.isPressed
    assert not button.player


def test_can_line_be_connected_con_enemy_dot():
    button = Button(screen, game.COLORS[0], (255, 75), 15, game.COLORS)
    game.turn = False
    game.lineInit = [True, (255, 75)]
    game.lineCon = [True, (255, 195)]
    assert not button.can_line_be_connected(game)


def test_can_line_be_connected_con_same_dot():
    button = Button(screen, game.COLORS[0], (255, 75), 15, game.COLORS)
    game.turn = True
    game.lineInit = [True, (255, 75)]
    game.lineCon = [True, (255, 75)]
    assert not button.can_line_be_connected(game)


def test_can_line_be_connected_con_far_dot():
    button = Button(screen, game.COLORS[0], (255, 75), 15, game.COLORS)
    game.turn = True
    game.lineInit = [True, (255, 75)]
    game.lineCon = [True, (255, 435)]
    assert not button.can_line_be_connected(game)


def test_can_line_be_connected_true():
    button = Button(screen, game.COLORS[0], (255, 195), 15, game.COLORS)
    game.turn = True
    game.lineInit = [True, (255, 75)]
    game.lineCon = [True, (255, 195)]
    assert button.can_line_be_connected(game)


def test_append_graph():
    red.lines = [[(135, 75), (135, 195)], [(135, 195), (255, 195)],
                 [(255, 195), (255, 315)]]
    red.graph = {
        (135, 75): [(135, 195)],
        (135, 195): [(135, 75), (255, 195)],
        (255, 195): [(135, 195)]
    }
    red.append_graph()
    graph = {
        (135, 75): [(135, 195)],
        (135, 195): [(135, 75), (255, 195)],
        (255, 195): [(135, 195), (255, 315)],
        (255, 315): [(255, 195)]
    }
    assert red.graph == graph
