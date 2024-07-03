class Pai:
    def __init__(self, nome):
        self.nome = nome

    def diga_ola(self):
        print(f"Olá, eu sou {self.nome}")

class Filho(Pai):
    def __init__(self, nome, idade):
        super().__init__(nome)  # Chama o __init__ da classe Pai
        self.idade = idade

    def diga_ola(self):
        super().diga_ola()  # Chama o método diga_ola da classe Pai
        print(f"Eu tenho {self.idade} anos")

# Exemplo de uso
filho = Filho("João", 12)
filho.diga_ola()
