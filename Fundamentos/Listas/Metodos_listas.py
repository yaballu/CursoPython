lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)

listinha = [1, "Python", [40, 30, 20]]
print(listinha)
listinha.clear()
print(listinha)

littlelist = [5, "bunda", [45, 455, 54]]
l2 = littlelist.copy()
print(littlelist)
print(id(l2), id(littlelist))

l2[0] = 2
print(l2)
print(littlelist)