# POSITIONAL ONLY

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0",
combustivel="Gasolina") # válido

# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0",
# combustivel="Gasolina") # inválido

# KEYWORD ONLY

def criar_carrinho(*, modelo, ano, marca, placa, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carrinho(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat",
motor="1.0", combustivel="Gasolina") # Válido

# criar_carrinho("Palio", 1999, "ABC-1234", "Fiat",
# "1.0", "Gasolina") # inválido

# KEYWORD AND POSITIONAL ONLY

def criar_carrodnv(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carrodnv("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # Válido

# criar_carrodnv(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # Inválido

# OBJETOS DE PRIMEIRA CLASSE

def somar(a,b):
    return a + b

def subtrair(a,b):
    return a - b

def test(a,b):
    return a*2 + b*3

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação = {resultado}")

exibir_resultado(10,10,somar)
exibir_resultado(20,15,subtrair)
exibir_resultado(3,9,test)

op = somar
print(op(1,23))

# ESCOPO LOCAL E ESCOPO GLOBAL

salario = 2000

def salario_bonus(bonus, lista):
    global salario 

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux={lista_aux}")
    
    salario += bonus
    return salario 

lista = [1]
salario_bonus(500, lista)
print(salario)
print(lista)

