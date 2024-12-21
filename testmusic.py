import pygame
pygame.init()
pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)  # Loop indefinitely
while True:
    pass  # Keep the program running to hear the music
