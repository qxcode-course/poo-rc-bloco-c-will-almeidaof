class Pessoa:
    def __init__(self, nome: str) -> None:
        self.nome = nome
    
    def __str__(self):
        return self.nome
    
class Mercantil:
    def __init__(self, n_caixas: int): 
        self.espera: list[Pessoa] = []
        self.caixas: list[Pessoa | None] = []
        for _ in range(n_caixas):
            self.caixas.append(None)

    def chegar(self, pessoa: Pessoa):
        self.espera.append(pessoa)

    def chamar(self, index:int):
        if index < 0 or index >= len(self.caixas):
            print("index invalido")
            return
        if self.caixas[index] is not None:
            print("caixa oxupado")
            return
        if len(self.espera) == 0:
            print("ninguem esperando")
            return
        self.caixas[index] = self.espera[0]
        del self.espera[0]

    def finalizar(self, index: int) -> Pessoa | None:
        if index < 0 or index >= len(self.caixas):
            print("index invalido")
