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
            print("fail: caixa ocupado")
            return
    
        
        if len(self.espera) == 0:
            print("fail: sem clientes")
            return

        self.caixas[index] = self.espera[0]
        del self.espera[0]


    def finalizar(self, index: int):

        if index < 0 or index >= len(self.caixas):
            print("fail: caixa inexistente")
            return None

        if self.caixas[index] is None:
            print("fail: caixa vazio")
            return None
        
        aux = self.caixas[index]
        self.caixas[index] = None
        return aux





    def __str__(self):
        caixas = ", ".join([str(x) if x else "-----" for x in self.caixas])
        espera = ", ".join([str(x) for x in self.espera])
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"


def main():
    budega = Budega(0)
    while True:
        line = input()
        print("$"+line)
        args: list[str] = line.split()
        if args[0] == "end":
            break
        elif args[0] == "init":
            budega = Budega(int(args[1]))
        elif args[0] == "show":
            print(budega)
        elif args[0] == "arrive":
            budega.chegar(args[1])
        elif args[0] == "call":
            budega.chamar(int(args[1]))
        elif args[0] == "finish":
            budega.finalizar(int(args[1]))
main()
