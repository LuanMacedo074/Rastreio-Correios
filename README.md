<h1>
Rastreador de encomendas dos Correios
</h1>

<h2>
Sobre
</h2>
<p>
Este é um script desenvolvido em Python 3.11.3 que permite rastrear múltiplas encomendas dos Correios. Ele utiliza a API dos Correios para obter as informações de rastreamento das encomendas.
</p>
<h2>
Requisitos
</h2>
<p>
Certifique-se de ter o Python 3.11.3 instalado em seu sistema. Além disso, é necessário instalar as dependências do projeto listadas no arquivo requirements.txt. Para instalá-las, execute o seguinte comando:

```shell
pip install -r requirements.txt
```
</p>
<h2>
Configurações
</h2>
<p>
Antes de executar o script, você precisa fazer algumas configurações:

Renomeie o arquivo config.ini.example para config.ini.
Abra o arquivo config.py e insira suas informações de autenticação da API dos Correios.

Renomeie também o arquivo codigos.rastreio.example para codigos.rastreio. Abra o arquivo codigos.rastreio e insira os codigos de rastreios separados por virgula.
</p>
<h2>
Uso
</h2>
<p>
Para executar o script e rastrear as encomendas, siga as etapas abaixo:

Abra um terminal ou prompt de comando.
Navegue até o diretório do projeto.
Execute o seguinte comando:
```shell
py main.py
```
O script irá rastrear as encomendas e exibir as informações de rastreamento no console, além de gravar as informações em arquivos json legíveis na pasta rastreios.
</p>
<h2>
Contribuições
</h2>
<p>
Contribuições são bem-vindas! Se você encontrar algum problema ou tiver melhorias para sugerir, sinta-se à vontade para abrir uma issue ou enviar um pull request.
</p>
<h2>
Licença
</h2>
<p>
Este projeto está licenciado sob a <a href="https://opensource.org/license/mit"> MIT License. </a>
</p>
