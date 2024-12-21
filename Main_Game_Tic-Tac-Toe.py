#Importing necessary modules
import pygame
import sys
import time
import random
from pygame import mixer

pygame.init()
mixer.init()

#Setting up the required global variables
board = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

player = random.choice(["X", "O"])
position = []
clicked = False
game_over = False
win = False
draw = False
running = True
x_score = 0
o_score = 0
draws = 0


#Designing the display function
screen_width = 650
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Tic-Tac-Toe")

def draw_board():
    bg = '#DCD3FF'
    grid_1 = (12, 9, 10)
    grid_2 = (195, 98, 65)
    screen.fill(bg)

    try:
        bg_size = pygame.transform.scale(bg_img, (screen_width, screen_height))
        screen.blit(bg_size, (0, 0))
    except:
        pass

    for i in range(4):
        pygame.draw.line(screen, grid_1, (25, i * 200 + 125), (625, i * 200 + 125), 8)
        pygame.draw.line(screen, grid_1, (i * 200 + 25, 125), (i * 200 + 25, 725), 8)
    for i in range(4):
        pygame.draw.line(screen, grid_2, (25, i * 200 + 125), (625, i * 200 + 125), 2)
        pygame.draw.line(screen, grid_2, (i * 200 + 25, 125), (i * 200 + 25, 725), 2)

try:
    x_img = pygame.image.load(r"x_mark.png")
    x_img = pygame.transform.scale(x_img, (100, 100))

    o_img = pygame.image.load("o_mark.png")
    o_img = pygame.transform.scale(o_img, (100, 100))

    logo_img = pygame.image.load('tic-tac-toe_logo.png')
    bg_img = pygame.image.load('game_bg.jpg')
except Exception as e:
    print("The first one failed to run due to", e, ". The second one will run instead.")
    
    x_img = pygame.image.load(r"D:\Uni\CSE_200\Tic-Tac-Toe__pygame_project\x_mark.png")
    x_img = pygame.transform.scale(x_img, (100, 100))

    o_img = pygame.image.load("D:/Uni/CSE_200/Tic-Tac-Toe__pygame_project/o_mark.png")
    o_img = pygame.transform.scale(o_img, (100, 100))

    logo_img = pygame.image.load('D:/Uni/CSE_200/Tic-Tac-Toe__pygame_project/tic-tac-toe_logo.png')
    bg_img = pygame.image.load('D:/Uni/CSE_200/Tic-Tac-Toe__pygame_project/game_bg.jpg')
pygame.display.set_icon(logo_img)


def text_on_top(text):
    font = pygame.font.Font(None, 50)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(screen_width // 2, 100))
    screen.blit(text_surface, text_rect)

#Keeping track of time
def time_over_left_corner(minutes, remaining_seconds):
    font = pygame.font.Font(None, 25)
    text = f"{minutes:02}:{remaining_seconds:02}"
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(25, 10))
    screen.blit(text_surface, text_rect)


start_ticks = pygame.time.get_ticks()

def timer_count():
    elapsed_ticks = pygame.time.get_ticks() - start_ticks
    seconds = elapsed_ticks // 1000
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return minutes, remaining_seconds

#Updating Game Score
def update_score():
    font = pygame.font.Font(None, 25)
    scoring = [f"X win: {x_score}", f"O win: {o_score}", f"Draw:  {draws}"]
    y_pos = 10
    for score in scoring:
        score_surface = font.render(score, True, (0, 0, 0))
        score_rect = score_surface.get_rect(topright=(630, y_pos))
        screen.blit(score_surface, score_rect)
        y_pos += 25

#Making sound effects
def sound_effect():
    try:
        x_sound = pygame.mixer.Sound("x_sound_effect.mp3")
        o_sound = pygame.mixer.Sound("o_sound_effect.mp3")
        win_sound = pygame.mixer.Sound("winning_sound_effect.mp3")
        draw_sound = pygame.mixer.Sound("draw_sound_effect.wav")
        mixer.music.load("bg_music.mp3")
        
    except Exception as e:
        print("The first one failed to run due to", e, ". The second one will run instead.")
        x_sound = pygame.mixer.Sound("D:/Uni/CSE_200/Tic-Tac-Toe__pygame_project/x_sound_effect.mp3")
        o_sound = pygame.mixer.Sound("D:/Uni/CSE_200/Tic-Tac-Toe__pygame_project/o_sound_effect.mp3")
        win_sound = pygame.mixer.Sound("D:/Uni/CSE_200/Tic-Tac-Toe__pygame_project/winning_sound_effect.mp3")
        draw_sound = pygame.mixer.Sound("D:/Uni/CSE_200/Tic-Tac-Toe__pygame_project/draw_sound_effect.wav")
        mixer.music.load("D:/Uni/CSE_200/Tic-Tac-Toe__pygame_project/bg_music.mp3")
    
    win_sound.set_volume(.3)
    draw_sound.set_volume(.4)
    return x_sound, o_sound, win_sound, draw_sound

#Main algorithm of win and draw
def check_win():
    stripe = '#12AD2B'
    # Horizontal Check
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            y_position = (i * 200) + 225
            pygame.draw.line(screen, stripe, (50, y_position), (600, y_position), 15)
            win_sound.play()
            return True

    # Vertical Check
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            x_position = (i * 200) + 125  
            pygame.draw.line(screen, stripe, (x_position, 150), (x_position, 700), 15)
            win_sound.play()
            return True

    # Diagonal Check (Top-Left to Bottom-Right)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        pygame.draw.line(screen, stripe, (50, 150), (600, 700), 15)
        win_sound.play()
        return True

    # Diagonal Check (Top-Right to Bottom-Left)
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        pygame.draw.line(screen, stripe, (600, 150), (50, 700), 15)
        win_sound.play()
        return True

    return False

def check_draw():
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    draw_sound.play()
    return True

def game_outcome_check():
    global x_score, o_score, draws
    if check_win():
        text_on_top(f"{player} wins!")
        if player == "X":
            x_score += 1
        elif player == "O":
            o_score += 1
        return True
    elif check_draw():
        text_on_top("Draw!")
        draws += 1
        return True

#Getting user input & displaying "X" or "O" on the board
def draw_marks():
    for row in range(3):
        for col in range(3):
            x_center = col * 200 + 125
            y_center = row * 200 + 225
            if board[row][col] == "X":
                # Center the "X" image
                screen.blit(x_img, (x_center - x_img.get_width() // 2, y_center - x_img.get_height() // 2))
            elif board[row][col] == "O":
                # Center the "O" image
                screen.blit(o_img, (x_center - o_img.get_width() // 2, y_center - o_img.get_height() // 2))

#Setting up the game
x_sound, o_sound, win_sound, draw_sound = sound_effect()
mixer.music.set_volume(0.7)
mixer.music.play(-1)

while running:
    draw_board()
    draw_marks()
    update_score()

    minutes, remaining_seconds = timer_count()
    time_over_left_corner(minutes, remaining_seconds)

    game_over = game_outcome_check()
    
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                pos = pygame.mouse.get_pos()
                col = (pos[0] - 25) // 200
                row = (pos[1] - 125) // 200

                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    board[row][col] = player
                    draw_marks()

                    game_over = game_outcome_check()

                    if not game_over:
                        time.sleep(.2)
                        if player == "X":
                            x_sound.play()
                            player = "O"
                        else:
                            player = "X"
                            o_sound.play()
    if not game_over:
        text_on_top(f"Player {player}'s Turn")
                
    if game_over:
        pygame.display.update()
        time.sleep(3)
        board = [[" ", " ", " "],
                 [" ", " ", " "],
                 [" ", " ", " "]]
        player = random.choice(["X", "O"])
        game_over = False
        start_ticks = pygame.time.get_ticks()

    pygame.display.update()
pygame.quit()
sys.exit()