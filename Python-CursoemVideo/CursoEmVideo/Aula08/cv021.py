import pygame
pygame.mixer.init()
pygame.mixer.music.load('CursoEmVideo\Aula08\musica.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
