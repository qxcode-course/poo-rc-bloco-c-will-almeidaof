class Kid:
    def __init__(self, nome: str , idade: int):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}:{self.idade}"
        
class Trampoline:
    def __init__(self):
        self.playing: list[Kid] = []
        self.waiting: dict[str, Kid] = {}   



    def arrive(self, kid: Kid):
        if kid.nome in self.waiting or any(k.nome == kid.nome for k in self.playing):
            raise Exception("fail: pessoa com o mesmo nome")
        self.waiting[kid.nome] = kid




    def get_kid(self, nome: str):
        try:
            return self.waiting[nome]
        except KeyError as _:
            raise Exception(f"{nome} já existe")

    def remove(self, nome:str):
        if nome in self.waiting:
            del self.waiting[nome]
            return
        for kid in self.playing:
            if kid.nome == nome:
                self.playing.remove(kid)
                return
        else:
            print(f"fail: {nome} nao esta no pula-pula")
        
    def listar_kids(self) -> list[Kid]:
        lista: list[Kid] = []
        for kid in self.waiting.values():
            lista.append(kid)
        return lista[::-1]
    

    def enter(self):
        if self.waiting:
            primeiro = list(self.waiting.keys())[0]
            kid = self.waiting.pop(primeiro)
            self.playing.insert(0, kid)


    def leave(self):
        if not self.playing:
            return
        kid = self.playing.pop()
        self.waiting[kid.nome] = kid




    def __str__(self):
        waiting = ", ".join(str(kid) if kid else "" for kid in self.listar_kids())
        playing = ", ".join(str(k) for k in self.playing) if self.playing else ""
        playing = f"{playing}" if playing else ""

        return f"[{waiting}] => [{playing}]"
    
def main():
    trampolim = Trampoline()
    while True:
        line = input()
        print("$"+line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(trampolim)
        elif args[0] == "arrive":
            nome = args[1]
            idade = int(args[2])
            kid = Kid(nome, idade)
            trampolim.arrive(kid)
        elif args[0] == "enter":
            trampolim.enter()
        elif args[0] == "leave":
            trampolim.leave()
        elif args[0] == "remove":
            trampolim.remove(args[1])

main()