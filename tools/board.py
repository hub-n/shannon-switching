import pygame
from tools.classes import Button, Player, Game
from tools.user_interface import create_ui_buttons
from tools.check_path import check_path_red, check_path_blue


def create_board(screen: pygame.surface.Surface, red: Player,
                 blue: Player, buttonsUI: list, game: Game) -> None:
    create_buttons(screen, red, blue, game.COLORS)
    create_ui_buttons(screen, buttonsUI, game.COLORS)


def draw_board(screen: pygame.surface.Surface, red: Player,
               blue: Player, game: Game) -> None:

    draw_lines(screen, red, blue, game)

    draw_buttons(red, blue, game)


def create_buttons(screen: pygame.surface.Surface, red: Player,
                   blue: Player, COLORS: list) -> None:
    for y in range(75, 676, 120):
        for x in range(135, 616, 120):
            button = Button(screen, COLORS[0], (x, y), 15, COLORS)
            red.buttons.append(button)

    for y in range(135, 616, 120):
        for x in range(75, 676, 120):
            button = Button(screen, COLORS[1], (x, y), 15, COLORS)
            blue.buttons.append(button)


def draw_buttons(red: Player, blue: Player, game: Game) -> None:
    for button in red.buttons:
        button.draw(game)

    for button in blue.buttons:
        button.draw(game)


def draw_lines(screen: pygame.surface.Surface, red: Player,
               blue: Player, game: Game) -> None:
    if not red.lines and not blue.lines:
        draw_turn(screen, game.turn, game.COLORS)

    # checking if a new line was connected
    if game.lineInit[0] and game.lineCon[0]:
        if game.turn:
            red.lines.append([game.lineInit[1], game.lineCon[1]])
            check_illegal_moves_red(red, blue, game)
            if game.turn:
                draw_turn(screen, not game.turn, game.COLORS)
                red.append_graph()
                if check_path_red(red.graph):
                    game.end[0] = True
                    game.end[1] = True
                    pygame.draw.line(screen, game.COLORS[0], red.lines[-1][0],
                                     red.lines[-1][1], 6)
        else:
            blue.lines.append([game.lineInit[1], game.lineCon[1]])
            check_illegal_moves_blue(red, blue, game)
            if not game.turn:
                draw_turn(screen, not game.turn, game.COLORS)
                blue.append_graph()
                if check_path_blue(blue.graph):
                    game.end[0] = True
                    pygame.draw.line(screen, game.COLORS[1], blue.lines[-1][0],
                                     blue.lines[-1][1], 6)
        game.lineInit[0] = False
        game.lineCon[0] = False
        game.turn = not game.turn

    # drawing last lines of each color
    if red.lines:
        pygame.draw.line(screen, game.COLORS[0], red.lines[-1][0],
                         red.lines[-1][1], 6)
    if blue.lines:
        pygame.draw.line(screen, game.COLORS[1], blue.lines[-1][0],
                         blue.lines[-1][1], 6)


def draw_turn(screen: pygame.surface.Surface,
              turn: list, COLORS: list) -> None:
    if turn:
        pygame.draw.circle(screen, COLORS[0], (0, 0), 50)
    else:
        pygame.draw.circle(screen, COLORS[1], (0, 0), 50)


def check_illegal_moves_red(red: Player, blue: Player, game: Game) -> None:
    # organize lines for them to start at a lower coordinate
    for line in red.lines:
        if line[0][0] == line[1][0] and line[0][1] > line[1][1]:
            line[0], line[1] = line[1], line[0]
        if line[0][1] == line[1][1] and line[0][0] > line[1][0]:
            line[0], line[1] = line[1], line[0]

    # checking if line is connected on 'home' rows
    p1 = red.lines[-1][0][1] == 675 and red.lines[-1][1][1] == 675
    p2 = red.lines[-1][0][1] == 75 and red.lines[-1][1][1] == 75
    if p1 or p2:
        red.lines.pop(-1)
        game.turn = not game.turn
        return

    # checking if last added red line intersects an enemy line
    vertical = abs(red.lines[-1][0][0] - red.lines[-1][1][0]) == 0
    if vertical:
        for lineBlue in blue.lines:
            p1 = lineBlue[0][0] < red.lines[-1][0][0]
            p2 = lineBlue[1][0] > red.lines[-1][0][0]
            p3 = red.lines[-1][0][1] < lineBlue[0][1]
            p4 = red.lines[-1][1][1] > lineBlue[0][1]
            if p1 and p2 and p3 and p4:
                red.lines.pop(-1)
                game.turn = not game.turn
                return
    else:
        for lineBlue in blue.lines:
            p1 = lineBlue[0][1] < red.lines[-1][0][1]
            p2 = lineBlue[1][1] > red.lines[-1][0][1]
            p3 = red.lines[-1][0][0] < lineBlue[0][0]
            p4 = red.lines[-1][1][0] > lineBlue[0][0]
            if p1 and p2 and p3 and p4:
                red.lines.pop(-1)
                game.turn = not game.turn
                return

    # eliminating repeating lines
    for i in range(len(red.lines)-1):
        for j in range(i+1, len(red.lines)):
            if red.lines[i] == red.lines[j]:
                red.lines.pop(j)
                game.turn = not game.turn
                return


def check_illegal_moves_blue(red: Player, blue: Player, game: Game) -> None:
    # organize lines for them to start at a lower coordinate
    for line in blue.lines:
        if line[0][0] == line[1][0] and line[0][1] > line[1][1]:
            line[0], line[1] = line[1], line[0]
        if line[0][1] == line[1][1] and line[0][0] > line[1][0]:
            line[0], line[1] = line[1], line[0]

    # checking if line is connected on 'home' rows
    p1 = blue.lines[-1][0][0] == 675 and blue.lines[-1][1][0] == 675
    p2 = blue.lines[-1][0][0] == 75 and blue.lines[-1][1][0] == 75
    if p1 or p2:
        blue.lines.pop(-1)
        game.turn = not game.turn
        return

    # checking if last added blue line intersects an enemy line
    vertical = abs(blue.lines[-1][0][0] - blue.lines[-1][1][0]) == 0
    if vertical:
        for lineRed in red.lines:
            p1 = lineRed[0][0] < blue.lines[-1][0][0]
            p2 = lineRed[1][0] > blue.lines[-1][0][0]
            p3 = blue.lines[-1][0][1] < lineRed[0][1]
            p4 = blue.lines[-1][1][1] > lineRed[0][1]
            if p1 and p2 and p3 and p4:
                blue.lines.pop(-1)
                game.turn = not game.turn
                return
    else:
        for lineRed in red.lines:
            p1 = lineRed[0][1] < blue.lines[-1][0][1]
            p2 = lineRed[1][1] > blue.lines[-1][0][1]
            p3 = blue.lines[-1][0][0] < lineRed[0][0]
            p4 = blue.lines[-1][1][0] > lineRed[0][0]
            if p1 and p2 and p3 and p4:
                blue.lines.pop(-1)
                game.turn = not game.turn
                return

    # eliminating repeating lines
    for i in range(len(blue.lines)-1):
        for j in range(i+1, len(blue.lines)):
            if blue.lines[i] == blue.lines[j]:
                blue.lines.pop(j)
                game.turn = not game.turn
                return


def sort_lines(lines: list) -> None:
    for line in lines:
        if line[0][0] == line[1][0] and line[0][1] > line[1][1]:
            line[0], line[1] = line[1], line[0]
        if line[0][1] == line[1][1] and line[0][0] > line[1][0]:
            line[0], line[1] = line[1], line[0]
