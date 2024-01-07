import pygame
import math


class Game():
    def __init__(self) -> None:
        """
        Class Game. Contains attributes:
        :param turn: which player's turn is it
        :type turn: bool

        :param run: game run settings
        :type run: list

        :param end: game result
        :type end: list

        :param lineInit: is line(button) initialized, button's coordinates
        :type lineInit: list

        :param lineCon: is line(button) connected, button's coordinates
        :type lineCon: list

        :param COLRS: game's color palette
        :type COLORS: list

        :param info: get instruction for the game
        :type info: bool
        """
        self.turn = True

        # run game?, game type, game lvl
        self.run = [False, False, False]

        # end game?, game winner
        self.end = [False, False]

        self.lineInit = [False, (0, 0)]
        self.lineCon = [False, (0, 0)]

        # default game colors
        self.COLORS = ['white', 'darkred', 'grey85', (110, 0, 0)]

        self.info = False

    def set_colors(self, color1p: str | tuple, color2p: str | tuple,
                   color1s: str | tuple, color2s: str | tuple) -> None:
        if color1p:
            self.COLORS[0] = color1p
        if color2p:
            self.COLORS[0] = color2p
        if color1s:
            self.COLORS[0] = color1s
        if color2s:
            self.COLORS[0] = color2s


class Button():
    def __init__(self, surface, color, coordinate,
                 radius, COLORS=None) -> None:
        """
        Class Button. Contains attributes:
        :param surface: button's drawing surface
        :type surface: pygame.surface.Surface

        :param color: button's drawing color
        :type color: string | tuple

        :param coordinate: button's drawing coordinate
        :type coordinate: tuple

        :param radius: button's drawing radius
        :type radius: int

        :param rect: rectangle that fits around the button
        :type surface: pygame.rect.Rect

        :param isPressed: is the button being pressed
        :type surface: bool

        :param player: which player does the button belong to
        :type player: bool
        """
        self.surface = surface
        self.color = color
        self.coordinate = coordinate
        self.radius = radius
        self.rect = pygame.Rect(coordinate[0]-radius, coordinate[1]-radius,
                                2*radius, 2*radius)
        self.isPressed = False
        if COLORS:
            self.player = True if self.color == COLORS[0] else False

    def draw(self, game: Game) -> None:
        # drawing the button and checking if it's clicked
        pygame.draw.circle(self.surface, self.color,
                           self.coordinate, self.radius)
        self.on_click(game)

    def on_click(self, game: Game) -> None:
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                # the button is being clicked
                self.isPressed = True

                # button colors to secondary for the time of pressing
                if self.color == game.COLORS[1]:
                    self.color = game.COLORS[3]
                elif self.color == game.COLORS[0]:
                    self.color = game.COLORS[2]

            elif self.isPressed:
                # button was let go by the user
                self.button_was_pressed(game)

    def button_was_pressed(self, game: Game) -> None:
        if not game.lineInit[0] and self.player == game.turn:
            # initializing button - storing coordinate
            game.lineInit[0] = True
            game.lineInit[1] = self.coordinate
            self.rect = pygame.Rect(self.coordinate[0]-self.radius,
                                    self.coordinate[1]-self.radius,
                                    2*self.radius, 2*self.radius)
        elif self.can_line_be_connected(game):
            # connecting buttons - storing coordinate
            game.lineCon[0] = True
            game.lineCon[1] = self.coordinate
        elif game.lineInit[1] == self.coordinate:
            # not connecting buttons but keeping button initialized
            game.lineInit[0] = True
            game.lineInit[1] = self.coordinate
            game.lineCon[0] = False
        else:
            # deactivating button
            game.lineInit[0] = False
            game.lineCon[0] = False
        self.isPressed = False

        # reverting button colors back to primary
        if self.color == game.COLORS[3]:
            self.color = game.COLORS[1]
        else:
            self.color = game.COLORS[0]

    def can_line_be_connected(self, game: Game) -> bool:
        # check if player connects his own dots
        p1 = self.player == game.turn
        # check if player connects two different dots
        p2 = game.lineInit[1] != self.coordinate
        # check if player connects dots that are next to each other
        p3 = math.dist(self.coordinate, game.lineInit[1]) == 120
        return p1 and p2 and p3


class UI_Button(Button):
    def __init__(self, surface, color, coordinate, radius):
        super().__init__(surface, color, coordinate, radius)

    def draw_ui(self, game: Game) -> None:
        # drawing the button and checking if it's clicked
        pygame.draw.circle(self.surface, self.color,
                           self.coordinate, self.radius)
        self.on_click_ui(game)

    def on_click_ui(self, game: Game) -> None:
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                # button is being clicked
                self.isPressed = True
            elif self.isPressed:
                # button was let go by the user
                game.run[0] = True
                if self.coordinate == (712, 35):
                    game.info = not game.info
                    game.run[0] = False
                elif self.coordinate != (225, 535):
                    game.run[1] = True
                    if self.coordinate == (570, 535):
                        game.run[2] = True
                self.isPressed = False


class Player():
    def __init__(self) -> None:
        """
        Class Player. Contains attributes:
        :param buttons: buttons on the players graph
        :type buttons: list

        :param lines: lines on the players graph
        :type lines: list

        :param graph: graph of the player's connected lines
        :type graph: dict
        """
        self.buttons = []
        self.lines = []
        self.graph = {}

    def append_graph(self) -> None:
        # appending the graph with the newest line
        line = self.lines[-1]
        for point in line:
            if point not in self.graph:
                self.graph[point] = []
        for point1 in self.graph:
            for point2 in self.graph:
                p2 = point2 not in self.graph[point1]
                p3 = [point1, point2] in self.lines
                p4 = [point2, point1] in self.lines
                if math.dist(point1, point2) == 120 and p2 and (p3 or p4):
                    self.graph[point1].append(point2)
