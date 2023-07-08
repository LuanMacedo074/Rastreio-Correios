import json
from typing import List
from Objeto import Objeto
from Evento import Evento
import os

class Rastreio:
    def __init__(self, versao: str, quantidade: int, resultado: str, objetos: List[Objeto]):
        self.versao = versao
        self.quantidade = quantidade
        self.resultado = resultado
        self.objetos = objetos

    def to_dict(self):
        return{
        'objetos': [objeto.to_dict() for objeto in self.objetos],
        'versao': self.versao,
        'quantidade': self.quantidade,
        'resultado': self.resultado
        }

    @classmethod
    def from_json(cls, json_string: str):
        json_data = json.loads(json_string)
        objetos = []
        for objeto_data in json_data['objetos']:
            codObjeto = objeto_data['codObjeto']
            tipoPostal = objeto_data['tipoPostal']
            habilitaAutoDeclaracao = objeto_data['habilitaAutoDeclaracao']
            habilitaPercorridaCarteiro = objeto_data['habilitaPercorridaCarteiro']
            bloqueioObjeto = objeto_data['bloqueioObjeto']
            possuiLocker = objeto_data['possuiLocker']
            habilitaLocker = objeto_data['habilitaLocker']
            habilitaCrowdshipping = objeto_data['habilitaCrowdshipping']
            temServicoAr = objeto_data['temServicoAr']
            permiteEncargoImportacao = objeto_data['permiteEncargoImportacao']
            eventos = []
            for evento_data in objeto_data['eventos']:
                codigo = evento_data['codigo']
                tipo = evento_data['tipo']
                dtHrCriado = evento_data['dtHrCriado']
                descricao = evento_data['descricao']
                unidade = evento_data['unidade']
                unidadeDestino = evento_data['unidadeDestino'] if 'unidadeDestino' in evento_data else None
                urlIcone = evento_data['urlIcone']
                eventos.append(Evento(codigo, tipo, dtHrCriado, descricao, unidade, unidadeDestino, urlIcone))
            objeto = Objeto(codObjeto, eventos, tipoPostal, habilitaAutoDeclaracao, permiteEncargoImportacao, habilitaPercorridaCarteiro, bloqueioObjeto, possuiLocker
                             , habilitaLocker, habilitaCrowdshipping, temServicoAr)
            objetos.append(objeto)
        versao = json_data['versao']
        quantidade = json_data['quantidade']
        resultado = json_data['resultado']

        return cls(versao, quantidade, resultado, objetos)
    
    def save_rastreio(self) -> None:
        data = self.to_dict()
        nome_arquivo = f'./rastreios/{self.objetos[0].codObjeto}.json'

        with open(nome_arquivo, "w", encoding='utf-8') as arquivo:
            arquivo.write(json.dumps(data, indent = 4, ensure_ascii=False))

    def check_change(self, path: str) -> str:
        if not os.path.exists(path):
            return (f'''O Objeto {self.objetos[0].codObjeto} teve a última movimentação em:
                    Saida: {self.objetos[0].eventos[0].unidade['endereco']['cidade'] if 
                            'cidade' in self.objetos[0].eventos[0].unidade['endereco'] else self.objetos[0].eventos[0].unidade['nome']}
                    Destino: {self.objetos[0].eventos[0].to_dict()['unidadeDestino']['endereco']['cidade'] if 
                                'cidade' in self.objetos[0].eventos[0].to_dict()['unidadeDestino']['endereco']
                                else self.objetos[0].eventos[0].to_dict()['unidadeDestino']['endereco']['uf'] }''')


        with open(path, 'r')as arquivo:
            old = json.loads(arquivo.read())

        if ((self.to_dict()) == old):
            return (f'o Objeto {self.objetos[0].codObjeto} não teve alterações desde o último rastreio')
    
        return (f'''O Objeto {self.objetos[0].codObjeto} teve a última movimentação em:
                    Saida: {self.objetos[0].eventos[0].unidade['endereco']['cidade'] if 
                            'cidade' in self.objetos[0].eventos[0].unidade['endereco'] else self.objetos[0].eventos[0].unidade['nome']}
                    Destino: {self.objetos[0].eventos[0].to_dict()['unidadeDestino']['endereco']['cidade'] if 
                                'cidade' in self.objetos[0].eventos[0].to_dict()['unidadeDestino']['endereco']
                                else self.objetos[0].eventos[0].to_dict()['unidadeDestino']['endereco']['uf'] }''')

    



