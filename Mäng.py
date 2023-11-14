import time
import random
import pygame
import sys
import os

### reaktsioonikiiruse mini-game
def gunslinger():
    pygame.init()
    screen = pygame.display.set_mode((720, 720))
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
                    pygame.quit()
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


while True:
    valik = str(input("Mis raskustaset soovite? (tavaline/põrgu) ")).lower()
    if valik == "tavaline":
        lasud = random.randint(2, 6)
        relv = "revolver"
        elud = 5
        break
    if valik == "põrgu":
        lasud = random.randint(1, 3)
        elud = 1
        break
    else:
        print("Palun vali endale raskustase!")
        continue


time.sleep(1)  ### Siin on lihtsalt intro
print("Teil on", elud, "elu")
time.sleep(2)
print("Te ärkate keset kõrbe, kuuma päikese all.")
time.sleep(3)
print("Te ei tea kus te täpselt olete, aga hakkate rändama, et leida vastuseid.")
time.sleep(4)
print("Te olete rändur oma paremates aastates, kes on avastamas metsikut Läänt Ameerikas, aastal 1899.")
time.sleep(5)
print("Teil on ka revolver, millel on", lasud, "lask(u).")

time.sleep(4)
print("Eesmärk: Jää ellu.")
print()
time.sleep(3)


### Mängu põhi loogika  on siin
wave = 0
while elud > 0:
    print("Kõndisid kõrbes ja ", end="")
    olukord = random.randint(1, 10)
    if olukord == 1 or olukord == 3 or olukord == 5 or olukord == 10:
        print("näed põõsast, mille sees on kahtlane olend.....")
        time.sleep(3)
        print()
        if random.randint(1, 2) == 1:
            if lasud == 0 and valik == "põrgu":
                print("Välja hüppas kobra, kes hammustas teid nii, et kaotasite 1 elu.")
                elud -= 1
                wave += 1
                print()
                time.sleep(3)
            else:
                lasud1 = int(random.randint(1, 2))
                if lasud - lasud1 < 0:
                    lasud1 = 1
                if lasud == 0:
                    lasud1 = 0
                print(
                    "Välja hüppas kobra, kes hammustas teid nii, et kaotasite 1 elu ning pillasite maha revolvri ja revolvrist kukkus välja " + str(
                        lasud1) + " kuul(i).")
                elud -= 1
                wave += 1
                print()
                time.sleep(3)
                if lasud > 0:
                    lasud -= lasud1
        else:
            print("Pistad pea põõsa sisse ja ei näinud midagi huvitavat, võib-olla kuumusega näete luulusi.")
            print()
            time.sleep(3)
            wave += 1
    elif olukord == 2:
        print("uurisid lendavad kotkast taevas ja selletõttu kõndisid kaktusele otsa ja kaotasid 1 elu.")
        elud -= 1
        wave += 1
        print()
        time.sleep(3)
    elif olukord == 4 or olukord == 6 or olukord == 7 or olukord == 8:
        print("Karavan sõitis teist mõõda ja sealt hüppas välja El Bandito")
        print()
        time.sleep(3)
        aeg = gunslinger()
        print()
        if aeg <= 500 and lasud > 0:
            print("lasite El Banditot ja tapsite ta ära")
            lasud -= 1
            wave += 1
        elif lasud == 0:
            wave += 1
            elud -= 2
            print("El Bantido peksis teid läbi, kuna teil polnud relval kuule ja kaotasite 2 elu")
        else:
            print("El Bantido peksis teid läbi, kuna te olite liiga aeglane revolvriga ja kaotasite 2 elu")
            wave += 1
            elud -= 2
        time.sleep(2)
    elif olukord == 9 or olukord == 2:
        if valik == "tavaline":
            print("Karavan sõitis teist mõõda ja sealt kukkus maha seljakott")
            print()
            time.sleep(2)
            print('Seljakotis leidsite kuule')
            lasud2 = random.randint(2, 3)
            lasud += lasud2
            wave += 1
        else:
            print("Karavan sõitis teist mõõda ja sealt kukkus maha seljakott")
            print()
            time.sleep(2)
            print('Seljakotis leidsite toitu, mis annab teile 1 elu juurde')
            wave += 1
            elud += 1

    print("Nüüd on teil " + str(elud) + " elu, " + str(lasud) + " lask(u) ja olete ellu jäänud " + str(
        wave) + " round(i)")
    input("Jätkamiseks vajutage Enter-klahvi.")
    print()
    time.sleep(1)
print("""
   _____
  / ____|
 | |  __  __ _ _ __ ___   ___    _____   _____ _ __
 | | |_ |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | (_) \ V /  __/ |
  \_____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|
""")
print("Te saite surma, sest teie elud said otsa.")
print("Jäite ellu " + str(wave) + " roundi.")