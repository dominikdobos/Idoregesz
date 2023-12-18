import kepek
import szoveg


def helyszin_0():
    kepek.idoregesz_ascii()
    disz = "{:─^91}".format("")
    kiiras = "{:^91}".format("Üdv az Időrégész játékban!")
    kiiras2 = "{:^91}".format("Ebben a játékban írásos módon tudsz majd tájékozódni a szintek között,")
    kiiras3 = "{:^91}".format("az elérhető parancsszavak megfelelő kibővítésével.")
    kiiras4 = "{:^91}".format("Parancsszavak: 'megy' | 'eszik' | 'felvesz' | 'hasznal' | 'eszkoztar' | 'segitseg'")
    kiiras5 = "{:^91}".format("Sok sikert!")
    print(disz)
    print(kiiras)
    print(kiiras2)
    print(kiiras3)
    print(kiiras4)
    print(kiiras5)
    print(disz+"\n")


def helyszin_1():
    kepek.mezo_ascii()
    szoveg.szoveg_1()


def helyszin_2():
    kepek.kastely_kut_ascii()
    szoveg.szoveg_2()


def helyszin_3():
    kepek.kut_ascii()
    szoveg.szoveg_3()


def helyszin_4():
    kepek.penz_ascii()
    szoveg.szoveg_4()


def helyszin_5():
    kepek.varudvar_ascii()
    szoveg.szoveg_5()


def helyszin_6():
    kepek.szerzetes_ascii()
    szoveg.szoveg_6()


def helyszin_7():
    kepek.kinyujt_kulcs_ascii()
    szoveg.szoveg_7()


def helyszin_8():
    kepek.kulcs_nalunk_ascii()
    szoveg.szoveg_8()


def helyszin_9():
    kepek.kamra_ascii()
    szoveg.szoveg_9()


def helyszin_10():
    kepek.faajto_ascii()
    szoveg.szoveg_10()


def helyszin_11():
    kepek.kis_lada_ascii()
    szoveg.szoveg_11()


def helyszin_13():
    kepek.rossz_ajto_ascii()
    szoveg.szoveg_13()
