class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("inicializando a classe")
        self.nome= nome
        self.cor= cor
        self.acordado= acordado

    def __del__(self):
        print("Removendo a instância da classe")

    def falar(self):
        print("Auau")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco", False)
    print(c.nome)

c = Cachorro("Chappie", "amarelo")
c.falar()

del c

print("Olá mundo")
print("Olá mundo")
print("Olá mundo")
print("Olá mundo")

criar_cachorro()