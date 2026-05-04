import tkinter as tk 
import random 

#configuração
simbolos =  ["🍵", "♠️", "🐘", "✩","🍊"]
saldo = 20.0
custo_giro = 2 

# Função de Girar 
def girar():
    global saldo

    if saldo < custo_giro:
        resultado_Label:any
        resultado_Label.config(text="Saldo insuficiente!", fg="red")
        return
    saldo -= custo_giro

    resultado = [random.choice(simbolos) for _ in range(3)]

    #atualiza os slots

    slot1.config(text=resultado[0])
    slot2.config(text=resultado[1])
    slot3.config(text=resultado[2])

    #Verifica vitória 
    if resultado[0] == resultado[1] == resultado [2]:
        premio = 20
        saldo += premio 
        resultado_Label.config(text=f"🎉 JACKPOT! +R$ {premio}", fg="green")
    else:
        resultado_Label.config(text=f"😟 Tente novamente...", fg = "black")

    saldo_label:any
    saldo_label.config(text=f"Saldo: R$ {saldo: .2f}")

#Janela principal
janela = tk.Tk
janela.title = ("KASSINÃO do Sesi")
janela.geometry ("400x200")
janela.resizable (True,True)

#TITULO
titulo = tk.Label(janela, text="KASSINÃO do Sesi", font= ("Arial", 16, "bold"))
titulo.pack(pady=10)

# Frame dos slots 
frame_slots = tk.frame(janela)
frame_slots.pack(pack=10)

slot1 = tk.LAbel(frame_slots, text="⁉️", font=("Arial", 30))