from typing import Dict

class Evento:
    def __init__(self, codigo: str, tipo: str, dtHrCriado: str, descricao: str, unidade: Dict[str, str], unidadeDestino: Dict[str, str], 
                urlIcone: str):
        self.codigo = codigo
        self.tipo = tipo
        self.dtHrCriado = dtHrCriado
        self.descricao = descricao
        self.unidade = unidade
        self.unidadeDestino = unidadeDestino
        self.urlIcone = urlIcone