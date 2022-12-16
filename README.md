# minifb
Projeto para fazer aplicativo de mensagens e amigos


# Como rodar?

  - para rodar o programa é preciso instalar as bibliotecas que estão dentro de requirements.txt

`pip install -r requirements.txt`


  - Sabendo que as bibliotecas já estão instaladas, execute o programa 'run.py' no diretorio principal:

`python3 run.py`



# Como configurar?
Veja myapp/config/myconfig.json
Neste arquivo é possível configurar as informações 'default' da aplicação.
É possível também importar arquivos, que irão sobrescrever as informações atuais.
Isso é interessante para termos uma configuração padrão e outras configurações como 'teste', 'development' e 'release'.


## 12Factor:
  - O gerenciamento de configuração é uma prática presente no 12Factor.

  - Veja mais no link: https://12factor.net/


# VERSÕES:

## versão 2.0:
  - adicionado programação orientada a objetos

## versão 3.0:
  - separado o diretório de configuração do diretório de `myapp`

