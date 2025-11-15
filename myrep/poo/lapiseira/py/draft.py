class Grafite:
    def __init__(self, dureza : str, calibre: float, size: int):
        self.dureza = dureza
        self.calibre = calibre
        self.tamanho = size

    def __str__(self):
        return f"{self.dureza}:{self.calibre}:{self.tamanho}"
    

class Lapiseira:
    def __init__(self,calibre : float):
        self.calibre = calibre
        self.bico: list[Grafite|None] = []
        self.tambor: list[Grafite] = []

    def inserir(self, grafite: Grafite):
        self.tambor.append(grafite)

    def __str__(self):
        tambor = ":".join([str(x)if x else "" for x in self.tambor])
        return f"{tambor}"
lapiseira = Lapiseira(0.5)
grafite = Grafite("2B",4.0,10)
lapiseira.inserir(grafite)
print(lapiseira)