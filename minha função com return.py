geral = "Essa variável posso chamar onde quiser"
def minha_funcao ():
    print('Essa é minha função')
    local = "Essa váriavel só pode ser utilizada na função"
    return local 
#chamando minha função
variavel = minha_funcao()
print (variavel)