class Aluno:
    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self):
        return f"{self.nome}"
    







class Onibus:
    def __init__(self, n_cadeiras: int):
        self.cadeiras: list[Aluno|None] = []
        for _ in range(n_cadeiras):
            self.cadeiras.append(None)



    def add(self, nome: str, index: int):
        aluno = Aluno(nome)
        self.cadeiras[index] = aluno


    def remove(self, index: int):
        aux = self.cadeiras[index]
        self.cadeiras[index] = None
        return aux

    def __str__(self):
        cadeiras = " ".join([str(x) if x else "-" for x in self.cadeiras])
        return f"[{cadeiras}]"

bus = Onibus(4)
print(bus)
bus.add("will",2)
print(bus)
bus.remove(2)
print(bus)