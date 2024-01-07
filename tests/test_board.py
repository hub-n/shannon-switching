import pygame
from tools.classes import Player, Game
from tools.board import create_buttons, draw_lines, check_illegal_moves_red
from tools.config import config

red = Player()
blue = Player()
game = Game()
FPS, screen, clock = config([None], game)
screen = pygame.display.set_mode((750, 750))


def test_create_buttons():
    create_buttons(screen, red, blue, game.COLORS)
    button = red.buttons[0]
    assert button.surface == screen
    assert button.coordinate == (135, 75)
    assert button.color == 'white'


def test_draw_lines_silent():
    game.turn = True
    game.lineInit = [False, (0, 0)]
    game.lineCon = [False, (0, 0)]
    draw_lines(screen, red, blue, game)
    assert game.turn


def test_draw_lines_only_init():
    game.turn = True
    game.lineInit = [True, (135, 75)]
    game.lineCon = [False, (0, 0)]
    draw_lines(screen, red, blue, game)
    assert game.turn


def test_draw_lines_only_con():
    game.turn = True
    game.lineInit = [False, (0, 0)]
    game.lineCon = [True, (135, 75)]
    draw_lines(screen, red, blue, game)
    assert game.turn


def test_draw_lines_connected():
    game.turn = True
    game.lineInit = [True, (135, 75)]
    game.lineCon = [True, (135, 195)]
    draw_lines(screen, red, blue, game)
    assert not game.turn


def test_draw_lines_connected_blue():
    game.turn = False
    game.lineInit = [True, (135, 75)]
    game.lineCon = [True, (135, 195)]
    draw_lines(screen, red, blue, game)
    assert game.turn


def test_check_illegal_moves_red_legal_move():
    red.lines = [[(135, 75), (135, 195)],
                 [(135, 195), (255, 195)]]
    blue.lines = [[(75, 615), (195, 615)],
                  [(195, 615), (315, 615)]]
    game.turn = True
    check_illegal_moves_red(red, blue, game)
    assert red.lines == [[(135, 75), (135, 195)],
                         [(135, 195), (255, 195)]]
    assert blue.lines == [[(75, 615), (195, 615)],
                          [(195, 615), (315, 615)]]


def test_check_illegal_moves_red_organise():
    red.lines = [[(135, 195), (135, 75)],
                 [(135, 195), (255, 195)]]
    blue.lines = [[(75, 615), (195, 615)],
                  [(195, 615), (315, 615)]]
    game.turn = True
    check_illegal_moves_red(red, blue, game)
    assert red.lines == [[(135, 75), (135, 195)],
                         [(135, 195), (255, 195)]]
    assert blue.lines == [[(75, 615), (195, 615)],
                          [(195, 615), (315, 615)]]


def test_check_illegal_moves_red_home_row():
    red.lines = [[(135, 75), (135, 195)],
                 [(255, 75), (375, 75)]]
    blue.lines = [[(75, 615), (195, 615)],
                  [(195, 615), (315, 615)]]
    game.turn = True
    check_illegal_moves_red(red, blue, game)
    assert red.lines == [[(135, 75), (135, 195)]]
    assert blue.lines == [[(75, 615), (195, 615)],
                          [(195, 615), (315, 615)]]


def test_check_illegal_moves_red_intersection_horizontal():
    red.lines = [[(135, 75), (135, 195)],
                 [(255, 315), (375, 315)]]
    blue.lines = [[(315, 255), (315, 375)]]
    game.turn = True
    check_illegal_moves_red(red, blue, game)
    assert red.lines == [[(135, 75), (135, 195)]]
    assert blue.lines == [[(315, 255), (315, 375)]]


def test_check_illegal_moves_red_intersection_vertical():
    red.lines = [[(135, 75), (135, 195)],
                 [(375, 195), (375, 315)]]
    blue.lines = [[(315, 255), (435, 255)]]
    game.turn = True
    check_illegal_moves_red(red, blue, game)
    assert red.lines == [[(135, 75), (135, 195)]]
    assert blue.lines == [[(315, 255), (435, 255)]]


def test_check_illegal_moves_red_repeating():
    red.lines = [[(135, 195), (135, 75)],
                 [(135, 195), (135, 75)]]
    blue.lines = [[(75, 615), (195, 615)]]
    game.turn = True
    check_illegal_moves_red(red, blue, game)
    assert red.lines == [[(135, 75), (135, 195)]]
    assert blue.lines == [[(75, 615), (195, 615)]]


def test_check_illegal_moves_red_legal_move_blue():
    red.lines = [[(135, 75), (135, 195)]]
    blue.lines = [[(75, 615), (195, 615)],
                  [(195, 615), (315, 615)]]
    game.turn = True
    check_illegal_moves_red(red, blue, game)
    assert red.lines == [[(135, 75), (135, 195)]]
    assert blue.lines == [[(75, 615), (195, 615)],
                          [(195, 615), (315, 615)]]
