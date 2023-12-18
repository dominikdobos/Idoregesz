class Jatekos:
    def __init__(self, eletero, evett_korok, evett):
        self.eletero = eletero
        self.evett_korok = evett_korok
        self.evett = evett

    def __str__(self):
        return (f"Jelenlegi életerő: {self.eletero}\n"
                f"Étkezés óta eltert körök: {'Nem evett' if self.evett_korok == 0 else self.evett_korok}")