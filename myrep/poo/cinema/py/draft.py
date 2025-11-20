class Cliente:
    def __init__(self, id: str, phone: int):
        self.__id = id
        self.__phone = phone


    def get_id(self):
        return self.__id
    def set_id(self, id: str):
        self.__id = id



    def __str__(self):
        return f"{self.__id}:{self.__phone}"








class Sala:
    def __init__(self, n_cadeiras: int):
        self.cadeiras: list[None | Cliente] = []
        for _ in range(n_cadeiras):
            self.cadeiras.append(None)



    def add(self, id: str, phone: int, index: int):
        cliente: Cliente = Cliente(id, phone)
        if index > len(self.cadeiras) or index < 0:
            print("fail: cadeira nao existe")
            return
        if self.cadeiras[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return
        for c in self.cadeiras:
            if c is not None and c.get_id() == id:
                print("fail: cliente ja esta no cinema")
                return
        self.cadeiras[index] = cliente




    def cancel(self, id: str):
        for i, c in enumerate(self.cadeiras):
            if c is not None and c.get_id() == id:
                self.cadeiras[i] = None
                return
        print("fail: cliente nao esta no cinema")



    def __str__(self):
        cadeiras = " ".join([str(x) if x else "-" for x in self.cadeiras])
        return f"[{cadeiras}]"
    





def main():
    sala = Sala(0)
    while True:
        line = input()
        print("$"+line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "show":
            print(sala)
        elif args[0] == "init":
            sala = Sala(int(args[1]))
        elif args[0] == "reserve":
            id = args[1]
            phone = int(args[2])
            cliente = Cliente(id,phone)
            sala.add(id,phone,int(args[3]))
        elif args[0] == "cancel":
            nome = args[1]
            sala.cancel(nome)


main()