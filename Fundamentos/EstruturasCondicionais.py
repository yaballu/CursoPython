MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe a sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CHN")



if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")

else:
    print("Ainda não pode tirar a CHN")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")

elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas teóricas, mas não pode fazer as aulas práticas")

else:
    print("Ainda não pode tirar a CHN")

