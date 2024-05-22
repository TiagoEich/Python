# Faça um programa que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load("Song.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass
pygame.quit()

""" from playsound import playsound
playsound("song.mp3") """