pessoa = {"nome": "Ket", "idade": 17}

pessoa = dict(nome="Ket", idade=17)

pessoa["telefone"] = "6666-9999"

print(pessoa)

dados = {"nome": "Keteli", "idade": 17, "telefone": "6666-9999"}

print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

dados["nome"] = "Anabelle"
dados["idade"] = 16
dados["telefone"] = "4444-5555"

print(dados)

# Dicionários aninhados

contatos = {
    "keteli@gmail.com": {"nome": "Ket", "idade": 17},
    "anabelle@gmail.com": {"nome": "ana", "idade": 16},
    "roxanne@gmail.com": {"nome": "roxanne", "idade": 23},
    "dalia@gmail.com": {"nome": "dalia", "idade": 30},
}

print(contatos["anabelle@gmail.com"]["idade"])

# Iterar dicionário

for chave in contatos:
    print(chave, contatos[chave])

# forma recomendada de iterar

for chave, valor in contatos.items():
    print(chave,valor)
