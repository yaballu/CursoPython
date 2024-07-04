def mensagem(nome):
    print("Executando nome")
    return f"Oi {nome}"

def mensagem_longa(nome):
    print("Executando mensagem longa")
    return f"Olá tudo bem com você {nome}?"

def executar(funcao, nome):
    print("Executando executar")
    return funcao(nome)

print(executar(mensagem, "Ket"))
print(executar(mensagem_longa, "Ket"))