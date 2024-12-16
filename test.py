import gui

import pygame

pygame.init()

win = pygame.display.set_mode((800, 600))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gui.draw_text(win, "X hello X", gui.GUIAlignment(0, 0, gui.GUIAlignmentType.CENTER_X | gui.GUIAlignmentType.CENTER_Y), "FSEX300.ttf", 24)

    pygame.display.flip()
