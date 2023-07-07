from typing import List,Dict
from Evento import Evento

class Objeto:
    def __init__(self, codObjeto: str, tipoPostal: Dict[str, str], dtPrevista: str, modalidade: str,
                 peso: float, formato: str, eventos: List[Evento]):
        self.codObjeto = codObjeto
        self.tipoPostal = tipoPostal
        self.dtPrevista = dtPrevista
        self.modalidade = modalidade
        self.peso = peso
        self.formato = formato
        self.eventos = eventos