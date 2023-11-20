# PROJETO DE TESTES COM PYTHON

## Instalação Básica
### Passos:
- Montar um ambiente virtual (venv)
```
python -m venv .
```
- Ativar o ambiente virtual (venv)
```
source Scripts/activate
```
- Instalar o selenium
```
pip install selenium
```
- Instalar o pytest
```
pip install pytest
```
- Instalar o pytest html para gerar relatórios
```
pip install pytest-html
```
- Criar pasta tests na raiz do projeto
```
touch tests
```
- Dentro da pasta tests criar seu arquivo de testes:
###### Precisar ter o prefixo "test_" no nome do seu arquivo para que os testes sejam automaticamente rastreados pelo pytest
```
touch test_name.py 
Exemplo:

def test_one():
    assert 1 + 1 == 2
```
- Para rodar o teste execute:
```
pytest tests/
```
- Para rodar o teste e gerar o relatório execute:
```
pytest tests/ --html=report.html
```


## Instalação com Pipenv
###### Pipenv facilita instalar automacticamente as libs

01 - criar o arquivo pipfile para gerenciar as libs: 
```
pipenv --python three
```
###### Pipfile que é o arquivo responsável pelo gerenciamento dos pacotes em uma pasta oculta .env que será responsável por armazenar nosso ambiente do python na versão 3 que foi criado graças a flag --three, que é a versao do python que será utilizada no ambiente virtual

02 - listar as bibliotecas do ambiente virtual criado:
```
pipenv run pip freeze
```
03 - ativar o ambiente virtual:
```
pipenv shell
```