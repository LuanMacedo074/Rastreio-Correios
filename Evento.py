from typing import Dict

class Evento:
    def __init__(self, codigo: str, descricao: str, dtHrCriado: str, tipo: str, unidade: Dict[Dict[str, str] | str, str], unidadeDestino: Dict[Dict[str, str] | str, str], 
                urlIcone: str):
        self.codigo = codigo
        self.tipo = tipo
        self.dtHrCriado = dtHrCriado
        self.descricao = descricao
        self.unidade = unidade
        self.unidadeDestino = unidadeDestino
        self.urlIcone = urlIcone