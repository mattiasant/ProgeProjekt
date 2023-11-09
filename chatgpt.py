import pygame
import sys
import time

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

# Main loop
running = True
input_lines = []  # Store individual input lines
input_text = "C:\\Users\Greal>  "
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                input_lines.append(input_text)
                if input_text=='C:\\Users\Greal>  exit' or input_text=='C:\\Users\Greal>  logout':
                    running = False
                input_text = "C:\\Users\Greal>  "
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Combine terminal content and current input lines
    all_lines = terminal_lines + input_lines

    # Display terminal content
    y = TERMINAL_MARGIN
    for line in reversed(all_lines):
        text_surface = font.render(line, True, TEXT_COLOR)
        screen.blit(text_surface, (TERMINAL_MARGIN, y))
        y += FONT_SIZE

    # Display the current input text
    input_surface = font.render(input_text, True, TEXT_COLOR)
    screen.blit(input_surface, (TERMINAL_MARGIN, HEIGHT - TERMINAL_MARGIN - FONT_SIZE))

    # Cursor blink
    if time.time() - cursor_last_toggle >= CURSOR_BLINK_INTERVAL:
        cursor_visible = not cursor_visible
        cursor_last_toggle = time.time()

    if cursor_visible:
        cursor_x = TERMINAL_MARGIN + font.size(input_text)[0]
        cursor_y = HEIGHT - TERMINAL_MARGIN - FONT_SIZE + FONT_SIZE/3.5
        cursor_rect = pygame.Rect(cursor_x, cursor_y, CURSOR_WIDTH, FONT_SIZE)
        pygame.draw.rect(screen, TEXT_COLOR, cursor_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
