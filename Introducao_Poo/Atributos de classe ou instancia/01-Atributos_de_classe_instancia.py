class Estudante: 
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    

aluna_1 = Estudante("Ket", 1)
aluna_2 = Estudante("Annabelle", 2)
mostrar_valores(aluna_1, aluna_2)

Estudante.escola = "Python"
aluna_3 = Estudante("Cecilia", 3)
mostrar_valores(aluna_1, aluna_2, aluna_3)