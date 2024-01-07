import pygame
from tools.classes import Player, Game
from tools.computer_player import computer_move_best
from tools.config import config

red = Player()
blue = Player()
game = Game()
FPS, screen, clock = config([None], game)
screen = pygame.display.set_mode((750, 750))


def test_computer_move_best_goal1_a():
    game.turn = False
    red.lines = [[(135, 75), (135, 195)]]
    blue.lines = []
    computer_move_best(red, blue, game)
    assert blue.lines == [[(75, 615), (195, 615)]]


def test_computer_move_best_goal1_b():
    game.turn = False
    red.lines = [[(255, 195), (255, 315)]]
    blue.lines = []
    computer_move_best(red, blue, game)
    assert blue.lines == [[(195, 615), (315, 615)]]


def test_computer_move_best_goal2_a():
    game.turn = False
    red.lines = [[(255, 195), (255, 315)], [(375, 435), (375, 555)],
                 [(375, 315), (375, 435)]]
    blue.lines = [[(195, 615), (315, 615)], [(315, 615), (435, 615)]]
    computer_move_best(red, blue, game)
    assert blue.lines == [[(195, 615), (315, 615)], [(315, 615), (435, 615)],
                          [(315, 255), (315, 375)]]


def test_computer_move_best_goal2_b():
    game.turn = False
    red.lines = [[(375, 315), (495, 315)], [(255, 555), (375, 555)],
                 [(375, 435), (375, 555)]]
    blue.lines = [[(435, 615), (555, 615)], [(315, 615), (435, 615)]]
    computer_move_best(red, blue, game)
    assert blue.lines == [[(435, 615), (555, 615)], [(315, 615), (435, 615)],
                          [(315, 375), (435, 375)]]


def test_computer_move_best_goal2_c():
    game.turn = False
    red.lines = [[(255, 435), (255, 555)], [(495, 195), (495, 315)],
                 [(375, 315), (495, 315)], [(375, 315), (375, 435)]]
    blue.lines = [[(195, 615), (315, 615)], [(435, 615), (555, 615)],
                  [(315, 615), (435, 615)]]
    computer_move_best(red, blue, game)
    assert blue.lines == [[(195, 615), (315, 615)], [(435, 615), (555, 615)],
                          [(315, 615), (435, 615)], [(315, 375), (315, 495)]]


def test_computer_move_best_goal3_vertical_a():
    game.turn = False
    red.lines = [[(255, 75), (255, 195)], [(255, 195), (255, 315)]]
    blue.lines = [[(195, 615), (315, 615)]]
    computer_move_best(red, blue, game)
    assert blue.lines == [[(195, 615), (315, 615)], [(195, 375), (315, 375)]]


def test_computer_move_best_goal3_vertical_b():
    game.turn = False
    red.lines = [[(255, 315), (255, 435)], [(255, 195), (255, 315)]]
    blue.lines = [[(195, 615), (315, 615)]]
    computer_move_best(red, blue, game)
    assert blue.lines == [[(195, 615), (315, 615)], [(195, 135), (315, 135)]]


def test_computer_move_best_goal3_horizontal():
    game.turn = False
    red.lines = [[(255, 195), (375, 195)], [(255, 315), (375, 315)],
                 [(255, 435), (375, 435)]]
    blue.lines = [[(315, 615), (435, 615)], [(195, 615), (315, 615)]]
    computer_move_best(red, blue, game)
    assert blue.lines == [[(315, 615), (435, 615)], [(195, 615), (315, 615)],
                          [(195, 375), (315, 375)]]
