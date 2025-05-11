def olaMundo():
    print("Olá, Mundo!")

    def olaPessoa(nome):
        print(f'Olá, {nome}!')

def dobro(numero):
    return numero * 2

def mutiplicaDoisNumeros(a = 100, b = 4):
    """ Multiplica dois números"""
    return a * b

# print(mutiplicaDoisNumeros(55, 96))
# print(mutiplicaDoisNumeros())

x = 5 # Variável global
def soma():
    x = 10 # Variável local
    print(x)
    return x + 5
soma()
print(x)