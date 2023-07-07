from typing import List,Dict
from Evento import Evento

class Objeto:
    def __init__(self, codObjeto: str, eventos: List[Evento], tipoPostal: Dict[str, str], habilitaAutoDeclaracao: str,
                  permiteEncargoImportacao: str, habilitaPercorridaCarteiro: str, bloqueioObjeto: str,possuiLocker: str,
                    habilitaLocker: str, habilitaCrowdshipping: str, temServicoAr: str):
        self.codObjeto = codObjeto
        self.tipoPostal = tipoPostal
        self.habilitaAutoDeclaracao = habilitaAutoDeclaracao
        self.permiteEncargoImportacao = permiteEncargoImportacao
        self.habilitaPercorridaCarteiro = habilitaPercorridaCarteiro
        self.bloqueioObjeto = bloqueioObjeto
        self.possuiLocker = possuiLocker
        self.habilitaLocker = habilitaLocker
        self.habilitaCrowdshipping = habilitaCrowdshipping
        self.temServicoAr = temServicoAr
        self.eventos = eventos