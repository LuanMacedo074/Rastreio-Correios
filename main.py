from Rastreio import Rastreio
import urllib.request
import json

if __name__ == '__main__':

    with open("rastreio.json", 'r', encoding="utf-8") as arquivo:
        dados_json = arquivo.read()
        rastreio = Rastreio.from_json(dados_json)

json_string = json.dumps(rastreio.__dict__)

# Imprimir o JSON resultante
print(json_string)