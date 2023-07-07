import json
from typing import List
from Objeto import Objeto
from Evento import Evento


class Rastreio:
    def __init__(self, versao: str, quantidade: int, resultado: str, objetos: List[Objeto]):
        self.versao = versao
        self.quantidade = quantidade
        self.resultado = resultado
        self.objetos = objetos

    @classmethod
    def from_json(cls, json_string: str):
        json_data = json.loads(json_string)
        versao = json_data['versao']
        quantidade = json_data['quantidade']
        resultado = json_data['resultado']
        objetos = []
        for objeto_data in json_data['objetos']:
            codObjeto = objeto_data['codObjeto']
            tipoPostal = objeto_data['tipoPostal']
            dtPrevista = objeto_data['dtPrevista']
            modalidade = objeto_data['modalidade']
            peso = objeto_data['peso']
            formato = objeto_data['formato']
            eventos = []
            for evento_data in objeto_data['eventos']:
                codigo = evento_data['codigo']
                tipo = evento_data['tipo']
                dtHrCriado = evento_data['dtHrCriado']
                descricao = evento_data['descricao']
                unidade = evento_data['unidade']
                eventos.append(Evento(codigo, tipo, dtHrCriado, descricao, unidade))
            objeto = Objeto(codObjeto, tipoPostal, dtPrevista, modalidade, peso, formato, eventos)
            objetos.append(objeto)
        return cls(versao, quantidade, resultado, objetos)

