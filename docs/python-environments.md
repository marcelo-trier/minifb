# CONDA ENVIRONMENTS -- INTRO
Os chamados **virtual environments** em python (ou apenas **environments**) são uma forma de criarmos um conjunto de bibliotecas para rodar uma aplicação. Isso se torna necessário para que possamos ter diferentes aplicações que rodam com diferentes versões do python e/ou diferentes versões das bibliotecas.

Para que haja essa separação de um **ambiente de execução** e outro para nossas aplicações, utilizamos a estratégia de **virtual environment**. Existem várias maneiras de criarmos um environment, sendo o **venv** o padrão do python. No entanto esta maneira de criar environment, manterá sempre a mesma versão do python em questão e mudará apenas as versões das bibliotecas.

Caso queiramos uma forma de instalar environments que contenham diferentes versões do python teremos que recorrer a outras possibilidades, como por exemplo o projeto **Anaconda**. Considero que o anaconda é um bom candidato a fazer o gerenciamento de diferentes versões de python e também de suas bibliotecas. O ambiente **miniconda** é uma versão *light*, mas com todas funcionalidades. No entanto, **miniconda** é gerenciado em modo texto, através de comandos do *shell* ou do *prompt de comandos*.

Utilizaremos neste projeto o **miniconda**, e irei adicionar aqui o arquivo **requirements.yml** de configuração do nosso ambiente de desenvolvimento!

  - CONDA MANUAL:
  https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html


# Criando um environment com conda:
  - `conda create --name myclass38 python=3.8 ipython`

## Criando environment a partir de um arquivo de configuração:
  - `conda env create -f environment.yml`

# Listar os environments criados:
  - `conda env list`

# Entrando no environment criado:
  - `conda activate myclass38`

# Verificando a versao do python:
  - `python --version`
  - obs: verifique se vc está dentro do environment

## Verificando versão do pip (pip é o gerenciador de pacotes do python):
  - `pip --version`
  - obs: verifique se vc está dentro do environment

### Atualizando **pip**:
  - `pip install --upgrade pip`
  - obs: verifique se vc está dentro do environment

# Instalar as dependencias do projeto:
  - primeiro ative o ambiente
  - `pip install -r requirements.txt`


# Python environments:
  - from: https://stackoverflow.com/q/56713744

  `conda create -n "env_name" python=3.3.0 ipython`

  `conda env create -f environment.yml`

  `conda install -f -y -q --name env_name -c conda-forge --file requirements.txt`

