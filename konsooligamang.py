import random
import sys
import time

import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 16
FONT_NAME = 'SpaceMono-Regular.ttf'
TERMINAL_ROWS = HEIGHT // FONT_SIZE
TERMINAL_COLS = WIDTH // (FONT_SIZE // 2)
TERMINAL_MARGIN = 16
CURSOR_BLINK_INTERVAL = 0.5  # Cursor blink interval in seconds
CURSOR_WIDTH = 2  # Width of the cursor block

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Unix-like Terminal Emulator")

# Define a font
font = pygame.font.Font(FONT_NAME, FONT_SIZE)

# Terminal content
terminal_lines = []

# Cursor variables
cursor_visible = True
cursor_last_toggle = time.time()

# Intro cycle
introjooks = True
intro_lines = []
intro_lines.append("Ärkate keset kõrbe, kuuma päikese all.")
intro_lines.append("Te ei tea kus te täpselt olete, aga hakkate rändama, et leida vastuseid.")
intro_lines.append("Olete rändur oma paremates aastates, avastamas metsikut Läänt, aastal 1899.")
intro_lines.append("Valige raskusaste: kerge/mõõdukas/AAR")

# Narratorcycle
narrator_lines = []
narrator_lines.append('Näed põõsast, mille sees on kahtlane olend')
narrator_lines.append('Uurisid lendavad kotkast taevas ja selletõttu kõndisid otsa kaktusele ja said haiget.')
narrator_lines.append('Karavan sõitis teist mõõda ja sealt hüppas välja el bandito kellel oli pew pew ja ta tahab sind siit ilmast pagendada')
kysievent = False
kysieventolukord = False
olukord0 = False
olukord1 = False
olukord2 = False

# Main loop
running = True
input_lines = []  # Store individual input lines
input_text = ""
difficulty = "default"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                input_lines.append(input_text)

                if difficulty == 'default':
                    if input_text == 'kerge':
                        difficulty = 'kerge'
                    elif input_text == 'mõõdukas':
                        difficulty = 'mõõdukas'
                    elif input_text == 'AAR':
                        difficulty = 'põrgu'
                    if difficulty != 'default':
                        kysievent = True
                        kysieventolukord = True

                if input_text == 'exit' or input_text == 'logout':
                    running = False
                input_text = ""
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)
    y = TERMINAL_MARGIN
    # INTRO
    if introjooks:
        for line in intro_lines:
            user_surface = font.render('C:\\Users\Alexa>', True, TEXT_COLOR)
            screen.blit(user_surface, (TERMINAL_MARGIN, y))

            words = line.split()
            wrapped_lines = []
            wrapped_line = ""

            for word in words:
                test_line = wrapped_line + word + " "
                if font.size(test_line)[0] < WIDTH - TERMINAL_MARGIN * 2 - 160:
                    wrapped_line = test_line
                else:
                    wrapped_lines.append(wrapped_line)
                    wrapped_line = word + " "
            wrapped_lines.append(wrapped_line)

            for wrapped_line in wrapped_lines:
                intro_surface = font.render(wrapped_line, True, TEXT_COLOR)
                screen.blit(intro_surface, (TERMINAL_MARGIN + 160, y))
                y += FONT_SIZE + 5
    # Combine terminal content and current input lines
    all_lines = terminal_lines + input_lines

    # Display terminal content
    user_surface = font.render('C:\\Users\Glean>', True, TEXT_COLOR)
    screen.blit(user_surface, (16, HEIGHT - 16 - FONT_SIZE))

    for line in (all_lines):
        user_surface = font.render('C:\\Users\Glean>', True, TEXT_COLOR)
        screen.blit(user_surface, (TERMINAL_MARGIN, y))

        text_surface = font.render(line, True, TEXT_COLOR)
        screen.blit(text_surface, (TERMINAL_MARGIN + 160, y))
        y += FONT_SIZE + 5

    # Narrator #TODO fix narrator_lines[x] displaying below already entered input

    if kysievent:
        olukord_surface = font.render('C:\\Users\Alexa>', True, TEXT_COLOR)
        screen.blit(olukord_surface, (TERMINAL_MARGIN, y))

        if kysieventolukord:
            olukord = random.randint(0, len(narrator_lines) - 1)
            if olukord == 0:
                olukord0 = True
                kysieventolukord = False
            elif olukord == 1:
                olukord1 = True
                kysieventolukord = False
            elif olukord == 2:
                olukord2 = True
                kysieventolukord = False

    if olukord0:
        olukord_surface = font.render(narrator_lines[0], True, TEXT_COLOR)
        screen.blit(olukord_surface, (TERMINAL_MARGIN + 160, y))
        y += FONT_SIZE + 5
    elif olukord1:

        words = narrator_lines[1].split()
        wrapped_lines = []
        wrapped_line = ""

        for word in words:
            test_line = wrapped_line + word + " "
            if font.size(test_line)[0] < WIDTH - TERMINAL_MARGIN * 2 - 160:
                wrapped_line = test_line
            else:
                wrapped_lines.append(wrapped_line)
                wrapped_line = word + " "
        wrapped_lines.append(wrapped_line)

        for wrapped_line in wrapped_lines:
            intro_surface = font.render(wrapped_line, True, TEXT_COLOR)
            screen.blit(intro_surface, (TERMINAL_MARGIN + 160, y))
            y += FONT_SIZE + 5

    elif olukord2:
        words = narrator_lines[2].split()
        wrapped_lines = []
        wrapped_line = ""

        for word in words:
            test_line = wrapped_line + word + " "
            if font.size(test_line)[0] < WIDTH - TERMINAL_MARGIN * 2 - 160:
                wrapped_line = test_line
            else:
                wrapped_lines.append(wrapped_line)
                wrapped_line = word + " "
        wrapped_lines.append(wrapped_line)

        for wrapped_line in wrapped_lines:
            intro_surface = font.render(wrapped_line, True, TEXT_COLOR)
            screen.blit(intro_surface, (TERMINAL_MARGIN + 160, y))
            y += FONT_SIZE + 5

    # Display the current input text
    input_surface = font.render(input_text, True, TEXT_COLOR)
    screen.blit(input_surface, (TERMINAL_MARGIN + 160, HEIGHT - TERMINAL_MARGIN - FONT_SIZE))

    # Cursor blink
    if time.time() - cursor_last_toggle >= CURSOR_BLINK_INTERVAL:
        cursor_visible = not cursor_visible
        cursor_last_toggle = time.time()

    if cursor_visible:
        cursor_x = TERMINAL_MARGIN + 160 + font.size(input_text)[0]
        cursor_y = HEIGHT - TERMINAL_MARGIN - FONT_SIZE + FONT_SIZE / 3.5
        cursor_rect = pygame.Rect(cursor_x, cursor_y, CURSOR_WIDTH, FONT_SIZE)
        pygame.draw.rect(screen, TEXT_COLOR, cursor_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
