from Rastreio import Rastreio
from Correios import Correios
import json

if __name__ == '__main__':
    correios = Correios()
    rastreio = correios.get_rastreio('TG637457002BR')
    print (rastreio.objetos[0].codObjeto)
