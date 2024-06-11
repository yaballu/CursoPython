saldo = 0.0
limite = 500
extrato = []
usuarios = {}
contas = {}
numero_saques = 0
LIMITE_SAQUES = 3

def Saque(*, saldo, extrato, numero_saques, limite):
    if numero_saques >= 3:
            print("Atingiu o limite de saques.")
            return saldo, extrato, numero_saques
    else:
        saque = float(input("Digite o valor do saque:"))
        if saque > saldo:
            print("Saldo insuficiente")
            return saldo, extrato, numero_saques
        elif saque > limite:
            print("Limite atingido, insira um número menor ou igual a 500")
            return saldo, extrato, numero_saques
        elif saque <= 0:
            print("O valor do depósito deve se maior que zero") 
            return saldo, extrato, numero_saques
        else:
            saldo -= saque
            numero_saques += 1
            extrato.append(("saque", saque))
            print(f"Saque de R${saque:.2f} realizado com sucesso.")
            return saldo, extrato, numero_saques

def Deposito(saldo, extrato):
    try:
        deposito = float(input("Deposite o valor desejado:"))
        if deposito <= 0:
            print("O valor do depósito deve ser maior que zero.")
            return saldo, extrato
        else:
            saldo += deposito
            extrato.append(("deposito", deposito))
            print(f"Depósito de R${deposito:.2f} realizado com sucesso.")
            return saldo, extrato
    except ValueError:
        print("Por favor, insira um valor válido")
        return saldo, extrato
    
def Extrato(saldo, *, extrato):
    if not extrato:
        print("Não foram realizadas movimentações.")
        return saldo, extrato
    else:
        print("Extrato:")
        for tipo, valor in extrato:
            if tipo == "deposito":
                print(f"Depósito: R${valor:.2f}")
            elif tipo == "saque":
                print(f"Saque: R${valor:.2f}")
        print(f"Saldo atual: R${saldo:.2f}")
        return saldo, extrato

def Criar_Usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("digite sua data de nascimento: ")
    cpf = input("Digite seu cpf(Somente números!): ")
    rua = input("Digite sua rua: ")
    nro = input("Digite o número: ")
    bairro = input("Digite seu bairro: ")
    cidade = input("Digite sua cidade: ")
    estado = input("Digite seu estado: ")
    endereco = rua + ", " + nro + ", " + bairro + ", " + cidade + ", " + estado + "."
    
    print("Confirme se o endereço está correto: ")
    print(endereco)
    confirmacao = input("O endereço está correto? (s/n): ").lower()

    if confirmacao != 's':
        print("Endereço incorreto. Cadastro cancelado")
        return usuarios

    if cpf in usuarios:
            print("CPF já cadastrado. Não é possível cadastrar o mesmo CPF novamente.")
            return usuarios
        
    usuario = {
        cpf:{
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
        }
    }
    usuarios.update(usuario)
    
    print("Usuário cadastrado com sucesso.")
    return usuarios
    

def Criar_Conta(contas, usuarios):
    AGENCIA = "0001"

    if not usuarios:
        print("Não existem usuários cadastrados. Crie um usuário primeiro.")
        return contas

    cpf_usuario = input("Digite o CPF do usuário para associar à conta: ")
    
    if cpf_usuario in usuarios:
        print("Usuário encontrado!")
        usuario_novo = usuarios[cpf_usuario]['nome']     
        numero_conta = len(contas) + 1

        nova_conta = {
            'agencia': AGENCIA,
            'numero_conta': numero_conta,
            'usuario': usuario_novo,
            'cpf': cpf_usuario
        }

        contas[numero_conta] = nova_conta
        print("Conta criada com sucesso.")
        print(f"Seu usuário é: {nova_conta}")
    else:
        print("Usuário não encontrado")
    return contas

while True:
    opcao = input("""
                  Insira a operação que deseja realizar: 
                  1- Cadastrar usuário
                  2- Cadastrar conta
                  3- Logar na conta
                  4- Sair
                  
                  """)
    
    if opcao == "1":
        try:
            usuarios = Criar_Usuario(usuarios)
        except ValueError:
            print("Erro ao cadastrar usuário.")
        finally:
            print("Fim do cadastro.")
    elif opcao == "2":
        try:
            contas = Criar_Conta(contas, usuarios)
        except ValueError:
            print("Erro ao cadastrar conta.")
        finally:
            print("Fim do cadastro.")
    elif opcao == "4":
        break
    elif opcao == "3":
        try:
            cpf = input("Digite o cpf associado à conta: ")

            conta_encontrada = None
            for conta in contas.values():
                if conta['cpf'] == cpf:
                    conta_encontrada = conta
                    break

            if conta_encontrada:
                print("Conta encontrada. Logado com sucesso!")
            
                while True:
                        operacao = input("""
                                            Escolha a operação que deseja realizar:
                                            [deposito] Para depositar
                                            [saque] Para sacar
                                            [extrato] Para checar seu extrato
                                            [sair] Para sair                                                                          
                                            """)
                        if operacao == "deposito":
                            try:
                                saldo, extrato = Deposito(saldo, extrato)
                            except:
                                print("Falha ao tentar realizar o depósito.")
                            finally:
                                print("Operação de depósito finalizada.")
                                    
                        elif operacao == "saque":
                            try:
                                saldo, extrato, numero_saques = Saque(saldo=saldo, extrato=extrato, numero_saques=numero_saques, limite=limite)
                            except:
                                print("Falha ao tentar realizar o saque.")
                            finally:
                                print("Operação de saque finalizada.")
                            
                        elif operacao == "extrato":
                            try:
                                saldo, extrato = Extrato(saldo, extrato=extrato)
                            except:
                                print("Falha ao tentar exibir o extrato.")
                            finally:
                                print("Operação de extrato finalizada.")
                            
                        elif operacao == "sair":
                            break        
                            
            else:
                print("Conta não encontrada.")
        except ValueError:
            print("Erro ao logar na conta.")
        finally:
            print("Fim da operação")
