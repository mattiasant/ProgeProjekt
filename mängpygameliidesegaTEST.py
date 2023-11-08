import random
import pygame

pygame.init()

win = pygame.display.set_mode((1250, 750))

pygame.display.set_caption('Wild West')

import time
import random

valik = str(input("Mis raskustaset soovite? (kerge/mõõdukas/põrgu) ")).lower()

if valik == "kerge":
    raskusvalik = "kerge.txt"
    lasud = random.randint(3, 6)
elif valik == "mõõdukas":
    raskusvalik = "mõõdukas.txt"
    lasud = random.randint(1, 3)
elif valik == "põrgu":
    raskusvalik = "põrgu.txt"
else:
    print("Palun vali endale raskustase!")

with open(raskusvalik, encoding="UTF-8") as fail:
    ridanumber = fail.readlines()
    elud = int(ridanumber[0].strip("\n"))
    relv = str(ridanumber[1].strip("\n"))

fail.close()

time.sleep(1)
print("Teil on", elud, "elu")
time.sleep(2)
print("Te ärkate keset kõrbe, kuuma päikese all.")
time.sleep(3)
print("Te ei tea kus te olete, aga hakkata rändama, et leida vastuseid.")
time.sleep(4)
print("Te olete rändur oma paremates aastates, kes on avastamas metsikut Läänt Ameerikas, aastal 1899.")
time.sleep(5)
if relv == "revolver":
    print("Teil on ka revolver, millel on", lasud, "lask(u).")
else:
    print("Teil puudub relv.")
time.sleep(4)
print("Eesmärk: Jää ellu.")

run = True
class button():
    def __init__(self, colour, xa, ya, widtha, heighta, text=''):
        self.color = colour
        self.x = xa
        self.y = ya
        self.width = widtha
        self.height = heighta
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

greenbutton = button((255, 255, 255), 150, 225, 250, 100, 'vaatade ringi')
button2 = button((255, 255, 255), 550, 225, 250, 100, 'teete mitte midagi')


def redrawwindow():
    win.fill((255, 255, 255))
    greenbutton.draw(win, (0, 0, 0))
    button2.draw(win, (0, 0, 0))

x = 150
y = 150
vel = 5
while run:
    redrawwindow()
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if greenbutton.isOver(pos):
                print('paremal näete võimsaid mägesid')
        if event.type == pygame.MOUSEMOTION:
            if greenbutton.isOver(pos):
                greenbutton.colour = (255, 0, 255)
            else:
                greenbutton.colour = (0, 255, 0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button2.isOver(pos):
                print('te olete kasutu')
        if event.type == pygame.MOUSEMOTION:
            if button2.isOver(pos):
                button2.colour = (255, 0, 255)
            else:
                button2.colour = (0, 255, 0)

    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 255, 0), (x, y, 50, 50))