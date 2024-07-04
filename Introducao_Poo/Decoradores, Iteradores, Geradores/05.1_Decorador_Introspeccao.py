import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print('faz algo antes de executar')
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois de executar")
        return resultado
    
    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo! {nome}")
    return nome.upper()

print(ola_mundo.__name__)