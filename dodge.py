import random
import pygame as pigame

pigame.init()
window_width = 1500
window_height = 600
window = pigame.display.set_mode((window_width, window_height))
pigame.display.set_caption("Dodge this!")
this_font = pigame.font.SysFont("Comic Sans", 20)
maintitle = this_font.render("Liigu vasakule ja paremale, et vältida klotse", True, "black")
title_loc = maintitle.get_rect(center=(250, 50))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#obstacle colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
Obstacle_colours = [RED, GREEN, YELLOW, BLUE]

player_width = 40
player_height = 100
player_x = window_width // 2 - player_width // 2
player_y = window_height - player_height - 10
player_speed = 7

obstacle_width = 60
obstacle_height = 60
obstacle_speed = 6

# Create the player rectangle
player = pigame.Rect(player_x, player_y, player_width, player_height)

obstacles = []
def väldi():
    pigame.init()
    window_width = 1500
    window_height = 600
    window = pigame.display.set_mode((window_width, window_height))
    pigame.display.set_caption("Dodge this!")
    this_font = pigame.font.SysFont("Comic Sans", 20)
    maintitle = this_font.render("Liigu vasakule ja paremale, et vältida klotse", True, "black")
    title_loc = maintitle.get_rect(center=(250, 50))

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    #obstacle colours
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    BLUE = (0, 0, 255)
    Obstacle_colours = [RED, GREEN, YELLOW, BLUE]

    player_width = 40
    player_height = 100
    player_x = window_width // 2 - player_width // 2
    player_y = window_height - player_height - 10
    player_speed = 7

    obstacle_width = 60
    obstacle_height = 60
    obstacle_speed = 6

    # Create the player rectangle
    player = pigame.Rect(player_x, player_y, player_width, player_height)

    obstacles = []
    def create_obstacle():
        obstacle_x = random.randint(0, window_width - obstacle_width)
        obstacle_y = -obstacle_height
        obstacle = pigame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
        obstacles.append(obstacle)
    def move_obstacles():
        for obstacle in obstacles:
            obstacle.y += obstacle_speed
            if obstacle.y > window_height:
                obstacles.remove(obstacle)
    def check_collision():
        for obstacle in obstacles:
            if player.colliderect(obstacle):
                return True
        return False
    def game_loop():
        running = True
        clock = pigame.time.Clock()
        success = 0

        start_time = pigame.time.get_ticks()
        while running:
            for event in pigame.event.get():
                if event.type == pigame.QUIT:
                    running = False
            #Player movement
            keys = pigame.key.get_pressed()
            if keys[pigame.K_LEFT] and player.x > 0:
                player.x -= player_speed
            if keys[pigame.K_RIGHT] and player.x < window_width - player_width:
                player.x += player_speed
            if random.random() < 0.05:
                create_obstacle()
            move_obstacles()
            if check_collision():
                running = False
            window.fill(WHITE)
            window.blit(maintitle, title_loc)
            # Draw the player
            pigame.draw.rect(window, BLACK, player)

            # Draw the obstacles
            for obstacle in obstacles:
                pigame.draw.rect(window, random.choice(Obstacle_colours), obstacle)

            current_time = pigame.time.get_ticks()
            if current_time - start_time >= 12000:
                success += 1
                running = False

            pigame.display.update()
            clock.tick(60)
        #pigame.quit()
        return success

    if game_loop() == 1:
        return "Success"
    else:
        return "Fail"
