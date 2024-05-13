menu = """

[deposito] Para depositar
[saque] Para sacar
[extrato] Para checar seu extrato
[sair] Para sair

"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "deposito":
        try:
            deposito = float(input("Deposite o valor desejado:"))
            if deposito <= 0:
                print("O valor do depósito deve ser maior que zero.")
            else:
                saldo += deposito
                extrato.append(("deposito", deposito))
                print(f"Depósito de R${deposito:.2f} realizado com sucesso.")
        except ValueError:
            print("Por favor, insira um valor válido")
    
    elif opcao == "saque":
        if numero_saques >= 3:
            print("Atingiu o limite de saques.")
        else:
            saque = float(input("Digite o valor do saque:"))
            if saque > saldo:
                print("Saldo insuficiente")
            elif saque > limite:
                print("Limite atingido, insira um número menor ou igual a 500")
            else:
                saldo -= saque
                numero_saques += 1
                extrato.append(("saque", saque))
                print(f"Saque de R${saque:.2f} realizado com sucesso.")

    elif opcao == "extrato":
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for tipo, valor in extrato:
                if tipo == "deposito":
                    print(f"Depósito: R${valor:.2f}")
                elif tipo == "saque":
                    print(f"Saque: R${valor:.2f}")
            print(f"Saldo atual: R${saldo:.2f}")
    
    elif opcao == "sair":
        break
