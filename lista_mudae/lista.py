#proposito, uma lista em python onde é possivel adicionar personagens e series
arquivojson = "lista_mudae.json"
import json
try:
    with open(arquivojson,mode="r",encoding="utf-8") as arquivo:
        lista_mudae = json.load(arquivo)
except (FileNotFoundError,json.decoder.JSONDecodeError):
    lista_mudae = {
    'lista_personagem' : [],
    'lista_serie' : []
    }
    with open(arquivojson,mode="w",encoding="utf-8") as arquivo:
        json.dump(lista_mudae,arquivo,indent=4)

def salvar():
    with open(arquivojson,mode="w",encoding="utf-8") as arquivo:
        json.dump(lista_mudae,arquivo,indent=4)
def adicionar_lista(personagem=None,serie=None):
    if personagem is None and serie is None:
        print("Nada a se mostrar aqui")

    elif personagem is not None and serie is not None:
        lista_mudae['lista_personagem'].append(personagem)
        lista_mudae['lista_serie'].append(serie)
        salvar()
    elif personagem is not None or serie is not None:
        if personagem is not None:
            lista_mudae['lista_personagem'].append(personagem)
            salvar()
        elif serie is not None:
            lista_mudae['lista_serie'].append(serie)
            salvar()
if __name__ == '__main__':
    while True:
        escolha = input("deseja adicionar personagem ou série? ")
        if escolha == 'personagem':
            personagem = input("digite o personagem a ser adicionado: ")
            adicionar_lista(personagem)
        elif escolha == 'serie':
            serie = input("digite a serie a ser adicionado: ")
            adicionar_lista(serie=serie)
        elif escolha == 'ambos':
            personagem = input("digite um personagem: ")
            serie = input("digite uma série: ")
            adicionar_lista(personagem,serie)
        elif escolha == 'sair':
            break
        print(lista_mudae)