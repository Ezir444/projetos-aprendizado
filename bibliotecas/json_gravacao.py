import json
import os
class Json_gravacao:
    def __init__(self,nome:str):
        self.nome = f'{nome}.json'
        if not os.path.isfile(self.nome):
            self.criar_json()

    def criar_json(self):
        with open(self.nome,mode='w',encoding='utf-8') as json_file:
            json.dump({},json_file,indent=4)

    def ler_json(self):
        with open(self.nome,mode='r',encoding='utf-8') as json_file:
            return json.load(json_file)
        
    def gravar_json(self,arquivo):
        with open(self.nome,mode='w',encoding='utf-8') as json_file:
            json.dump(arquivo,json_file,indent=4)

if __name__ == "__main__":
    teste = Json_gravacao("json_gravacao")
    lista = [1,2,3]
    teste.gravar_json("oi")