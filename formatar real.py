def formatar_real(valor):
    return f"R$ {valor: ,.2f}".replace(",","X").replace(".",",").replace("X",".")
#Uso: 
preco_hospedagem = 49.9
print(formatar_real(preco_hospedagem)) #R$ 49,90