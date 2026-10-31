import tkinter as tk
from tkinter import ttk

def pegar_texto():
    texto = caixa_texto.get()
    print(texto)

janela = tk.Tk()
janela.title("meu programa")
janela.geometry("640x480")
janela.minsize(320,240)

caixa_texto = tk.Entry(janela,width=30)
caixa_texto.pack(pady=20)

botao = tk.Button(janela,text="mostrar texto", command=pegar_texto)
botao.pack()
janela.mainloop()