import random
import sys
import time
import pygame
from dodge import väldi
from mccree import gunslinger

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1500, 600
BACKGROUND_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 16
FONT_NAME = 'SpaceMono-Regular.ttf'
TERMINAL_MARGIN = 16

introjooks = True
kysievent = False
olukord = ''
tmain = None

niki = pygame.mixer.Sound('RomanHolidayNickiMinaj.mp3')
kaktus = pygame.mixer.Sound('MarioFall.mp3')
bandito = pygame.mixer.Sound('USAAnthemModified.mp3')

pygame.mixer.Sound.set_volume(niki, 0.4)
pygame.mixer.Sound.set_volume(kaktus, 0.8)
pygame.mixer.Sound.set_volume(bandito, 0.4)

# Terminal properties
TERMINAL_ROWS = HEIGHT // FONT_SIZE
TERMINAL_COLS = WIDTH // (FONT_SIZE // 2)
CURSOR_BLINK_INTERVAL = 0.5  # Cursor blink interval in seconds
CURSOR_WIDTH = 2  # Width of the cursor block

# Create the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Unix-like Terminal Emulator")

# Define a font
font = pygame.font.Font(FONT_NAME, FONT_SIZE)

# Terminal content
terminal_lines = []
event_lines = []
all_lines = []

# Cursor variables
cursor_visible = True
cursor_last_toggle = time.time()

# Intro messages
final_lines = [
    ("Ärkate keset kõrbe, kuuma päikese all.", True),
    ("Te ei tea kus te täpselt olete, aga hakkate rändama, et leida vastuseid.", True),
    ("Olete rändur oma paremates aastates, avastamas metsikut Läänt, aastal 1899.", True),
    ("Valige raskusaste: kerge/mõõdukas/AAR", True)
]

# Narrator messages
narrator_lines = [
    'Näed sahisevat põõsast... paistab, et kaisteväelaste maskeering on alla käinud...',
    'Näed taevas lendavat lindu, või on see hoopis lennuk?',
    'Karavan sõitis teist mõõda ja sealt hüppas välja el bandito kellel oli pew pew ja ta tahab sind siit ilmast pagendada'
]
# Main loop
running = True
input_lines = []  # Store individual input lines
input_text = ""
difficulty = "default"


def ol1():
    global olukord
    if time.time() - t1 >= 5:
        olukord = -1
        väärtus = väldi()
        # print(väärtus)
        if väärtus == 'Success':
            return 'pos'
            # all_lines.append(
            #    "Uurides lendavat kotkast taevas oleksite peaaegu kaktusele otsa kõndinud, aga õnneks teil olid kiired jalad")

        elif väärtus == 'Fail':
            return 'neg'
            # all_lines.append("Uurides lendavat kotkast taevas kõndisite kaktusele otsa ja kaotasite 1 elu.")


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_RETURN:
                final_lines.append((input_text, False))
                y += FONT_SIZE + 5

                # Handle difficulty selection
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
                        y += FONT_SIZE + 5

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

    if kysievent:
        t1 = time.time()
        t0 = time.time()
        t2 = time.time()
        # olukord_surface = font.render('C:\\Users\Alexa>', True, TEXT_COLOR)
        # screen.blit(olukord_surface, (TERMINAL_MARGIN, y))
        olukord = random.randint(0, 2)

    if olukord == 0:
        if kysievent:
            kysievent = False
            final_lines.append((narrator_lines[0], True))
        rand0 = random.randint(1, 2)
        if t0 != None and time.time() - t0 >= 4 and rand0 == 1:
            final_lines.append(('Veider, põõsas ei ole kedagi. Aga ei noh väike skiso käibki asja juurde', True))
            t0 = None
            tmain = time.time()
            olukord = -1
        elif t0 != None and time.time() - t0 >= 4 and rand0 == 2:
            final_lines.append(('Põõsast hüppas välja Nicki Minaj ja viskas ühe anaconda sulle näkku. -1 HP', True))
            pygame.mixer.Sound.play(niki, 0, 0, 0)
            t0 = None
            olukord = -1
            tmain = time.time() + 4

    elif olukord == 1:
        if kysievent:
            final_lines.append((narrator_lines[1], True))
            kysievent = False
        vaartus = ol1()
        print(vaartus)
        if vaartus == 'pos':
            final_lines.append(
                (
                "Uurides lendavat kotkast taevas oleksite peaaegu kaktusele otsa kõndinud, aga õnneks teil olid kiired jalad",
                True))
        elif vaartus == 'neg':
            final_lines.append(("Uurides lendavat kotkast taevas kõndisite kaktusele otsa ja kaotasite 1 elu.", True))
            pygame.mixer.Sound.play(kaktus)
        # y += FONT_SIZE + 5
        tmain = time.time() + 3
        # olukord = -1

    elif olukord == 2:
        if kysievent:
            kysievent = False
            final_lines.append((narrator_lines[2], True))
        if time.time() - t2 >= 5:
            aeg = gunslinger()
            if aeg <= 500:
                final_lines.append(('Lasite el banditot, kes sai surma. -9999999999999999 social credit', True))
                pygame.mixer.Sound.play(bandito, 0, 0, 0)
                tmain = time.time() + 13
            else:
                final_lines.append(
                    ('el bandito peksis teid läbi ja võttis teie limited edition louis vuitton käekoti endaga kaasa.' +
                     ' -1 limited edition louis vuitton käekott, +10 emotional damage', True))
                tmain = time.time()
            olukord = -1

    if olukord == -1 and tmain != None and time.time() - tmain >= 5:
        kysievent = True
        tmain = None

    # Combine terminal content and current input lines
    all_lines = terminal_lines + input_lines + event_lines

    # Display terminal content
    luser_surface = font.render('C:\\Users\Glean>', True, TEXT_COLOR)
    screen.blit(luser_surface, (16, HEIGHT - 16 - FONT_SIZE))

    # Blit terminal content
    for line in final_lines:
        if line[1] == True:
            user_surface = font.render('C:\\Users\Alexa>', True, TEXT_COLOR)
            screen.blit(user_surface, (TERMINAL_MARGIN, y))
        else:
            user_surface = font.render('C:\\Users\Glean>', True, TEXT_COLOR)
            screen.blit(user_surface, (TERMINAL_MARGIN, y))
        text_surface = font.render(line[0], True, TEXT_COLOR)
        screen.blit(text_surface, (TERMINAL_MARGIN + 160, y))
        y += FONT_SIZE + 5

    # Display the current input text
    input_surface = font.render(input_text, True, TEXT_COLOR)
    screen.blit(input_surface, (TERMINAL_MARGIN + 160, HEIGHT - 16 - FONT_SIZE))

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
