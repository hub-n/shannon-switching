import pygame
from random import randrange
from tools.board import check_illegal_moves_blue, sort_lines, draw_turn
from tools.classes import Player, Game
import math
from tools.check_path import check_path_red, check_path_blue


def computer_move(screen: pygame.surface.Surface, red: Player,
                  blue: Player, game: Game) -> None:
    draw_turn(screen, not game.turn, game.COLORS)

    # checking if opponent won
    red.append_graph()
    if check_path_red(red.graph):
        game.end[0] = True
        game.end[1] = True
        pygame.draw.line(screen, game.COLORS[0], red.lines[-1][0],
                         red.lines[-1][1], 6)

    if game.run[2]:
        computer_move_best(red, blue, game)
    else:
        computer_move_random(red, blue, game)

    # checking if computer player won
    blue.append_graph()
    if check_path_blue(blue.graph):
        game.end[0] = True
        pygame.draw.line(screen, game.COLORS[1], blue.lines[-1][0],
                         blue.lines[-1][1], 6)


def computer_move_random(red: Player, blue: Player, game: Game) -> None:
    # generate random legal computer move
    while not game.turn:
        i = randrange(30)
        if randrange(2) == 0:
            if (i + 1) % 6 == 0:
                i += -1
            # connect right
            line_start_pos = blue.buttons[i].coordinate
            line_end_pos = (blue.buttons[i].coordinate[0] + 120,
                            blue.buttons[i].coordinate[1])
        else:
            if i > 23:
                i += -6
            # connect down
            line_start_pos = blue.buttons[i].coordinate
            line_end_pos = (blue.buttons[i].coordinate[0],
                            blue.buttons[i].coordinate[1] + 120)
        blue.lines.append([line_start_pos, line_end_pos])
        check_illegal_moves_blue(red, blue, game)
        game.turn = not game.turn


def computer_move_best(red: Player, blue: Player, game: Game) -> None:
    # generate best computer move according to 5 main criteria
    oppMove = red.lines[-1]
    vertical = abs(oppMove[0][0] - oppMove[1][0]) == 0

    # goal 1: fill bottom row according to each new enemy line
    if vertical and oppMove[1][1] != 675:
        line_start_pos = (oppMove[0][0] - 60, 615)
        line_end_pos = (oppMove[0][0] + 60, 615)
        line = [line_start_pos, line_end_pos]
        if try_move(red, blue, game, line):
            return
    else:
        for i in range(1, -1, -1):
            line_start_pos = (oppMove[i][0] - 60, 615)
            line_end_pos = (oppMove[i][0] + 60, 615)
            line = [line_start_pos, line_end_pos]
            if try_move(red, blue, game, line):
                return

    # goal 2: disallow connections between neighbouring enemy lines
    neighbours = neighbouring_lines_coordinates(red)
    if neighbours:
        if abs(neighbours[0][0] - neighbours[1][0]) == 0:
            y = int((neighbours[0][1] + neighbours[1][1]) / 2)
            line_start_pos = (neighbours[0][0] - 60, y)
            line_end_pos = (neighbours[0][0] + 60, y)
        else:
            x = int((neighbours[0][0] + neighbours[1][0]) / 2)
            line_start_pos = (x, neighbours[0][1] - 60)
            line_end_pos = (x, neighbours[0][1] + 60)
    line = [line_start_pos, line_end_pos]
    if try_move(red, blue, game, line):
        return

    # goal 3: block each new enemy line with the nearest line
    order = [0, 1, 2, 3]
    if vertical:
        order = [3, 0]

    for j in order:
        for i in range(1, -1, -1):
            if j == 0:
                # line above point
                line_start_pos = (oppMove[i][0] - 60, oppMove[i][1] - 60)
                line_end_pos = (oppMove[i][0] + 60, oppMove[i][1] - 60)
            elif j == 1:
                # line to the left of point
                line_start_pos = (oppMove[i][0] - 60, oppMove[i][1] - 60)
                line_end_pos = (oppMove[i][0] - 60, oppMove[i][1] + 60)
            elif j == 2:
                # line to the right of point
                line_start_pos = (oppMove[i][0] + 60, oppMove[i][1] - 60)
                line_end_pos = (oppMove[i][0] + 60, oppMove[i][1] + 60)
            else:
                # line below point
                line_start_pos = (oppMove[i][0] - 60, oppMove[i][1] + 60)
                line_end_pos = (oppMove[i][0] + 60, oppMove[i][1] + 60)
            line = [line_start_pos, line_end_pos]
            if try_move(red, blue, game, line):
                return

    # goal 4: fill missing lines in bottom row
    for i in range(24, 29):
        line_start_pos = blue.buttons[i].coordinate
        line_end_pos = blue.buttons[i+1].coordinate
        line = [line_start_pos, line_end_pos]
        if try_move(red, blue, game, line):
            return

    # goal 5: random move
    computer_move_random(red, blue, game)


def try_move(red: Player, blue: Player, game: Game, line: list) -> bool | None:
    # check if move is legal
    blue.lines.append(line)
    check_illegal_moves_blue(red, blue, game)
    p1 = line[0][1] < 135 or line[1][1] < 135
    p2 = line[0][1] > 615 or line[1][1] > 615
    p3 = line[0][0] < 75 or line[1][0] < 75
    p4 = line[0][0] > 675 or line[1][0] > 675
    if p1 or p2 or p3 or p4:
        blue.lines.pop(-1)
        game.turn = not game.turn
    game.turn = not game.turn
    if game.turn:
        return True


def neighbouring_lines_coordinates(red: Player) -> list | None:
    # return points of neighbouring enemy lines (if they exist)
    for line in red.lines[:-1]:
        for point in line:
            for i in range(2):
                tryLine = [[red.lines[-1][i], point]]
                sort_lines(tryLine)
                p2 = tryLine[0] not in red.lines
                if math.dist(red.lines[-1][i], point) == 120 and p2:
                    return [red.lines[-1][i], point]
