import pygame
import random
import setup
import pyautogui

def aimlab():
    pygame.init()

    if setup.var1.get()==1:
        WIDTH = pyautogui.size()[0]
        HEIGHT = pyautogui.size()[1]
        screen = pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)

    else:
        WIDTH=800
        HEIGHT=600
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

    FPS = 60
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)

    pygame.display.set_caption("Aimlab")
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("Comic Sans", 28)

    score = 0
    game_time = 10
    clicked = False

    def draw_text(text, font, color, x, y, align="left"):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)

        if align == "left":
            text_rect.topleft = (x, y)
        elif align == "right":
            text_rect.topright = (x, y)

        screen.blit(text_surface, text_rect)


    def spawn_square():
        square_size = 40
        x = random.randint(0, WIDTH - square_size)
        y = random.randint(0, HEIGHT - square_size)
        return pygame.Rect(x, y, square_size, square_size)

    # Start game loop
    start_time = pygame.time.get_ticks()
    squares = []
    running = True

    while running:
        screen.fill(BLACK)

        # timer calculation
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) // 1000
        time_left = game_time - elapsed_time

        if time_left <= 0:
            running = False

        # timer
        draw_text(f"Aeg: {time_left}", font, WHITE, 10, 10, align="left")

        if not squares or clicked:
            squares.append(spawn_square())
            clicked = False

        # Draw/update squares
        for square in squares[:]:
            pygame.draw.rect(screen, YELLOW , square)
            if time_left > 0:
                mouse_pos = pygame.mouse.get_pos()
            if square.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    squares.remove(square)
                    clicked = True
                    score += 1

        # score
        draw_text(f"Skoor: {score}", font, WHITE, WIDTH - 50, 10, align="right")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(FPS)

    if score <= 8:
        return "Fail"
    elif score >= 8:
        return "Success"
    pygame.quit()
