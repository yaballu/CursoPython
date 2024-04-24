nome = "keteli"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá mundo   "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip()+ ".")

menu = "Python"

print("####"+menu+"####")
print(menu.center(14))
print(menu.center(30,"#"))
print("-".join(menu))

#Com for ia ser essa chatice toda, muito mais simples com join

for letra in menu:
    print(letra, end="-") 