import szintek
import szoveg
from jatekos import Jatekos

bejart_helyszinek = [1]
targyak = []
kiadott_parancsok = []
jatekos = Jatekos(5, 0, False)


def jatekmenet():
    szintek.helyszin_0()
    indul = input("| Játékhoz: 'jatek' | Kilépéshez: 'kilep' |\n# ")
    while indul != "jatek" or indul != "kilep":
        if indul == "jatek":
            if jatekos.eletero <= 1:
                quit("Elfogyott az életerőd... Vesztettél!")

            szintek.helyszin_1()
            bemenet = input("# ")
            kiadott_parancsok.append(bemenet)
            hanyadik = bejart_helyszinek[-1]
            vissza = 0

            while bemenet != "kilep" and jatekos.eletero > 1:
                if kiadott_parancsok[-1] != "vissza":
                    vissza = 0

                if bemenet == "vissza":
                    if hanyadik != 4 and hanyadik != 8:
                        try:
                            vissza += 1
                            hanyadik = bejart_helyszinek[-1 - vissza]
                            helyszin(hanyadik)
                            print(jatekos)
                        except:
                            print("Nem tudsz visszább menni!")
                    else:
                        print("Nem tudsz visszább menni!")

                if bemenet == "segitseg":
                    print("{:^91}".format("Parancsszavak: 'megy' | 'eszik' | 'felvesz' | 'hasznal' | 'eszkoztar' |"
                                          " 'segitseg'"))

                if bemenet == "eszkoztar":
                    kimenet = "Tárgyaid: | "
                    if len(targyak) > 0:
                        for i in range(len(targyak)):
                            kimenet += targyak[i]+" | "
                        print(kimenet)
                    else:
                        print("Üres az eszköztárad.")

                if hanyadik == 1 and bemenet == "megy epulet":
                    hanyadik = szintvaltas(2)

                if hanyadik == 2 and bemenet == "megy kut":
                    hanyadik = szintvaltas(3)

                if hanyadik == 2 and bemenet == "megy kastely":
                    hanyadik = szintvaltas(5)

                if hanyadik == 3 and bemenet == "felvesz penz":
                    targyak.append("pénz")
                    hanyadik = szintvaltas(4)

                if hanyadik == 3 and bemenet == "megy epulet":
                    hanyadik = szintvaltas(5)

                if hanyadik == 4 and bemenet == "megy kastely":
                    hanyadik = szintvaltas(5)

                if hanyadik == 5 and bemenet == "megy vartemplom":
                    hanyadik = szintvaltas(6)

                if hanyadik == 6 and bemenet == "hasznal penz":
                    if "pénz" in targyak:
                        targyak.remove("pénz")
                        hanyadik = szintvaltas(7)

                if hanyadik == 7 and bemenet == "felvesz kulcs":
                    targyak.append("kulcs")
                    hanyadik = szintvaltas(8)

                if hanyadik == 8 and bemenet == "megy varudvar":
                    hanyadik = szintvaltas(5)

                if hanyadik == 5 and bemenet == "megy ajto":
                    hanyadik = szintvaltas(13)

                if hanyadik == 6 and bemenet == "megy kamra":
                    hanyadik = szintvaltas(9)

                if hanyadik == 6 and bemenet == "megy ajto":
                    hanyadik = szintvaltas(13)

                if hanyadik == 13 and bemenet == "hasznal kulcs":
                    if "kulcs" in targyak:
                        szoveg.szoveg_14()
                    else:
                        print("Nincs kulcs nálad!")

                if hanyadik == 5 and bemenet == "megy kamra":
                    hanyadik = szintvaltas(9)

                if hanyadik == 9 and bemenet == "megy faajto":
                    hanyadik = szintvaltas(10)

                if hanyadik == 9 and bemenet == "eszik etel":
                    szoveg.szoveg_12()
                    jatekos.evett = True
                    jatekos.eletero = 10
                    jatekos.evett_korok += 1

                if hanyadik == 10 and bemenet == "hasznal kulcs":
                    if "kulcs" in targyak:
                        szintvaltas(11)
                        quit("Nyertél!")
                    else:
                        print("Nincs kulcs nálad!")

                if hanyadik == 12 and bemenet == "hasznal kulcs":
                    if "kulcs" in targyak:
                        szintvaltas(11)
                        quit("Nyertél!")
                    else:
                        print("Nincs kulcs nálad!")
                bemenet = input("# ")
                kiadott_parancsok.append(bemenet)

                if bemenet == "kilep":
                    quit("Kilépés a játékból...")

        elif indul == "kilep":
            quit("Kilépés a játékból...")

        else:
            indul = input("| Játékhoz: 'jatek' | Kilépéshez: 'kilep' |\n# ")


def szintvaltas(szint):
    jelenlegi_helyszin = szint
    helyszin(jelenlegi_helyszin)
    bejart_helyszinek.append(jelenlegi_helyszin)
    hanyadik = bejart_helyszinek[-1]
    if len(bejart_helyszinek) > 3 and not jatekos.evett:
        jatekos.eletero -= 1
    elif jatekos.evett:
        jatekos.evett_korok += 1
        if jatekos.evett_korok % 3 == 0:
            jatekos.evett = False
            jatekos.evett_korok = 0
    print(jatekos)
    return hanyadik


def helyszin(hanyadik):
    if hanyadik == 1:
        return szintek.helyszin_1()
    if hanyadik == 2:
        return szintek.helyszin_2()
    if hanyadik == 3:
        return szintek.helyszin_3()
    if hanyadik == 4:
        return szintek.helyszin_4()
    if hanyadik == 5:
        return szintek.helyszin_5()
    if hanyadik == 6:
        return szintek.helyszin_6()
    if hanyadik == 7:
        return szintek.helyszin_7()
    if hanyadik == 8:
        return szintek.helyszin_8()
    if hanyadik == 9:
        return szintek.helyszin_9()
    if hanyadik == 10:
        return szintek.helyszin_10()
    if hanyadik == 11:
        return szintek.helyszin_11()
    if hanyadik == 13:
        return szintek.helyszin_13()
