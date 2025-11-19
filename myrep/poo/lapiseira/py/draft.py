class Grafite:
    def __init__(self,calibre: float, dureza : str, size: int):
        self.dureza = dureza
        self.calibre = calibre
        self.tamanho = size

    def get_calibre(self):
        return self.calibre
    def get_tamanho(self):
        return self.tamanho
    def set_tamanho(self, tamanho: int):
        self.tamanho = tamanho

    def GastoFolha(self):
        if self.dureza == "HB":
            return 1
        elif self.dureza == "2B":
            return 2
        elif self.dureza == "4B":
            return 4
        elif self.dureza == "6B":
            return 6
        else:
            return 0

    def __str__(self):
        return f"[{self.calibre}:{self.dureza}:{self.tamanho}]"
    

class Lapiseira:
    def __init__(self,calibre : float):
        self.calibre = calibre
        self.bico: Grafite|None = None
        self.tambor: list[Grafite] = []

    def inserir(self,calibre: float, dureza: str, tamanho: int):
        if calibre != self.calibre:
            print("fail: calibre incompatível")
            return
        grafite = Grafite(calibre, dureza,tamanho)
        self.tambor.append(grafite)



    def puxar(self):
        if self.bico is not None:
            print("fail: ja existe grafite no bico")
            return False
        elif not self.tambor:
            print("fail: sem grafite")
            return False

        self.bico = self.tambor[0]
        del self.tambor[0]
        return True

    def escreverPag(self):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return
        if self.bico.get_tamanho() <= 10:
            print("fail: tamanho insuficiente")
            self.bico = None
            return
        consumo = self.bico.GastoFolha()
        if self.bico.get_tamanho() - consumo < 10:
            print("fail: folha incompleta")
            self.bico.set_tamanho(10)
            return
        self.bico.set_tamanho(self.bico.get_tamanho()-consumo)


    def remover(self):
        if self.bico is None:
            print("fail: não ha grafite no bico ")
            return 
        aux = self.bico
        self.bico = None
        return aux


    def __str__(self):
        tambor = "".join([str(x)if x else "" for x in self.tambor])
        bico = f"{self.bico}" if self.bico else "[]"
        return f"calibre: {self.calibre}, bico: {bico}, tambor: <{tambor}>"


def main():
    lapiseira = Lapiseira(0)
    while True:
        line = input()
        print("$"+line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(lapiseira)
        elif args[0] == "init":
            calibre = float(args[1])
            lapiseira = Lapiseira(calibre)
        elif args[0] == "insert":
            calibre = float(args[1])
            dureza = args[2]
            tamanho = int(args[3])
            lapiseira.inserir(calibre, dureza, tamanho)
        elif args[0] == "pull":
            lapiseira.puxar()
        elif args[0] == "remove":
            lapiseira.remover()
        elif args[0] == "write":
            lapiseira.escreverPag()
        


main()