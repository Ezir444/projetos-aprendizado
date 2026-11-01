from tkinter import *
from tkinter import ttk
import tkinter as tk
from lista import adicionar_lista,ver_lista
def mostrar_lista_botao3():
    if len(ver_lista(personagem=True)) == 0:
        mensagem_alerta["text"] = "Nenhum personagem adicionado a lista"
    else:    
        campo_text.delete("1.0",END)
        campo_text.insert(INSERT,ver_lista(personagem=True))
        print("Botão precionado")

def mostrar_lista_botao4():
    if len(ver_lista(serie=True)) == 0:
        mensagem_alerta["text"] = "Nenhuma série adicionado a lista"
    else:
        campo_text.delete("1.0",END)
        campo_text.insert(INSERT,ver_lista(serie=True))
        print("botão precionado")
    

def limpar():
    campo_personagem.delete(0, END)
    campo_serie.delete(0,END)

def bt_click():
    personagem = str(campo_personagem.get()).lower()
    serie = str(campo_serie.get()).lower()
    
    if len(campo_personagem.get()) == 0 and len(campo_serie.get()) == 0:
        mensagem_alerta["text"] = "Nenhum personagem ou série adicionado"
    elif len(campo_personagem.get()) > 0 or len(campo_serie.get()) > 0:
        if len(campo_personagem.get()) > 0 and len(campo_serie.get()) > 0:
            adicionar_lista(personagem=personagem,serie=serie)
            mensagem_alerta["text"] = f"o personagem {campo_personagem.get()} e a série {campo_serie.get()} foi adicionado a lista"
        elif len(campo_personagem.get()) > 0:
            adicionar_lista(personagem=personagem)
            mensagem_alerta["text"] = f"O personagem {campo_personagem.get()} foi adicionado"
        else:
            adicionar_lista(serie=serie)
            mensagem_alerta["text"] = f"A série {campo_serie.get()} foi adicionado"
    
#Cria uma instancia de tk, que fica referenciada na variavel janela
janela = Tk()
janela.title('mudae lista')

janela["background"] = "blue"

janela.geometry("1020x720") #dimensões da janela
ttk.Frame(janela,padding=10)


ttk.Label(janela, text='Personagem',background="blue").place(x=50,y=10,width=90,height=26)
ttk.Label(janela, text='Série',background="blue").place(x=235,y=10,width=90,height=26)

campo_personagem = ttk.Entry(janela, text='campo-personagem', textvariable=Text) 
campo_personagem.place(x=10,y=36,width=170,height=30)

campo_serie = ttk.Entry(janela,text='campo-serie')
campo_serie.place(x=200,y=36,width=160,height=30)

campo_text = tk.Text(janela,width=30,height=5)
campo_text.pack(pady=10,side="bottom")

mensagem_alerta = ttk.Label(janela, text="",background="blue",font=("Arial",14,"bold"),foreground="red")
mensagem_alerta.place(x=10,y=80,width=330,height=30)

botao = ttk.Button(janela, text='Salvar',command=bt_click).place(x=370,y=35,width=96,height=32)
botao2 = ttk.Button(janela, text='Limpar',command=limpar).place(x=480,y=35,width=96,height=32)

botao3 = ttk.Button(janela,text="Mostrar personagens",command=mostrar_lista_botao3).pack(side="bottom",padx=200)
botao4 = ttk.Button(janela,text="Mostrar series",command=mostrar_lista_botao4).pack(side="bottom")

#Cria um laço de repetição onde a janela é criada
janela.mainloop()