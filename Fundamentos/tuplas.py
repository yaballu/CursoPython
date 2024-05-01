frutas = ("laranja", "pera", "uva",)

print(frutas)
print(frutas[0])
print(frutas[2])
print(frutas[-1])
print(frutas[-2])

letras = tuple("python")

print(letras)

numeros = tuple([1,2,3,4])

print(numeros)

pais = ("Brasil",)

# matriz

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

# fatiamento

tupla = ("p", "y", "t", "h", "o", "n",)

print(tupla[2:])
print(tupla[2:])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[::])
print(tupla[::-1])

# iteração

carros = ("gol", "celta", "palio",)

for carro in carros:
    print(carro)

# metódos

# count

cores = ("ciano", "amarelo", "turquesa", "ciano", "turquesa", "ciano",)
print(cores.count("ciano"))
print(cores.count("amarelo"))
print(cores.count("turquesa"))

# index

linguagens = ("python", "js", "c", "java", "csharp",)

print(linguagens.index("java"))
print(linguagens.index("python"))

# len

linguagens = ("python", "js", "c", "java", "csharp",)

print(len(linguagens))