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
    lasud = 0
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
print("Te ei tea kus te täpselt olete, aga hakkate rändama, et leida vastuseid.")
time.sleep(4)
print("Te olete rändur oma paremates aastates, kes on avastamas metsikut Läänt Ameerikas, aastal 1899.")
time.sleep(5)
if relv == "revolver":
    print("Teil on ka revolver, millel on", lasud, "lask(u).")
else:
    print("Teil puudub relv.")
time.sleep(4)
print("Eesmärk: Jää ellu.")
print()
time.sleep(3)

wave = 0
score = 0
while elud > 0:
    print("Kõndisid kõrbes ja ", end="")
    olukord = random.randint(1, 10)
    if olukord == 1 or olukord == 3 or olukord == 5 or olukord == 10:
        print("näed põõsast, mille sees on kahtlane olend.....")
        time.sleep(3)
        print()
        if random.randint(1, 2) == 1:
            if lasud == 0 and valik == "põrgu":
                print("Välja hüppas kobra, kes hammustas teid nii, et saite haiget.")
                elud -= 1
                wave += 1
                score += 1
                print()
                time.sleep(3)
            else:
                lasud1 = int(random.randint(1, 2))
                if lasud - lasud1 < 0:
                    lasud1 = 1
                if lasud == 0:
                    lasud1 = 0
                print(
                    "Välja hüppas kobra, kes hammustas teid nii, et pillasite maha revolvri ja revolvrist kukkus välja " + str(
                        lasud1) + " kuul(i).")
                elud -= 1
                wave += 1
                score += 1
                print()
                time.sleep(3)
                if lasud > 0:
                    lasud -= lasud1
        else:
            print("Pistad pea põõsa sisse ja ei näinud midagi huvitavat, võib-olla kuumusega näete luulusi.")
            print()
            time.sleep(3)
            score += 1
            wave += 1
    elif olukord == 2 or olukord == 7 or olukord == 8:
        print("uurisid lendavad kotkast taevas ja selletõttu kõndisid kaktusele otsa ja said haiget.")
        elud -= 1
        wave += 1
        score += 1
        print()
        time.sleep(3)
    elif olukord == 4 or olukord == 6:
        print("Karavan sõitis teist mõõda ja sealt hüppas välja el bandito")
        print()
        time.sleep(3)
        if lasud > 0:
            print("lasite el banditot ja tapsite ta ära")
            lasud -= 1
            wave += 1
            score += 3
        else:
            print("el bantido peksis teid läbi")
            wave += 1
            elud -= 2
            score += 1
            time.sleep(2)
    elif olukord == 9:
        if valik == "kerge" or valik == "mõõdukas":
            print("karavan sõitis teist mõõda ja sealt kukkus maha seljakott")
            print()
            time.sleep(2)
            print('Seljakotis leidsite kuule')
            lasud2 = random.randint(1, 2)
            lasud += lasud2
            wave += 1
            score += 2
        else:
            print("karavan sõitis teist mõõda ja sealt kukkus maha seljakott")
            print()
            time.sleep(2)
            print('Seljakotis leidsite toitu')
            wave += 1
            score += 3
            elud += 1

    print("Nüüd on teil " + str(elud) + " elu, " + str(lasud) + " lask(u) ja olete ellu jäänud " + str(
        wave) + " round(i).")
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
print("Mängu skoor on " + str(score) + ".")