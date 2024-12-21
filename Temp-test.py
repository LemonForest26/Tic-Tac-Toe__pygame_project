import pygame as pg
import sys
import time

# Initialize pygame
pg.init()

# Set up display
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Tic Tac Toe")
screen.fill(WHITE)

# Load images
X_IMG = pg.image.load("x_mark.png")
O_IMG = pg.image.load("o_mark.png")
X_IMG = pg.transform.scale(X_IMG, (150, 150))
O_IMG = pg.transform.scale(O_IMG, (150, 150))

# Board state
board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]


def draw_lines():
    # Horizontal lines
    for row in range(1, BOARD_ROWS):
        pg.draw.line(screen, BLACK, (0, row * HEIGHT // BOARD_ROWS), (WIDTH, row * HEIGHT // BOARD_ROWS), LINE_WIDTH)

    # Vertical lines
    for col in range(1, BOARD_COLS):
        pg.draw.line(screen, BLACK, (col * WIDTH // BOARD_COLS, 0), (col * WIDTH // BOARD_COLS, HEIGHT), LINE_WIDTH)


def draw_status(message):
    font = pg.font.Font(None, 50)
    text = font.render(message, True, RED)
    screen.fill(WHITE, (0, HEIGHT, WIDTH, 100))  # Clear the status bar
    screen.blit(text, (WIDTH // 3, HEIGHT - 50))
    pg.display.update()


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "X":
                screen.blit(X_IMG, (col * WIDTH // BOARD_COLS + 25, row * HEIGHT // BOARD_ROWS + 25))
            elif board[row][col] == "O":
                screen.blit(O_IMG, (col * WIDTH // BOARD_COLS + 25, row * HEIGHT // BOARD_ROWS + 25))


def reset_game():
    global board
    board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]
    screen.fill(WHITE)
    draw_lines()
    pg.display.update()


def check_win():
    # Check rows and columns
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]

    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def check_draw():
    for row in board:
        if None in row:
            return False
    return True


def main():
    draw_lines()
    pg.display.update()
    running = True
    player = "X"

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                clicked_row = mouse_y // (HEIGHT // BOARD_ROWS)
                clicked_col = mouse_x // (WIDTH // BOARD_COLS)

                # Place player's mark
                if board[clicked_row][clicked_col] is None:
                    board[clicked_row][clicked_col] = player
                    if player == "X":
                        player = "O"
                    else:
                        player = "X"

                draw_figures()

                # Check win
                winner = check_win()
                if winner:
                    draw_status(f"{winner} wins!")
                    time.sleep(2)
                    reset_game()
                    player = "X"

                # Check draw
                elif check_draw():
                    draw_status("It's a draw!")
                    time.sleep(2)
                    reset_game()
                    player = "X"

        pg.display.update()


if __name__ == "__main__":
    main()
