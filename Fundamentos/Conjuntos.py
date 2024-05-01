numeros = set([1,2,3,1,3,4])

print(numeros)

fruta = set("abacaxi")

print(fruta)

carros = set(("palio", "gol", "celta", "palio"))

print(carros)

# também é possível declarar conjuntos usando chaves 

produtos = {"hidratante", "serum", "hidratante"}
print(produtos)

# para indexar ou fatiar, é necessário converter o conjunto para lista

pares = {2,4,6,2}

pares = list(pares)

print(pares[0])

# Iteração de conjuntos

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

# Métodos da classe set

# union

conjunto_a = {1,2}
conjunto_b = {3,4}

print(conjunto_a.union(conjunto_b))

# interesction

conjunto_c = {1,2,3}
conjunto_d = {2,3,4}

print(conjunto_c.intersection(conjunto_d))

# difference

conjunto_e = {1,2,3}
conjunto_f = {2,3,4}

print(conjunto_e.difference(conjunto_f))
print(conjunto_f.difference(conjunto_e))

# symmetric_difference

conjunto_g = {1,2,3}
conjunto_h = {2,3,4}

print(conjunto_g.symmetric_difference(conjunto_h))

# issubset

conjunto_i = {1,2,3}
conjunto_j = {4,1,2,5,6,3}

print(conjunto_i.issubset(conjunto_j))
print(conjunto_j.issubset(conjunto_i))

# issuperset

conjunto_k = {1,2,3}
conjunto_l = {4,1,2,5,6,3}

print(conjunto_k.issuperset(conjunto_l))
print(conjunto_l.issuperset(conjunto_k))

# isdisjoint

conjunto_m = {1,2,3,4,5}
conjunto_n = {6,7,8,9}
conjunto_o = {1,0}

print(conjunto_m.isdisjoint(conjunto_n))
print(conjunto_a.isdisjoint(conjunto_o))

# add

sorteio = {1,23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)

print(sorteio)

# clear

sorteio = {1,23}
sorteio.clear()
print(sorteio)

# copy

sorteio = {1,23}
sorteio.copy()
print(sorteio)

# discard

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(numeros)
numeros.discard(1)
numeros.discard(45)
print(numeros)

# pop

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(numeros)
numeros.pop()
numeros.pop()
print(numeros)

# remove

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
print(numeros)
numeros.remove(0)
print(numeros)

# len

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}
print(len(numeros))

# in

numeros = {1,2,3,1,2,4,5,5,6,7,8,9,0}

print(1 in numeros) 
print(10 in numeros)
