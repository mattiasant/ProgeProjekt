import random
import pygame
import setup
import pyautogui


pygame.init()

def väldi():
    pygame.init()

    if setup.var1.get()==1:
        WIDTH = pyautogui.size()[0]
        HEIGHT = pyautogui.size()[1]
        window = pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)

    else:
        WIDTH=800
        HEIGHT=600
        window = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Dodge this!")
    this_font = pygame.font.SysFont("Comic Sans", 20)
    maintitle = this_font.render("Liigu vasakule ja paremale, et vältida klotse", True, "black")
    title_loc = maintitle.get_rect(center=(250, 50))

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    #obstacle colours
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    Obstacle_colours = RED

    player_width = 40
    player_height = 100
    player_x = WIDTH // 2 - player_width // 2
    player_y = HEIGHT - player_height - 10
    player_speed = 7

    obstacle_width = 60
    obstacle_height = 60
    obstacle_speed = 7

    # Create the player rectangle
    player = pygame.Rect(player_x, player_y, player_width, player_height)

    obstacles = []
    def create_obstacle():
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        obstacle_y = -obstacle_height
        obstacle = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
        obstacles.append(obstacle)
    def move_obstacles():
        for obstacle in obstacles:
            obstacle.y += obstacle_speed
            if obstacle.y > HEIGHT:
                obstacles.remove(obstacle)
    def check_collision():
        for obstacle in obstacles:
            if player.colliderect(obstacle):
                return True
        return False
    def game_loop():
        running = True

        clock = pygame.time.Clock()
        success = 0

        start_time = pygame.time.get_ticks()
        while running:
            print(player.x,player.y)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            #Player movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.x > 0:
                player.x -= player_speed
            if keys[pygame.K_RIGHT] and player.x < WIDTH - player_width:
                player.x += player_speed
            if random.random() < 0.05:
                create_obstacle()
            move_obstacles()
            if check_collision():
                running = False
            window.fill(WHITE)
            window.blit(maintitle, title_loc)
            # Draw the player
            pygame.draw.rect(window, BLACK, player)

            # Draw the obstacles
            for obstacle in obstacles:
                pygame.draw.rect(window, RED, obstacle)

            current_time = pygame.time.get_ticks()
            if current_time - start_time >= 12000:
                success += 1
                running = False

            pygame.display.update()
            clock.tick(60)
        #pygame.quit()
        return success

    if game_loop() == 1:
        return "Success"
    else:
        return "Fail"
