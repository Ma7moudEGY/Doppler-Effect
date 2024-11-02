import pygame
import numpy as np
import sounddevice as sd
from body import Body
from slider import Slider

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
SOUND_SPEED = 343.0
running = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

Source = Body(40, HEIGHT/2 - 10, "red", 10, "Source")
Reciver = Body(WIDTH - 40, HEIGHT/2 - 10, "blue", 0, "Reciver")

vslider = Slider(20, 20, "V", Source.velocity)
hslider = Slider(520, 20, "H", Source.velocity)


def draw_window():
    screen.fill('black')
    Source.draw(screen)
    Reciver.draw(screen)
    vslider.draw(screen)
    hslider.draw(screen)
    pygame.display.update()


def Doppler(source, reciver):
    inital_frequency = 440
    sample_rate = 44100
    duration = 10

    apparent_frequency = inital_frequency * ((SOUND_SPEED + reciver.velocity) / (SOUND_SPEED - source.velocity))

    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    sine_wave = 0.05 * (np.sin(2*np.pi * apparent_frequency * t))

    sd.play(sine_wave, sample_rate)


Doppler(Source, Reciver)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    clock.tick(FPS)

    Source.move()
    Reciver.move()

    draw_window()


pygame.quit()