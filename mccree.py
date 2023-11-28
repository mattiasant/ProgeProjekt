import time
import random
import pygame

def gunslinger():
    pygame.init()
    screen = pygame.display.set_mode((1500, 720))
    pygame.display.set_caption("High Noon Time!")
    main_font = pygame.font.SysFont("Comic Sans", 28)
    second_font = pygame.font.SysFont("Roboto", 40)

    title = main_font.render("Reageeri piisavalt kiiresti, et tulistada El Banditot!", True, "white")
    title_rect = title.get_rect(center=(360, 50))
    click_to_start = second_font.render("Vajuta vasakut hiire klõpsu kui valmis", True, "red")
    click_to_start_rect = click_to_start.get_rect(center=(360, 360))
    waiting = second_font.render("Oota...", True, "black")
    waiting_rect = waiting.get_rect(center=(360, 360))
    click = second_font.render("TULISTA!!!", True, "black")
    click_rect = click.get_rect(center=(360, 360))
    score = second_font.render("Speed: 1000 ms", True, "red")
    score_rect = score.get_rect(center=(360, 360))
    score_text_below = main_font.render("Vajuta paremat klõpsu, et jätkata", True, "red")
    score_rect_below = score_text_below.get_rect(center=(360, 400))

    game_state = "Click to Start"
    start_time, end_time = 0, 0
    reaction_time = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_state == "Click to Start":
                    game_state = "Waiting"
                elif game_state == "Test Starting":
                    ending_time = time.time()
                    game_state = "Showing Results"
                elif game_state == "Showing Results":
                    return reaction_time

        screen.fill("black")
        screen.blit(title, title_rect)

        if game_state == "Click to Start":
            screen.blit(click_to_start, click_to_start_rect)
        elif game_state == "Waiting":
            screen.fill("yellow")
            screen.blit(waiting, waiting_rect)
            pygame.display.update()
            delay_time = random.uniform(1, 6)
            time.sleep(delay_time)
            game_state = "Test Starting"
            starting_time = time.time()
        elif game_state == "Test Starting":
            screen.fill("green")
            screen.blit(click, click_rect)
        elif game_state == "Showing Results":
            reaction_time = round((ending_time - starting_time) * 1000)
            score_text = main_font.render(f"Kiirus: {reaction_time} ms", True, "white")
            screen.blit(score_text, score_rect)
            screen.blit(score_text_below, score_rect_below)

        pygame.display.update()

#gunslinger()