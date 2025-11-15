class Grafite:
    def __init__(self, dureza : str, calibre: float, size: int):
        self.dureza = dureza
        self.calibre = calibre
        self.tamanho = size

    def get_calibre(self):
        return self.calibre



    def __str__(self):
        return f"{self.dureza}:{self.calibre}:{self.tamanho}"
    

class Lapiseira:
    def __init__(self,calibre : float):
        self.calibre = calibre
        self.bico: list[Grafite|None] = [None]
        self.tambor: list[Grafite] = []

    def inserir(self, grafite: Grafite):
        if self.calibre != grafite.get_calibre():
            print("fail: calibre incompatível")
            return
        self.tambor.append(grafite)



    def puxar(self):
        if self.bico is not None:
            print("fail: ja existe grafite no bico")
            return
        
        if len(self.tambor) == 0:
            print("fail: tambor esta vazio")
            return

        self.bico[0] = self.tambor[0]
        del self.tambor[0]


    def __str__(self):
        tambor = ":".join([str(x)if x else "" for x in self.tambor])
        bico = ":".join([str(x)if x else "" for x in self.bico])
        return f"calibre: {self.calibre}, bico: [{bico}], tambor: <{tambor}>"


lapiseira = Lapiseira(0.5)
grafite = Grafite("2B",0.5,10)
lapiseira.inserir(grafite)
print(lapiseira)
lapiseira.puxar()
print(lapiseira)
grafite1 = Grafite("2B",0.5,10)
lapiseira.inserir(grafite1)
print(lapiseira)
lapiseira.puxar()
print(lapiseira)
