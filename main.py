from Rastreio import Rastreio
from Correios import Correios

def get_codigos():
    with open('codigos.rastreio', "r") as arquivo:
        return arquivo.read().split(", ")


if __name__ == '__main__':
    correios = Correios()
    codigos = get_codigos()
    
    for codigo in codigos:
        rastreio = correios.get_rastreio(f'{codigo}')
        rastreio.save_rastreio()
