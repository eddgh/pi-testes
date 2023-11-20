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
