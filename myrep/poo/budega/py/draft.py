class Pessoa:
    def __init__(self, nome: str) -> None:
        self.nome = nome
    
    def __str__(self):
        return self.nome
    
class Budega:
    def __init__(self, n_caixas):
        self.espera: list[Pessoa] = []
        self.caixas: list[Pessoa | None] = []
        for _ in range(n_caixas):
            self.caixas.append(None)

    def chegar(self, pessoa: Pessoa):
        self.espera.append(pessoa)

    def chamar(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print("index invalido")
            return
            
        if self.caixas[index] is not None:
            print("caixa ocupado")
            return
    
        
        if len(self.espera) == 0:
            print("ninguem esperando")
            return

        self.caixas[index] = self.espera[0]
        del self.espera[0]


    def finalizar(self, index: int):

        if index < 0 or index >= len(self.caixas):
            print("index invalido")
            return None

        if self.caixas[index] is None:
            print("caixa ja esta vazio")
            return None
        
        aux = self.caixas[index]
        self.caixas[index] = None
        return aux





    def __str__(self):
        caixas = ", ".join([str(x) if x else "----" for x in self.caixas])
        espera = ", ".join([str(x) for x in self.espera])
        return f"Caixas: [{caixas}], Espera: [{espera}]"
        


budega = Budega(3)
print(budega)
pessoa = Pessoa("Bruno")
budega.chegar(pessoa)
print(budega)
budega.chamar(2)
print(budega)
budega.chamar(1)
budega.finalizar(0)
print(budega)
