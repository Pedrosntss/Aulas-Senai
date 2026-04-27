nome = "Alan" #Global 

def saudacao():
    sobrenome = "Code" #Local
    print(f"Olá, {nome} {sobrenome}")
saudacao()

def somar(n1, n2): #n1 e n2 são parâmetros
    print(f"A soma é {n1 + n2}")

somar(6, 40) #6 e 40 são argumentos