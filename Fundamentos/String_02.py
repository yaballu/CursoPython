nome = "Ket"
idade = 17
profissao = "desempregada😭"
linguagem = "python"

# Forma velha e sem graça de concatenar strings, usando %
#%s é pra string, %d é pra tipo inteiro e %f é pra tipo float.

print("Oi, meu nome é %s. Tenho %d anos de idade, minha ocupação é %s e estou fazendo um curso de %s." % (nome, idade, profissao, linguagem))

# Esse é o método format que tambem é chatão, e tem alguns jeitos de fazer, sendo este o primeiro:

print("Oi, meu nome é {}. Tenho {} anos de idade, minha ocupação é {} e estou fazendo um curso de {}.".format(nome, idade, profissao, linguagem))

# Esse é o segundo jeito, que te permite por na ordem que você quiser, na minha opinião acho meio besta

print("Oi, meu nome é {3}. Tenho {2} anos de idade, minha ocupação é {1} e estou fazendo um curso de {0}.".format(linguagem, profissao, idade, nome))

# Método f-string mt melhor de fazer obviamente ne😘

print(f"Oi, meu nome é {nome}. Tenho {idade} anos de idade, minha ocupação é {profissao} e estou fazendo um curso de {linguagem}.")

# Formatação com f-string

PI = 3.14159

print(f"Valor de pi: {PI:.2f}")
print(f"Valor de pi: {PI:10.2f}")