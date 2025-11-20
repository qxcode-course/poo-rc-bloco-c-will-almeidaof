class Kid:
    def __init__(self, nome: str , idade: int):
        self.nome: dict[str, Kid] = {}
        self.idade = idade

    def __str__(self):
        return f"{self.nome}:{self.idade}"
        
class Trampoline:
    def __init__(self):
        self.playing: list[Kid] = []
        self.waiting: list[Kid] = []



    def arrive(self, nome: str, idade: int):
        kid = Kid(nome, idade)
        self.waiting.append(kid)














    def __str__(self):
        waiting = ", ".join([str(x) if x else "" for x in self.waiting])
        playing = f"{self.playing}" if self.playing else "[]"
        return f"[{waiting}] => {playing}"