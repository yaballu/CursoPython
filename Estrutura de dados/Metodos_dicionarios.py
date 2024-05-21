# clear

contatos = {
    "keteli@gmail.com": {"nome": "Ket", "idade": 17},
    "anabelle@gmail.com": {"nome": "ana", "idade": 16},
    "roxanne@gmail.com": {"nome": "roxanne", "idade": 23},
    "dalia@gmail.com": {"nome": "dalia", "idade": 30},
}

contatos.clear()
print(contatos)

# copy

contatos = {
    "keteli@gmail.com": {"nome": "Keteli", "idade": 17},
}

copia = contatos.copy()
copia["keteli@gmail.com"] = {"nome": "Ket"}

print(contatos["keteli@gmail.com"])
print(copia["keteli@gmail.com"])

# fromkeys

contatos = {
    "keteli@gmail.com": {"nome": "Keteli", "idade": 17},
}

contatos = dict.fromkeys(["nome", "idade"])
contatos = dict.fromkeys(["nome", "idade"], "vazio")

print(contatos)

# get

informacao = {
    "keteli@gmail.com": {"nome": "Keteli", "idade": 17},
}

# Comentarei a linha abaixo pq ela tá dando erro
# informacao["chave"]

informacao.get("chave")
informacao.get("chave", {})
informacao.get("keteli@gmail.com", {})

# items

contatos = {
    "keteli@gmail.com": {"nome": "Keteli", "idade": 17},
}

print(contatos.items())

# keys

contatos = {
    "keteli@gmail.com": {"nome": "Keteli", "idade": 17},
}

print(contatos.keys())

# pop

contatos = {
    "keteli@gmail.com": {"nome": "Keteli", "idade": 17},
}

print(contatos.pop("keteli@gmail.com"))
print(contatos.pop("keteli@gmail.com", {}))

# popitem

contatos = {
    "keteli@gmail.com": {"nome": "Keteli", "idade": 17},
}
# print(contatos.popitem())
# print(contatos.popitem())

# setdefault

contatos = {
    "keteli@gmail.com": {"nome": "Keteli", "idade": 17},
}

contatos.setdefault("nome", "anabelle")
print(contatos)

contatos.setdefault("especialidade", "cozinheira")
print(contatos)

# update

contatos = {
    "keteli@gmail.com": {"nome": "Keteli", "idade": 17},
}

contatos.update({"keteli@gmail.com": {"nome":"Ket"}})
print(contatos)

contatos.update({"anabelle@gmail.com": {"nome": "belle", "idade": 16}})
print(contatos)

# values

contatos = {
    "keteli@gmail.com": {"nome": "Ket", "idade": 17},
    "anabelle@gmail.com": {"nome": "ana", "idade": 16},
    "roxanne@gmail.com": {"nome": "roxanne", "idade": 23},
    "dalia@gmail.com": {"nome": "dalia", "idade": 30},
}

print(contatos.values())

# in

contatos = {
    "keteli@gmail.com": {"nome": "Ket", "idade": 17},
    "anabelle@gmail.com": {"nome": "ana", "idade": 16},
    "roxanne@gmail.com": {"nome": "roxanne", "idade": 23},
    "dalia@gmail.com": {"nome": "dalia", "idade": 30},
}

print("keteli@gmail.com" in contatos)
print("coco@gmail.com" in contatos)
print("idade" in contatos["keteli@gmail.com"])
print("telefone" in contatos["anabelle@gmail.com"])

# del

contatos = {
    "keteli@gmail.com": {"nome": "Ket", "idade": 17},
    "anabelle@gmail.com": {"nome": "ana", "idade": 16},
    "roxanne@gmail.com": {"nome": "roxanne", "idade": 23},
    "dalia@gmail.com": {"nome": "dalia", "idade": 30},
}

del contatos["keteli@gmail.com"]["idade"]
del contatos["roxanne@gmail.com"]

print(contatos)