import pygame

pygame.init()

width = pygame.display.Info().current_w
heigth = pygame.display.Info().current_h

print(width)
print(heigth)

mew = width
meh = heigth

ekraan = pygame.display.set_mode((width, heigth))
pygame.display.set_caption('amogus was not the imposter')

jookseb = True

white = 255, 255, 255
black = 0, 0, 0

xvahe = 0
yvahe = 0

ikoon = pygame.image.load('sus.png')
ikoon = pygame.transform.scale(ikoon, (200, 200))

pildix = width / 2
pildiy = heigth / 2

kiirus = 1


def pilt(pildix, pildiy):
    ekraan.blit(ikoon, (pildix, pildiy))


while jookseb:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jookseb = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                jookseb = False
            if event.key == pygame.K_LEFT:
                xvahe = 0 - kiirus
            if event.key == pygame.K_RIGHT:
                xvahe = kiirus
            if event.key == pygame.K_UP:
                yvahe = 0 - kiirus
            if event.key == pygame.K_DOWN:
                yvahe = kiirus

            if event.key == pygame.K_r:
                pildix = width / 2
                pildiy = heigth / 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xvahe = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                yvahe = 0

    pildix = pildix + xvahe
    pildiy += yvahe

    ekraan.fill(black)
    pilt(pildix, pildiy)
    pygame.display.update()

pygame.quit()
quit()
