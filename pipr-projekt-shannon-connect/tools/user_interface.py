from tools.classes import UI_Button, Game
import pygame


def draw_start_screen_background(screen: pygame.surface.Surface) -> None:
    # drawing start screen background
    screen.blit(pygame.image.load('graphics/start_screen.jpg'), (0, 0))
    screen.blit(pygame.image.load('graphics/start_text.png'), (0, 0))


def create_ui_buttons(screen: pygame.surface.Surface,
                      buttonsUI: license, COLORS: list) -> None:
    # creating buttons for start screen
    buttonAbscissa = [225, 420, 570]
    for x in buttonAbscissa:
        button = UI_Button(screen, COLORS[1], (x, 535), 32)
        buttonsUI.append(button)
    button = UI_Button(screen, COLORS[1], (712, 35), 15)
    buttonsUI.append(button)


def instructions(screen: pygame.surface.Surface,
                 buttonsUI: list, game: Game) -> None:
    # drawing background
    screen.blit(pygame.image.load('graphics/start_screen.jpg'), (0, 0))

    # drawing button
    buttonsUI[-1].draw_ui(game)
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render('<', True, game.COLORS[0])
    textRect = text.get_rect(center=(711, 33))
    screen.blit(text, textRect)

    # drawing instructions
    screen.blit(pygame.image.load('graphics/instructions.png'), (75, 180))
    if not game.info:
        draw_start_screen_background(screen)


def start_screen(screen: pygame.surface.Surface,
                 game: Game, buttonsUI: list) -> None:
    # drawing and initializing buttons
    buttonAbscissa = [225, 420, 570]
    for i, x in enumerate(buttonAbscissa):
        pygame.draw.circle(screen, game.COLORS[0], (x, 535), 34)
        buttonsUI[i].draw_ui(game)
    buttonsUI[-1].draw_ui(game)

    # drawing instructions button
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render('?', True, game.COLORS[0])
    textRect = text.get_rect(center=(711, 36))
    screen.blit(text, textRect)

    # drawing background for the board
    if game.run[0]:
        background = pygame.image.load('graphics/board.jpg')
        screen.blit(background, (0, 0))
        for x in range(135, 616, 120):
            for y in range(75, 676, 600):
                pygame.draw.circle(screen, 'Black', (x, y), 18)
        for y in range(135, 616, 120):
            for x in range(75, 676, 600):
                pygame.draw.circle(screen, 'Black', (x, y), 18)


def end_screen(screen: pygame.surface.Surface, game: Game) -> None:
    # drawing result message
    if game.run[1] and game.end[1]:
        screen.blit(pygame.image.load('graphics/you_win.png'), (200, 303))
    elif game.run[1]:
        screen.blit(pygame.image.load('graphics/you_lost.png'), (200, 303))
    elif game.end[1]:
        screen.blit(pygame.image.load('graphics/white_wins.png'), (200, 303))
    else:
        screen.blit(pygame.image.load('graphics/red_wins.png'), (200, 303))
