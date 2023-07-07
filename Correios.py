from configparser import ConfigParser
import hashlib
from datetime import datetime
import pytz
from Rastreio import Rastreio
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import json


class Correios:

    def __init__(self):
        self.token = self._get_token('config.ini')
        self.data = self._get_data()
        self.get_rastreio('TG637457002BR')
    	
    def _get_data(self) -> str:
        return datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M:%S')
    
    def _get_token(self, path: str) -> str:
        config = ConfigParser()
        config.read(path)
        
        return config.get('DEFAULT', 'token')
    
    def _generate_sign(self) -> str:
        data = self.data

        token = self.token

        hash_object = hashlib.md5()
        hash_object.update(f'requestToken{token}data{data}'.encode())

        return hash_object.hexdigest()
    
    def get_rastreio(self, codigo_rastreio: str):
        url = 'https://proxyapp.correios.com.br/v2/app-validation'
        headers = {'Content-Type': 'application/json', 'User-Agent': 'Dart/2.18 (dart:io)'}
        sign = self._generate_sign()
        body  = {'requestToken': f'{self.token}',
                  'data': f'{self.data}', 
                  'sign': f'{sign}'}
        body_encoded = json.dumps(body).encode('utf-8')
        request = Request(url, data=body_encoded , headers=headers, method='POST')

        response = urlopen(request)
        content = response.read()

        content_decoded = json.loads(content.decode('utf-8'))

        request_token = content_decoded['token']

        headers['app-check-token'] = request_token
        url = f'https://proxyapp.correios.com.br/v1/sro-rastro/{codigo_rastreio}'

        request = Request(url,headers=headers)

        response = urlopen(request)

        rastreio = response.read()
        rastreio_decoded  = json.loads(rastreio.decode('utf-8'))

        print (rastreio_decoded)


    

